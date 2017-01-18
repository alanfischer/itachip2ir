"""
Control an itach ip2ir gateway using libitachip2ir
"""
from ctypes import *
import os

libitachip2ir = cdll.LoadLibrary(os.path.dirname(__file__) + "/libitachip2ir.dylib")
libitachip2ir.ITachIP2IR_new.argtypes = [c_char_p, c_char_p, c_int]
libitachip2ir.ITachIP2IR_new.restype = c_void_p
libitachip2ir.ITachIP2IR_delete.argtypes = [c_void_p]
libitachip2ir.ITachIP2IR_ready.argtypes = [c_void_p, c_int]
libitachip2ir.ITachIP2IR_ready.restype = c_bool
libitachip2ir.ITachIP2IR_update.argtypes = [c_void_p]
libitachip2ir.ITachIP2IR_addDevice.argtypes = [c_void_p, c_char_p, c_int, c_int, c_char_p]
libitachip2ir.ITachIP2IR_addDevice.restype = c_bool
libitachip2ir.ITachIP2IR_send.argtypes = [c_void_p, c_char_p, c_char_p, c_int]
libitachip2ir.ITachIP2IR_send.restype = c_bool

class ITachIP2IR(object):
    def __init__(self, mac, ip, port):
        self.itachip2ir = libitachip2ir.ITachIP2IR_new(bytes(mac,'utf-8'), bytes(ip,'utf-8'), port)

    def __del__(self):
        libitachip2ir.ITachIP2IR_delete(self.itachip2ir)

    def update(self):
        libitachip2ir.ITachIP2IR_update(self.itachip2ir)

    def addDevice(self, name, modaddr, connaddr, cmddata):
        return libitachip2ir.ITachIP2IR_addDevice(self.itachip2ir, bytes(name,'utf-8'), modaddr, connaddr, bytes(cmddata,'utf-8'))

    def send(self, device, command, count):
        libitachip2ir.ITachIP2IR_send(self.itachip2ir, bytes(device,'utf-8'), bytes(command,'utf-8'), count)
