# README #

## ITachIP2IR library ##

A C++ library with python bindings for sending IR commands to an ITach IP2IR gateway.

It can be given an ip address and port to connect to, or it can be given a mac address and will listen for broadcasts from any ITach gateway that matches the mac address.

It gets the IR commands from a command library file that follows the format of:

```
CH1
0000 006D 0000 0022 00AC 00AB 0015 0041 0015 0041 0015 0041 0015 0016 0015 0016 0015 0016 0015 0016 0015 0016 0015 0041 0015 0041 0015 0041 0015 0016 0015 0016 0015 0016 0015 0016 0015 0016 0015 0016 0015 0016 0015 0041 0015 0016 0015 0016 0015 0016 0015 0016 0015 0016 0015 0041 0015 0041 0015 0016 0015 0041 0015 0041 0015 0041 0015 0041 0015 0041 0015 0689

CH2
0000 006D 0000 0022 00AC 00AB 0015 0041 0015 0041 0015 0041 0015 0016 0015 0016 0015 0016 0015 0016 0015 0016 0015 0041 0015 0041 0015 0041 0015 0016 0015 0016 0015 0016 0015 0016 0015 0016 0015 0041 0015 0016 0015 0041 0015 0016 0015 0016 0015 0016 0015 0016 0015 0016 0015 0016 0015 0041 0015 0016 0015 0041 0015 0041 0015 0041 0015 0041 0015 0041 0015 0689
```

## Dependencies ##
  * CMake 2.8
  * Python 2 or 3 (optional)

## How to build ##
  * cmake .

## How to run ##
  * Command line interface for sending one shot ir commands
    `./itachip2ir [ip-of-itach] [itach-listening-port] [ir-commands.txt] [name-of-ir-command] [itach-mod] [itach-conn] [message-count]`

## License ##
  * MIT License


Any questions please contact: alan@lightningtoads.com