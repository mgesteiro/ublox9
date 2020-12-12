"""
ublox9 globals and constants definitions

Based on the ZED-F9P u-blox GNSS receiver documentation:
https://www.u-blox.com/en/docs/UBX-18010854

Created on 27 Nov 2020

@author: mgesteiro
"""
MSG_NMEA = 2
MSG_UBX = 3
MSG_RTCM = 4

VALGET_RAM = bytes([0b0000])  # 0
VALGET_BBR = bytes([0b0001])  # 1
VALGET_FLASH = bytes([0b0010])  # 2
VALGET_DEFAULT = bytes([0b0111])  # 7

VALSET_RAM = bytes([0b0001])  # 1
VALSET_BBR = bytes([0b0010])  # 2
VALSET_FLASH = bytes([0b0100])  # 3
VALSET_ALL = bytes([0b0111])  # 7