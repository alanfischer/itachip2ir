"""
Control an itach ip2ir gateway using libitachip2ir
"""
from ctypes import *
import os
import sys

libitachip2ir = None
for ext in ['so','dylib','dll']:
    for pre in ['lib','']:
        try:
            libitachip2ir = cdll.LoadLibrary(os.path.dirname(__file__) + "/" + pre + "itachip2ir." + ext)
            break
        except OSError:
            pass
if libitachip2ir is None:
    raise OSError("Unable to find itachip2ir library")

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

if sys.version_info >= (3, 0):
    def tochar(data):
        return bytes(data,'utf-8')
else:
    def tochar(data):
        return str(data)

class ITachIP2IR(object):
    def __init__(self, mac, ip, port):
        self.itachip2ir = libitachip2ir.ITachIP2IR_new(tochar(mac), tochar(ip), port)

    def __del__(self):
        libitachip2ir.ITachIP2IR_delete(self.itachip2ir)

    def update(self):
        libitachip2ir.ITachIP2IR_update(self.itachip2ir)

    def addDevice(self, name, modaddr, connaddr, cmddata):
        return libitachip2ir.ITachIP2IR_addDevice(self.itachip2ir, tochar(name), modaddr, connaddr, tochar(cmddata))

    def send(self, device, command, count):
        libitachip2ir.ITachIP2IR_send(self.itachip2ir, tochar(device), tochar(command), count)
