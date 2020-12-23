#!/usr/bin/env python3

import serial
from ublox9 import ublox9stream

print("ublox9 message dumping demo:\nstarting ...\n")

try:
    sport = serial.Serial("/dev/tty.usbmodem14401", 115200, timeout=1)
    ub9stream = ublox9stream.Ublox9Stream(sport)

    for message in ub9stream:
        print(message)

except (serial.SerialException, KeyboardInterrupt) as ex:
    print(ex)

print("\nfinished!\n")
