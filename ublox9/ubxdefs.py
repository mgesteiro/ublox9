"""
UBX protocol and messages handling definitions and functions.
"""
UBX_DISABLED = b"\x00"  # False
UBX_ENABLED = b"\x01"  # True


def to_u1(key: int) -> bytes:
    """wrapper to express an int in u-blox bytes format U1"""
    return key.to_bytes(1, byteorder="little", signed=False)


def to_u4(key: int) -> bytes:
    """wrapper to express an int in u-blox bytes format U4"""
    return key.to_bytes(4, byteorder="little", signed=False)


"""
Section 3.8, UBX messages overview
extracted verbatim from https://www.u-blox.com/en/docs/UBX-18010854#page=49&zoom=auto,-74,575
"""
# UBX-ACK – Acknowledgement and negative acknowledgement messages
UBX_ACK = {
    "UBX-ACK-ACK": b"\x05\x01",  # Message acknowledged (Output)
    "UBX-ACK-NAK": b"\x05\x00",  # Message not acknowledged (Output)
}

# UBX-CFG – Configuration and command messages
UBX_CFG = {
    "UBX-CFG-ANT": b"\x06\x13",  # Antenna control settings (Get/set)
    "UBX-CFG-CFG": b"\x06\x09",  # Clear, save and load configurations (Command)
    "UBX-CFG-DAT": b"\x06\x06",  # Set user-defined datum (Set) • Get currently defined datum (Get)
    "UBX-CFG-DGNSS": b"\x06\x70",  # DGNSS configuration (Get/set)
    "UBX-CFG-GEOFENCE": b"\x06\x69",  # Geofencing configuration (Get/set)
    "UBX-CFG-GNSS": b"\x06\x3e",  # GNSS system configuration (Get/set)
    "UBX-CFG-INF": b"\x06\x02",  # Poll configuration for one protocol (Poll request) • Information message configuration (Get/set)
    "UBX-CFG-ITFM": b"\x06\x39",  # Jamming/interference monitor configuration (Get/set)
    "UBX-CFG-LOGFILTER": b"\x06\x47",  # Data logger configuration (Get/set)
    "UBX-CFG-MSG": b"\x06\x01",  # Poll a message configuration (Poll request) • Set message rate(s) (Get/set) • Set message rate (Get/set)
    "UBX-CFG-NAV5": b"\x06\x24",  # Navigation engine settings (Get/set)
    "UBX-CFG-NAVX5": b"\x06\x23",  # Navigation engine expert settings (Get/set)
    "UBX-CFG-NMEA": b"\x06\x17",  # Extended NMEA protocol configuration V1 (Get/set)
    "UBX-CFG-ODO": b"\x06\x1e",  # Odometer, low-speed COG engine settings (Get/set)
    "UBX-CFG-PRT": b"\x06\x00",  # Polls the configuration for one I/O port (Poll request) • Port configuration for UART ports (Get/set) • Port configuration for USB port (Get/set) • Port configuration for SPI port (Get/set) • Port configuration for I2C (DDC) port (Get/set)
    "UBX-CFG-PWR": b"\x06\x57",  # Put receiver in a defined power state (Set)
    "UBX-CFG-RATE": b"\x06\x08",  # Navigation/measurement rate settings (Get/set)
    "UBX-CFG-RINV": b"\x06\x34",  # Contents of remote inventory (Get/set)
    "UBX-CFG-RST": b"\x06\x04",  # Reset receiver / Clear backup data structures (Command)
    "UBX-CFG-SBAS": b"\x06\x16",  # SBAS configuration (Get/set)
    "UBX-CFG-TMODE3": b"\x06\x71",  # Time mode settings 3 (Get/set)
    "UBX-CFG-TP5": b"\x06\x31",  # Time pulse parameters (Get/set)
    "UBX-CFG-USB": b"\x06\x1b",  # USB configuration (Get/set)
    "UBX-CFG-VALDEL": b"\x06\x8c",  # Delete configuration item values (Set) • Delete configuration item values (with transaction) (Set)
    "UBX-CFG-VALGET": b"\x06\x8b",  # Get configuration items (Poll request) • Configuration items (Polled)
    "UBX-CFG-VALSET": b"\x06\x8a",  # Set configuration item values (Set) • Set configuration item values (with transaction) (Set)
}

# UBX-INF – Information messages
UBX_INF = {
    "UBX-INF-DEBUG": b"\x04\x04",  # ASCII output with debug contents (Output)
    "UBX-INF-ERROR": b"\x04\x00",  # ASCII output with error contents (Output)
    "UBX-INF-NOTICE": b"\x04\x02",  # ASCII output with informational contents (Output)
    "UBX-INF-TEST": b"\x04\x03",  # ASCII output with test contents (Output)
    "UBX-INF-WARNING": b"\x04\x01",  # ASCII output with warning contents (Output)
}

# UBX-LOG – Logging messages
UBX_LOG = {
    "UBX-LOG-CREATE": b"\x21\x07",  # Create log file (Command)
    "UBX-LOG-ERASE": b"\x21\x03",  # Erase logged data (Command)
    "UBX-LOG-FINDTIME": b"\x21\x0e",  # Find index of a log entry based on a given time (Input) • Response to FINDTIME request (Output)
    "UBX-LOG-INFO": b"\x21\x08",  # Poll for log information (Poll request) • Log information (Output)
    "UBX-LOG-RETRIEVE": b"\x21\x09",  # Request log data (Command)
    "UBX-LOG-RETRIEVEPOS": b"\x21\x0b",  # Position fix log entry (Output)
    "UBX-LOG-RETRIEVEPOSEXTRA": b"\x21\x0f",  # Odometer log entry (Output)
    "UBX-LOG-RETRIEVESTRING": b"\x21\x0d",  # Byte string log entry (Output)
    "UBX-LOG-STRING": b"\x21\x04",  # Store arbitrary string in on-board flash (Command)
}

# UBX-MGA – GNSS assistance (A-GNSS) messages
UBX_MGA = {
    "UBX-MGA-ACK": b"\x13\x60",  # Multiple GNSS acknowledge message (Output)
    "UBX-MGA-BDS": b"\x13\x03",  # BeiDou ephemeris assistance (Input) • BeiDou almanac assistance (Input) • BeiDou health assistance (Input) • BeiDou UTC assistance (Input) • BeiDou ionosphere assistance (Input)
    "UBX-MGA-DBD": b"\x13\x80",  # Poll the navigation database (Poll request) • Navigation database dump entry (Input/output)
    "UBX-MGA-GAL": b"\x13\x02",  # Galileo ephemeris assistance (Input) • Galileo almanac assistance (Input) • Galileo GPS time offset assistance (Input) • Galileo UTC assistance (Input)
    "UBX-MGA-GLO": b"\x13\x06",  # GLONASS ephemeris assistance (Input) • GLONASS almanac assistance (Input) • GLONASS auxiliary time offset assistance (Input)
    "UBX-MGA-GPS": b"\x13\x00",  # GPS ephemeris assistance (Input) • GPS almanac assistance (Input) • GPS health assistance (Input) • GPS UTC assistance (Input) • GPS ionosphere assistance (Input)
    "UBX-MGA-INI": b"\x13\x40",  # Initial position assistance (Input) • Initial time assistance (Input) • Initial clock drift assistance (Input) • Initial frequency assistance (Input)
    "UBX-MGA-QZSS": b"\x13\x05",  # QZSS ephemeris assistance (Input) • QZSS almanac assistance (Input) • QZSS health assistance (Input)
}

# UBX-MON – Monitoring messages
UBX_MON = {
    "UBX-MON-COMMS": b"\x0a\x36",  # Communication port information (Periodic/polled)
    "UBX-MON-GNSS": b"\x0a\x28",  # Information message major GNSS selection (Polled)
    "UBX-MON-HW": b"\x0a\x09",  # Hardware status (Periodic/polled)
    "UBX-MON-HW2": b"\x0a\x0b",  # Extended hardware status (Periodic/polled)
    "UBX-MON-HW3": b"\x0a\x37",  # I/O pin status (Periodic/polled)
    "UBX-MON-IO": b"\x0a\x02",  # I/O system status (Periodic/polled)
    "UBX-MON-MSGPP": b"\x0a\x06",  # Message parse and process status (Periodic/polled)
    "UBX-MON-PATCH": b"\x0a\x27",  # Installed patches (Polled)
    "UBX-MON-RF": b"\x0a\x38",  # RF information (Periodic/polled)
    "UBX-MON-RXBUF": b"\x0a\x07",  # Receiver buffer status (Periodic/polled)
    "UBX-MON-RXR": b"\x0a\x21",  # Receiver status information (Output)
    "UBX-MON-SPAN": b"\x0a\x31",  # Signal characteristics (Periodic/polled)
    "UBX-MON-TXBUF": b"\x0a\x08",  # Transmitter buffer status (Periodic/polled)
    "UBX-MON-VER": b"\x0a\x04",  # Receiver and software version (Polled)
}

# UBX-NAV – Navigation solution messages
UBX_NAV = {
    "UBX-NAV-CLOCK": b"\x01\x22",  # Clock solution (Periodic/polled)
    "UBX-NAV-DOP": b"\x01\x04",  # Dilution of precision (Periodic/polled)
    "UBX-NAV-EOE": b"\x01\x61",  # End of epoch (Periodic)
    "UBX-NAV-GEOFENCE": b"\x01\x39",  # Geofencing status (Periodic/polled)
    "UBX-NAV-HPPOSECEF": b"\x01\x13",  # High precision position solution in ECEF (Periodic/polled)
    "UBX-NAV-HPPOSLLH": b"\x01\x14",  # High precision geodetic position solution (Periodic/polled)
    "UBX-NAV-ODO": b"\x01\x09",  # Odometer solution (Periodic/polled)
    "UBX-NAV-ORB": b"\x01\x34",  # GNSS orbit database info (Periodic/polled)
    "UBX-NAV-POSECEF": b"\x01\x01",  # Position solution in ECEF (Periodic/polled)
    "UBX-NAV-POSLLH": b"\x01\x02",  # Geodetic position solution (Periodic/polled)
    "UBX-NAV-PVT": b"\x01\x07",  # Navigation position velocity time solution (Periodic/polled)
    "UBX-NAV-RELPOSNED": b"\x01\x3c",  # Relative positioning information in NED frame (Periodic/polled)
    "UBX-NAV-RESETODO": b"\x01\x10",  # Reset odometer (Command)
    "UBX-NAV-SAT": b"\x01\x35",  # Satellite information (Periodic/polled)
    "UBX-NAV-SBAS": b"\x01\x32",  # SBAS status data (Periodic/polled)
    "UBX-NAV-SIG": b"\x01\x43",  # Signal information (Periodic/polled)
    "UBX-NAV-SLAS": b"\x01\x42",  # QZSS L1S SLAS status data (Periodic/polled)
    "UBX-NAV-STATUS": b"\x01\x03",  # Receiver navigation status (Periodic/polled)
    "UBX-NAV-SVIN": b"\x01\x3b",  # Survey-in data (Periodic/polled)
    "UBX-NAV-TIMEBDS": b"\x01\x24",  # BeiDou time solution (Periodic/polled)
    "UBX-NAV-TIMEGAL": b"\x01\x25",  # Galileo time solution (Periodic/polled)
    "UBX-NAV-TIMEGLO": b"\x01\x23",  # GLONASS time solution (Periodic/polled)
    "UBX-NAV-TIMELS": b"\x01\x26",  # Leap second event information (Periodic/polled)
    "UBX-NAV-TIMEQZSS": b"\x01\x27",  # QZSS time solution (Periodic/polled)
    "UBX-NAV-TIMEUTC": b"\x01\x21",  # UTC time solution (Periodic/polled)
    "UBX-NAV-VELECEF": b"\x01\x11",  # Velocity solution in ECEF (Periodic/polled)
    "UBX-NAV-VELNED": b"\x01\x12",  # Velocity solution in NED frame (Periodic/polled)
}

# UBX-RXM – Receiver manager messages
UBX_RXM = {
    "UBX-RXM-MEASX": b"\x02\x14",  # Satellite measurements for RRLP (Periodic/polled)
    "UBX-RXM-PMREQ": b"\x02\x41",  # Power management request (Command)
    "UBX-RXM-RAWX": b"\x02\x15",  # Multi-GNSS raw measurements (Periodic/polled)
    "UBX-RXM-RLM": b"\x02\x59",  # Galileo SAR short-RLM report (Output) • Galileo SAR long-RLM report (Output)
    "UBX-RXM-RTCM": b"\x02\x32",  # RTCM input status (Output)
    "UBX-RXM-SFRBX": b"\x02\x13",  # Broadcast navigation data subframe (Output)
}

# UBX-SEC – Security messages
UBX_SEC = {
    "UBX-SEC-UNIQID": b"\x27\x03",  # Unique chip ID (Output)
}

# UBX-TIM – Timing messages
UBX_TIM = {
    "UBX-TIM-TM2": b"\x0d\x03",  # Time mark data (Periodic/polled)
    "UBX-TIM-TP": b"\x0d\x01",  # Time pulse time data (Periodic/polled)
    "UBX-TIM-VRFY": b"\x0d\x06",  # Sourced time verification (Periodic/polled)
}

# UBX-UPD – Firmware update messages
UBX_UPD = {
    "UBX-UPD-SOS": b"\x09\x14",  # Poll backup restore status (Poll request) • Create backup in flash (Command) • Clear backup in flash (Command) • Backup creation acknowledge (Output) • System restored from backup (Output)
}

# All the ClassIDs put together
UBX_CLASSIDS = {
    # GROUP: CLASSIDS
    "UBX-ACK": UBX_ACK,  # Acknowledgement and negative acknowledgement messages
    "UBX-CFG": UBX_CFG,  # Configuration and command messages
    "UBX-INF": UBX_INF,  # Information messages
    "UBX-LOG": UBX_LOG,  # Logging messages
    "UBX-MGA": UBX_MGA,  # GNSS assistance (A-GNSS) messages
    "UBX-MON": UBX_MON,  # Monitoring messages
    "UBX-NAV": UBX_NAV,  # Navigation solution messages
    "UBX-RXM": UBX_RXM,  # Receiver manager messages
    "UBX-SEC": UBX_SEC,  # Security messages
    "UBX-TIM": UBX_TIM,  # Timing messages
    "UBX-UPD": UBX_UPD  # Firmware update messages
}

"""
Section 5.8, Configuration overview
extracted verbatim from https://www.u-blox.com/en/docs/UBX-18010854#page=180&zoom=auto,-74,522

These are the configuration key-pairs for the u-blox generation 9 modules.
As of 20201223 not all the keys are ported here yet. See the final CFG_KEYPAIRS
to know exactly which are or aren't.
"""
# CFG-INFMSG: Information message configuration
# Information message configuration for the NMEA and UBX protocols.
# https://www.u-blox.com/en/docs/UBX-18010854#page=184&zoom=auto,-70,539
CFG_INFMSG = {
    "CFG-INFMSG-UBX_I2C": to_u4(0x20920001),  # X1 - - Information message enable flags for the UBX protocol on the I2C interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-UBX_UART1": to_u4(0x20920002),  # X1 - - Information message enable flags for the UBX protocol on the UART1 interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-UBX_UART2": to_u4(0x20920003),  # X1 - - Information message enable flags for the UBX protocol on the UART2 interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-UBX_USB": to_u4(0x20920004),  # X1 - - Information message enable flags for the UBX protocol on the USB interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-UBX_SPI": to_u4(0x20920005),  # X1 - - Information message enable flags for the UBX protocol on the SPI interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-NMEA_I2C": to_u4(0x20920006),  # X1 - - Information message enable flags for the NMEA protocol on the I2C interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-NMEA_UART1": to_u4(0x20920007),  # X1 - - Information message enable flags for the NMEA protocol on the UART1 interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-NMEA_UART2": to_u4(0x20920008),  # X1 - - Information message enable flags for the NMEA protocol on the UART2 interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-NMEA_USB": to_u4(0x20920009),  # X1 - - Information message enable flags for the NMEA protocol on the USB interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-NMEA_SPI": to_u4(0x2092000a),  # X1 - - Information message enable flags for the NMEA protocol on the SPI interface.  See  Table 11  below for a list of possible constants for this item.
}
TBL11_CFG_INFMSG = {  # Table 11
    "DISABLED": b"\x00",  # Disable any message
    "ERROR": b"\x01",  # Enable ERROR information messages
    "WARNING": b"\x02",  # Enable WARNING information messages
    "NOTICE": b"\x04",  # Enable NOTICE information messages
    "TEST": b"\x08",  # Enable TEST information messages
    "DEBUG": b"\x10",  # Enable DEBUG information messages
}

# CFG-MSGOUT: Message output configuration
# For each message and port a separate output rate (per second, per epoch) can be configured.
# https://www.u-blox.com/en/docs/UBX-18010854#page=186&zoom=auto,-70,208
CFG_MSGOUT = {
    "CFG-MSGOUT-NMEA_ID_DTM_I2C": to_u4(0x209100a6),  # U1 - - Output rate of the NMEA-GX-DTM message on port I2C
    "CFG-MSGOUT-NMEA_ID_DTM_SPI": to_u4(0x209100aa),  # U1 - - Output rate of the NMEA-GX-DTM message on port SPI
    "CFG-MSGOUT-NMEA_ID_DTM_UART1": to_u4(0x209100a7),  # U1 - - Output rate of the NMEA-GX-DTM message on port UART1
    "CFG-MSGOUT-NMEA_ID_DTM_UART2": to_u4(0x209100a8),  # U1 - - Output rate of the NMEA-GX-DTM message on port UART2
    "CFG-MSGOUT-NMEA_ID_DTM_USB": to_u4(0x209100a9),  # U1 - - Output rate of the NMEA-GX-DTM message on port USB
    "CFG-MSGOUT-NMEA_ID_GBS_I2C": to_u4(0x209100dd),  # U1 - - Output rate of the NMEA-GX-GBS message on port I2C
    "CFG-MSGOUT-NMEA_ID_GBS_SPI": to_u4(0x209100e1),  # U1 - - Output rate of the NMEA-GX-GBS message on port SPI
    "CFG-MSGOUT-NMEA_ID_GBS_UART1": to_u4(0x209100de),  # U1 - - Output rate of the NMEA-GX-GBS message on port UART1
    "CFG-MSGOUT-NMEA_ID_GBS_UART2": to_u4(0x209100df),  # U1 - - Output rate of the NMEA-GX-GBS message on port UART2
    "CFG-MSGOUT-NMEA_ID_GBS_USB": to_u4(0x209100e0),  # U1 - - Output rate of the NMEA-GX-GBS message on port USB
    "CFG-MSGOUT-NMEA_ID_GGA_I2C": to_u4(0x209100ba),  # U1 - - Output rate of the NMEA-GX-GGA message on port I2C
    "CFG-MSGOUT-NMEA_ID_GGA_SPI": to_u4(0x209100be),  # U1 - - Output rate of the NMEA-GX-GGA message on port SPI
    "CFG-MSGOUT-NMEA_ID_GGA_UART1": to_u4(0x209100bb),  # U1 - - Output rate of the NMEA-GX-GGA message on port UART1
    "CFG-MSGOUT-NMEA_ID_GGA_UART2": to_u4(0x209100bc),  # U1 - - Output rate of the NMEA-GX-GGA message on port UART2
    "CFG-MSGOUT-NMEA_ID_GGA_USB": to_u4(0x209100bd),  # U1 - - Output rate of the NMEA-GX-GGA message on port USB
    "CFG-MSGOUT-NMEA_ID_GLL_I2C": to_u4(0x209100c9),  # U1 - - Output rate of the NMEA-GX-GLL message on port I2C
    "CFG-MSGOUT-NMEA_ID_GLL_SPI": to_u4(0x209100cd),  # U1 - - Output rate of the NMEA-GX-GLL message on port SPI
    "CFG-MSGOUT-NMEA_ID_GLL_UART1": to_u4(0x209100ca),  # U1 - - Output rate of the NMEA-GX-GLL message on port UART1
    "CFG-MSGOUT-NMEA_ID_GLL_UART2": to_u4(0x209100cb),  # U1 - - Output rate of the NMEA-GX-GLL message on port UART2
    "CFG-MSGOUT-NMEA_ID_GLL_USB": to_u4(0x209100cc),  # U1 - - Output rate of the NMEA-GX-GLL message on port USB
    "CFG-MSGOUT-NMEA_ID_GNS_I2C": to_u4(0x209100b5),  # U1 - - Output rate of the NMEA-GX-GNS message on port I2C
    "CFG-MSGOUT-NMEA_ID_GNS_SPI": to_u4(0x209100b9),  # U1 - - Output rate of the NMEA-GX-GNS message on port SPI
    "CFG-MSGOUT-NMEA_ID_GNS_UART1": to_u4(0x209100b6),  # U1 - - Output rate of the NMEA-GX-GNS message on port UART1
    "CFG-MSGOUT-NMEA_ID_GNS_UART2": to_u4(0x209100b7),  # U1 - - Output rate of the NMEA-GX-GNS message on port UART2
    "CFG-MSGOUT-NMEA_ID_GNS_USB": to_u4(0x209100b8),  # U1 - - Output rate of the NMEA-GX-GNS message on port USB
    "CFG-MSGOUT-NMEA_ID_GRS_I2C": to_u4(0x209100ce),  # U1 - - Output rate of the NMEA-GX-GRS message on port I2C
    "CFG-MSGOUT-NMEA_ID_GRS_SPI": to_u4(0x209100d2),  # U1 - - Output rate of the NMEA-GX-GRS message on port SPI
    "CFG-MSGOUT-NMEA_ID_GRS_UART1": to_u4(0x209100cf),  # U1 - - Output rate of the NMEA-GX-GRS message on port UART1
    "CFG-MSGOUT-NMEA_ID_GRS_UART2": to_u4(0x209100d0),  # U1 - - Output rate of the NMEA-GX-GRS message on port UART2
    "CFG-MSGOUT-NMEA_ID_GRS_USB": to_u4(0x209100d1),  # U1 - - Output rate of the NMEA-GX-GRS message on port USB
    "CFG-MSGOUT-NMEA_ID_GSA_I2C": to_u4(0x209100bf),  # U1 - - Output rate of the NMEA-GX-GSA message on port I2C
    "CFG-MSGOUT-NMEA_ID_GSA_SPI": to_u4(0x209100c3),  # U1 - - Output rate of the NMEA-GX-GSA message on port SPI
    "CFG-MSGOUT-NMEA_ID_GSA_UART1": to_u4(0x209100c0),  # U1 - - Output rate of the NMEA-GX-GSA message on port UART1
    "CFG-MSGOUT-NMEA_ID_GSA_UART2": to_u4(0x209100c1),  # U1 - - Output rate of the NMEA-GX-GSA message on port UART2
    "CFG-MSGOUT-NMEA_ID_GSA_USB": to_u4(0x209100c2),  # U1 - - Output rate of the NMEA-GX-GSA message on port USB
    "CFG-MSGOUT-NMEA_ID_GST_I2C": to_u4(0x209100d3),  # U1 - - Output rate of the NMEA-GX-GST message on port I2C
    "CFG-MSGOUT-NMEA_ID_GST_SPI": to_u4(0x209100d7),  # U1 - - Output rate of the NMEA-GX-GST message on port SPI
    "CFG-MSGOUT-NMEA_ID_GST_UART1": to_u4(0x209100d4),  # U1 - - Output rate of the NMEA-GX-GST message on port UART1
    "CFG-MSGOUT-NMEA_ID_GST_UART2": to_u4(0x209100d5),  # U1 - - Output rate of the NMEA-GX-GST message on port UART2
    "CFG-MSGOUT-NMEA_ID_GST_USB": to_u4(0x209100d6),  # U1 - - Output rate of the NMEA-GX-GST message on port USB
    "CFG-MSGOUT-NMEA_ID_GSV_I2C": to_u4(0x209100c4),  # U1 - - Output rate of the NMEA-GX-GSV message on port I2C
    "CFG-MSGOUT-NMEA_ID_GSV_SPI": to_u4(0x209100c8),  # U1 - - Output rate of the NMEA-GX-GSV message on port SPI
    "CFG-MSGOUT-NMEA_ID_GSV_UART1": to_u4(0x209100c5),  # U1 - - Output rate of the NMEA-GX-GSV message on port UART1
    "CFG-MSGOUT-NMEA_ID_GSV_UART2": to_u4(0x209100c6),  # U1 - - Output rate of the NMEA-GX-GSV message on port UART2
    "CFG-MSGOUT-NMEA_ID_GSV_USB": to_u4(0x209100c7),  # U1 - - Output rate of the NMEA-GX-GSV message on port USB
    "CFG-MSGOUT-NMEA_ID_RLM_I2C": to_u4(0x20910400),  # U1 - - Output rate of the NMEA-GX-RLM message on port I2C
    "CFG-MSGOUT-NMEA_ID_RLM_SPI": to_u4(0x20910404),  # U1 - - Output rate of the NMEA-GX-RLM message on port SPI
    "CFG-MSGOUT-NMEA_ID_RLM_UART1": to_u4(0x20910401),  # U1 - - Output rate of the NMEA-GX-RLM message on port UART1
    "CFG-MSGOUT-NMEA_ID_RLM_UART2": to_u4(0x20910402),  # U1 - - Output rate of the NMEA-GX-RLM message on port UART2
    "CFG-MSGOUT-NMEA_ID_RLM_USB": to_u4(0x20910403),  # U1 - - Output rate of the NMEA-GX-RLM message on port USB
    "CFG-MSGOUT-NMEA_ID_RMC_I2C": to_u4(0x209100ab),  # U1 - - Output rate of the NMEA-GX-RMC message on port I2C
    "CFG-MSGOUT-NMEA_ID_RMC_SPI": to_u4(0x209100af),  # U1 - - Output rate of the NMEA-GX-RMC message on port SPI
    "CFG-MSGOUT-NMEA_ID_RMC_UART1": to_u4(0x209100ac),  # U1 - - Output rate of the NMEA-GX-RMC message on port UART1
    "CFG-MSGOUT-NMEA_ID_RMC_UART2": to_u4(0x209100ad),  # U1 - - Output rate of the NMEA-GX-RMC message on port UART2
    "CFG-MSGOUT-NMEA_ID_RMC_USB": to_u4(0x209100ae),  # U1 - - Output rate of the NMEA-GX-RMC message on port USB
    "CFG-MSGOUT-NMEA_ID_VLW_I2C": to_u4(0x209100e7),  # U1 - - Output rate of the NMEA-GX-VLW message on port I2C
    "CFG-MSGOUT-NMEA_ID_VLW_SPI": to_u4(0x209100eb),  # U1 - - Output rate of the NMEA-GX-VLW message on port SPI
    "CFG-MSGOUT-NMEA_ID_VLW_UART1": to_u4(0x209100e8),  # U1 - - Output rate of the NMEA-GX-VLW message on port UART1
    "CFG-MSGOUT-NMEA_ID_VLW_UART2": to_u4(0x209100e9),  # U1 - - Output rate of the NMEA-GX-VLW message on port UART2
    "CFG-MSGOUT-NMEA_ID_VLW_USB": to_u4(0x209100ea),  # U1 - - Output rate of the NMEA-GX-VLW message on port USB
    "CFG-MSGOUT-NMEA_ID_VTG_I2C": to_u4(0x209100b0),  # U1 - - Output rate of the NMEA-GX-VTG message on port I2C
    "CFG-MSGOUT-NMEA_ID_VTG_SPI": to_u4(0x209100b4),  # U1 - - Output rate of the NMEA-GX-VTG message on port SPI
    "CFG-MSGOUT-NMEA_ID_VTG_UART1": to_u4(0x209100b1),  # U1 - - Output rate of the NMEA-GX-VTG message on port UART1
    "CFG-MSGOUT-NMEA_ID_VTG_UART2": to_u4(0x209100b2),  # U1 - - Output rate of the NMEA-GX-VTG message on port UART2
    "CFG-MSGOUT-NMEA_ID_VTG_USB": to_u4(0x209100b3),  # U1 - - Output rate of the NMEA-GX-VTG message on port USB
    "CFG-MSGOUT-NMEA_ID_ZDA_I2C": to_u4(0x209100d8),  # U1 - - Output rate of the NMEA-GX-ZDA message on port I2C
    "CFG-MSGOUT-NMEA_ID_ZDA_SPI": to_u4(0x209100dc),  # U1 - - Output rate of the NMEA-GX-ZDA message on port SPI
    "CFG-MSGOUT-NMEA_ID_ZDA_UART1": to_u4(0x209100d9),  # U1 - - Output rate of the NMEA-GX-ZDA message on port UART1
    "CFG-MSGOUT-NMEA_ID_ZDA_UART2": to_u4(0x209100da),  # U1 - - Output rate of the NMEA-GX-ZDA message on port UART2
    "CFG-MSGOUT-NMEA_ID_ZDA_USB": to_u4(0x209100db),  # U1 - - Output rate of the NMEA-GX-ZDA message on port USB
    "CFG-MSGOUT-PUBX_ID_POLYP_I2C": to_u4(0x209100ec),  # U1 - - Output rate of the NMEA-GX-PUBX00 message on port I2C
    "CFG-MSGOUT-PUBX_ID_POLYP_SPI": to_u4(0x209100f0),  # U1 - - Output rate of the NMEA-GX-PUBX00 message on port SPI
    "CFG-MSGOUT-PUBX_ID_POLYP_UART1": to_u4(0x209100ed),  # U1 - - Output rate of the NMEA-GX-PUBX00 message on port UART1
    "CFG-MSGOUT-PUBX_ID_POLYP_UART2": to_u4(0x209100ee),  # U1 - - Output rate of the NMEA-GX-PUBX00 message on port UART2
    "CFG-MSGOUT-PUBX_ID_POLYP_USB": to_u4(0x209100ef),  # U1 - - Output rate of the NMEA-GX-PUBX00 message on port USB
    "CFG-MSGOUT-PUBX_ID_POLYS_I2C": to_u4(0x209100f1),  # U1 - - Output rate of the NMEA-GX-PUBX03 message on port I2C
    "CFG-MSGOUT-PUBX_ID_POLYS_SPI": to_u4(0x209100f5),  # U1 - - Output rate of the NMEA-GX-PUBX03 message on port SPI
    "CFG-MSGOUT-PUBX_ID_POLYS_UART1": to_u4(0x209100f2),  # U1 - - Output rate of the NMEA-GX-PUBX03 message on port UART1
    "CFG-MSGOUT-PUBX_ID_POLYS_UART2": to_u4(0x209100f3),  # U1 - - Output rate of the NMEA-GX-PUBX03 message on port UART2
    "CFG-MSGOUT-PUBX_ID_POLYS_USB": to_u4(0x209100f4),  # U1 - - Output rate of the NMEA-GX-PUBX03 message on port USB
    "CFG-MSGOUT-PUBX_ID_POLYT_I2C": to_u4(0x209100f6),  # U1 - - Output rate of the NMEA-GX-PUBX04 message on port I2C
    "CFG-MSGOUT-PUBX_ID_POLYT_SPI": to_u4(0x209100fa),  # U1 - - Output rate of the NMEA-GX-PUBX04 message on port SPI
    "CFG-MSGOUT-PUBX_ID_POLYT_UART1": to_u4(0x209100f7),  # U1 - - Output rate of the NMEA-GX-PUBX04 message on port UART1
    "CFG-MSGOUT-PUBX_ID_POLYT_UART2": to_u4(0x209100f8),  # U1 - - Output rate of the NMEA-GX-PUBX04 message on port UART2
    "CFG-MSGOUT-PUBX_ID_POLYT_USB": to_u4(0x209100f9),  # U1 - - Output rate of the NMEA-GX-PUBX04 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1005_I2C": to_u4(0x209102bd),  # U1 - - Output rate of the RTCM-3X-TYPE1005 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1005_SPI": to_u4(0x209102c1),  # U1 - - Output rate of the RTCM-3X-TYPE1005 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1005_UART1": to_u4(0x209102be),  # U1 - - Output rate of the RTCM-3X-TYPE1005 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1005_UART2": to_u4(0x209102bf),  # U1 - - Output rate of the RTCM-3X-TYPE1005 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1005_USB": to_u4(0x209102c0),  # U1 - - Output rate of the RTCM-3X-TYPE1005 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1074_I2C": to_u4(0x2091035e),  # U1 - - Output rate of the RTCM-3X-TYPE1074 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1074_SPI": to_u4(0x20910362),  # U1 - - Output rate of the RTCM-3X-TYPE1074 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1074_UART1": to_u4(0x2091035f),  # U1 - - Output rate of the RTCM-3X-TYPE1074 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1074_UART2": to_u4(0x20910360),  # U1 - - Output rate of the RTCM-3X-TYPE1074 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1074_USB": to_u4(0x20910361),  # U1 - - Output rate of the RTCM-3X-TYPE1074 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1077_I2C": to_u4(0x209102cc),  # U1 - - Output rate of the RTCM-3X-TYPE1077 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1077_SPI": to_u4(0x209102d0),  # U1 - - Output rate of the RTCM-3X-TYPE1077 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1077_UART1": to_u4(0x209102cd),  # U1 - - Output rate of the RTCM-3X-TYPE1077 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1077_UART2": to_u4(0x209102ce),  # U1 - - Output rate of the RTCM-3X-TYPE1077 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1077_USB": to_u4(0x209102cf),  # U1 - - Output rate of the RTCM-3X-TYPE1077 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1084_I2C": to_u4(0x20910363),  # U1 - - Output rate of the RTCM-3X-TYPE1084 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1084_SPI": to_u4(0x20910367),  # U1 - - Output rate of the RTCM-3X-TYPE1084 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1084_UART1": to_u4(0x20910364),  # U1 - - Output rate of the RTCM-3X-TYPE1084 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1084_UART2": to_u4(0x20910365),  # U1 - - Output rate of the RTCM-3X-TYPE1084 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1084_USB": to_u4(0x20910366),  # U1 - - Output rate of the RTCM-3X-TYPE1084 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1087_I2C": to_u4(0x209102d1),  # U1 - - Output rate of the RTCM-3X-TYPE1087 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1087_SPI": to_u4(0x209102d5),  # U1 - - Output rate of the RTCM-3X-TYPE1087 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1087_UART1": to_u4(0x209102d2),  # U1 - - Output rate of the RTCM-3X-TYPE1087 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1087_UART2": to_u4(0x209102d3),  # U1 - - Output rate of the RTCM-3X-TYPE1087 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1087_USB": to_u4(0x209102d4),  # U1 - - Output rate of the RTCM-3X-TYPE1087 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1094_I2C": to_u4(0x20910368),  # U1 - - Output rate of the RTCM-3X-TYPE1094 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1094_SPI": to_u4(0x2091036c),  # U1 - - Output rate of the RTCM-3X-TYPE1094 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1094_UART1": to_u4(0x20910369),  # U1 - - Output rate of the RTCM-3X-TYPE1094 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1094_UART2": to_u4(0x2091036a),  # U1 - - Output rate of the RTCM-3X-TYPE1094 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1094_USB": to_u4(0x2091036b),  # U1 - - Output rate of the RTCM-3X-TYPE1094 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1097_I2C": to_u4(0x20910318),  # U1 - - Output rate of the RTCM-3X-TYPE1097 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1097_SPI": to_u4(0x2091031c),  # U1 - - Output rate of the RTCM-3X-TYPE1097 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1097_UART1": to_u4(0x20910319),  # U1 - - Output rate of the RTCM-3X-TYPE1097 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1097_UART2": to_u4(0x2091031a),  # U1 - - Output rate of the RTCM-3X-TYPE1097 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1097_USB": to_u4(0x2091031b),  # U1 - - Output rate of the RTCM-3X-TYPE1097 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1124_I2C": to_u4(0x2091036d),  # U1 - - Output rate of the RTCM-3X-TYPE1124 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1124_SPI": to_u4(0x20910371),  # U1 - - Output rate of the RTCM-3X-TYPE1124 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1124_UART1": to_u4(0x2091036e),  # U1 - - Output rate of the RTCM-3X-TYPE1124 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1124_UART2": to_u4(0x2091036f),  # U1 - - Output rate of the RTCM-3X-TYPE1124 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1124_USB": to_u4(0x20910370),  # U1 - - Output rate of the RTCM-3X-TYPE1124 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1127_I2C": to_u4(0x209102d6),  # U1 - - Output rate of the RTCM-3X-TYPE1127 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1127_SPI": to_u4(0x209102da),  # U1 - - Output rate of the RTCM-3X-TYPE1127 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1127_UART1": to_u4(0x209102d7),  # U1 - - Output rate of the RTCM-3X-TYPE1127 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1127_UART2": to_u4(0x209102d8),  # U1 - - Output rate of the RTCM-3X-TYPE1127 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1127_USB": to_u4(0x209102d9),  # U1 - - Output rate of the RTCM-3X-TYPE1127 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1230_I2C": to_u4(0x20910303),  # U1 - - Output rate of the RTCM-3X-TYPE1230 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1230_SPI": to_u4(0x20910307),  # U1 - - Output rate of the RTCM-3X-TYPE1230 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1230_UART1": to_u4(0x20910304),  # U1 - - Output rate of the RTCM-3X-TYPE1230 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1230_UART2": to_u4(0x20910305),  # U1 - - Output rate of the RTCM-3X-TYPE1230 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1230_USB": to_u4(0x20910306),  # U1 - - Output rate of the RTCM-3X-TYPE1230 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE4072_0_I2C": to_u4(0x209102fe),  # U1 - - Output rate of the RTCM-3X-TYPE4072_0 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE4072_0_SPI": to_u4(0x20910302),  # U1 - - Output rate of the RTCM-3X-TYPE4072_0 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE4072_0_UART1": to_u4(0x209102ff),  # U1 - - Output rate of the RTCM-3X-TYPE4072_0 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE4072_0_UART2": to_u4(0x20910300),  # U1 - - Output rate of the RTCM-3X-TYPE4072_0 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE4072_0_USB": to_u4(0x20910301),  # U1 - - Output rate of the RTCM-3X-TYPE4072_0 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE4072_1_I2C": to_u4(0x20910381),  # U1 - - Output rate of the RTCM-3X-TYPE4072_1 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE4072_1_SPI": to_u4(0x20910385),  # U1 - - Output rate of the RTCM-3X-TYPE4072_1 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE4072_1_UART1": to_u4(0x20910382),  # U1 - - Output rate of the RTCM-3X-TYPE4072_1 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE4072_1_UART2": to_u4(0x20910383),  # U1 - - Output rate of the RTCM-3X-TYPE4072_1 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE4072_1_USB": to_u4(0x20910384),  # U1 - - Output rate of the RTCM-3X-TYPE4072_1 message on port USB
    "CFG-MSGOUT-UBX_LOG_INFO_I2C": to_u4(0x20910259),  # U1 - - Output rate of the UBX-LOG-INFO message on port I2C
    "CFG-MSGOUT-UBX_LOG_INFO_SPI": to_u4(0x2091025d),  # U1 - - Output rate of the UBX-LOG-INFO message on port SPI
    "CFG-MSGOUT-UBX_LOG_INFO_UART1": to_u4(0x2091025a),  # U1 - - Output rate of the UBX-LOG-INFO message on port UART1
    "CFG-MSGOUT-UBX_LOG_INFO_UART2": to_u4(0x2091025b),  # U1 - - Output rate of the UBX-LOG-INFO message on port UART2
    "CFG-MSGOUT-UBX_LOG_INFO_USB": to_u4(0x2091025c),  # U1 - - Output rate of the UBX-LOG-INFO message on port USB
    "CFG-MSGOUT-UBX_MON_COMMS_I2C": to_u4(0x2091034f),  # U1 - - Output rate of the UBX-MON-COMMS message on port I2C
    "CFG-MSGOUT-UBX_MON_COMMS_SPI": to_u4(0x20910353),  # U1 - - Output rate of the UBX-MON-COMMS message on port SPI
    "CFG-MSGOUT-UBX_MON_COMMS_UART1": to_u4(0x20910350),  # U1 - - Output rate of the UBX-MON-COMMS message on port UART1
    "CFG-MSGOUT-UBX_MON_COMMS_UART2": to_u4(0x20910351),  # U1 - - Output rate of the UBX-MON-COMMS message on port UART2
    "CFG-MSGOUT-UBX_MON_COMMS_USB": to_u4(0x20910352),  # U1 - - Output rate of the UBX-MON-COMMS message on port USB
    "CFG-MSGOUT-UBX_MON_HW2_I2C": to_u4(0x209101b9),  # U1 - - Output rate of the UBX-MON-HW2 message on port I2C
    "CFG-MSGOUT-UBX_MON_HW2_SPI": to_u4(0x209101bd),  # U1 - - Output rate of the UBX-MON-HW2 message on port SPI
    "CFG-MSGOUT-UBX_MON_HW2_UART1": to_u4(0x209101ba),  # U1 - - Output rate of the UBX-MON-HW2 message on port UART1
    "CFG-MSGOUT-UBX_MON_HW2_UART2": to_u4(0x209101bb),  # U1 - - Output rate of the UBX-MON-HW2 message on port UART2
    "CFG-MSGOUT-UBX_MON_HW2_USB": to_u4(0x209101bc),  # U1 - - Output rate of the UBX-MON-HW2 message on port USB
    "CFG-MSGOUT-UBX_MON_HW3_I2C": to_u4(0x20910354),  # U1 - - Output rate of the UBX-MON-HW3 message on port I2C
    "CFG-MSGOUT-UBX_MON_HW3_SPI": to_u4(0x20910358),  # U1 - - Output rate of the UBX-MON-HW3 message on port SPI
    "CFG-MSGOUT-UBX_MON_HW3_UART1": to_u4(0x20910355),  # U1 - - Output rate of the UBX-MON-HW3 message on port UART1
    "CFG-MSGOUT-UBX_MON_HW3_UART2": to_u4(0x20910356),  # U1 - - Output rate of the UBX-MON-HW3 message on port UART2
    "CFG-MSGOUT-UBX_MON_HW3_USB": to_u4(0x20910357),  # U1 - - Output rate of the UBX-MON-HW3 message on port USB
    "CFG-MSGOUT-UBX_MON_HW_I2C": to_u4(0x209101b4),  # U1 - - Output rate of the UBX-MON-HW message on port I2C
    "CFG-MSGOUT-UBX_MON_HW_SPI": to_u4(0x209101b8),  # U1 - - Output rate of the UBX-MON-HW message on port SPI
    "CFG-MSGOUT-UBX_MON_HW_UART1": to_u4(0x209101b5),  # U1 - - Output rate of the UBX-MON-HW message on port UART1
    "CFG-MSGOUT-UBX_MON_HW_UART2": to_u4(0x209101b6),  # U1 - - Output rate of the UBX-MON-HW message on port UART2
    "CFG-MSGOUT-UBX_MON_HW_USB": to_u4(0x209101b7),  # U1 - - Output rate of the UBX-MON-HW message on port USB
    "CFG-MSGOUT-UBX_MON_IO_I2C": to_u4(0x209101a5),  # U1 - - Output rate of the UBX-MON-IO message on port I2C
    "CFG-MSGOUT-UBX_MON_IO_SPI": to_u4(0x209101a9),  # U1 - - Output rate of the UBX-MON-IO message on port SPI
    "CFG-MSGOUT-UBX_MON_IO_UART1": to_u4(0x209101a6),  # U1 - - Output rate of the UBX-MON-IO message on port UART1
    "CFG-MSGOUT-UBX_MON_IO_UART2": to_u4(0x209101a7),  # U1 - - Output rate of the UBX-MON-IO message on port UART2
    "CFG-MSGOUT-UBX_MON_IO_USB": to_u4(0x209101a8),  # U1 - - Output rate of the UBX-MON-IO message on port USB
    "CFG-MSGOUT-UBX_MON_MSGPP_I2C": to_u4(0x20910196),  # U1 - - Output rate of the UBX-MON-MSGPP message on port I2C
    "CFG-MSGOUT-UBX_MON_MSGPP_SPI": to_u4(0x2091019a),  # U1 - - Output rate of the UBX-MON-MSGPP message on port SPI
    "CFG-MSGOUT-UBX_MON_MSGPP_UART1": to_u4(0x20910197),  # U1 - - Output rate of the UBX-MON-MSGPP message on port UART1
    "CFG-MSGOUT-UBX_MON_MSGPP_UART2": to_u4(0x20910198),  # U1 - - Output rate of the UBX-MON-MSGPP message on port UART2
    "CFG-MSGOUT-UBX_MON_MSGPP_USB": to_u4(0x20910199),  # U1 - - Output rate of the UBX-MON-MSGPP message on port USB
    "CFG-MSGOUT-UBX_MON_RF_I2C": to_u4(0x20910359),  # U1 - - Output rate of the UBX-MON-RF message on port I2C
    "CFG-MSGOUT-UBX_MON_RF_SPI": to_u4(0x2091035d),  # U1 - - Output rate of the UBX-MON-RF message on port SPI
    "CFG-MSGOUT-UBX_MON_RF_UART1": to_u4(0x2091035a),  # U1 - - Output rate of the UBX-MON-RF message on port UART1
    "CFG-MSGOUT-UBX_MON_RF_UART2": to_u4(0x2091035b),  # U1 - - Output rate of the UBX-MON-RF message on port UART2
    "CFG-MSGOUT-UBX_MON_RF_USB": to_u4(0x2091035c),  # U1 - - Output rate of the UBX-MON-RF message on port USB
    "CFG-MSGOUT-UBX_MON_RXBUF_I2C": to_u4(0x209101a0),  # U1 - - Output rate of the UBX-MON-RXBUF message on port I2C
    "CFG-MSGOUT-UBX_MON_RXBUF_SPI": to_u4(0x209101a4),  # U1 - - Output rate of the UBX-MON-RXBUF message on port SPI
    "CFG-MSGOUT-UBX_MON_RXBUF_UART1": to_u4(0x209101a1),  # U1 - - Output rate of the UBX-MON-RXBUF message on port UART1
    "CFG-MSGOUT-UBX_MON_RXBUF_UART2": to_u4(0x209101a2),  # U1 - - Output rate of the UBX-MON-RXBUF message on port UART2
    "CFG-MSGOUT-UBX_MON_RXBUF_USB": to_u4(0x209101a3),  # U1 - - Output rate of the UBX-MON-RXBUF message on port USB
    "CFG-MSGOUT-UBX_MON_RXR_I2C": to_u4(0x20910187),  # U1 - - Output rate of the UBX-MON-RXR message on port I2C
    "CFG-MSGOUT-UBX_MON_RXR_SPI": to_u4(0x2091018b),  # U1 - - Output rate of the UBX-MON-RXR message on port SPI
    "CFG-MSGOUT-UBX_MON_RXR_UART1": to_u4(0x20910188),  # U1 - - Output rate of the UBX-MON-RXR message on port UART1
    "CFG-MSGOUT-UBX_MON_RXR_UART2": to_u4(0x20910189),  # U1 - - Output rate of the UBX-MON-RXR message on port UART2
    "CFG-MSGOUT-UBX_MON_RXR_USB": to_u4(0x2091018a),  # U1 - - Output rate of the UBX-MON-RXR message on port USB
    "CFG-MSGOUT-UBX_MON_SPAN_I2C": to_u4(0x2091038b),  # U1 - - Output rate of the UBX-MON-SPAN message on port I2C
    "CFG-MSGOUT-UBX_MON_SPAN_SPI": to_u4(0x2091038f),  # U1 - - Output rate of the UBX-MON-SPAN message on port SPI
    "CFG-MSGOUT-UBX_MON_SPAN_UART1": to_u4(0x2091038c),  # U1 - - Output rate of the UBX-MON-SPAN message on port UART1
    "CFG-MSGOUT-UBX_MON_SPAN_UART2": to_u4(0x2091038d),  # U1 - - Output rate of the UBX-MON-SPAN message on port UART2
    "CFG-MSGOUT-UBX_MON_SPAN_USB": to_u4(0x2091038e),  # U1 - - Output rate of the UBX-MON-SPAN message on port USB
    "CFG-MSGOUT-UBX_MON_TXBUF_I2C": to_u4(0x2091019b),  # U1 - - Output rate of the UBX-MON-TXBUF message on port I2C
    "CFG-MSGOUT-UBX_MON_TXBUF_SPI": to_u4(0x2091019f),  # U1 - - Output rate of the UBX-MON-TXBUF message on port SPI
    "CFG-MSGOUT-UBX_MON_TXBUF_UART1": to_u4(0x2091019c),  # U1 - - Output rate of the UBX-MON-TXBUF message on port UART1
    "CFG-MSGOUT-UBX_MON_TXBUF_UART2": to_u4(0x2091019d),  # U1 - - Output rate of the UBX-MON-TXBUF message on port UART2
    "CFG-MSGOUT-UBX_MON_TXBUF_USB": to_u4(0x2091019e),  # U1 - - Output rate of the UBX-MON-TXBUF message on port USB
    "CFG-MSGOUT-UBX_NAV_CLOCK_I2C": to_u4(0x20910065),  # U1 - - Output rate of the UBX-NAV-CLOCK message on port I2C
    "CFG-MSGOUT-UBX_NAV_CLOCK_SPI": to_u4(0x20910069),  # U1 - - Output rate of the UBX-NAV-CLOCK message on port SPI
    "CFG-MSGOUT-UBX_NAV_CLOCK_UART1": to_u4(0x20910066),  # U1 - - Output rate of the UBX-NAV-CLOCK message on port UART1
    "CFG-MSGOUT-UBX_NAV_CLOCK_UART2": to_u4(0x20910067),  # U1 - - Output rate of the UBX-NAV-CLOCK message on port UART2
    "CFG-MSGOUT-UBX_NAV_CLOCK_USB": to_u4(0x20910068),  # U1 - - Output rate of the UBX-NAV-CLOCK message on port USB
    "CFG-MSGOUT-UBX_NAV_DOP_I2C": to_u4(0x20910038),  # U1 - - Output rate of the UBX-NAV-DOP message on port I2C
    "CFG-MSGOUT-UBX_NAV_DOP_SPI": to_u4(0x2091003c),  # U1 - - Output rate of the UBX-NAV-DOP message on port SPI
    "CFG-MSGOUT-UBX_NAV_DOP_UART1": to_u4(0x20910039),  # U1 - - Output rate of the UBX-NAV-DOP message on port UART1
    "CFG-MSGOUT-UBX_NAV_DOP_UART2": to_u4(0x2091003a),  # U1 - - Output rate of the UBX-NAV-DOP message on port UART2
    "CFG-MSGOUT-UBX_NAV_DOP_USB": to_u4(0x2091003b),  # U1 - - Output rate of the UBX-NAV-DOP message on port USB
    "CFG-MSGOUT-UBX_NAV_EOE_I2C": to_u4(0x2091015f),  # U1 - - Output rate of the UBX-NAV-EOE message on port I2C
    "CFG-MSGOUT-UBX_NAV_EOE_SPI": to_u4(0x20910163),  # U1 - - Output rate of the UBX-NAV-EOE message on port SPI
    "CFG-MSGOUT-UBX_NAV_EOE_UART1": to_u4(0x20910160),  # U1 - - Output rate of the UBX-NAV-EOE message on port UART1
    "CFG-MSGOUT-UBX_NAV_EOE_UART2": to_u4(0x20910161),  # U1 - - Output rate of the UBX-NAV-EOE message on port UART2
    "CFG-MSGOUT-UBX_NAV_EOE_USB": to_u4(0x20910162),  # U1 - - Output rate of the UBX-NAV-EOE message on port USB
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_I2C": to_u4(0x209100a1),  # U1 - - Output rate of the UBX-NAV-GEOFENCE message on port I2C
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_SPI": to_u4(0x209100a5),  # U1 - - Output rate of the UBX-NAV-GEOFENCE message on port SPI
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_UART1": to_u4(0x209100a2),  # U1 - - Output rate of the UBX-NAV-GEOFENCE message on port UART1
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_UART2": to_u4(0x209100a3),  # U1 - - Output rate of the UBX-NAV-GEOFENCE message on port UART2
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_USB": to_u4(0x209100a4),  # U1 - - Output rate of the UBX-NAV-GEOFENCE message on port USB
    "CFG-MSGOUT-UBX_NAV_HPPOSECEF_I2C": to_u4(0x2091002e),  # U1 - - Output rate of the UBX-NAV-HPPOSECEF message on port I2C
    "CFG-MSGOUT-UBX_NAV_HPPOSECEF_SPI": to_u4(0x20910032),  # U1 - - Output rate of the UBX-NAV-HPPOSECEF message on port SPI
    "CFG-MSGOUT-UBX_NAV_HPPOSECEF_UART1": to_u4(0x2091002f),  # U1 - - Output rate of the UBX-NAV-HPPOSECEF message on port UART1
    "CFG-MSGOUT-UBX_NAV_HPPOSECEF_UART2": to_u4(0x20910030),  # U1 - - Output rate of the UBX-NAV-HPPOSECEF message on port UART2
    "CFG-MSGOUT-UBX_NAV_HPPOSECEF_USB": to_u4(0x20910031),  # U1 - - Output rate of the UBX-NAV-HPPOSECEF message on port USB
    "CFG-MSGOUT-UBX_NAV_HPPOSLLH_I2C": to_u4(0x20910033),  # U1 - - Output rate of the UBX-NAV-HPPOSLLH message on port I2C
    "CFG-MSGOUT-UBX_NAV_HPPOSLLH_SPI": to_u4(0x20910037),  # U1 - - Output rate of the UBX-NAV-HPPOSLLH message on port SPI
    "CFG-MSGOUT-UBX_NAV_HPPOSLLH_UART1": to_u4(0x20910034),  # U1 - - Output rate of the UBX-NAV-HPPOSLLH message on port UART1
    "CFG-MSGOUT-UBX_NAV_HPPOSLLH_UART2": to_u4(0x20910035),  # U1 - - Output rate of the UBX-NAV-HPPOSLLH message on port UART2
    "CFG-MSGOUT-UBX_NAV_HPPOSLLH_USB": to_u4(0x20910036),  # U1 - - Output rate of the UBX-NAV-HPPOSLLH message on port USB
    "CFG-MSGOUT-UBX_NAV_ODO_I2C": to_u4(0x2091007e),  # U1 - - Output rate of the UBX-NAV-ODO message on port I2C
    "CFG-MSGOUT-UBX_NAV_ODO_SPI": to_u4(0x20910082),  # U1 - - Output rate of the UBX-NAV-ODO message on port SPI
    "CFG-MSGOUT-UBX_NAV_ODO_UART1": to_u4(0x2091007f),  # U1 - - Output rate of the UBX-NAV-ODO message on port UART1
    "CFG-MSGOUT-UBX_NAV_ODO_UART2": to_u4(0x20910080),  # U1 - - Output rate of the UBX-NAV-ODO message on port UART2
    "CFG-MSGOUT-UBX_NAV_ODO_USB": to_u4(0x20910081),  # U1 - - Output rate of the UBX-NAV-ODO message on port USB
    "CFG-MSGOUT-UBX_NAV_ORB_I2C": to_u4(0x20910010),  # U1 - - Output rate of the UBX-NAV-ORB message on port I2C
    "CFG-MSGOUT-UBX_NAV_ORB_SPI": to_u4(0x20910014),  # U1 - - Output rate of the UBX-NAV-ORB message on port SPI
    "CFG-MSGOUT-UBX_NAV_ORB_UART1": to_u4(0x20910011),  # U1 - - Output rate of the UBX-NAV-ORB message on port UART1
    "CFG-MSGOUT-UBX_NAV_ORB_UART2": to_u4(0x20910012),  # U1 - - Output rate of the UBX-NAV-ORB message on port UART2
    "CFG-MSGOUT-UBX_NAV_ORB_USB": to_u4(0x20910013),  # U1 - - Output rate of the UBX-NAV-ORB message on port USB
    "CFG-MSGOUT-UBX_NAV_POSECEF_I2C": to_u4(0x20910024),  # U1 - - Output rate of the UBX-NAV-POSECEF message on port I2C
    "CFG-MSGOUT-UBX_NAV_POSECEF_SPI": to_u4(0x20910028),  # U1 - - Output rate of the UBX-NAV-POSECEF message on port SPI
    "CFG-MSGOUT-UBX_NAV_POSECEF_UART1": to_u4(0x20910025),  # U1 - - Output rate of the UBX-NAV-POSECEF message on port UART1
    "CFG-MSGOUT-UBX_NAV_POSECEF_UART2": to_u4(0x20910026),  # U1 - - Output rate of the UBX-NAV-POSECEF message on port UART2
    "CFG-MSGOUT-UBX_NAV_POSECEF_USB": to_u4(0x20910027),  # U1 - - Output rate of the UBX-NAV-POSECEF message on port USB
    "CFG-MSGOUT-UBX_NAV_POSLLH_I2C": to_u4(0x20910029),  # U1 - - Output rate of the UBX-NAV-POSLLH message on port I2C
    "CFG-MSGOUT-UBX_NAV_POSLLH_SPI": to_u4(0x2091002d),  # U1 - - Output rate of the UBX-NAV-POSLLH message on port SPI
    "CFG-MSGOUT-UBX_NAV_POSLLH_UART1": to_u4(0x2091002a),  # U1 - - Output rate of the UBX-NAV-POSLLH message on port UART1
    "CFG-MSGOUT-UBX_NAV_POSLLH_UART2": to_u4(0x2091002b),  # U1 - - Output rate of the UBX-NAV-POSLLH message on port UART2
    "CFG-MSGOUT-UBX_NAV_POSLLH_USB": to_u4(0x2091002c),  # U1 - - Output rate of the UBX-NAV-POSLLH message on port USB
    "CFG-MSGOUT-UBX_NAV_PVT_I2C": to_u4(0x20910006),  # U1 - - Output rate of the UBX-NAV-PVT message on port I2C
    "CFG-MSGOUT-UBX_NAV_PVT_SPI": to_u4(0x2091000a),  # U1 - - Output rate of the UBX-NAV-PVT message on port SPI
    "CFG-MSGOUT-UBX_NAV_PVT_UART1": to_u4(0x20910007),  # U1 - - Output rate of the UBX-NAV-PVT message on port UART1
    "CFG-MSGOUT-UBX_NAV_PVT_UART2": to_u4(0x20910008),  # U1 - - Output rate of the UBX-NAV-PVT message on port UART2
    "CFG-MSGOUT-UBX_NAV_PVT_USB": to_u4(0x20910009),  # U1 - - Output rate of the UBX-NAV-PVT message on port USB
    "CFG-MSGOUT-UBX_NAV_RELPOSNED_I2C": to_u4(0x2091008d),  # U1 - - Output rate of the UBX-NAV-RELPOSNED message on port I2C
    "CFG-MSGOUT-UBX_NAV_RELPOSNED_SPI": to_u4(0x20910091),  # U1 - - Output rate of the UBX-NAV-RELPOSNED message on port SPI
    "CFG-MSGOUT-UBX_NAV_RELPOSNED_UART1": to_u4(0x2091008e),  # U1 - - Output rate of the UBX-NAV-RELPOSNED message on port UART1
    "CFG-MSGOUT-UBX_NAV_RELPOSNED_UART2": to_u4(0x2091008f),  # U1 - - Output rate of the UBX-NAV-RELPOSNED message on port UART2
    "CFG-MSGOUT-UBX_NAV_RELPOSNED_USB": to_u4(0x20910090),  # U1 - - Output rate of the UBX-NAV-RELPOSNED message on port USB
    "CFG-MSGOUT-UBX_NAV_SAT_I2C": to_u4(0x20910015),  # U1 - - Output rate of the UBX-NAV-SAT message on port I2C
    "CFG-MSGOUT-UBX_NAV_SAT_SPI": to_u4(0x20910019),  # U1 - - Output rate of the UBX-NAV-SAT message on port SPI
    "CFG-MSGOUT-UBX_NAV_SAT_UART1": to_u4(0x20910016),  # U1 - - Output rate of the UBX-NAV-SAT message on port UART1
    "CFG-MSGOUT-UBX_NAV_SAT_UART2": to_u4(0x20910017),  # U1 - - Output rate of the UBX-NAV-SAT message on port UART2
    "CFG-MSGOUT-UBX_NAV_SAT_USB": to_u4(0x20910018),  # U1 - - Output rate of the UBX-NAV-SAT message on port USB
    "CFG-MSGOUT-UBX_NAV_SBAS_I2C": to_u4(0x2091006a),  # U1 - - Output rate of the UBX-NAV-SBAS message on port I2C
    "CFG-MSGOUT-UBX_NAV_SBAS_SPI": to_u4(0x2091006e),  # U1 - - Output rate of the UBX-NAV-SBAS message on port SPI
    "CFG-MSGOUT-UBX_NAV_SBAS_UART1": to_u4(0x2091006b),  # U1 - - Output rate of the UBX-NAV-SBAS message on port UART1
    "CFG-MSGOUT-UBX_NAV_SBAS_UART2": to_u4(0x2091006c),  # U1 - - Output rate of the UBX-NAV-SBAS message on port UART2
    "CFG-MSGOUT-UBX_NAV_SBAS_USB": to_u4(0x2091006d),  # U1 - - Output rate of the UBX-NAV-SBAS message on port USB
    "CFG-MSGOUT-UBX_NAV_SIG_I2C": to_u4(0x20910345),  # U1 - - Output rate of the UBX-NAV-SIG message on port I2C
    "CFG-MSGOUT-UBX_NAV_SIG_SPI": to_u4(0x20910349),  # U1 - - Output rate of the UBX-NAV-SIG message on port SPI
    "CFG-MSGOUT-UBX_NAV_SIG_UART1": to_u4(0x20910346),  # U1 - - Output rate of the UBX-NAV-SIG message on port UART1
    "CFG-MSGOUT-UBX_NAV_SIG_UART2": to_u4(0x20910347),  # U1 - - Output rate of the UBX-NAV-SIG message on port UART2
    "CFG-MSGOUT-UBX_NAV_SIG_USB": to_u4(0x20910348),  # U1 - - Output rate of the UBX-NAV-SIG message on port USB
    "CFG-MSGOUT-UBX_NAV_SLAS_I2C": to_u4(0x20910336),  # U1 - - Output rate of the UBX-NAV-SLAS message on port I2C
    "CFG-MSGOUT-UBX_NAV_SLAS_SPI": to_u4(0x2091033a),  # U1 - - Output rate of the UBX-NAV-SLAS message on port SPI
    "CFG-MSGOUT-UBX_NAV_SLAS_UART1": to_u4(0x20910337),  # U1 - - Output rate of the UBX-NAV-SLAS message on port UART1
    "CFG-MSGOUT-UBX_NAV_SLAS_UART2": to_u4(0x20910338),  # U1 - - Output rate of the UBX-NAV-SLAS message on port UART2
    "CFG-MSGOUT-UBX_NAV_SLAS_USB": to_u4(0x20910339),  # U1 - - Output rate of the UBX-NAV-SLAS message on port USB
    "CFG-MSGOUT-UBX_NAV_STATUS_I2C": to_u4(0x2091001a),  # U1 - - Output rate of the UBX-NAV-STATUS message on port I2C
    "CFG-MSGOUT-UBX_NAV_STATUS_SPI": to_u4(0x2091001e),  # U1 - - Output rate of the UBX-NAV-STATUS message on port SPI
    "CFG-MSGOUT-UBX_NAV_STATUS_UART1": to_u4(0x2091001b),  # U1 - - Output rate of the UBX-NAV-STATUS message on port UART1
    "CFG-MSGOUT-UBX_NAV_STATUS_UART2": to_u4(0x2091001c),  # U1 - - Output rate of the UBX-NAV-STATUS message on port UART2
    "CFG-MSGOUT-UBX_NAV_STATUS_USB": to_u4(0x2091001d),  # U1 - - Output rate of the UBX-NAV-STATUS message on port USB
    "CFG-MSGOUT-UBX_NAV_SVIN_I2C": to_u4(0x20910088),  # U1 - - Output rate of the UBX-NAV-SVIN message on port I2C
    "CFG-MSGOUT-UBX_NAV_SVIN_SPI": to_u4(0x2091008c),  # U1 - - Output rate of the UBX-NAV-SVIN message on port SPI
    "CFG-MSGOUT-UBX_NAV_SVIN_UART1": to_u4(0x20910089),  # U1 - - Output rate of the UBX-NAV-SVIN message on port UART1
    "CFG-MSGOUT-UBX_NAV_SVIN_UART2": to_u4(0x2091008a),  # U1 - - Output rate of the UBX-NAV-SVIN message on port UART2
    "CFG-MSGOUT-UBX_NAV_SVIN_USB": to_u4(0x2091008b),  # U1 - - Output rate of the UBX-NAV-SVIN message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_I2C": to_u4(0x20910051),  # U1 - - Output rate of the UBX-NAV-TIMEBDS message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_SPI": to_u4(0x20910055),  # U1 - - Output rate of the UBX-NAV-TIMEBDS message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_UART1": to_u4(0x20910052),  # U1 - - Output rate of the UBX-NAV-TIMEBDS message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_UART2": to_u4(0x20910053),  # U1 - - Output rate of the UBX-NAV-TIMEBDS message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_USB": to_u4(0x20910054),  # U1 - - Output rate of the UBX-NAV-TIMEBDS message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_I2C": to_u4(0x20910056),  # U1 - - Output rate of the UBX-NAV-TIMEGAL message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_SPI": to_u4(0x2091005a),  # U1 - - Output rate of the UBX-NAV-TIMEGAL message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_UART1": to_u4(0x20910057),  # U1 - - Output rate of the UBX-NAV-TIMEGAL message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_UART2": to_u4(0x20910058),  # U1 - - Output rate of the UBX-NAV-TIMEGAL message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_USB": to_u4(0x20910059),  # U1 - - Output rate of the UBX-NAV-TIMEGAL message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_I2C": to_u4(0x2091004c),  # U1 - - Output rate of the UBX-NAV-TIMEGLO message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_SPI": to_u4(0x20910050),  # U1 - - Output rate of the UBX-NAV-TIMEGLO message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_UART1": to_u4(0x2091004d),  # U1 - - Output rate of the UBX-NAV-TIMEGLO message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_UART2": to_u4(0x2091004e),  # U1 - - Output rate of the UBX-NAV-TIMEGLO message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_USB": to_u4(0x2091004f),  # U1 - - Output rate of the UBX-NAV-TIMEGLO message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_I2C": to_u4(0x20910047),  # U1 - - Output rate of the UBX-NAV-TIMEGPS message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_SPI": to_u4(0x2091004b),  # U1 - - Output rate of the UBX-NAV-TIMEGPS message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_UART1": to_u4(0x20910048),  # U1 - - Output rate of the UBX-NAV-TIMEGPS message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_UART2": to_u4(0x20910049),  # U1 - - Output rate of the UBX-NAV-TIMEGPS message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_USB": to_u4(0x2091004a),  # U1 - - Output rate of the UBX-NAV-TIMEGPS message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMELS_I2C": to_u4(0x20910060),  # U1 - - Output rate of the UBX-NAV-TIMELS message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMELS_SPI": to_u4(0x20910064),  # U1 - - Output rate of the UBX-NAV-TIMELS message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMELS_UART1": to_u4(0x20910061),  # U1 - - Output rate of the UBX-NAV-TIMELS message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMELS_UART2": to_u4(0x20910062),  # U1 - - Output rate of the UBX-NAV-TIMELS message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMELS_USB": to_u4(0x20910063),  # U1 - - Output rate of the UBX-NAV-TIMELS message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_I2C": to_u4(0x20910386),  # U1 - - Output rate of the UBX-NAV-TIMEQZSS message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_SPI": to_u4(0x2091038a),  # U1 - - Output rate of the UBX-NAV-TIMEQZSS message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_UART1": to_u4(0x20910387),  # U1 - - Output rate of the UBX-NAV-TIMEQZSS message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_UART2": to_u4(0x20910388),  # U1 - - Output rate of the UBX-NAV-TIMEQZSS message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_USB": to_u4(0x20910389),  # U1 - - Output rate of the UBX-NAV-TIMEQZSS message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_I2C": to_u4(0x2091005b),  # U1 - - Output rate of the UBX-NAV-TIMEUTC message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_SPI": to_u4(0x2091005f),  # U1 - - Output rate of the UBX-NAV-TIMEUTC message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_UART1": to_u4(0x2091005c),  # U1 - - Output rate of the UBX-NAV-TIMEUTC message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_UART2": to_u4(0x2091005d),  # U1 - - Output rate of the UBX-NAV-TIMEUTC message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_USB": to_u4(0x2091005e),  # U1 - - Output rate of the UBX-NAV-TIMEUTC message on port USB
    "CFG-MSGOUT-UBX_NAV_VELECEF_I2C": to_u4(0x2091003d),  # U1 - - Output rate of the UBX-NAV-VELECEF message on port I2C
    "CFG-MSGOUT-UBX_NAV_VELECEF_SPI": to_u4(0x20910041),  # U1 - - Output rate of the UBX-NAV-VELECEF message on port SPI
    "CFG-MSGOUT-UBX_NAV_VELECEF_UART1": to_u4(0x2091003e),  # U1 - - Output rate of the UBX-NAV-VELECEF message on port UART1
    "CFG-MSGOUT-UBX_NAV_VELECEF_UART2": to_u4(0x2091003f),  # U1 - - Output rate of the UBX-NAV-VELECEF message on port UART2
    "CFG-MSGOUT-UBX_NAV_VELECEF_USB": to_u4(0x20910040),  # U1 - - Output rate of the UBX-NAV-VELECEF message on port USB
    "CFG-MSGOUT-UBX_NAV_VELNED_I2C": to_u4(0x20910042),  # U1 - - Output rate of the UBX-NAV-VELNED message on port I2C
    "CFG-MSGOUT-UBX_NAV_VELNED_SPI": to_u4(0x20910046),  # U1 - - Output rate of the UBX-NAV-VELNED message on port SPI
    "CFG-MSGOUT-UBX_NAV_VELNED_UART1": to_u4(0x20910043),  # U1 - - Output rate of the UBX-NAV-VELNED message on port UART1
    "CFG-MSGOUT-UBX_NAV_VELNED_UART2": to_u4(0x20910044),  # U1 - - Output rate of the UBX-NAV-VELNED message on port UART2
    "CFG-MSGOUT-UBX_NAV_VELNED_USB": to_u4(0x20910045),  # U1 - - Output rate of the UBX-NAV-VELNED message on port USB
    "CFG-MSGOUT-UBX_RXM_MEASX_I2C": to_u4(0x20910204),  # U1 - - Output rate of the UBX-RXM-MEASX message on port I2C
    "CFG-MSGOUT-UBX_RXM_MEASX_SPI": to_u4(0x20910208),  # U1 - - Output rate of the UBX-RXM-MEASX message on port SPI
    "CFG-MSGOUT-UBX_RXM_MEASX_UART1": to_u4(0x20910205),  # U1 - - Output rate of the UBX-RXM-MEASX message on port UART1
    "CFG-MSGOUT-UBX_RXM_MEASX_UART2": to_u4(0x20910206),  # U1 - - Output rate of the UBX-RXM-MEASX message on port UART2
    "CFG-MSGOUT-UBX_RXM_MEASX_USB": to_u4(0x20910207),  # U1 - - Output rate of the UBX-RXM-MEASX message on port USB
    "CFG-MSGOUT-UBX_RXM_RAWX_I2C": to_u4(0x209102a4),  # U1 - - Output rate of the UBX-RXM-RAWX message on port I2C
    "CFG-MSGOUT-UBX_RXM_RAWX_SPI": to_u4(0x209102a8),  # U1 - - Output rate of the UBX-RXM-RAWX message on port SPI
    "CFG-MSGOUT-UBX_RXM_RAWX_UART1": to_u4(0x209102a5),  # U1 - - Output rate of the UBX-RXM-RAWX message on port UART1
    "CFG-MSGOUT-UBX_RXM_RAWX_UART2": to_u4(0x209102a6),  # U1 - - Output rate of the UBX-RXM-RAWX message on port UART2
    "CFG-MSGOUT-UBX_RXM_RAWX_USB": to_u4(0x209102a7),  # U1 - - Output rate of the UBX-RXM-RAWX message on port USB
    "CFG-MSGOUT-UBX_RXM_RLM_I2C": to_u4(0x2091025e),  # U1 - - Output rate of the UBX-RXM-RLM message on port I2C
    "CFG-MSGOUT-UBX_RXM_RLM_SPI": to_u4(0x20910262),  # U1 - - Output rate of the UBX-RXM-RLM message on port SPI
    "CFG-MSGOUT-UBX_RXM_RLM_UART1": to_u4(0x2091025f),  # U1 - - Output rate of the UBX-RXM-RLM message on port UART1
    "CFG-MSGOUT-UBX_RXM_RLM_UART2": to_u4(0x20910260),  # U1 - - Output rate of the UBX-RXM-RLM message on port UART2
    "CFG-MSGOUT-UBX_RXM_RLM_USB": to_u4(0x20910261),  # U1 - - Output rate of the UBX-RXM-RLM message on port USB
    "CFG-MSGOUT-UBX_RXM_RTCM_I2C": to_u4(0x20910268),  # U1 - - Output rate of the UBX-RXM-RTCM message on port I2C
    "CFG-MSGOUT-UBX_RXM_RTCM_SPI": to_u4(0x2091026c),  # U1 - - Output rate of the UBX-RXM-RTCM message on port SPI
    "CFG-MSGOUT-UBX_RXM_RTCM_UART1": to_u4(0x20910269),  # U1 - - Output rate of the UBX-RXM-RTCM message on port UART1
    "CFG-MSGOUT-UBX_RXM_RTCM_UART2": to_u4(0x2091026a),  # U1 - - Output rate of the UBX-RXM-RTCM message on port UART2
    "CFG-MSGOUT-UBX_RXM_RTCM_USB": to_u4(0x2091026b),  # U1 - - Output rate of the UBX-RXM-RTCM message on port USB
    "CFG-MSGOUT-UBX_RXM_SFRBX_I2C": to_u4(0x20910231),  # U1 - - Output rate of the UBX-RXM-SFRBX message on port I2C
    "CFG-MSGOUT-UBX_RXM_SFRBX_SPI": to_u4(0x20910235),  # U1 - - Output rate of the UBX-RXM-SFRBX message on port SPI
    "CFG-MSGOUT-UBX_RXM_SFRBX_UART1": to_u4(0x20910232),  # U1 - - Output rate of the UBX-RXM-SFRBX message on port UART1
    "CFG-MSGOUT-UBX_RXM_SFRBX_UART2": to_u4(0x20910233),  # U1 - - Output rate of the UBX-RXM-SFRBX message on port UART2
    "CFG-MSGOUT-UBX_RXM_SFRBX_USB": to_u4(0x20910234),  # U1 - - Output rate of the UBX-RXM-SFRBX message on port USB
    "CFG-MSGOUT-UBX_TIM_TM2_I2C": to_u4(0x20910178),  # U1 - - Output rate of the UBX-TIM-TM2 message on port I2C
    "CFG-MSGOUT-UBX_TIM_TM2_SPI": to_u4(0x2091017c),  # U1 - - Output rate of the UBX-TIM-TM2 message on port SPI
    "CFG-MSGOUT-UBX_TIM_TM2_UART1": to_u4(0x20910179),  # U1 - - Output rate of the UBX-TIM-TM2 message on port UART1
    "CFG-MSGOUT-UBX_TIM_TM2_UART2": to_u4(0x2091017a),  # U1 - - Output rate of the UBX-TIM-TM2 message on port UART2
    "CFG-MSGOUT-UBX_TIM_TM2_USB": to_u4(0x2091017b),  # U1 - - Output rate of the UBX-TIM-TM2 message on port USB
    "CFG-MSGOUT-UBX_TIM_TP_I2C": to_u4(0x2091017d),  # U1 - - Output rate of the UBX-TIM-TP message on port I2C
    "CFG-MSGOUT-UBX_TIM_TP_SPI": to_u4(0x20910181),  # U1 - - Output rate of the UBX-TIM-TP message on port SPI
    "CFG-MSGOUT-UBX_TIM_TP_UART1": to_u4(0x2091017e),  # U1 - - Output rate of the UBX-TIM-TP message on port UART1
    "CFG-MSGOUT-UBX_TIM_TP_UART2": to_u4(0x2091017f),  # U1 - - Output rate of the UBX-TIM-TP message on port UART2
    "CFG-MSGOUT-UBX_TIM_TP_USB": to_u4(0x20910180),  # U1 - - Output rate of the UBX-TIM-TP message on port USB
    "CFG-MSGOUT-UBX_TIM_VRFY_I2C": to_u4(0x20910092),  # U1 - - Output rate of the UBX-TIM-VRFY message on port I2C
    "CFG-MSGOUT-UBX_TIM_VRFY_SPI": to_u4(0x20910096),  # U1 - - Output rate of the UBX-TIM-VRFY message on port SPI
    "CFG-MSGOUT-UBX_TIM_VRFY_UART1": to_u4(0x20910093),  # U1 - - Output rate of the UBX-TIM-VRFY message on port UART1
    "CFG-MSGOUT-UBX_TIM_VRFY_UART2": to_u4(0x20910094),  # U1 - - Output rate of the UBX-TIM-VRFY message on port UART2
    "CFG-MSGOUT-UBX_TIM_VRFY_USB": to_u4(0x20910095),  # U1 - - Output rate of the UBX-TIM-VRFY message on port USB
}

# CFG-NAVHPG: High precision navigation configuration
# This group configures items related to the operation of the receiver in high precision, for example Differential correction and other related features.
# https://www.u-blox.com/en/docs/UBX-18010854#page=201&zoom=auto,-70,370
CFG_NAVHPG = {
    "CFG-NAVHPG-DGNSSMODE": to_u4(0x20140011),  # E1 - - Differential corrections mode. See Table 18 below for a list of possible constants for this item.
}
TBL18_CFG_NAVHPG = {  # Table 18
    "RTK_FLOAT": b"\x02",  # No attempts made to fix ambiguities
    "RTK_FIXED": b"\x03",  # Ambiguities are fixed whenever possible
}

# CFG-NAVSPG: Standard precision navigation configuration
# This group contains configuration items related to the operation of the receiver at standard. precision, including configuring postition fix mode, ionospheric model selection and other related items.
# https://www.u-blox.com/en/docs/UBX-18010854#page=201&zoom=auto,-70,187
CFG_NAVSPG = {
    "CFG-NAVSPG-FIXMODE": to_u4(0x20110011),  # E1 - - Position fix mode. See Table 20 below for a list of possible constants for this item.
    "CFG-NAVSPG-INIFIX3D": to_u4(0x10110013),  # L - - Initial fix must be a 3D fix.
    "CFG-NAVSPG-WKNROLLOVER": to_u4(0x30110017),  # U2 - - GPS week rollover number. GPS week numbers will be set correctly from this week up to 1024 weeks after this week. Range is from 1 to 4096.
    "CFG-NAVSPG-UTCSTANDARD": to_u4(0x2011001c),  # E1 - - UTC standard to be used. See also the section GNSS time base in the Integration manual. See Table 21 below for a list of possible constants for this item.
    "CFG-NAVSPG-DYNMODEL": to_u4(0x20110021),  # E1 - - Dynamic platform model. See Table 22 below for a list of possible constants for this item.
    "CFG-NAVSPG-ACKAIDING": to_u4(0x10110025),  # L - - Acknowledge assistance input messages.
    "CFG-NAVSPG-USE_USRDAT": to_u4(0x10110061),  # L - - Use user geodetic datum parameters. This must be set together with all CFG-NAVSPG-USERDAT_* parameters.
    "CFG-NAVSPG-USRDAT_MAJA": to_u4(0x50110062),  # R8 - m Geodetic datum semi-major axis. Accepted range is from 6,300,000.0 to 6,500,000.0 meters. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_FLAT": to_u4(0x50110063),  # R8 - - Geodetic datum 1.0 / flattening. Accepted range is 0.0 to 500.0. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_DX": to_u4(0x40110064),  # R4 - m Geodetic datum X axis shift at the origin. Accepted range is +/- 5000.0 meters. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_DY": to_u4(0x40110065),  # R4 - m Geodetic datum Y axis shift at the origin. Accepted range is +/- 5000.0 meters. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_DZ": to_u4(0x40110066),  # R4 - m Geodetic datum Z axis shift at the origin. Accepted range is +/- 5000.0 meters. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_.. parameters.
    "CFG-NAVSPG-USRDAT_ROTX": to_u4(0x40110067),  # R4 - arcsec Geodetic datum rotation about the X axis. Accepted range is +/- 20.0 milli arc seconds. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_ROTY": to_u4(0x40110068),  # R4 - arcsec Geodetic datum rotation about the Y axis (). Accepted range is +/- 20.0 milli-arc seconds. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_*. parameters.
    "CFG-NAVSPG-USRDAT_ROTZ": to_u4(0x40110069),  # R4 - arcsec Geodetic datum rotation about the Z axis. Accepted range is +/- 20.0 milli-arc seconds. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_SCALE": to_u4(0x4011006a),  # R4 - ppm Geodetic datum scale factor. Accepted range is 0.0 to 50.0 parts per million. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-INFIL_MINSVS": to_u4(0x201100a1),  # U1 - - Minimum number of satellites for navigation.
    "CFG-NAVSPG-INFIL_MAXSVS": to_u4(0x201100a2),  # U1 - - Maximum number of satellites for navigation.
    "CFG-NAVSPG-INFIL_MINCNO": to_u4(0x201100a3),  # U1 - dBHz Minimum satellite signal level for navigation.
    "CFG-NAVSPG-INFIL_MINELEV": to_u4(0x201100a4),  # I1 - deg Minimum elevation for a GNSS satellite to be. used in navigation.
    "CFG-NAVSPG-INFIL_NCNOTHRS": to_u4(0x201100aa),  # U1 - - Number of satellites required to have C/N0. above CFG-NAVSPG-INFIL_CNOTHRS for a fix to. be attempted.
    "CFG-NAVSPG-INFIL_CNOTHRS": to_u4(0x201100ab),  # U1 - - C/N0 threshold for deciding whether to attempt. a fix.
    "CFG-NAVSPG-OUTFIL_PDOP": to_u4(0x301100b1),  # U2 0.1 - Output filter position DOP mask (threshold).
    "CFG-NAVSPG-OUTFIL_TDOP": to_u4(0x301100b2),  # U2 0.1 - Output filter time DOP mask (threshold).
    "CFG-NAVSPG-OUTFIL_PACC": to_u4(0x301100b3),  # U2 - m Output filter position accuracy mask (threshold).
    "CFG-NAVSPG-OUTFIL_TACC": to_u4(0x301100b4),  # U2 - m Output filter time accuracy mask (threshold).
    "CFG-NAVSPG-OUTFIL_FACC": to_u4(0x301100b5),  # U2 0.01 m/s Output filter frequency accuracy mask. (threshold).
    "CFG-NAVSPG-CONSTR_ALT": to_u4(0x401100c1),  # I4 0.01 m Fixed altitude (mean sea level) for 2D fix mode.
    "CFG-NAVSPG-CONSTR_ALTVAR": to_u4(0x401100c2),  # U4 0.0001 m^2 Fixed altitude variance for 2D mode.
    "CFG-NAVSPG-CONSTR_DGNSSTO": to_u4(0x201100c4),  # U1 - s DGNSS timeout
}
TBL20_CFG_NAVSPG = {  #Table 20
    "2DONLY": b"\x01",  # 2D only
    "3DONLY": b"\x02",  # 3D only
    "AUTO": b"\x03",  # Auto 2D/3D
}
TBL21_CFG_NAVSPG = {  #Table 21
    "AUTO": b"\x00",  # Automatic; receiver selects based on GNSS configuration
    "USNO": b"\x03",  # UTC as operated by the U.S. Naval Observatory (USNO); derived from GPS time
    "EU": b"\x05",  # UTC as combined from multiple European laboratories; derived from Galileo time
    "SU": b"\x06",  # UTC as operated by the former Soviet Union (SU); derived from GLONASS time
    "NTSC": b"\x07",  # UTC as operated by the National Time Service Center (NTSC), China; derived from BeiDou time
}
TBL22_CFG_NAVSPG = {  # Table 22
    "PORT": b"\x00",  # Portable
    "STAT": b"\x02",  # Stationary
    "PED": b"\x03",  # Pedestrian
    "AUTOMOT": b"\x04",  # Automotive
    "SEA": b"\x05",  # Sea
    "AIR1": b"\x06",  # Airborne with <1g acceleration
    "AIR2": b"\x07",  # Airborne with <2g acceleration
    "AIR4": b"\x08",  # Airborne with <4g acceleration
    "WRIST": b"\x09",  # Wrist-worn watch (not available in all products)
}

# CFG-NMEA: NMEA protocol configuration
# This group configures the NMEA protocol. See section NMEA protocol configuration for a detailed description of the configuration effects on NMEA output.
# https://www.u-blox.com/en/docs/UBX-18010854#page=204&zoom=auto,-70,631
CFG_NMEA = {
    "CFG-NMEA-PROTVER": to_u4(0x20930001),  # E1 - - NMEA protocol version - - See Table 24 below for a list of possible constants for this item.
    "CFG-NMEA-MAXSVS": to_u4(0x20930002),  # E1 - - Maximum number of SVs to report per Talker ID - - See Table 25 below for a list of possible constants for this item.
    "CFG-NMEA-COMPAT": to_u4(0x10930003),  # L - - Enable compatibility mode - - This might be needed for certain applications, e.g. for an NMEA parser that expects a fixed number of digits in position coordinates.
    "CFG-NMEA-CONSIDER": to_u4(0x10930004),  # L - - Enable considering mode. This will affect NMEA output used satellite count. If set, also considered satellites (e.g. RAIMED) are counted as used satellites as well.
    "CFG-NMEA-LIMIT82": to_u4(0x10930005),  # L - - Enable strict limit to 82 characters maximum NMEA message length
    "CFG-NMEA-HIGHPREC": to_u4(0x10930006),  # L - - Enable high precision mode - - This flag cannot be set in conjunction with either CFG-NMEA-COMPAT or CFG-NMEA-LIMIT82 mode.
    "CFG-NMEA-SVNUMBERING": to_u4(0x20930007),  # E1 - - Display configuration for SVs that do not have value defined in NMEA. Configures the display of satellites that do not have an NMEA-defined value. Note: this does not apply to satellites with an unknown ID. See also Satellite Numbering. See Table 26 below for a list of possible constants for this item.
    "CFG-NMEA-FILT_GPS": to_u4(0x10930011),  # L - - Disable reporting of GPS satellites
    "CFG-NMEA-FILT_SBAS": to_u4(0x10930012),  # L - - Disable reporting of SBAS satellites
    "CFG-NMEA-FILT_GAL": to_u4(0x10930013),  # L - - Disable reporting of Galileo satellites
    "CFG-NMEA-FILT_QZSS": to_u4(0x10930015),  # L - - Disable reporting of QZSS satellites
    "CFG-NMEA-FILT_GLO": to_u4(0x10930016),  # L - - Disable reporting of GLONASS satellites
    "CFG-NMEA-FILT_BDS": to_u4(0x10930017),  # L - - Disable reporting of BeiDou satellites
    "CFG-NMEA-OUT_INVFIX": to_u4(0x10930021),  # L - - Enable position output for failed or invalid fixes
    "CFG-NMEA-OUT_MSKFIX": to_u4(0x10930022),  # L - - Enable position output for invalid fixes
    "CFG-NMEA-OUT_INVTIME": to_u4(0x10930023),  # L - - Enable time output for invalid times
    "CFG-NMEA-OUT_INVDATE": to_u4(0x10930024),  # L - - Enable date output for invalid dates
    "CFG-NMEA-OUT_ONLYGPS": to_u4(0x10930025),  # L - - Restrict output to GPS satellites only
    "CFG-NMEA-OUT_FROZENCOG": to_u4(0x10930026),  # L - - Enable course over ground output even if it is frozen
    "CFG-NMEA-MAINTALKERID": to_u4(0x20930031),  # E1 - - Main Talker ID. By default the main Talker ID (i.e. the Talker ID used for all messages other than GSV) is determined by the GNSS assignment of the receiver's channels (see CFG-SIGNAL). This field enables the main Talker ID to be overridden. See Table 27 below for a list of possible constants for this item.
    "CFG-NMEA-GSVTALKERID": to_u4(0x20930032),  # E1 - - Talker ID for GSV NMEA messages. By default the Talker ID for GSV messages is GNSS-specific (as defined by NMEA). This field enables the GSV Talker ID to be overridden. See Table 28 below for a list of possible constants for this item.
    "CFG-NMEA-BDSTALKERID": to_u4(0x30930033),  # U2 - - BeiDou Talker ID. Sets the two ASCII characters that should be used for the BeiDou Talker ID. If these are set to zero, the default BeiDou Talker ID will be used.
}
TBL24_CFG_NMEA = {  # Table 24
    "V21": int(21).to_bytes(1, "little"),  # NMEA protocol version 2.1
    "V23": int(23).to_bytes(1, "little"),  # NMEA protocol version 2.3
    "V40": int(40).to_bytes(1, "little"),  # NMEA protocol version 4.0 (not available in all products)
    "V41": int(41).to_bytes(1, "little"),  # NMEA protocol version 4.10 (not available in all products)
    "V411": int(42).to_bytes(1, "little"),  # NMEA protocol version 4.11 (not available in all products)
}
TBL25_CFG_NMEA = {  # Table 25
    "UNLIM": int(0).to_bytes(1, "little"),  # Unlimited
    "8SVS": int(8).to_bytes(1, "little"),  # 8 SVs
    "12SVS": int(12).to_bytes(1, "little"),  # 12 SVs
    "16SVS": int(16).to_bytes(1, "little"),  # 16 SVs
}
TBL26_CFG_NMEA = {  # Table 26
    "STRICT": b"\x00",  # Strict - satellites are not output
    "EXTENDED": b"\x01",  # Extended - use proprietary numbering
}
TBL27_CFG_NMEA = {  # Table 27
    "AUTO": b"\x00",  # Main Talker ID is not overridden
    "GP": b"\x01",  # Set main Talker ID to 'GP'
    "GL": b"\x02",  # Set main Talker ID to 'GL'
    "GN": b"\x03",  # Set main Talker ID to 'GN'
    "GA": b"\x04",  # Set main Talker ID to 'GA' (not available in all products)
    "GB": b"\x05",  # Set main Talker ID to 'GB' (not available in all products)
    "GQ": b"\x07",  # Set main Talker ID to 'GQ' (not available in all products)
}
TBL28_CFG_NMEA = {  # Table 28
    "GNSS": b"\x00",  # Use GNSS-specific Talker ID (as defined by NMEA)
    "MAIN": b"\x01",  # Use the main Talker ID
}

# CFG-RATE: Navigation and measurement rate configuration
# The configuration items in this group allow the user to alter the rate at which navigation solutions (and the measurements that they depend on) are generated by the receiver. The calculation of the navigation solution will always be aligned to the top of a second zero (first second of the week) of the configured reference time system. The navigation period is an integer multiple of the measurement period.
# https://www.u-blox.com/en/docs/UBX-18010854#page=207&zoom=auto,-70,676
CFG_RATE = {
    "CFG-RATE-MEAS": to_u4(0x30210001),  # U2 0.001 s Nominal time between GNSS measurements. E.g. 100 ms results in 10 Hz measurement rate, 1000 ms = 1 Hz measurement rate.
    "CFG-RATE-NAV": to_u4(0x30210002),  # U2 - - Ratio of number of measurements to number of navigation solutions. E.g. 5 means five measurements for every navigation solution. The maximum value is 128.
    "CFG-RATE-TIMEREF": to_u4(0x20210003),  # E1 - - Time system to which measurements are aligned. See Table 33 below for a list of possible constants for this item.
}
TBL33_CFG_RATE = {  # Table 33
    "UTC ": b"\x00",  # Align measurements to UTC time
    "GPS ": b"\x01",  # Align measurements to GPS time
    "GLO ": b"\x02",  # Align measurements to GLONASS time
    "BDS ": b"\x03",  # Align measurements to BeiDou time
    "GAL ": b"\x04",  # Align measurements to Galileo time
}

# CFG-TMODE: Time mode configuration
# Configuration for operation of the receiver in Time mode. The position referred to in the configuration items is that of the Antenna Reference Point (ARP).
# https://www.u-blox.com/en/docs/UBX-18010854#page=211&zoom=auto,-70,301
CFG_TMODE = {
    "CFG-TMODE-MODE": to_u4(0x20030001),  # E1 - - Receiver mode. See Table 44 below for a list of possible constants for this item.
    "CFG-TMODE-POS_TYPE": to_u4(0x20030002),  # E1 - - Determines whether the ARP position is given in. ECEF or LAT/LON/HEIGHT?. See Table 45 below for a list of possible constants for this item.
    "CFG-TMODE-ECEF_X": to_u4(0x40030003),  # I4 - cm ECEF X coordinate of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-ECEF_Y": to_u4(0x40030004),  # I4 - cm ECEF Y coordinate of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-ECEF_Z": to_u4(0x40030005),  # I4 - cm ECEF Z coordinate of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-ECEF_X_HP": to_u4(0x20030006),  # I1 0.1 mm High-precision ECEF X coordinate of the ARP. position.. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-ECEF_Y_HP": to_u4(0x20030007),  # I1 0.1 mm High-precision ECEF Y coordinate of the ARP. position.. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-ECEF_Z_HP": to_u4(0x20030008),  # I1 0.1 mm High-precision ECEF Z coordinate of the ARP. position.. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-LAT": to_u4(0x40030009),  # I4 1e-7 deg Latitude of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-LON": to_u4(0x4003000a),  # I4 1e-7 deg Longitude of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-HEIGHT": to_u4(0x4003000b),  # I4 - cm Height of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-LAT_HP": to_u4(0x2003000c),  # I1 1e-9 deg High-precision latitude of the ARP position. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-LON_HP": to_u4(0x2003000d),  # I1 1e-9 deg High-precision longitude of the ARP position.. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-HEIGHT_HP": to_u4(0x2003000e),  # I1 0.1 mm High-precision height of the ARP position.. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-FIXED_POS_ACC": to_u4(0x4003000f),  # U4 0.1 mm Fixed position 3D accuracy.
    "CFG-TMODE-SVIN_MIN_DUR": to_u4(0x40030010),  # U4 - s Survey-in minimum duration. This will only be used if CFG-TMODE-MODE=SURVEY_IN.
    "CFG-TMODE-SVIN_ACC_LIMIT": to_u4(0x40030011),  # U4 0.1 mm Survey-in position accuracy limit. This will only be used if CFG-TMODE-MODE=SURVEY_IN.
}
TBL44_CFG_TMODE = { # Table 44
    "DISABLED": b"\x00",  # Disabled
    "SURVEY_IN": b"\x01",  # Survey in
    "FIXED": b"\x02",  # Fixed mode (true ARP position information required)
}
TBL45_CFG_TMODE = {  # Table 45
    "ECEF": b"\x00",  # Position is ECEF
    "LLH": b"\x01",  # Position is Lat/Lon/Height
}

# CFG-TP: Timepulse configuration
# Use this group to configure the generation of timepulses.
# https://www.u-blox.com/en/docs/UBX-18010854#page=213&zoom=auto,-70,694
CFG_TP = {
    "CFG-TP-PULSE_DEF": to_u4(0x20050023),  # E1 - - Determines whether the time pulse is interpreted as frequency or period. See Table 47 below for a list of possible constants for this item.
    "CFG-TP-PULSE_LENGTH_DEF": to_u4(0x20050030),  # E1 - - Determines whether the time pulse length is interpreted as length[us] or pulse ratio[%]. See Table 48 below for a list of possible constants for this item.
    "CFG-TP-ANT_CABLEDELAY": to_u4(0x30050001),  # I2 1e-9 s Antenna cable delay
    "CFG-TP-PERIOD_TP1": to_u4(0x40050002),  # U4 1e-6 s Time pulse period (TP1)
    "CFG-TP-PERIOD_LOCK_TP1": to_u4(0x40050003),  # U4 1e-6 s Time pulse period when locked to GNSS time (TP1) Only used if CFG-TP-USE_LOCKED_TP1 is set.
    "CFG-TP-FREQ_TP1": to_u4(0x40050024),  # U4 - Hz Time pulse frequency (TP1) This will only be used if CFG-TP-PULSE_DEF=FREQ.
    "CFG-TP-FREQ_LOCK_TP1": to_u4(0x40050025),  # U4 - Hz Time pulse frequency when locked to GNSS time (TP1) Only used if CFG-TP-USE_LOCKED_TP1 is set.
    "CFG-TP-LEN_TP1": to_u4(0x40050004),  # U4 1e-6 s Time pulse length (TP1)
    "CFG-TP-LEN_LOCK_TP1": to_u4(0x40050005),  # U4 1e-6 s Time pulse length when locked to GNSS time (TP1) Only used if CFG-TP-USE_LOCKED_TP1 is set.
    "CFG-TP-DUTY_TP1": to_u4(0x5005002a),  # R8 - % Time pulse duty cycle (TP1) Only used if CFG-TP-PULSE_LENGTH_DEF=RATIO is set.
    "CFG-TP-DUTY_LOCK_TP1": to_u4(0x5005002b),  # R8 - % Time pulse duty cycle when locked to GNSS time (TP1) Only used if CFG-TP-PULSE_LENGTH_DEF=RATIO and CFG-TP-USE_LOCKED_TP1 are set.
    "CFG-TP-USER_DELAY_TP1": to_u4(0x40050006),  # I4 1e-9 s User-configurable time pulse delay (TP1)
    "CFG-TP-TP1_ENA": to_u4(0x10050007),  # L - - Enable the first timepulse if pin associated with time pulse is assigned for another function, the other function takes precedence. Must be set for frequency-time products.
    "CFG-TP-SYNC_GNSS_TP1": to_u4(0x10050008),  # L - - Sync time pulse to GNSS time or local clock (TP1). If set, sync to GNSS if GNSS time is valid otherwise, if not set or not available, use local clock. Ignored by time-frequency product variants, which will attempt to use the best available time/frequency reference (not necessarily GNSS). This flag can be unset only in Timing product variants.
    "CFG-TP-USE_LOCKED_TP1": to_u4(0x10050009),  # L - - Use locked parameters when possible (TP1). If set, use CFG-TP-PERIOD_LOCK_TP1 and CFG-TP-LEN_LOCK_TP1 as soon as GNSS time is valid. Otherwise if not valid or not set, use CFG-TP-PERIOD_TP1 and CFG-TP-LEN_TP1.
    "CFG-TP-ALIGN_TO_TOW_TP1": to_u4(0x1005000a),  # L - - Align time pulse to top of second (TP1). To use this feature, CFG-TP-USE_LOCKED_TP1 must be set. Time pulse period must be an integer fraction of 1 second. Ignored in time-frequency product variants, where it is assumed always enabled.
    "CFG-TP-POL_TP1": to_u4(0x1005000b),  # L - - Set time pulse polarity (TP1). false (0) : falling edge at top of second. true (1) : rising edge at top of second.
    "CFG-TP-TIMEGRID_TP1": to_u4(0x2005000c),  # E1 - - Time grid to use (TP1). Only relevant if CFG-TP-USE_LOCKED_TP1 and ALIGN_TO_TOW_TP1 are set. Note that configured GNSS time is estimated by the receiver if locked to any GNSS system. If the receiver has a valid GNSS fix it will attempt to steer the TP to the specified time grid even if the specified time is not based on information from the constellation's satellites. To ensure timing based purely on a given GNSS, restrict the supported constellations in CFG-SIGNAL-*.
}
TBL47_CFG_TP = {  # Table 47
    "PERIOD": b"\x00",  # Time pulse period [us]
    "FREQ": b"\x01",  # Time pulse frequency [Hz]
}
TBL48_CFG_TP = {  # Table 48
    "RATIO": b"\x00",  # Time pulse ratio
    "LENGTH": b"\x01",  # Time pulse length
}
TBL49_CFG_TP = {  # Table 49
    "UTC": b"\x00",  # UTC time reference
    "GPS": b"\x01",  # GPS time reference
    "GLO": b"\x02",  # GLONASS time reference
    "BDS": b"\x03",  # BeiDou time reference
    "GAL": b"\x04",  # Galileo time reference
}

# CFG-UART1: Configuration of the UART1 interface
# Settings needed to configure the UART1 communication interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=215&zoom=auto,-70,678
CFG_UART1 = {
    "CFG-UART1-BAUDRATE": to_u4(0x40520001),  # U4 - - The baud rate that should be configured on the UART1
    "CFG-UART1-STOPBITS": to_u4(0x20520002),  # E1 - - Number of stopbits that should be used on UART1 See  Table 53  below for a list of possible constants for this item.
    "CFG-UART1-DATABITS": to_u4(0x20520003),  # E1 - - Number of databits that should be used on UART1 See  Table 54  below for a list of possible constants for this item.
    "CFG-UART1-PARITY": to_u4(0x20520004),  # E1 - - Parity mode that should be used on UART1 See  Table 55  below for a list of possible constants for this item.
    "CFG-UART1-ENABLED": to_u4(0x10520005),  # L - - Flag to indicate if the UART1 should be enabled
}
TBL53_CFG_UART1 = {  # Table 53
    "HALF": b"\x00",  # 0.5 stopbits
    "ONE": b"\x01",  # 1.0 stopbits
    "ONEHALF": b"\x02",  # 1.5 stopbits
    "TWO": b"\x03",  # 2.0 stopbits
}
TBL54_CFG_UART1 = {  # Table 54
    "EIGHT": b"\x00",  # 8 databits
    "SEVEN": b"\x01",  # 7 databits
}
TBL55_CFG_UART1 = {  # Table 55
    "NONE": b"\x00",  # No parity bit
    "ODD": b"\x01",  # Add an odd parity bit
    "EVEN": b"\x02",  # Add an even parity bit
}

# CFG-UART1INPROT: Input protocol configuration of the UART1 interface
# Input protocol enable flags of the UART1 interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=215&zoom=auto,-70,211
CFG_UART1INPROT = {
    "CFG-UART1INPROT-UBX": to_u4(0x10730001),  # L - - Flag to indicate if UBX should be an input protocol on UART1
    "CFG-UART1INPROT-NMEA": to_u4(0x10730002),  # L - - Flag to indicate if NMEA should be an input protocol on UART1
    "CFG-UART1INPROT-RTCM3X": to_u4(0x10730004),  # L - - Flag to indicate if RTCM3X should be an input protocol on UART1
}

# CFG-UART1OUTPROT: Output protocol configuration of the UART1 interface
# Output protocol enable flags of the UART1 interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=216&zoom=auto,-70,685
CFG_UART1OUTPROT = {
    "CFG-UART1OUTPROT-UBX": to_u4(0x10740001),  # L - - Flag to indicate if UBX should be an output protocol on UART1
    "CFG-UART1OUTPROT-NMEA": to_u4(0x10740002),  # L - - Flag to indicate if NMEA should be an output protocol on UART1
    "CFG-UART1OUTPROT-RTCM3X": to_u4(0x10740004),  # L - - Flag to indicate if RTCM3X should be an output protocol on UART1
}

# CFG-UART2: Configuration of the UART2 interface
# Settings needed to configure the UART2 communication interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=216&zoom=auto,-70,524
CFG_UART2 = {
    "CFG-UART2-BAUDRATE": to_u4(0x40530001),  # U4 - - The baud rate that should be configured on the UART2
    "CFG-UART2-STOPBITS": to_u4(0x20530002),  # E1 - - Number of stopbits that should be used on UART2 See  Table 59  below for a list of possible constants for this item.
    "CFG-UART2-DATABITS": to_u4(0x20530003),  # E1 - - Number of databits that should be used on UART2 See  Table 60  below for a list of possible constants for this item.
    "CFG-UART2-PARITY": to_u4(0x20530004),  # E1 - - Parity mode that should be used on UART2 See  Table 61  below for a list of possible constants for this item.
    "CFG-UART2-ENABLED": to_u4(0x10530005),  # L - - Flag to indicate if the UART2 should be enabled
    "CFG-UART2-REMAP": to_u4(0x10530006),  # L - - UART2 Remapping
}
TBL59_CFG_UART2 = TBL53_CFG_UART1
TBL60_CFG_UART2 = TBL54_CFG_UART1
TBL61_CFG_UART2 = TBL55_CFG_UART1


# CFG-UART2INPROT: Input protocol configuration of the UART2 interface
# Input protocol enable flags of the UART2 interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=217&zoom=auto,-70,678
CFG_UART2INPROT = {
    "CFG-UART2INPROT-UBX": to_u4(0x10750001),  # L - - Flag to indicate if UBX should be an input protocol on UART2
    "CFG-UART2INPROT-NMEA": to_u4(0x10750002),  # L - - Flag to indicate if NMEA should be an input protocol on UART2
    "CFG-UART2INPROT-RTCM3X": to_u4(0x10750004),  # L - - Flag to indicate if RTCM3X should be an input protocol on UART2
}

# CFG-UART2OUTPROT: Output protocol configuration of the UART2 interface
# Output protocol enable flags of the UART2 interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=217&zoom=auto,-70,532
CFG_UART2OUTPROT = {
    "CFG-UART2OUTPROT-UBX": to_u4(0x10760001),  # L - - Flag to indicate if UBX should be an output protocol on UART2
    "CFG-UART2OUTPROT-NMEA": to_u4(0x10760002),  # L - - Flag to indicate if NMEA should be an output protocol on UART2
    "CFG-UART2OUTPROT-RTCM3X": to_u4(0x10760004),  # L - - Flag to indicate if RTCM3X should be an output protocol on UART2
}

# CFG-USB: Configuration of the USB interface
# Settings needed to configure the USB communication interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=217&zoom=auto,-70,371
CFG_USB = {
    "CFG-USB-ENABLED": to_u4(0x10650001),  # L - - Flag to indicate if the USB interface should be enabled
    "CFG-USB-SELFPOW": to_u4(0x10650002),  # L - - Self-powered device
    "CFG-USB-VENDOR_ID": to_u4(0x3065000a),  # U2 - - Vendor ID
    "CFG-USB-PRODUCT_ID": to_u4(0x3065000b),  # U2 - - Vendor ID
    "CFG-USB-POWER": to_u4(0x3065000c),  # U2 - mA Power consumption
    "CFG-USB-VENDOR_STR0": to_u4(0x5065000d),  # X8 - - Vendor string characters 0-7
    "CFG-USB-VENDOR_STR1": to_u4(0x5065000e),  # X8 - - Vendor string characters 8-15
    "CFG-USB-VENDOR_STR2": to_u4(0x5065000f),  # X8 - - Vendor string characters 16-23
    "CFG-USB-VENDOR_STR3": to_u4(0x50650010),  # X8 - - Vendor string characters 24-31
    "CFG-USB-PRODUCT_STR0": to_u4(0x50650011),  # X8 - - Product string characters 0-7
    "CFG-USB-PRODUCT_STR1": to_u4(0x50650012),  # X8 - - Product string characters 8-15
    "CFG-USB-PRODUCT_STR2": to_u4(0x50650013),  # X8 - - Product string characters 16-23
    "CFG-USB-PRODUCT_STR3": to_u4(0x50650014),  # X8 - - Product string characters 24-31
    "CFG-USB-SERIAL_NO_STR0": to_u4(0x50650015),  # X8 - - Serial number string characters 0-7
    "CFG-USB-SERIAL_NO_STR1": to_u4(0x50650016),  # X8 - - Serial number string characters 8-15
    "CFG-USB-SERIAL_NO_STR2": to_u4(0x50650017),  # X8 - - Serial number string characters 16-23
    "CFG-USB-SERIAL_NO_STR3": to_u4(0x50650018),  # X8 - - Serial number string characters 24-31
}

# CFG-USBINPROT: Input protocol configuration of the USB interface
# Input protocol enable flags of the USB interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=218&zoom=auto,-70,662
CFG_USBINPROT = {
    "CFG-USBINPROT-UBX": to_u4(0x10770001),  # L - - Flag to indicate if UBX should be an input protocol on USB
    "CFG-USBINPROT-NMEA": to_u4(0x10770002),  # L - - Flag to indicate if NMEA should be an input protocol on USB
    "CFG-USBINPROT-RTCM3X": to_u4(0x10770004),  # L - - Flag to indicate if RTCM3X should be an input protocol on USB
}

# CFG-USBOUTPROT: Output protocol configuration of the USB interface
# Output protocol enable flags of the USB interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=218&zoom=auto,-70,517
CFG_USBOUTPROT = {
    "CFG-USBOUTPROT-UBX": to_u4(0x10780001),  # L - - Flag to indicate if UBX should be an output protocol on USB
    "CFG-USBOUTPROT-NMEA": to_u4(0x10780002),  # L - - Flag to indicate if NMEA should be an output protocol on USB
    "CFG-USBOUTPROT-RTCM3X": to_u4(0x10780004),  # L - - Flag to indicate if RTCM3X should be an output protocol on USB
}

# All the config keys put together
# The commented out are not yet ported into this file
CFG_KEYPAIRS = {
    # GROUP-NAME: {KEYS}
    # "CFG-BDS": CFG_BDS,  # BeiDou system configuration
    # "CFG-GEOFENCE": CFG_GEOFENCE,  # Geofencing configuration
    # "CFG-HW": CFG_HW,  # Hardware configuration
    # "CFG-I2C": CFG_I2C,  # Configuration of the I2C interface
    # "CFG-I2CINPROT": CFG_I2CINPROT,  # Input protocol configuration of the I2C interface
    # "CFG-I2COUTPROT": CFG_I2COUTPROT,  # Output protocol configuration of the I2C interface
    "CFG-INFMSG": CFG_INFMSG,  # Information message configuration
    # "CFG-ITFM": CFG_ITFM,  # Jamming and interference monitor configuration
    # "CFG-LOGFILTER": CFG_LOGFILTER,  # Data logger configuration
    # "CFG-MOT": CFG_MOT,  # Motion detector configuration
    "CFG-MSGOUT": CFG_MSGOUT,  # Message output configuration
    "CFG-NAVHPG": CFG_NAVHPG,  # High precision navigation configuration
    "CFG-NAVSPG": CFG_NAVSPG,  # Standard precision navigation configuration
    "CFG-NMEA": CFG_NMEA,  # NMEA protocol configuration
    # "CFG-ODO": CFG_ODO,  # Odometer and low-speed course over ground filter configuration
    # "CFG-QZSS": CFG_QZSS,  # QZSS system configuration
    "CFG-RATE": CFG_RATE,  # Navigation and measurement rate configuration
    # "CFG-RINV": CFG_RINV,  # Remote inventory
    # "CFG-RTCM": CFG_RTCM,  # RTCM protocol configuration
    # "CFG-SBAS": CFG_SBAS,  # SBAS configuration
    # "CFG-SIGNAL": CFG_SIGNAL,  # Satellite systems (GNSS) signal configuration
    # "CFG-SPI": CFG_SPI,  # Configuration of the SPI interface
    # "CFG-SPIINPROT": CFG_SPIINPROT,  # Input protocol configuration of the SPI interface
    # "CFG-SPIOUTPROT": CFG_SPIOUTPROT,  # Output protocol configuration of the SPI interface
    "CFG-TMODE": CFG_TMODE,  # Time mode configuration
    "CFG-TP": CFG_TP,  # Timepulse configuration
    # "CFG-TXREADY": CFG_TXREADY,  # TX ready configuration
    "CFG-UART1": CFG_UART1,  # Configuration of the UART1 interface
    "CFG-UART1INPROT": CFG_UART1INPROT,  # Input protocol configuration of the UART1 interface
    "CFG-UART1OUTPROT": CFG_UART1OUTPROT,  # Output protocol configuration of the UART1 interface
    "CFG-UART2": CFG_UART2,  # Configuration of the UART2 interface
    "CFG-UART2INPROT": CFG_UART2INPROT,  # Input protocol configuration of the UART2 interface
    "CFG-UART2OUTPROT": CFG_UART2OUTPROT,  # Output protocol configuration of the UART2 interface
    "CFG-USB": CFG_USB,  # Configuration of the USB interface
    "CFG-USBINPROT": CFG_USBINPROT,  # Input protocol configuration of the USB interface
    "CFG-USBOUTPROT": CFG_USBOUTPROT  # Output protocol configuration of the USB interface
}
