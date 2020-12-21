#!/usr/bin/env python3

import serial
from ublox9.ublox9stream import Ublox9Stream

print("ublox9 message dumping demo:\nstarting ...\n")

try:
    # sport = serial.Serial("/dev/tty.usbserial-A50285BI", 115200, timeout=1)
    sport = serial.Serial("/dev/cu.usbmodem14301", 115200, timeout=1)
    ubs9 = Ublox9Stream(sport)
    for message in ubs9:
        print(message)
except (serial.SerialException, KeyboardInterrupt) as ex:
    print(ex)

print("\nfinished!\n")
