"""
Control an itach ip2ir gateway using libitachip2ir
"""
import logging
import os
from ctypes import *

from homeassistant.components.switch import PLATFORM_SCHEMA
from homeassistant.const import DEVICE_DEFAULT_NAME
from homeassistant.helpers.entity import ToggleEntity

_LOGGER = logging.getLogger(__name__)

CONF_MAC = 'mac'
CONF_IP = 'ip'
CONF_PORT = 'port'
CONF_FILE ='file'
CONF_DEVICES = 'devices'

libitachip2ir = cdll.LoadLibrary(os.path.dirname(__file__) + "/libitachip2ir.dylib")
libitachip2ir.ITachIP2IR_new.argtypes = [c_char_p, c_char_p, c_int]
libitachip2ir.ITachIP2IR_new.restype = c_void_p
libitachip2ir.ITachIP2IR_delete.argtypes = [c_void_p]
libitachip2ir.ITachIP2IR_ready.argtypes = [c_void_p, c_int]
libitachip2ir.ITachIP2IR_ready.restype = c_bool
libitachip2ir.ITachIP2IR_update.argtypes = [c_void_p]
libitachip2ir.ITachIP2IR_loadCommands.argtypes = [c_void_p, c_char_p]
libitachip2ir.ITachIP2IR_loadCommands.restype = c_bool
libitachip2ir.ITachIP2IR_send.argtypes = [c_void_p, c_int, c_int, c_char_p, c_int]
libitachip2ir.ITachIP2IR_send.restype = c_bool


class ITachIP2IR(object):
    def __init__(self, mac, ip, port):
        self.itachip2ir = libitachip2ir.ITachIP2IR_new(bytes(mac,'utf-8'), bytes(ip,'utf-8'), port)

    def __del__(self):
        libitachip2ir.ITachIP2IR_delete(self.itachip2ir)

    def update(self):
        libitachip2ir.ITachIP2IR_update(self.itachip2ir)

    def loadCommands(self, file):
        in_file = open(os.path.dirname(__file__)+"/../../"+file, "r")
        return libitachip2ir.ITachIP2IR_loadCommands(self.itachip2ir, bytes(in_file.read(),'utf-8'))

    def send(self, modaddr, connaddr, command, count):
        libitachip2ir.ITachIP2IR_send(self.itachip2ir, modaddr, connaddr, bytes(command,'utf-8'), count)

# pylint: disable=unused-argument
def setup_platform(hass, config, add_devices, discovery_info=None):
    itachip2ir = ITachIP2IR(config.get(CONF_MAC), config.get(CONF_IP), int(config.get(CONF_PORT)))
    itachip2ir.loadCommands(config.get(CONF_FILE))
    devices = []
    for data in config.get(CONF_DEVICES):
        name = data['name']
        modaddr = int(data.get('modaddr',1))
        connaddr = int(data.get('connaddr',1))
        devices.append(ITachIP2IRSwitch(itachip2ir, name, modaddr, connaddr))
    add_devices(devices)


class ITachIP2IRSwitch(ToggleEntity):
    def __init__(self, itachip2ir, name, modaddr, connaddr):
        self.itachip2ir = itachip2ir
        self._name = name or DEVICE_DEFAULT_NAME
        self.modaddr = modaddr
        self.connaddr = connaddr

    @property
    def name(self):
        """Return the name of the switch."""
        return self._name

    @property
    def should_poll(self):
        return True

    @property
    def is_on(self):
        """Return true if device is on."""
        self.itachip2ir.update()
        return False#self.rfoutlet.getState(self.product, self.channel, self.outlet)

    def turn_on(self):
        """Turn the device on."""
        self.itachip2ir.send(self.modaddr,self.connaddr,"ON",1)
        self.schedule_update_ha_state()

    def turn_off(self):
        """Turn the device off."""
        self.itachip2ir.send(self.modaddr,self.connaddr,"OFF",1)
        self.schedule_update_ha_state()
