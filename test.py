#!/usr/bin/env python3

import serial
from ublox9.ublox9stream import Ublox9Stream

print("ublox9 message dumping demo:\nstarting ...\n")

try:
    sport = serial.Serial("/dev/tty.usbmodem14201", 115200, timeout=1)
    ub9stream = Ublox9Stream(sport)
    for message in ub9stream:
        print(message)
except (serial.SerialException, KeyboardInterrupt) as ex:
    print(ex)

print("\nfinished!\n")
