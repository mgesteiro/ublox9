"""
UBX payloads definitions (including generation 9)
"""
# 3.3.5 UBX data types
# https://www.u-blox.com/en/docs/UBX-18010854#page=45&zoom=auto,-70,312
# its value corresponds to its size in bytes
U1 = 1  # unsigned 8-bit integer 0...2^8-1 1
I1 = 1  # signed 8-bit integer, two's complement -2^7...2^7-1 1
X1 = 1  # 8-bit bitfield n/a n/a
U2 = 2  # unsigned little-endian 16-bit integer 0...2^16-1 1
I2 = 2  # signed little-endian 16-bit integer, two's complement -2^15...2^15-1 1
X2 = 2  # 16-bit little-endian bitfield n/a n/a
U4 = 4  # unsigned little-endian 32-bit integer 0...2^32-1 1
I4 = 4  # signed little-endian 32-bit integer, two's complement -2^31...2^31-1 1
X4 = 4  # 32-bit little-endian bitfield n/a n/a
R4 = 4  # IEEE 754 single (32-bit) precision -2^127...2^127 ~ value·2 -24
R8 = 8  # IEEE 754 double (64-bit) precision -2^1023...2^1023 ~ value·2 -53
CH = 1  # ASCII / ISO 8859-1 char (8-bit) n/a n/a
# U:n unsigned bitfield value of  n  bits width var. variable variable
# I:n signed (two's complement) bitfield value of  n  bits width var. variable variable
# S:n signed bitfield value of  n  bits width, in sign (most significant bit) and magnitude (remaining bits) notation var. variable variable

# 3.3.7 UBX repeated fields
# https://www.u-blox.com/en/docs/UBX-18010854#page=46&zoom=auto,-70,468
GROUPS_LENGTH = [
    "N",  # N fixed length groups
    "R",  # Rest of the payload
]

# 1.5.2 GNSS identifiers
# https://www.u-blox.com/en/docs/UBX-18010854#page=16&zoom=auto,-70,377
GNSS_IDENTFIERS = {
    "GPS": 0,  # GPS G 0 1 1 1
    "SBAS": 1,  # SBAS S 1 1 1 1
    "Galileo": 2,  # GAL E 2 n/a 3 3
    "BeiDou": 3,  # BDS B 3 n/a (4) 1 4
    "IMES": 4,  # IMES I 4 n/a n/a n/a
    "QZSS": 5,  # QZSS Q 5 n/a (1) 1 5
    "GLONASS": 6,  # GLO R 6 2 2 2
}


UBX_PAYLOADS = {
    # https://www.u-blox.com/en/docs/UBX-18010854#page=52&zoom=auto,-70,314
    "UBX-ACK-ACK": {
        "clsID": U1,  # 0 U1 - - Class ID of the Acknowledged Message
        "msgID": U1,  # 1 U1 - - Message ID of the Acknowledged Message
    },

    # https://www.u-blox.com/en/docs/UBX-18010854#page=53&zoom=auto,-70,719
    "UBX-ACK-NACK": {
        "clsID": U1,  # 0 U1 - - Class ID of the Not-Acknowledged Message
        "msgID": U1,  # 1 U1 - - Message ID of the Not-Acknowledged Message
    },

    # https://www.u-blox.com/en/docs/UBX-18010854#page=85&zoom=auto,-70,164
    "UBX-CFG-VALGET": {
        "version": U1,  # 0 U1 - - Message version (0x01 for this version)
        "layer": U1,  # 1 U1 - - The  layer  from  which  the  configuration  item  was retrieved: • 0 - RAM layer • 1 - BBR • 2 - Flash • 7 - Default
        "position": U2, # 2 U2 - - Number  of  configuration  items  skipped  in  the  result set  before  constructing  this  message  (mirrors  the equivalent field in the request message)
        "cfgData": ("R", U1) # 4 + n U1  - - Configuration data  (key and value pairs) End of repeated group ( N  times)
    },

    # https://www.u-blox.com/en/docs/UBX-18010854#page=86&zoom=auto,-70,496
    "UBX-CFG-VALSET": { 
        "version": U1,
        "layers": X1,
        "reserved0": 2,  # U1[2]
        "cfgData": ("R", U1)
    },

    # https://www.u-blox.com/en/docs/UBX-18010854#page=132&zoom=auto,-70,545
    "UBX-NAV-PVT": {
        "iTOW": U4,  #  0 - ms GPS time of week of the navigation epoch. See the section iTOW timestamps in Integration manual for details.
        "year": U2,  #  4 - y Year (UTC) 
        "month": U1,  #  6 - month Month, range 1..12 (UTC)
        "day": U1,  #  7 - d Day of month, range 1..31 (UTC)
        "hour": U1,  #  8 - h Hour of day, range 0..23 (UTC)
        "min": U1,  #  9 - min Minute of hour, range 0..59 (UTC)
        "sec": U1,  # 10 - s Seconds of minute, range 0..60 (UTC)
        "valid": X1,  # 11 - - Validity flags bit 0 U :1 validDate - - 1  =  valid  UTC  Date  (see  section  Time  validity  in Integration manual  for details) bit 1 U :1 validTime - - 1 = valid UTC time of day (see section Time validity in Integration manual  for details) bit 2 U :1 fullyResolved - - 1  =  UTC  time  of  day  has  been  fully  resolved  (no seconds uncertainty). Cannot be used to check if time is completely solved. bit 3 U :1 validMag - - 1 = valid magnetic declination
        "tAcc": U4,  # 12 - ns Time accuracy estimate (UTC
        "nano": I4,  # 16 - ns Fraction of second, range -1e9 .. 1e9 (UTC)
        "fixType": U1,  # 20 - - GNSSfix Type: • 0 = no fix • 1 = dead reckoning only • 2 = 2D-fix • 3 = 3D-fix • 4 = GNSS + dead reckoning combined • 5 = time only fix
        "flags": X1,  # 21 - - Fix status flags bit 0 U :1 gnssFixOK - - 1 = valid fix (i.e within DOP & accuracy masks) bit 1 U :1 diffSoln - - 1 = differential corrections were applied bits 4...2 U :3 psmState - - Power   save   mode   state   (see   Power   management section in  Integration Manual  for details. • 0 = PSM is not active • 1 = Enabled (an intermediate state before Acquisition state • 2 = Acquisition • 3 = Tracking • 4 = Power Optimized Tracking • 5 = Inactive bit 5 U :1 headVehValid - - 1 = heading of vehicle is valid, only set if the receiver is in sensor fusion mode bits 7...6 U :2 carrSoln - - Carrier phase range solution status: • 0 = no carrier phase range solution • 1 = carrier phase range solution with floating ambiguities • 2 = carrier phase range solution with fixed ambiguities (not supported for protocol versions less than 20.00)
        "flags2": X1,  # 22 - - Additional flags bit 5 U :1 confirmedAvai - - 1  =  information  about  UTC  Date  and  Time  of  Day validity  confirmation  is  available  (see  section  Time validity in  Integration manual  for details) This flag is only supported in  Protocol Versions 19.00, 19.10, 20.10, 20.20, 20.30, 22.00, 23.00, 23.01, 27 and 28 . bit 6 U :1 confirmedDate - - 1 = UTC Date validity could be confirmed (see section Time validity in  Integration manual  for details) bit 7 U :1 confirmedTime - - 1 = UTC Time of Day could be confirmed (see section Time validity in  Integration manual  for details)
        "numSV": U1,  # 23 - - Number of satellites used in Nav Solution
        "lon": I4,  # 24 1e-7 deg Longitude
        "lat": I4,  # 28 1e-7 deg Latitude
        "height": I4,  # 32 - mm Height above ellipsoid
        "hMSL": I4,  # 36 - mm Height above mean sea level
        "hAcc": U4,  # 40 - mm Horizontal accuracy estimate
        "vAcc": U4,  # 44 - mm Vertical accuracy estimate
        "velN": I4,  # 48 - mm/s NED north velocity
        "velE": I4,  # 52 - mm/s NED east velocity
        "velD": I4,  # 56 - mm/s NED down velocity
        "gSpeed": I4,  # 60 - mm/s Ground Speed (2-D)
        "headMot": I4,  # 64 1e-5 deg Heading of motion (2-D)
        "sAcc": U4,  # 68 - mm/s Speed accuracy estimate
        "headAcc": U4,  # 72 1e-5 deg Heading accuracy estimate (both motion and vehicle)
        "pDOP": U2,  # 76 0.01 - Position DOP
        "flags3": X1,  # 78 - - Additional flags bit 0 U :1 invalidLlh - - 1 = Invalid lon, lat, height and hMSL
        "reserved0": 5,  # U1[5] 79 - - Reserved
        "headVeh": I4,  # 84 1e-5 deg Heading   of   vehicle   (2-D),   this   is   only   valid   when headVehValid is set, otherwise the output is set to the heading of motion
        "magDec": I2,  # 88 1e-2 deg Magnetic declination. Only supported in ADR 4.10 and later.
        "magAcc": U2,  # 90 1e-2 deg Magnetic declination accuracy. Only supported in ADR 4.10 and later.
    },

    # https://www.u-blox.com/en/docs/UBX-18010854#page=141&zoom=auto,-70,719
    "UBX-NAV-SVIN": {
        "version " : U1,  # 0 - - - Message version (0x00 for this version)
        "reserved0" : 3,   # 1 - U1[3] - - Reserved
        "iTOW " : U4,  # 4 - - ms GPS time of week of the  navigation epoch. See the  description of iTOW  for details.
        "dur " : U4,  # 8 - - s Passed survey-in observation time
        "meanX " : I4,  # 12 - - cm Current survey-in mean position ECEF X coordinate
        "meanY " : I4,  # 16 - - cm Current survey-in mean position ECEF Y coordinate
        "meanZ " : I4,  # 20 - - cm Current survey-in mean position ECEF Z coordinate
        "meanXHP " : I1,  # 24 - - 0.1_mm Current high-precision survey-in mean position ECEF X coordinate. Must be in the range -99..+99. The    current    survey-in    mean    position    ECEF    X coordinate, in units of cm, is given by meanX + (0.01 * meanXHP)
        "meanYHP " : I1,  # 25 - - 0.1_mm Current high-precision survey-in mean position ECEF Y coordinate. Must be in the range -99..+99. The    current    survey-in    mean    position    ECEF    Y coordinate, in units of cm, is given by meanY + (0.01 * meanYHP)
        "meanZHP " : I1,  # 26 - - 0.1_mm Current high-precision survey-in mean position ECEF Z coordinate. Must be in the range -99..+99. The    current    survey-in    mean    position    ECEF    Z coordinate, in units of cm, is given by meanZ + (0.01 * meanZHP)
        "reserved1 " : U1,  # 27 - - - Reserved
        "meanAcc " : U4,  # 28 - - 0.1_mm Current survey-in mean position accuracy
        "obs " : U4,  # 32 - - - Number of position observations used during survey- in
        "valid " : U1,  # 36 - - - Survey-in position validity flag, 1 = valid, otherwise 0
        "active " : U1,  # 37 - - - Survey-in in progress flag, 1 = in-progress, otherwise 0
        "reserved2" : 2,   # 38 - U1[2] - - Reserved
    },

    # https://www.u-blox.com/en/docs/UBX-18010854#page=155&zoom=auto,-70,346
    "UBX-SEC-UNIQID": {
        "version": U1,  # 0 U1 - - Message version (0x01 for this version)
        "reserved0": 3,  # 1 U1[3] - - Reserved
        "uniqueId": 5,  # 4 U1[5] - - Unique chip ID
    },

    # https://www.u-blox.com/en/docs/UBX-18010854#page=125&zoom=auto,-70,616
    "UBX-MON-VER": {
        "swVersion": 30,  # 0 CH[30] - - Nul-terminated software version string.
        "hwVersion": 10,  # 30 CH[10] - - Nul-terminated hardware version string
        "extension": ("N", 30),  # 40 + n·30 CH[30] - - Extended software information strings. A series of nul-terminated strings. Each extension field is 30 characters long and contains varying software information. Not all extension fields may appear. Examples of reported information: the software version string of the underlying ROM (when the receiver's firmware is running from flash), the firmware version, the supported protocol version, the module identifier, the flash information structure (FIS) file information, the supported major GNSS, the supported augmentation systems. See Firmware and protocol versions for details.
    },

}
