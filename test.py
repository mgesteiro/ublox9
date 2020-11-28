#!/usr/bin/env python3

import serial, ublox9

print("ublox9 message dumping demo:\nstarting ...\n")

sport = serial.Serial("/dev/tty.usbserial-A50285BI", 115200, timeout=1)
ureader = ublox9.Ublox9Reader(sport)

try:
    for message in ureader:
        print(message)
except:
    pass

print("\nfinished!\n")
