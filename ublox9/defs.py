"""
ublox9 package basic definitions

Reference documents:
ZED-F9P - Interface Description - https://www.u-blox.com/en/docs/UBX-18010854
ZED-F9P - Integration manual - https://www.u-blox.com/en/docs/UBX-18010802
"""
# u-blox generation 9 messages types
MSG_UNKNOWN = 0
MSG_NMEA = 2
MSG_UBX = 3
MSG_RTCM3 = 4

# u-blox generation 9 VALGET possible layers: can't be combined
VALGET_RAM = bytes([0b0000])  # 0
VALGET_BBR = bytes([0b0001])  # 1
VALGET_FLASH = bytes([0b0010])  # 2
VALGET_DEFAULT = bytes([0b0111])  # 7

# u-blox generation 9 VALSET possible layers values: can be combined with OR
VALSET_RAM = bytes([0b0001])  # 1
VALSET_BBR = bytes([0b0010])  # 2
VALSET_FLASH = bytes([0b0100])  # 3
VALSET_ALL = bytes([0b0111])  # 7

