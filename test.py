#!/usr/bin/env python3

import serial, ublox9

print("ublox9 message dumping demo:\nstarting ...\n")

s = serial.Serial("/dev/tty.usbserial-A50285BI", 115200, timeout=1)
r = ublox9.ublox9Reader(s)

try:
    for message in r:
        print(message)
except:
    pass

print("\nfinished!\n")
