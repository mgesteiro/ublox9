# Section 3.8, UBX messages overview
# extracted verbatim from https://www.u-blox.com/en/docs/UBX-18010854#page=49&zoom=auto,-74,575

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

UBX_CLASSID_SET = [
    UBX_ACK, UBX_CFG, UBX_INF, UBX_LOG, UBX_MGA, UBX_MON,
    UBX_NAV, UBX_RXM, UBX_SEC, UBX_TIM, UBX_UPD
]

# Section 5.8, Configuration overview
# extracted verbatim from https://www.u-blox.com/en/docs/UBX-18010854#page=180&zoom=auto,-74,522
"""
The ones starting with * are already ported to this file

CFG-BDS BeiDou system configuration
CFG-GEOFENCE Geofencing configuration
CFG-HW Hardware configuration
CFG-I2C Configuration of the I2C interface
CFG-I2CINPROT Input protocol configuration of the I2C interface
CFG-I2COUTPROT Output protocol configuration of the I2C interface
* CFG-INFMSG Information message configuration
CFG-ITFM Jamming and interference monitor configuration
CFG-LOGFILTER Data logger configuration
CFG-MOT Motion detector configuration
* CFG-MSGOUT Message output configuration
* CFG-NAVHPG High precision navigation configuration
* CFG-NAVSPG Standard precision navigation configuration
* CFG-NMEA NMEA protocol configuration
CFG-ODO Odometer and low-speed course over ground filter configuration
CFG-QZSS QZSS system configuration
* CFG-RATE Navigation and measurement rate configuration
CFG-RINV Remote inventory
CFG-RTCM RTCM protocol configuration
CFG-SBAS SBAS configuration
CFG-SIGNAL Satellite systems (GNSS) signal configuration
CFG-SPI Configuration of the SPI interface
CFG-SPIINPROT Input protocol configuration of the SPI interface
CFG-SPIOUTPROT Output protocol configuration of the SPI interface
* CFG-TMODE Time mode configuration
* CFG-TP Timepulse configuration
CFG-TXREADY TX ready configuration
* CFG-UART1 Configuration of the UART1 interface
* CFG-UART1INPROT Input protocol configuration of the UART1 interface
* CFG-UART1OUTPROT Output protocol configuration of the UART1 interface
* CFG-UART2 Configuration of the UART2 interface
* CFG-UART2INPROT Input protocol configuration of the UART2 interface
* CFG-UART2OUTPROT Output protocol configuration of the UART2 interface
* CFG-USB Configuration of the USB interface
* CFG-USBINPROT Input protocol configuration of the USB interface
* CFG-USBOUTPROT Output protocol configuration of the USB interface
"""

# CFG-INFMSG: Information message configuration
# Information message configuration for the NMEA and UBX protocols.
# https://www.u-blox.com/en/docs/UBX-18010854#page=184&zoom=auto,-70,539
CFG_INFMSG = {
    "CFG-INFMSG-UBX_I2C": 0x20920001.to_bytes(4, "little", signed=False),  # X1 - - Information message enable flags for the UBX protocol on the I2C interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-UBX_UART1": 0x20920002.to_bytes(4, "little", signed=False),  # X1 - - Information message enable flags for the UBX protocol on the UART1 interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-UBX_UART2": 0x20920003.to_bytes(4, "little", signed=False),  # X1 - - Information message enable flags for the UBX protocol on the UART2 interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-UBX_USB": 0x20920004.to_bytes(4, "little", signed=False),  # X1 - - Information message enable flags for the UBX protocol on the USB interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-UBX_SPI": 0x20920005.to_bytes(4, "little", signed=False),  # X1 - - Information message enable flags for the UBX protocol on the SPI interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-NMEA_I2C": 0x20920006.to_bytes(4, "little", signed=False),  # X1 - - Information message enable flags for the NMEA protocol on the I2C interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-NMEA_UART1": 0x20920007.to_bytes(4, "little", signed=False),  # X1 - - Information message enable flags for the NMEA protocol on the UART1 interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-NMEA_UART2": 0x20920008.to_bytes(4, "little", signed=False),  # X1 - - Information message enable flags for the NMEA protocol on the UART2 interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-NMEA_USB": 0x20920009.to_bytes(4, "little", signed=False),  # X1 - - Information message enable flags for the NMEA protocol on the USB interface. See  Table 11  below for a list of possible constants for this item.
    "CFG-INFMSG-NMEA_SPI": 0x2092000a.to_bytes(4, "little", signed=False),  # X1 - - Information message enable flags for the NMEA protocol on the SPI interface.  See  Table 11  below for a list of possible constants for this item.
}
CFG_INFMSG_LEVEL = {  # Table 11
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
    "CFG-MSGOUT-NMEA_ID_DTM_I2C": 0x209100a6.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-DTM message on port I2C
    "CFG-MSGOUT-NMEA_ID_DTM_SPI": 0x209100aa.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-DTM message on port SPI
    "CFG-MSGOUT-NMEA_ID_DTM_UART1": 0x209100a7.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-DTM message on port UART1
    "CFG-MSGOUT-NMEA_ID_DTM_UART2": 0x209100a8.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-DTM message on port UART2
    "CFG-MSGOUT-NMEA_ID_DTM_USB": 0x209100a9.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-DTM message on port USB
    "CFG-MSGOUT-NMEA_ID_GBS_I2C": 0x209100dd.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GBS message on port I2C
    "CFG-MSGOUT-NMEA_ID_GBS_SPI": 0x209100e1.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GBS message on port SPI
    "CFG-MSGOUT-NMEA_ID_GBS_UART1": 0x209100de.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GBS message on port UART1
    "CFG-MSGOUT-NMEA_ID_GBS_UART2": 0x209100df.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GBS message on port UART2
    "CFG-MSGOUT-NMEA_ID_GBS_USB": 0x209100e0.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GBS message on port USB
    "CFG-MSGOUT-NMEA_ID_GGA_I2C": 0x209100ba.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GGA message on port I2C
    "CFG-MSGOUT-NMEA_ID_GGA_SPI": 0x209100be.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GGA message on port SPI
    "CFG-MSGOUT-NMEA_ID_GGA_UART1": 0x209100bb.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GGA message on port UART1
    "CFG-MSGOUT-NMEA_ID_GGA_UART2": 0x209100bc.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GGA message on port UART2
    "CFG-MSGOUT-NMEA_ID_GGA_USB": 0x209100bd.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GGA message on port USB
    "CFG-MSGOUT-NMEA_ID_GLL_I2C": 0x209100c9.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GLL message on port I2C
    "CFG-MSGOUT-NMEA_ID_GLL_SPI": 0x209100cd.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GLL message on port SPI
    "CFG-MSGOUT-NMEA_ID_GLL_UART1": 0x209100ca.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GLL message on port UART1
    "CFG-MSGOUT-NMEA_ID_GLL_UART2": 0x209100cb.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GLL message on port UART2
    "CFG-MSGOUT-NMEA_ID_GLL_USB": 0x209100cc.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GLL message on port USB
    "CFG-MSGOUT-NMEA_ID_GNS_I2C": 0x209100b5.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GNS message on port I2C
    "CFG-MSGOUT-NMEA_ID_GNS_SPI": 0x209100b9.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GNS message on port SPI
    "CFG-MSGOUT-NMEA_ID_GNS_UART1": 0x209100b6.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GNS message on port UART1
    "CFG-MSGOUT-NMEA_ID_GNS_UART2": 0x209100b7.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GNS message on port UART2
    "CFG-MSGOUT-NMEA_ID_GNS_USB": 0x209100b8.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GNS message on port USB
    "CFG-MSGOUT-NMEA_ID_GRS_I2C": 0x209100ce.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GRS message on port I2C
    "CFG-MSGOUT-NMEA_ID_GRS_SPI": 0x209100d2.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GRS message on port SPI
    "CFG-MSGOUT-NMEA_ID_GRS_UART1": 0x209100cf.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GRS message on port UART1
    "CFG-MSGOUT-NMEA_ID_GRS_UART2": 0x209100d0.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GRS message on port UART2
    "CFG-MSGOUT-NMEA_ID_GRS_USB": 0x209100d1.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GRS message on port USB
    "CFG-MSGOUT-NMEA_ID_GSA_I2C": 0x209100bf.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GSA message on port I2C
    "CFG-MSGOUT-NMEA_ID_GSA_SPI": 0x209100c3.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GSA message on port SPI
    "CFG-MSGOUT-NMEA_ID_GSA_UART1": 0x209100c0.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GSA message on port UART1
    "CFG-MSGOUT-NMEA_ID_GSA_UART2": 0x209100c1.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GSA message on port UART2
    "CFG-MSGOUT-NMEA_ID_GSA_USB": 0x209100c2.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GSA message on port USB
    "CFG-MSGOUT-NMEA_ID_GST_I2C": 0x209100d3.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GST message on port I2C
    "CFG-MSGOUT-NMEA_ID_GST_SPI": 0x209100d7.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GST message on port SPI
    "CFG-MSGOUT-NMEA_ID_GST_UART1": 0x209100d4.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GST message on port UART1
    "CFG-MSGOUT-NMEA_ID_GST_UART2": 0x209100d5.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GST message on port UART2
    "CFG-MSGOUT-NMEA_ID_GST_USB": 0x209100d6.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GST message on port USB
    "CFG-MSGOUT-NMEA_ID_GSV_I2C": 0x209100c4.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GSV message on port I2C
    "CFG-MSGOUT-NMEA_ID_GSV_SPI": 0x209100c8.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GSV message on port SPI
    "CFG-MSGOUT-NMEA_ID_GSV_UART1": 0x209100c5.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GSV message on port UART1
    "CFG-MSGOUT-NMEA_ID_GSV_UART2": 0x209100c6.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GSV message on port UART2
    "CFG-MSGOUT-NMEA_ID_GSV_USB": 0x209100c7.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-GSV message on port USB
    "CFG-MSGOUT-NMEA_ID_RLM_I2C": 0x20910400.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-RLM message on port I2C
    "CFG-MSGOUT-NMEA_ID_RLM_SPI": 0x20910404.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-RLM message on port SPI
    "CFG-MSGOUT-NMEA_ID_RLM_UART1": 0x20910401.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-RLM message on port UART1
    "CFG-MSGOUT-NMEA_ID_RLM_UART2": 0x20910402.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-RLM message on port UART2
    "CFG-MSGOUT-NMEA_ID_RLM_USB": 0x20910403.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-RLM message on port USB
    "CFG-MSGOUT-NMEA_ID_RMC_I2C": 0x209100ab.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-RMC message on port I2C
    "CFG-MSGOUT-NMEA_ID_RMC_SPI": 0x209100af.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-RMC message on port SPI
    "CFG-MSGOUT-NMEA_ID_RMC_UART1": 0x209100ac.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-RMC message on port UART1
    "CFG-MSGOUT-NMEA_ID_RMC_UART2": 0x209100ad.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-RMC message on port UART2
    "CFG-MSGOUT-NMEA_ID_RMC_USB": 0x209100ae.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-RMC message on port USB
    "CFG-MSGOUT-NMEA_ID_VLW_I2C": 0x209100e7.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-VLW message on port I2C
    "CFG-MSGOUT-NMEA_ID_VLW_SPI": 0x209100eb.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-VLW message on port SPI
    "CFG-MSGOUT-NMEA_ID_VLW_UART1": 0x209100e8.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-VLW message on port UART1
    "CFG-MSGOUT-NMEA_ID_VLW_UART2": 0x209100e9.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-VLW message on port UART2
    "CFG-MSGOUT-NMEA_ID_VLW_USB": 0x209100ea.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-VLW message on port USB
    "CFG-MSGOUT-NMEA_ID_VTG_I2C": 0x209100b0.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-VTG message on port I2C
    "CFG-MSGOUT-NMEA_ID_VTG_SPI": 0x209100b4.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-VTG message on port SPI
    "CFG-MSGOUT-NMEA_ID_VTG_UART1": 0x209100b1.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-VTG message on port UART1
    "CFG-MSGOUT-NMEA_ID_VTG_UART2": 0x209100b2.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-VTG message on port UART2
    "CFG-MSGOUT-NMEA_ID_VTG_USB": 0x209100b3.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-VTG message on port USB
    "CFG-MSGOUT-NMEA_ID_ZDA_I2C": 0x209100d8.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-ZDA message on port I2C
    "CFG-MSGOUT-NMEA_ID_ZDA_SPI": 0x209100dc.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-ZDA message on port SPI
    "CFG-MSGOUT-NMEA_ID_ZDA_UART1": 0x209100d9.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-ZDA message on port UART1
    "CFG-MSGOUT-NMEA_ID_ZDA_UART2": 0x209100da.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-ZDA message on port UART2
    "CFG-MSGOUT-NMEA_ID_ZDA_USB": 0x209100db.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-ZDA message on port USB
    "CFG-MSGOUT-PUBX_ID_POLYP_I2C": 0x209100ec.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-PUBX00 message on port I2C
    "CFG-MSGOUT-PUBX_ID_POLYP_SPI": 0x209100f0.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-PUBX00 message on port SPI
    "CFG-MSGOUT-PUBX_ID_POLYP_UART1": 0x209100ed.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-PUBX00 message on port UART1
    "CFG-MSGOUT-PUBX_ID_POLYP_UART2": 0x209100ee.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-PUBX00 message on port UART2
    "CFG-MSGOUT-PUBX_ID_POLYP_USB": 0x209100ef.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-PUBX00 message on port USB
    "CFG-MSGOUT-PUBX_ID_POLYS_I2C": 0x209100f1.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-PUBX03 message on port I2C
    "CFG-MSGOUT-PUBX_ID_POLYS_SPI": 0x209100f5.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-PUBX03 message on port SPI
    "CFG-MSGOUT-PUBX_ID_POLYS_UART1": 0x209100f2.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-PUBX03 message on port UART1
    "CFG-MSGOUT-PUBX_ID_POLYS_UART2": 0x209100f3.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-PUBX03 message on port UART2
    "CFG-MSGOUT-PUBX_ID_POLYS_USB": 0x209100f4.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-PUBX03 message on port USB
    "CFG-MSGOUT-PUBX_ID_POLYT_I2C": 0x209100f6.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-PUBX04 message on port I2C
    "CFG-MSGOUT-PUBX_ID_POLYT_SPI": 0x209100fa.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-PUBX04 message on port SPI
    "CFG-MSGOUT-PUBX_ID_POLYT_UART1": 0x209100f7.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-PUBX04 message on port UART1
    "CFG-MSGOUT-PUBX_ID_POLYT_UART2": 0x209100f8.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-PUBX04 message on port UART2
    "CFG-MSGOUT-PUBX_ID_POLYT_USB": 0x209100f9.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the NMEA-GX-PUBX04 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1005_I2C": 0x209102bd.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1005 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1005_SPI": 0x209102c1.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1005 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1005_UART1": 0x209102be.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1005 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1005_UART2": 0x209102bf.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1005 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1005_USB": 0x209102c0.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1005 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1074_I2C": 0x2091035e.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1074 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1074_SPI": 0x20910362.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1074 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1074_UART1": 0x2091035f.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1074 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1074_UART2": 0x20910360.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1074 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1074_USB": 0x20910361.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1074 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1077_I2C": 0x209102cc.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1077 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1077_SPI": 0x209102d0.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1077 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1077_UART1": 0x209102cd.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1077 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1077_UART2": 0x209102ce.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1077 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1077_USB": 0x209102cf.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1077 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1084_I2C": 0x20910363.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1084 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1084_SPI": 0x20910367.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1084 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1084_UART1": 0x20910364.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1084 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1084_UART2": 0x20910365.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1084 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1084_USB": 0x20910366.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1084 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1087_I2C": 0x209102d1.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1087 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1087_SPI": 0x209102d5.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1087 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1087_UART1": 0x209102d2.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1087 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1087_UART2": 0x209102d3.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1087 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1087_USB": 0x209102d4.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1087 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1094_I2C": 0x20910368.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1094 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1094_SPI": 0x2091036c.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1094 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1094_UART1": 0x20910369.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1094 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1094_UART2": 0x2091036a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1094 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1094_USB": 0x2091036b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1094 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1097_I2C": 0x20910318.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1097 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1097_SPI": 0x2091031c.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1097 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1097_UART1": 0x20910319.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1097 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1097_UART2": 0x2091031a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1097 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1097_USB": 0x2091031b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1097 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1124_I2C": 0x2091036d.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1124 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1124_SPI": 0x20910371.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1124 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1124_UART1": 0x2091036e.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1124 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1124_UART2": 0x2091036f.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1124 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1124_USB": 0x20910370.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1124 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1127_I2C": 0x209102d6.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1127 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1127_SPI": 0x209102da.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1127 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1127_UART1": 0x209102d7.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1127 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1127_UART2": 0x209102d8.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1127 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1127_USB": 0x209102d9.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1127 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1230_I2C": 0x20910303.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1230 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1230_SPI": 0x20910307.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1230 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1230_UART1": 0x20910304.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1230 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1230_UART2": 0x20910305.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1230 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1230_USB": 0x20910306.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE1230 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE4072_0_I2C": 0x209102fe.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE4072_0 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE4072_0_SPI": 0x20910302.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE4072_0 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE4072_0_UART1": 0x209102ff.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE4072_0 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE4072_0_UART2": 0x20910300.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE4072_0 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE4072_0_USB": 0x20910301.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE4072_0 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE4072_1_I2C": 0x20910381.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE4072_1 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE4072_1_SPI": 0x20910385.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE4072_1 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE4072_1_UART1": 0x20910382.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE4072_1 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE4072_1_UART2": 0x20910383.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE4072_1 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE4072_1_USB": 0x20910384.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the RTCM-3X-TYPE4072_1 message on port USB
    "CFG-MSGOUT-UBX_LOG_INFO_I2C": 0x20910259.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-LOG-INFO message on port I2C
    "CFG-MSGOUT-UBX_LOG_INFO_SPI": 0x2091025d.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-LOG-INFO message on port SPI
    "CFG-MSGOUT-UBX_LOG_INFO_UART1": 0x2091025a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-LOG-INFO message on port UART1
    "CFG-MSGOUT-UBX_LOG_INFO_UART2": 0x2091025b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-LOG-INFO message on port UART2
    "CFG-MSGOUT-UBX_LOG_INFO_USB": 0x2091025c.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-LOG-INFO message on port USB
    "CFG-MSGOUT-UBX_MON_COMMS_I2C": 0x2091034f.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-COMMS message on port I2C
    "CFG-MSGOUT-UBX_MON_COMMS_SPI": 0x20910353.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-COMMS message on port SPI
    "CFG-MSGOUT-UBX_MON_COMMS_UART1": 0x20910350.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-COMMS message on port UART1
    "CFG-MSGOUT-UBX_MON_COMMS_UART2": 0x20910351.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-COMMS message on port UART2
    "CFG-MSGOUT-UBX_MON_COMMS_USB": 0x20910352.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-COMMS message on port USB
    "CFG-MSGOUT-UBX_MON_HW2_I2C": 0x209101b9.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-HW2 message on port I2C
    "CFG-MSGOUT-UBX_MON_HW2_SPI": 0x209101bd.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-HW2 message on port SPI
    "CFG-MSGOUT-UBX_MON_HW2_UART1": 0x209101ba.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-HW2 message on port UART1
    "CFG-MSGOUT-UBX_MON_HW2_UART2": 0x209101bb.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-HW2 message on port UART2
    "CFG-MSGOUT-UBX_MON_HW2_USB": 0x209101bc.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-HW2 message on port USB
    "CFG-MSGOUT-UBX_MON_HW3_I2C": 0x20910354.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-HW3 message on port I2C
    "CFG-MSGOUT-UBX_MON_HW3_SPI": 0x20910358.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-HW3 message on port SPI
    "CFG-MSGOUT-UBX_MON_HW3_UART1": 0x20910355.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-HW3 message on port UART1
    "CFG-MSGOUT-UBX_MON_HW3_UART2": 0x20910356.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-HW3 message on port UART2
    "CFG-MSGOUT-UBX_MON_HW3_USB": 0x20910357.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-HW3 message on port USB
    "CFG-MSGOUT-UBX_MON_HW_I2C": 0x209101b4.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-HW message on port I2C
    "CFG-MSGOUT-UBX_MON_HW_SPI": 0x209101b8.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-HW message on port SPI
    "CFG-MSGOUT-UBX_MON_HW_UART1": 0x209101b5.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-HW message on port UART1
    "CFG-MSGOUT-UBX_MON_HW_UART2": 0x209101b6.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-HW message on port UART2
    "CFG-MSGOUT-UBX_MON_HW_USB": 0x209101b7.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-HW message on port USB
    "CFG-MSGOUT-UBX_MON_IO_I2C": 0x209101a5.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-IO message on port I2C
    "CFG-MSGOUT-UBX_MON_IO_SPI": 0x209101a9.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-IO message on port SPI
    "CFG-MSGOUT-UBX_MON_IO_UART1": 0x209101a6.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-IO message on port UART1
    "CFG-MSGOUT-UBX_MON_IO_UART2": 0x209101a7.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-IO message on port UART2
    "CFG-MSGOUT-UBX_MON_IO_USB": 0x209101a8.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-IO message on port USB
    "CFG-MSGOUT-UBX_MON_MSGPP_I2C": 0x20910196.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-MSGPP message on port I2C
    "CFG-MSGOUT-UBX_MON_MSGPP_SPI": 0x2091019a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-MSGPP message on port SPI
    "CFG-MSGOUT-UBX_MON_MSGPP_UART1": 0x20910197.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-MSGPP message on port UART1
    "CFG-MSGOUT-UBX_MON_MSGPP_UART2": 0x20910198.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-MSGPP message on port UART2
    "CFG-MSGOUT-UBX_MON_MSGPP_USB": 0x20910199.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-MSGPP message on port USB
    "CFG-MSGOUT-UBX_MON_RF_I2C": 0x20910359.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-RF message on port I2C
    "CFG-MSGOUT-UBX_MON_RF_SPI": 0x2091035d.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-RF message on port SPI
    "CFG-MSGOUT-UBX_MON_RF_UART1": 0x2091035a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-RF message on port UART1
    "CFG-MSGOUT-UBX_MON_RF_UART2": 0x2091035b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-RF message on port UART2
    "CFG-MSGOUT-UBX_MON_RF_USB": 0x2091035c.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-RF message on port USB
    "CFG-MSGOUT-UBX_MON_RXBUF_I2C": 0x209101a0.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-RXBUF message on port I2C
    "CFG-MSGOUT-UBX_MON_RXBUF_SPI": 0x209101a4.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-RXBUF message on port SPI
    "CFG-MSGOUT-UBX_MON_RXBUF_UART1": 0x209101a1.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-RXBUF message on port UART1
    "CFG-MSGOUT-UBX_MON_RXBUF_UART2": 0x209101a2.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-RXBUF message on port UART2
    "CFG-MSGOUT-UBX_MON_RXBUF_USB": 0x209101a3.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-RXBUF message on port USB
    "CFG-MSGOUT-UBX_MON_RXR_I2C": 0x20910187.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-RXR message on port I2C
    "CFG-MSGOUT-UBX_MON_RXR_SPI": 0x2091018b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-RXR message on port SPI
    "CFG-MSGOUT-UBX_MON_RXR_UART1": 0x20910188.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-RXR message on port UART1
    "CFG-MSGOUT-UBX_MON_RXR_UART2": 0x20910189.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-RXR message on port UART2
    "CFG-MSGOUT-UBX_MON_RXR_USB": 0x2091018a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-RXR message on port USB
    "CFG-MSGOUT-UBX_MON_SPAN_I2C": 0x2091038b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-SPAN message on port I2C
    "CFG-MSGOUT-UBX_MON_SPAN_SPI": 0x2091038f.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-SPAN message on port SPI
    "CFG-MSGOUT-UBX_MON_SPAN_UART1": 0x2091038c.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-SPAN message on port UART1
    "CFG-MSGOUT-UBX_MON_SPAN_UART2": 0x2091038d.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-SPAN message on port UART2
    "CFG-MSGOUT-UBX_MON_SPAN_USB": 0x2091038e.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-SPAN message on port USB
    "CFG-MSGOUT-UBX_MON_TXBUF_I2C": 0x2091019b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-TXBUF message on port I2C
    "CFG-MSGOUT-UBX_MON_TXBUF_SPI": 0x2091019f.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-TXBUF message on port SPI
    "CFG-MSGOUT-UBX_MON_TXBUF_UART1": 0x2091019c.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-TXBUF message on port UART1
    "CFG-MSGOUT-UBX_MON_TXBUF_UART2": 0x2091019d.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-TXBUF message on port UART2
    "CFG-MSGOUT-UBX_MON_TXBUF_USB": 0x2091019e.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-MON-TXBUF message on port USB
    "CFG-MSGOUT-UBX_NAV_CLOCK_I2C": 0x20910065.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-CLOCK message on port I2C
    "CFG-MSGOUT-UBX_NAV_CLOCK_SPI": 0x20910069.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-CLOCK message on port SPI
    "CFG-MSGOUT-UBX_NAV_CLOCK_UART1": 0x20910066.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-CLOCK message on port UART1
    "CFG-MSGOUT-UBX_NAV_CLOCK_UART2": 0x20910067.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-CLOCK message on port UART2
    "CFG-MSGOUT-UBX_NAV_CLOCK_USB": 0x20910068.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-CLOCK message on port USB
    "CFG-MSGOUT-UBX_NAV_DOP_I2C": 0x20910038.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-DOP message on port I2C
    "CFG-MSGOUT-UBX_NAV_DOP_SPI": 0x2091003c.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-DOP message on port SPI
    "CFG-MSGOUT-UBX_NAV_DOP_UART1": 0x20910039.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-DOP message on port UART1
    "CFG-MSGOUT-UBX_NAV_DOP_UART2": 0x2091003a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-DOP message on port UART2
    "CFG-MSGOUT-UBX_NAV_DOP_USB": 0x2091003b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-DOP message on port USB
    "CFG-MSGOUT-UBX_NAV_EOE_I2C": 0x2091015f.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-EOE message on port I2C
    "CFG-MSGOUT-UBX_NAV_EOE_SPI": 0x20910163.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-EOE message on port SPI
    "CFG-MSGOUT-UBX_NAV_EOE_UART1": 0x20910160.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-EOE message on port UART1
    "CFG-MSGOUT-UBX_NAV_EOE_UART2": 0x20910161.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-EOE message on port UART2
    "CFG-MSGOUT-UBX_NAV_EOE_USB": 0x20910162.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-EOE message on port USB
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_I2C": 0x209100a1.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-GEOFENCE message on port I2C
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_SPI": 0x209100a5.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-GEOFENCE message on port SPI
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_UART1": 0x209100a2.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-GEOFENCE message on port UART1
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_UART2": 0x209100a3.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-GEOFENCE message on port UART2
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_USB": 0x209100a4.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-GEOFENCE message on port USB
    "CFG-MSGOUT-UBX_NAV_HPPOSECEF_I2C": 0x2091002e.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-HPPOSECEF message on port I2C
    "CFG-MSGOUT-UBX_NAV_HPPOSECEF_SPI": 0x20910032.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-HPPOSECEF message on port SPI
    "CFG-MSGOUT-UBX_NAV_HPPOSECEF_UART1": 0x2091002f.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-HPPOSECEF message on port UART1
    "CFG-MSGOUT-UBX_NAV_HPPOSECEF_UART2": 0x20910030.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-HPPOSECEF message on port UART2
    "CFG-MSGOUT-UBX_NAV_HPPOSECEF_USB": 0x20910031.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-HPPOSECEF message on port USB
    "CFG-MSGOUT-UBX_NAV_HPPOSLLH_I2C": 0x20910033.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-HPPOSLLH message on port I2C
    "CFG-MSGOUT-UBX_NAV_HPPOSLLH_SPI": 0x20910037.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-HPPOSLLH message on port SPI
    "CFG-MSGOUT-UBX_NAV_HPPOSLLH_UART1": 0x20910034.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-HPPOSLLH message on port UART1
    "CFG-MSGOUT-UBX_NAV_HPPOSLLH_UART2": 0x20910035.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-HPPOSLLH message on port UART2
    "CFG-MSGOUT-UBX_NAV_HPPOSLLH_USB": 0x20910036.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-HPPOSLLH message on port USB
    "CFG-MSGOUT-UBX_NAV_ODO_I2C": 0x2091007e.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-ODO message on port I2C
    "CFG-MSGOUT-UBX_NAV_ODO_SPI": 0x20910082.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-ODO message on port SPI
    "CFG-MSGOUT-UBX_NAV_ODO_UART1": 0x2091007f.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-ODO message on port UART1
    "CFG-MSGOUT-UBX_NAV_ODO_UART2": 0x20910080.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-ODO message on port UART2
    "CFG-MSGOUT-UBX_NAV_ODO_USB": 0x20910081.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-ODO message on port USB
    "CFG-MSGOUT-UBX_NAV_ORB_I2C": 0x20910010.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-ORB message on port I2C
    "CFG-MSGOUT-UBX_NAV_ORB_SPI": 0x20910014.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-ORB message on port SPI
    "CFG-MSGOUT-UBX_NAV_ORB_UART1": 0x20910011.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-ORB message on port UART1
    "CFG-MSGOUT-UBX_NAV_ORB_UART2": 0x20910012.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-ORB message on port UART2
    "CFG-MSGOUT-UBX_NAV_ORB_USB": 0x20910013.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-ORB message on port USB
    "CFG-MSGOUT-UBX_NAV_POSECEF_I2C": 0x20910024.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-POSECEF message on port I2C
    "CFG-MSGOUT-UBX_NAV_POSECEF_SPI": 0x20910028.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-POSECEF message on port SPI
    "CFG-MSGOUT-UBX_NAV_POSECEF_UART1": 0x20910025.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-POSECEF message on port UART1
    "CFG-MSGOUT-UBX_NAV_POSECEF_UART2": 0x20910026.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-POSECEF message on port UART2
    "CFG-MSGOUT-UBX_NAV_POSECEF_USB": 0x20910027.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-POSECEF message on port USB
    "CFG-MSGOUT-UBX_NAV_POSLLH_I2C": 0x20910029.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-POSLLH message on port I2C
    "CFG-MSGOUT-UBX_NAV_POSLLH_SPI": 0x2091002d.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-POSLLH message on port SPI
    "CFG-MSGOUT-UBX_NAV_POSLLH_UART1": 0x2091002a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-POSLLH message on port UART1
    "CFG-MSGOUT-UBX_NAV_POSLLH_UART2": 0x2091002b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-POSLLH message on port UART2
    "CFG-MSGOUT-UBX_NAV_POSLLH_USB": 0x2091002c.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-POSLLH message on port USB
    "CFG-MSGOUT-UBX_NAV_PVT_I2C": 0x20910006.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-PVT message on port I2C
    "CFG-MSGOUT-UBX_NAV_PVT_SPI": 0x2091000a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-PVT message on port SPI
    "CFG-MSGOUT-UBX_NAV_PVT_UART1": 0x20910007.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-PVT message on port UART1
    "CFG-MSGOUT-UBX_NAV_PVT_UART2": 0x20910008.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-PVT message on port UART2
    "CFG-MSGOUT-UBX_NAV_PVT_USB": 0x20910009.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-PVT message on port USB
    "CFG-MSGOUT-UBX_NAV_RELPOSNED_I2C": 0x2091008d.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-RELPOSNED message on port I2C
    "CFG-MSGOUT-UBX_NAV_RELPOSNED_SPI": 0x20910091.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-RELPOSNED message on port SPI
    "CFG-MSGOUT-UBX_NAV_RELPOSNED_UART1": 0x2091008e.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-RELPOSNED message on port UART1
    "CFG-MSGOUT-UBX_NAV_RELPOSNED_UART2": 0x2091008f.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-RELPOSNED message on port UART2
    "CFG-MSGOUT-UBX_NAV_RELPOSNED_USB": 0x20910090.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-RELPOSNED message on port USB
    "CFG-MSGOUT-UBX_NAV_SAT_I2C": 0x20910015.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SAT message on port I2C
    "CFG-MSGOUT-UBX_NAV_SAT_SPI": 0x20910019.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SAT message on port SPI
    "CFG-MSGOUT-UBX_NAV_SAT_UART1": 0x20910016.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SAT message on port UART1
    "CFG-MSGOUT-UBX_NAV_SAT_UART2": 0x20910017.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SAT message on port UART2
    "CFG-MSGOUT-UBX_NAV_SAT_USB": 0x20910018.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SAT message on port USB
    "CFG-MSGOUT-UBX_NAV_SBAS_I2C": 0x2091006a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SBAS message on port I2C
    "CFG-MSGOUT-UBX_NAV_SBAS_SPI": 0x2091006e.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SBAS message on port SPI
    "CFG-MSGOUT-UBX_NAV_SBAS_UART1": 0x2091006b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SBAS message on port UART1
    "CFG-MSGOUT-UBX_NAV_SBAS_UART2": 0x2091006c.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SBAS message on port UART2
    "CFG-MSGOUT-UBX_NAV_SBAS_USB": 0x2091006d.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SBAS message on port USB
    "CFG-MSGOUT-UBX_NAV_SIG_I2C": 0x20910345.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SIG message on port I2C
    "CFG-MSGOUT-UBX_NAV_SIG_SPI": 0x20910349.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SIG message on port SPI
    "CFG-MSGOUT-UBX_NAV_SIG_UART1": 0x20910346.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SIG message on port UART1
    "CFG-MSGOUT-UBX_NAV_SIG_UART2": 0x20910347.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SIG message on port UART2
    "CFG-MSGOUT-UBX_NAV_SIG_USB": 0x20910348.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SIG message on port USB
    "CFG-MSGOUT-UBX_NAV_SLAS_I2C": 0x20910336.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SLAS message on port I2C
    "CFG-MSGOUT-UBX_NAV_SLAS_SPI": 0x2091033a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SLAS message on port SPI
    "CFG-MSGOUT-UBX_NAV_SLAS_UART1": 0x20910337.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SLAS message on port UART1
    "CFG-MSGOUT-UBX_NAV_SLAS_UART2": 0x20910338.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SLAS message on port UART2
    "CFG-MSGOUT-UBX_NAV_SLAS_USB": 0x20910339.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SLAS message on port USB
    "CFG-MSGOUT-UBX_NAV_STATUS_I2C": 0x2091001a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-STATUS message on port I2C
    "CFG-MSGOUT-UBX_NAV_STATUS_SPI": 0x2091001e.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-STATUS message on port SPI
    "CFG-MSGOUT-UBX_NAV_STATUS_UART1": 0x2091001b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-STATUS message on port UART1
    "CFG-MSGOUT-UBX_NAV_STATUS_UART2": 0x2091001c.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-STATUS message on port UART2
    "CFG-MSGOUT-UBX_NAV_STATUS_USB": 0x2091001d.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-STATUS message on port USB
    "CFG-MSGOUT-UBX_NAV_SVIN_I2C": 0x20910088.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SVIN message on port I2C
    "CFG-MSGOUT-UBX_NAV_SVIN_SPI": 0x2091008c.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SVIN message on port SPI
    "CFG-MSGOUT-UBX_NAV_SVIN_UART1": 0x20910089.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SVIN message on port UART1
    "CFG-MSGOUT-UBX_NAV_SVIN_UART2": 0x2091008a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SVIN message on port UART2
    "CFG-MSGOUT-UBX_NAV_SVIN_USB": 0x2091008b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-SVIN message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_I2C": 0x20910051.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEBDS message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_SPI": 0x20910055.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEBDS message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_UART1": 0x20910052.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEBDS message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_UART2": 0x20910053.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEBDS message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_USB": 0x20910054.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEBDS message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_I2C": 0x20910056.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEGAL message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_SPI": 0x2091005a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEGAL message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_UART1": 0x20910057.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEGAL message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_UART2": 0x20910058.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEGAL message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_USB": 0x20910059.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEGAL message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_I2C": 0x2091004c.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEGLO message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_SPI": 0x20910050.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEGLO message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_UART1": 0x2091004d.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEGLO message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_UART2": 0x2091004e.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEGLO message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_USB": 0x2091004f.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEGLO message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_I2C": 0x20910047.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEGPS message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_SPI": 0x2091004b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEGPS message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_UART1": 0x20910048.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEGPS message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_UART2": 0x20910049.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEGPS message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_USB": 0x2091004a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEGPS message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMELS_I2C": 0x20910060.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMELS message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMELS_SPI": 0x20910064.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMELS message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMELS_UART1": 0x20910061.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMELS message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMELS_UART2": 0x20910062.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMELS message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMELS_USB": 0x20910063.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMELS message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_I2C": 0x20910386.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEQZSS message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_SPI": 0x2091038a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEQZSS message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_UART1": 0x20910387.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEQZSS message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_UART2": 0x20910388.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEQZSS message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_USB": 0x20910389.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEQZSS message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_I2C": 0x2091005b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEUTC message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_SPI": 0x2091005f.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEUTC message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_UART1": 0x2091005c.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEUTC message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_UART2": 0x2091005d.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEUTC message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_USB": 0x2091005e.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-TIMEUTC message on port USB
    "CFG-MSGOUT-UBX_NAV_VELECEF_I2C": 0x2091003d.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-VELECEF message on port I2C
    "CFG-MSGOUT-UBX_NAV_VELECEF_SPI": 0x20910041.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-VELECEF message on port SPI
    "CFG-MSGOUT-UBX_NAV_VELECEF_UART1": 0x2091003e.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-VELECEF message on port UART1
    "CFG-MSGOUT-UBX_NAV_VELECEF_UART2": 0x2091003f.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-VELECEF message on port UART2
    "CFG-MSGOUT-UBX_NAV_VELECEF_USB": 0x20910040.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-VELECEF message on port USB
    "CFG-MSGOUT-UBX_NAV_VELNED_I2C": 0x20910042.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-VELNED message on port I2C
    "CFG-MSGOUT-UBX_NAV_VELNED_SPI": 0x20910046.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-VELNED message on port SPI
    "CFG-MSGOUT-UBX_NAV_VELNED_UART1": 0x20910043.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-VELNED message on port UART1
    "CFG-MSGOUT-UBX_NAV_VELNED_UART2": 0x20910044.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-VELNED message on port UART2
    "CFG-MSGOUT-UBX_NAV_VELNED_USB": 0x20910045.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-NAV-VELNED message on port USB
    "CFG-MSGOUT-UBX_RXM_MEASX_I2C": 0x20910204.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-MEASX message on port I2C
    "CFG-MSGOUT-UBX_RXM_MEASX_SPI": 0x20910208.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-MEASX message on port SPI
    "CFG-MSGOUT-UBX_RXM_MEASX_UART1": 0x20910205.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-MEASX message on port UART1
    "CFG-MSGOUT-UBX_RXM_MEASX_UART2": 0x20910206.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-MEASX message on port UART2
    "CFG-MSGOUT-UBX_RXM_MEASX_USB": 0x20910207.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-MEASX message on port USB
    "CFG-MSGOUT-UBX_RXM_RAWX_I2C": 0x209102a4.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-RAWX message on port I2C
    "CFG-MSGOUT-UBX_RXM_RAWX_SPI": 0x209102a8.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-RAWX message on port SPI
    "CFG-MSGOUT-UBX_RXM_RAWX_UART1": 0x209102a5.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-RAWX message on port UART1
    "CFG-MSGOUT-UBX_RXM_RAWX_UART2": 0x209102a6.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-RAWX message on port UART2
    "CFG-MSGOUT-UBX_RXM_RAWX_USB": 0x209102a7.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-RAWX message on port USB
    "CFG-MSGOUT-UBX_RXM_RLM_I2C": 0x2091025e.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-RLM message on port I2C
    "CFG-MSGOUT-UBX_RXM_RLM_SPI": 0x20910262.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-RLM message on port SPI
    "CFG-MSGOUT-UBX_RXM_RLM_UART1": 0x2091025f.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-RLM message on port UART1
    "CFG-MSGOUT-UBX_RXM_RLM_UART2": 0x20910260.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-RLM message on port UART2
    "CFG-MSGOUT-UBX_RXM_RLM_USB": 0x20910261.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-RLM message on port USB
    "CFG-MSGOUT-UBX_RXM_RTCM_I2C": 0x20910268.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-RTCM message on port I2C
    "CFG-MSGOUT-UBX_RXM_RTCM_SPI": 0x2091026c.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-RTCM message on port SPI
    "CFG-MSGOUT-UBX_RXM_RTCM_UART1": 0x20910269.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-RTCM message on port UART1
    "CFG-MSGOUT-UBX_RXM_RTCM_UART2": 0x2091026a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-RTCM message on port UART2
    "CFG-MSGOUT-UBX_RXM_RTCM_USB": 0x2091026b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-RTCM message on port USB
    "CFG-MSGOUT-UBX_RXM_SFRBX_I2C": 0x20910231.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-SFRBX message on port I2C
    "CFG-MSGOUT-UBX_RXM_SFRBX_SPI": 0x20910235.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-SFRBX message on port SPI
    "CFG-MSGOUT-UBX_RXM_SFRBX_UART1": 0x20910232.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-SFRBX message on port UART1
    "CFG-MSGOUT-UBX_RXM_SFRBX_UART2": 0x20910233.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-SFRBX message on port UART2
    "CFG-MSGOUT-UBX_RXM_SFRBX_USB": 0x20910234.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-RXM-SFRBX message on port USB
    "CFG-MSGOUT-UBX_TIM_TM2_I2C": 0x20910178.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-TIM-TM2 message on port I2C
    "CFG-MSGOUT-UBX_TIM_TM2_SPI": 0x2091017c.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-TIM-TM2 message on port SPI
    "CFG-MSGOUT-UBX_TIM_TM2_UART1": 0x20910179.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-TIM-TM2 message on port UART1
    "CFG-MSGOUT-UBX_TIM_TM2_UART2": 0x2091017a.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-TIM-TM2 message on port UART2
    "CFG-MSGOUT-UBX_TIM_TM2_USB": 0x2091017b.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-TIM-TM2 message on port USB
    "CFG-MSGOUT-UBX_TIM_TP_I2C": 0x2091017d.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-TIM-TP message on port I2C
    "CFG-MSGOUT-UBX_TIM_TP_SPI": 0x20910181.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-TIM-TP message on port SPI
    "CFG-MSGOUT-UBX_TIM_TP_UART1": 0x2091017e.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-TIM-TP message on port UART1
    "CFG-MSGOUT-UBX_TIM_TP_UART2": 0x2091017f.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-TIM-TP message on port UART2
    "CFG-MSGOUT-UBX_TIM_TP_USB": 0x20910180.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-TIM-TP message on port USB
    "CFG-MSGOUT-UBX_TIM_VRFY_I2C": 0x20910092.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-TIM-VRFY message on port I2C
    "CFG-MSGOUT-UBX_TIM_VRFY_SPI": 0x20910096.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-TIM-VRFY message on port SPI
    "CFG-MSGOUT-UBX_TIM_VRFY_UART1": 0x20910093.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-TIM-VRFY message on port UART1
    "CFG-MSGOUT-UBX_TIM_VRFY_UART2": 0x20910094.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-TIM-VRFY message on port UART2
    "CFG-MSGOUT-UBX_TIM_VRFY_USB": 0x20910095.to_bytes(4, "little", signed=False),  # U1 - - Output rate of the UBX-TIM-VRFY message on port USB
}

# CFG-NAVHPG: High precision navigation configuration
# This group configures items related to the operation of the receiver in high precision, for example Differential correction and other related features.
# https://www.u-blox.com/en/docs/UBX-18010854#page=201&zoom=auto,-70,370
CFG_NAVHPG = {
    "CFG-NAVHPG-DGNSSMODE", 0x20140011.to_bytes(4, "little", signed=False),  # E1 - - Differential corrections mode. See Table 18 below for a list of possible constants for this item.
}
CFG_NAVHPG_DGNSSMODE = {  # Table 18
    "RTK_FLOAT": b"\x02",  # No attempts made to fix ambiguities
    "RTK_FIXED": b"\x03",  # Ambiguities are fixed whenever possible
}

# CFG-NAVSPG: Standard precision navigation configuration
# This group contains configuration items related to the operation of the receiver at standard. precision, including configuring postition fix mode, ionospheric model selection and other related items.
# https://www.u-blox.com/en/docs/UBX-18010854#page=201&zoom=auto,-70,187
CFG_NAVSPG = {
    "CFG-NAVSPG-FIXMODE": 0x20110011.to_bytes(4, "little", signed=False),  # E1 - - Position fix mode. See Table 20 below for a list of possible constants for this item.
    "CFG-NAVSPG-INIFIX3D": 0x10110013.to_bytes(4, "little", signed=False),  # L - - Initial fix must be a 3D fix.
    "CFG-NAVSPG-WKNROLLOVER": 0x30110017.to_bytes(4, "little", signed=False),  # U2 - - GPS week rollover number. GPS week numbers will be set correctly from this week up to 1024 weeks after this week. Range is from 1 to 4096.
    "CFG-NAVSPG-UTCSTANDARD": 0x2011001c.to_bytes(4, "little", signed=False),  # E1 - - UTC standard to be used. See also the section GNSS time base in the Integration manual. See Table 21 below for a list of possible constants for this item.
    "CFG-NAVSPG-DYNMODEL": 0x20110021.to_bytes(4, "little", signed=False),  # E1 - - Dynamic platform model. See Table 22 below for a list of possible constants for this item.
    "CFG-NAVSPG-ACKAIDING": 0x10110025.to_bytes(4, "little", signed=False),  # L - - Acknowledge assistance input messages.
    "CFG-NAVSPG-USE_USRDAT": 0x10110061.to_bytes(4, "little", signed=False),  # L - - Use user geodetic datum parameters. This must be set together with all CFG-NAVSPG-USERDAT_* parameters.
    "CFG-NAVSPG-USRDAT_MAJA": 0x50110062.to_bytes(4, "little", signed=False),  # R8 - m Geodetic datum semi-major axis. Accepted range is from 6,300,000.0 to 6,500,000.0 meters. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_FLAT": 0x50110063.to_bytes(4, "little", signed=False),  # R8 - - Geodetic datum 1.0 / flattening. Accepted range is 0.0 to 500.0. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_DX": 0x40110064.to_bytes(4, "little", signed=False),  # R4 - m Geodetic datum X axis shift at the origin. Accepted range is +/- 5000.0 meters. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_DY": 0x40110065.to_bytes(4, "little", signed=False),  # R4 - m Geodetic datum Y axis shift at the origin. Accepted range is +/- 5000.0 meters. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_DZ": 0x40110066.to_bytes(4, "little", signed=False),  # R4 - m Geodetic datum Z axis shift at the origin. Accepted range is +/- 5000.0 meters. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_.. parameters.
    "CFG-NAVSPG-USRDAT_ROTX": 0x40110067.to_bytes(4, "little", signed=False),  # R4 - arcsec Geodetic datum rotation about the X axis. Accepted range is +/- 20.0 milli arc seconds. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_ROTY": 0x40110068.to_bytes(4, "little", signed=False),  # R4 - arcsec Geodetic datum rotation about the Y axis (). Accepted range is +/- 20.0 milli-arc seconds. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_*. parameters.
    "CFG-NAVSPG-USRDAT_ROTZ": 0x40110069.to_bytes(4, "little", signed=False),  # R4 - arcsec Geodetic datum rotation about the Z axis. Accepted range is +/- 20.0 milli-arc seconds. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_SCALE": 0x4011006a.to_bytes(4, "little", signed=False),  # R4 - ppm Geodetic datum scale factor. Accepted range is 0.0 to 50.0 parts per million. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-INFIL_MINSVS": 0x201100a1.to_bytes(4, "little", signed=False),  # U1 - - Minimum number of satellites for navigation.
    "CFG-NAVSPG-INFIL_MAXSVS": 0x201100a2.to_bytes(4, "little", signed=False),  # U1 - - Maximum number of satellites for navigation.
    "CFG-NAVSPG-INFIL_MINCNO": 0x201100a3.to_bytes(4, "little", signed=False),  # U1 - dBHz Minimum satellite signal level for navigation.
    "CFG-NAVSPG-INFIL_MINELEV": 0x201100a4.to_bytes(4, "little", signed=False),  # I1 - deg Minimum elevation for a GNSS satellite to be. used in navigation.
    "CFG-NAVSPG-INFIL_NCNOTHRS": 0x201100aa.to_bytes(4, "little", signed=False),  # U1 - - Number of satellites required to have C/N0. above CFG-NAVSPG-INFIL_CNOTHRS for a fix to. be attempted.
    "CFG-NAVSPG-INFIL_CNOTHRS": 0x201100ab.to_bytes(4, "little", signed=False),  # U1 - - C/N0 threshold for deciding whether to attempt. a fix.
    "CFG-NAVSPG-OUTFIL_PDOP": 0x301100b1.to_bytes(4, "little", signed=False),  # U2 0.1 - Output filter position DOP mask (threshold).
    "CFG-NAVSPG-OUTFIL_TDOP": 0x301100b2.to_bytes(4, "little", signed=False),  # U2 0.1 - Output filter time DOP mask (threshold).
    "CFG-NAVSPG-OUTFIL_PACC": 0x301100b3.to_bytes(4, "little", signed=False),  # U2 - m Output filter position accuracy mask (threshold).
    "CFG-NAVSPG-OUTFIL_TACC": 0x301100b4.to_bytes(4, "little", signed=False),  # U2 - m Output filter time accuracy mask (threshold).
    "CFG-NAVSPG-OUTFIL_FACC": 0x301100b5.to_bytes(4, "little", signed=False),  # U2 0.01 m/s Output filter frequency accuracy mask. (threshold).
    "CFG-NAVSPG-CONSTR_ALT": 0x401100c1.to_bytes(4, "little", signed=False),  # I4 0.01 m Fixed altitude (mean sea level) for 2D fix mode.
    "CFG-NAVSPG-CONSTR_ALTVAR": 0x401100c2.to_bytes(4, "little", signed=False),  # U4 0.0001 m^2 Fixed altitude variance for 2D mode.
    "CFG-NAVSPG-CONSTR_DGNSSTO": 0x201100c4.to_bytes(4, "little", signed=False),  # U1 - s DGNSS timeout
}
CFG_NAVSPG_FIXMODE = {  #Table 20
    "2DONLY": b"\x01",  # 2D only
    "3DONLY": b"\x02",  # 3D only
    "AUTO": b"\x03",  # Auto 2D/3D
}
CFG_NAVSPG_UTCSTANDARD = {  #Table 21
    "AUTO": b"\x00",  # Automatic; receiver selects based on GNSS configuration
    "USNO": b"\x03",  # UTC as operated by the U.S. Naval Observatory (USNO); derived from GPS time
    "EU": b"\x05",  # UTC as combined from multiple European laboratories; derived from Galileo time
    "SU": b"\x06",  # UTC as operated by the former Soviet Union (SU); derived from GLONASS time
    "NTSC": b"\x07",  # UTC as operated by the National Time Service Center (NTSC), China; derived from BeiDou time
}
CFG_NAVSPG_DYNMODEL = {  # Table 22
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
    "CFG-NMEA-PROTVER": 0x20930001.to_bytes(4, "little", signed=False),  # E1 - - NMEA protocol version - - See Table 24 below for a list of possible constants for this item.
    "CFG-NMEA-MAXSVS": 0x20930002.to_bytes(4, "little", signed=False),  # E1 - - Maximum number of SVs to report per Talker ID - - See Table 25 below for a list of possible constants for this item.
    "CFG-NMEA-COMPAT": 0x10930003.to_bytes(4, "little", signed=False),  # L - - Enable compatibility mode - - This might be needed for certain applications, e.g. for an NMEA parser that expects a fixed number of digits in position coordinates.
    "CFG-NMEA-CONSIDER": 0x10930004.to_bytes(4, "little", signed=False),  # L - - Enable considering mode. This will affect NMEA output used satellite count. If set, also considered satellites (e.g. RAIMED) are counted as used satellites as well.
    "CFG-NMEA-LIMIT82": 0x10930005.to_bytes(4, "little", signed=False),  # L - - Enable strict limit to 82 characters maximum NMEA message length
    "CFG-NMEA-HIGHPREC": 0x10930006.to_bytes(4, "little", signed=False),  # L - - Enable high precision mode - - This flag cannot be set in conjunction with either CFG-NMEA-COMPAT or CFG-NMEA-LIMIT82 mode.
    "CFG-NMEA-SVNUMBERING": 0x20930007.to_bytes(4, "little", signed=False),  # E1 - - Display configuration for SVs that do not have value defined in NMEA. Configures the display of satellites that do not have an NMEA-defined value. Note: this does not apply to satellites with an unknown ID. See also Satellite Numbering. See Table 26 below for a list of possible constants for this item.
    "CFG-NMEA-FILT_GPS": 0x10930011.to_bytes(4, "little", signed=False),  # L - - Disable reporting of GPS satellites
    "CFG-NMEA-FILT_SBAS": 0x10930012.to_bytes(4, "little", signed=False),  # L - - Disable reporting of SBAS satellites
    "CFG-NMEA-FILT_GAL": 0x10930013.to_bytes(4, "little", signed=False),  # L - - Disable reporting of Galileo satellites
    "CFG-NMEA-FILT_QZSS": 0x10930015.to_bytes(4, "little", signed=False),  # L - - Disable reporting of QZSS satellites
    "CFG-NMEA-FILT_GLO": 0x10930016.to_bytes(4, "little", signed=False),  # L - - Disable reporting of GLONASS satellites
    "CFG-NMEA-FILT_BDS": 0x10930017.to_bytes(4, "little", signed=False),  # L - - Disable reporting of BeiDou satellites
    "CFG-NMEA-OUT_INVFIX": 0x10930021.to_bytes(4, "little", signed=False),  # L - - Enable position output for failed or invalid fixes
    "CFG-NMEA-OUT_MSKFIX": 0x10930022.to_bytes(4, "little", signed=False),  # L - - Enable position output for invalid fixes
    "CFG-NMEA-OUT_INVTIME": 0x10930023.to_bytes(4, "little", signed=False),  # L - - Enable time output for invalid times
    "CFG-NMEA-OUT_INVDATE": 0x10930024.to_bytes(4, "little", signed=False),  # L - - Enable date output for invalid dates
    "CFG-NMEA-OUT_ONLYGPS": 0x10930025.to_bytes(4, "little", signed=False),  # L - - Restrict output to GPS satellites only
    "CFG-NMEA-OUT_FROZENCOG": 0x10930026.to_bytes(4, "little", signed=False),  # L - - Enable course over ground output even if it is frozen
    "CFG-NMEA-MAINTALKERID": 0x20930031.to_bytes(4, "little", signed=False),  # E1 - - Main Talker ID. By default the main Talker ID (i.e. the Talker ID used for all messages other than GSV) is determined by the GNSS assignment of the receiver's channels (see CFG-SIGNAL). This field enables the main Talker ID to be overridden. See Table 27 below for a list of possible constants for this item.
    "CFG-NMEA-GSVTALKERID": 0x20930032.to_bytes(4, "little", signed=False),  # E1 - - Talker ID for GSV NMEA messages. By default the Talker ID for GSV messages is GNSS-specific (as defined by NMEA). This field enables the GSV Talker ID to be overridden. See Table 28 below for a list of possible constants for this item.
    "CFG-NMEA-BDSTALKERID": 0x30930033.to_bytes(4, "little", signed=False),  # U2 - - BeiDou Talker ID. Sets the two ASCII characters that should be used for the BeiDou Talker ID. If these are set to zero, the default BeiDou Talker ID will be used.
}
CFG_NMEA_PROTVER = {  # Table 24
    "V21": int(21).to_bytes(1, "little"),  # NMEA protocol version 2.1
    "V23": int(23).to_bytes(1, "little"),  # NMEA protocol version 2.3
    "V40": int(40).to_bytes(1, "little"),  # NMEA protocol version 4.0 (not available in all products)
    "V41": int(41).to_bytes(1, "little"),  # NMEA protocol version 4.10 (not available in all products)
    "V411": int(42).to_bytes(1, "little"),  # NMEA protocol version 4.11 (not available in all products)
}
CFG_NMEA_MAXSVS = {  # Table 25
    "UNLIM": int(0).to_bytes(1, "little"),  # Unlimited
    "8SVS": int(8).to_bytes(1, "little"),  # 8 SVs
    "12SVS": int(12).to_bytes(1, "little"),  # 12 SVs
    "16SVS": int(16).to_bytes(1, "little"),  # 16 SVs
}
CFG_NMEA_SVNUMBERING = {  # Table 26
    "STRICT": b"\x00",  # Strict - satellites are not output
    "EXTENDED": b"\x01",  # Extended - use proprietary numbering
}
CFG_NMEA_MAINTALKERID = {  # Table 27
    "AUTO": b"\x00",  # Main Talker ID is not overridden
    "GP": b"\x01",  # Set main Talker ID to 'GP'
    "GL": b"\x02",  # Set main Talker ID to 'GL'
    "GN": b"\x03",  # Set main Talker ID to 'GN'
    "GA": b"\x04",  # Set main Talker ID to 'GA' (not available in all products)
    "GB": b"\x05",  # Set main Talker ID to 'GB' (not available in all products)
    "GQ": b"\x07",  # Set main Talker ID to 'GQ' (not available in all products)
}
CFG_NMEA_GSVTALKERID = {  # Table 28
    "GNSS": b"\x00",  # Use GNSS-specific Talker ID (as defined by NMEA)
    "MAIN": b"\x01",  # Use the main Talker ID
}

# CFG-RATE: Navigation and measurement rate configuration
# The configuration items in this group allow the user to alter the rate at which navigation solutions (and the measurements that they depend on) are generated by the receiver. The calculation of the navigation solution will always be aligned to the top of a second zero (first second of the week) of the configured reference time system. The navigation period is an integer multiple of the measurement period.
# https://www.u-blox.com/en/docs/UBX-18010854#page=207&zoom=auto,-70,676
CFG_RATE = {
    "CFG-RATE-MEAS": 0x30210001.to_bytes(4, "little", signed=False),  # U2 0.001 s Nominal time between GNSS measurements. E.g. 100 ms results in 10 Hz measurement rate, 1000 ms = 1 Hz measurement rate.
    "CFG-RATE-NAV": 0x30210002.to_bytes(4, "little", signed=False),  # U2 - - Ratio of number of measurements to number of navigation solutions. E.g. 5 means five measurements for every navigation solution. The maximum value is 128.
    "CFG-RATE-TIMEREF": 0x20210003.to_bytes(4, "little", signed=False),  # E1 - - Time system to which measurements are aligned. See Table 33 below for a list of possible constants for this item.
}
CFG_RATE_TIMEREF = {  # Table 33
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
    "CFG-TMODE-MODE": 0x20030001.to_bytes(4, "little", signed=False),  # E1 - - Receiver mode. See Table 44 below for a list of possible constants for this item.
    "CFG-TMODE-POS_TYPE": 0x20030002.to_bytes(4, "little", signed=False),  # E1 - - Determines whether the ARP position is given in. ECEF or LAT/LON/HEIGHT?. See Table 45 below for a list of possible constants for this item.
    "CFG-TMODE-ECEF_X": 0x40030003.to_bytes(4, "little", signed=False),  # I4 - cm ECEF X coordinate of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-ECEF_Y": 0x40030004.to_bytes(4, "little", signed=False),  # I4 - cm ECEF Y coordinate of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-ECEF_Z": 0x40030005.to_bytes(4, "little", signed=False),  # I4 - cm ECEF Z coordinate of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-ECEF_X_HP": 0x20030006.to_bytes(4, "little", signed=False),  # I1 0.1 mm High-precision ECEF X coordinate of the ARP. position.. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-ECEF_Y_HP": 0x20030007.to_bytes(4, "little", signed=False),  # I1 0.1 mm High-precision ECEF Y coordinate of the ARP. position.. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-ECEF_Z_HP": 0x20030008.to_bytes(4, "little", signed=False),  # I1 0.1 mm High-precision ECEF Z coordinate of the ARP. position.. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-LAT": 0x40030009.to_bytes(4, "little", signed=False),  # I4 1e-7 deg Latitude of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-LON": 0x4003000a.to_bytes(4, "little", signed=False),  # I4 1e-7 deg Longitude of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-HEIGHT": 0x4003000b.to_bytes(4, "little", signed=False),  # I4 - cm Height of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-LAT_HP": 0x2003000c.to_bytes(4, "little", signed=False),  # I1 1e-9 deg High-precision latitude of the ARP position. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-LON_HP": 0x2003000d.to_bytes(4, "little", signed=False),  # I1 1e-9 deg High-precision longitude of the ARP position.. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-HEIGHT_HP": 0x2003000e.to_bytes(4, "little", signed=False),  # I1 0.1 mm High-precision height of the ARP position.. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-FIXED_POS_ACC": 0x4003000f.to_bytes(4, "little", signed=False),  # U4 0.1 mm Fixed position 3D accuracy.
    "CFG-TMODE-SVIN_MIN_DUR": 0x40030010.to_bytes(4, "little", signed=False),  # U4 - s Survey-in minimum duration. This will only be used if CFG-TMODE-MODE=SURVEY_IN.
    "CFG-TMODE-SVIN_ACC_LIMIT": 0x40030011.to_bytes(4, "little", signed=False),  # U4 0.1 mm Survey-in position accuracy limit. This will only be used if CFG-TMODE-MODE=SURVEY_IN.
}
CFG_TMODE_MODE = { # Table 44
    "DISABLED": b"\x00",  # Disabled
    "SURVEY_IN": b"\x01",  # Survey in
    "FIXED": b"\x02",  # Fixed mode (true ARP position information required)
}
CFG_TMODE_POS_TYPE = {  # Table 45
    "ECEF": b"\x00",  # Position is ECEF
    "LLH": b"\x01",  # Position is Lat/Lon/Height
}

# CFG-TP: Timepulse configuration
# Use this group to configure the generation of timepulses.
# https://www.u-blox.com/en/docs/UBX-18010854#page=213&zoom=auto,-70,694
CFG_TP = {
    "CFG-TP-PULSE_DEF": 0x20050023.to_bytes(4, "little", signed=False),  # E1 - - Determines whether the time pulse is interpreted as frequency or period. See Table 47 below for a list of possible constants for this item.
    "CFG-TP-PULSE_LENGTH_DEF": 0x20050030.to_bytes(4, "little", signed=False),  # E1 - - Determines whether the time pulse length is interpreted as length[us] or pulse ratio[%]. See Table 48 below for a list of possible constants for this item.
    "CFG-TP-ANT_CABLEDELAY": 0x30050001.to_bytes(4, "little", signed=False),  # I2 1e-9 s Antenna cable delay
    "CFG-TP-PERIOD_TP1": 0x40050002.to_bytes(4, "little", signed=False),  # U4 1e-6 s Time pulse period (TP1)
    "CFG-TP-PERIOD_LOCK_TP1": 0x40050003.to_bytes(4, "little", signed=False),  # U4 1e-6 s Time pulse period when locked to GNSS time (TP1) Only used if CFG-TP-USE_LOCKED_TP1 is set.
    "CFG-TP-FREQ_TP1": 0x40050024.to_bytes(4, "little", signed=False),  # U4 - Hz Time pulse frequency (TP1) This will only be used if CFG-TP-PULSE_DEF=FREQ.
    "CFG-TP-FREQ_LOCK_TP1": 0x40050025.to_bytes(4, "little", signed=False),  # U4 - Hz Time pulse frequency when locked to GNSS time (TP1) Only used if CFG-TP-USE_LOCKED_TP1 is set.
    "CFG-TP-LEN_TP1": 0x40050004.to_bytes(4, "little", signed=False),  # U4 1e-6 s Time pulse length (TP1)
    "CFG-TP-LEN_LOCK_TP1": 0x40050005.to_bytes(4, "little", signed=False),  # U4 1e-6 s Time pulse length when locked to GNSS time (TP1) Only used if CFG-TP-USE_LOCKED_TP1 is set.
    "CFG-TP-DUTY_TP1": 0x5005002a.to_bytes(4, "little", signed=False),  # R8 - % Time pulse duty cycle (TP1) Only used if CFG-TP-PULSE_LENGTH_DEF=RATIO is set.
    "CFG-TP-DUTY_LOCK_TP1": 0x5005002b.to_bytes(4, "little", signed=False),  # R8 - % Time pulse duty cycle when locked to GNSS time (TP1) Only used if CFG-TP-PULSE_LENGTH_DEF=RATIO and CFG-TP-USE_LOCKED_TP1 are set.
    "CFG-TP-USER_DELAY_TP1": 0x40050006.to_bytes(4, "little", signed=False),  # I4 1e-9 s User-configurable time pulse delay (TP1)
    "CFG-TP-TP1_ENA": 0x10050007.to_bytes(4, "little", signed=False),  # L - - Enable the first timepulse if pin associated with time pulse is assigned for another function, the other function takes precedence. Must be set for frequency-time products.
    "CFG-TP-SYNC_GNSS_TP1": 0x10050008.to_bytes(4, "little", signed=False),  # L - - Sync time pulse to GNSS time or local clock (TP1). If set, sync to GNSS if GNSS time is valid otherwise, if not set or not available, use local clock. Ignored by time-frequency product variants, which will attempt to use the best available time/frequency reference (not necessarily GNSS). This flag can be unset only in Timing product variants.
    "CFG-TP-USE_LOCKED_TP1": 0x10050009.to_bytes(4, "little", signed=False),  # L - - Use locked parameters when possible (TP1). If set, use CFG-TP-PERIOD_LOCK_TP1 and CFG-TP-LEN_LOCK_TP1 as soon as GNSS time is valid. Otherwise if not valid or not set, use CFG-TP-PERIOD_TP1 and CFG-TP-LEN_TP1.
    "CFG-TP-ALIGN_TO_TOW_TP1": 0x1005000a.to_bytes(4, "little", signed=False),  # L - - Align time pulse to top of second (TP1). To use this feature, CFG-TP-USE_LOCKED_TP1 must be set. Time pulse period must be an integer fraction of 1 second. Ignored in time-frequency product variants, where it is assumed always enabled.
    "CFG-TP-POL_TP1": 0x1005000b.to_bytes(4, "little", signed=False),  # L - - Set time pulse polarity (TP1). false (0) : falling edge at top of second. true (1) : rising edge at top of second.
    "CFG-TP-TIMEGRID_TP1": 0x2005000c.to_bytes(4, "little", signed=False),  # E1 - - Time grid to use (TP1). Only relevant if CFG-TP-USE_LOCKED_TP1 and ALIGN_TO_TOW_TP1 are set. Note that configured GNSS time is estimated by the receiver if locked to any GNSS system. If the receiver has a valid GNSS fix it will attempt to steer the TP to the specified time grid even if the specified time is not based on information from the constellation's satellites. To ensure timing based purely on a given GNSS, restrict the supported constellations in CFG-SIGNAL-*.
}
CFG_TP_PULSE_DEF = {  # Table 47
    "PERIOD": b"\x00",  # Time pulse period [us]
    "FREQ": b"\x01",  # Time pulse frequency [Hz]
}
CFG_TP_PULSE_LENGTH_DEF = {  # Table 48
    "RATIO": b"\x00",  # Time pulse ratio
    "LENGTH": b"\x01",  # Time pulse length
}
CFG_TP_TIMEGRID_TP1 = {  # Table 49
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
    "CFG-UART1-BAUDRATE": 0x40520001.to_bytes(4, "little", signed=False),  # U4 - - The baud rate that should be configured on the UART1 
    "CFG-UART1-STOPBITS": 0x20520002.to_bytes(4, "little", signed=False),  # E1 - - Number of stopbits that should be used on UART1 See  Table 53  below for a list of possible constants for this item. 
    "CFG-UART1-DATABITS": 0x20520003.to_bytes(4, "little", signed=False),  # E1 - - Number of databits that should be used on UART1 See  Table 54  below for a list of possible constants for this item. 
    "CFG-UART1-PARITY": 0x20520004.to_bytes(4, "little", signed=False),  # E1 - - Parity mode that should be used on UART1 See  Table 55  below for a list of possible constants for this item. 
    "CFG-UART1-ENABLED": 0x10520005.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if the UART1 should be enabled
}
CFG_UART1_STOPBITS = {  # Table 53, Table 59
    "HALF": b"\x00",  # 0.5 stopbits
    "ONE": b"\x01",  # 1.0 stopbits
    "ONEHALF": b"\x02",  # 1.5 stopbits
    "TWO": b"\x03",  # 2.0 stopbits
}
CFG_UART1_DATABITS = {  # Table 54, Table 60
    "EIGHT": b"\x00",  # 8 databits
    "SEVEN": b"\x01",  # 7 databits
}
CFG_UART1_PARITY = {  # Table 55, Table 61
    "NONE": b"\x00",  # No parity bit
    "ODD": b"\x01",  # Add an odd parity bit
    "EVEN": b"\x02",  # Add an even parity bit
}

# CFG-UART1INPROT: Input protocol configuration of the UART1 interface
# Input protocol enable flags of the UART1 interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=215&zoom=auto,-70,211
CFG_UART1INPROT = {
    "CFG-UART1INPROT-UBX": 0x10730001.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if UBX should be an input protocol on UART1
    "CFG-UART1INPROT-NMEA": 0x10730002.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if NMEA should be an input protocol on UART1
    "CFG-UART1INPROT-RTCM3X": 0x10730004.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if RTCM3X should be an input protocol on UART1
}

# CFG-UART1OUTPROT: Output protocol configuration of the UART1 interface
# Output protocol enable flags of the UART1 interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=216&zoom=auto,-70,685
CFG_UART1OUTPROT = {
    "CFG-UART1OUTPROT-UBX": 0x10740001.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if UBX should be an output protocol on UART1
    "CFG-UART1OUTPROT-NMEA": 0x10740002.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if NMEA should be an output protocol on UART1
    "CFG-UART1OUTPROT-RTCM3X": 0x10740004.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if RTCM3X should be an output protocol on UART1
}

# CFG-UART2: Configuration of the UART2 interface
# Settings needed to configure the UART2 communication interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=216&zoom=auto,-70,524
CFG_UART2 = {
    "CFG-UART2-BAUDRATE": 0x40530001.to_bytes(4, "little", signed=False),  # U4 - - The baud rate that should be configured on the UART2
    "CFG-UART2-STOPBITS": 0x20530002.to_bytes(4, "little", signed=False),  # E1 - - Number of stopbits that should be used on UART2 See  Table 59  below for a list of possible constants for this item. 
    "CFG-UART2-DATABITS": 0x20530003.to_bytes(4, "little", signed=False),  # E1 - - Number of databits that should be used on UART2 See  Table 60  below for a list of possible constants for this item. 
    "CFG-UART2-PARITY": 0x20530004.to_bytes(4, "little", signed=False),  # E1 - - Parity mode that should be used on UART2 See  Table 61  below for a list of possible constants for this item. 
    "CFG-UART2-ENABLED": 0x10530005.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if the UART2 should be enabled
    "CFG-UART2-REMAP": 0x10530006.to_bytes(4, "little", signed=False),  # L - - UART2 Remapping
}
# contants tables are defined at CFG_UART1

# CFG-UART2INPROT: Input protocol configuration of the UART2 interface
# Input protocol enable flags of the UART2 interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=217&zoom=auto,-70,678
CFG_UART2INPROT = {
    "CFG-UART2INPROT-UBX": 0x10750001.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if UBX should be an input protocol on UART2
    "CFG-UART2INPROT-NMEA": 0x10750002.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if NMEA should be an input protocol on UART2
    "CFG-UART2INPROT-RTCM3X": 0x10750004.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if RTCM3X should be an input protocol on UART2
}

# CFG-UART2OUTPROT: Output protocol configuration of the UART2 interface
# Output protocol enable flags of the UART2 interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=217&zoom=auto,-70,532
CFG_UART2OUTPROT = {
    "CFG-UART2OUTPROT-UBX": 0x10760001.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if UBX should be an output protocol on UART2
    "CFG-UART2OUTPROT-NMEA": 0x10760002.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if NMEA should be an output protocol on UART2
    "CFG-UART2OUTPROT-RTCM3X": 0x10760004.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if RTCM3X should be an output protocol on UART2
}

# CFG-USB: Configuration of the USB interface
# Settings needed to configure the USB communication interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=217&zoom=auto,-70,371
CFG_USB = {
    "CFG-USB-ENABLED": 0x10650001.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if the USB interface should be enabled 
    "CFG-USB-SELFPOW": 0x10650002.to_bytes(4, "little", signed=False),  # L - - Self-powered device 
    "CFG-USB-VENDOR_ID": 0x3065000a.to_bytes(4, "little", signed=False),  # U2 - - Vendor ID 
    "CFG-USB-PRODUCT_ID": 0x3065000b.to_bytes(4, "little", signed=False),  # U2 - - Vendor ID 
    "CFG-USB-POWER": 0x3065000c.to_bytes(4, "little", signed=False),  # U2 - mA Power consumption 
    "CFG-USB-VENDOR_STR0": 0x5065000d.to_bytes(4, "little", signed=False),  # X8 - - Vendor string characters 0-7 
    "CFG-USB-VENDOR_STR1": 0x5065000e.to_bytes(4, "little", signed=False),  # X8 - - Vendor string characters 8-15 
    "CFG-USB-VENDOR_STR2": 0x5065000f.to_bytes(4, "little", signed=False),  # X8 - - Vendor string characters 16-23 
    "CFG-USB-VENDOR_STR3": 0x50650010.to_bytes(4, "little", signed=False),  # X8 - - Vendor string characters 24-31 
    "CFG-USB-PRODUCT_STR0": 0x50650011.to_bytes(4, "little", signed=False),  # X8 - - Product string characters 0-7 
    "CFG-USB-PRODUCT_STR1": 0x50650012.to_bytes(4, "little", signed=False),  # X8 - - Product string characters 8-15 
    "CFG-USB-PRODUCT_STR2": 0x50650013.to_bytes(4, "little", signed=False),  # X8 - - Product string characters 16-23 
    "CFG-USB-PRODUCT_STR3": 0x50650014.to_bytes(4, "little", signed=False),  # X8 - - Product string characters 24-31 
    "CFG-USB-SERIAL_NO_STR0": 0x50650015.to_bytes(4, "little", signed=False),  # X8 - - Serial number string characters 0-7 
    "CFG-USB-SERIAL_NO_STR1": 0x50650016.to_bytes(4, "little", signed=False),  # X8 - - Serial number string characters 8-15 
    "CFG-USB-SERIAL_NO_STR2": 0x50650017.to_bytes(4, "little", signed=False),  # X8 - - Serial number string characters 16-23 
    "CFG-USB-SERIAL_NO_STR3": 0x50650018.to_bytes(4, "little", signed=False),  # X8 - - Serial number string characters 24-31
}

# CFG-USBINPROT: Input protocol configuration of the USB interface
# Input protocol enable flags of the USB interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=218&zoom=auto,-70,662
CFG_USBINPROT = {
    "CFG-USBINPROT-UBX": 0x10770001.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if UBX should be an input protocol on USB 
    "CFG-USBINPROT-NMEA": 0x10770002.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if NMEA should be an input protocol on USB 
    "CFG-USBINPROT-RTCM3X": 0x10770004.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if RTCM3X should be an input protocol on USB
}

# CFG-USBOUTPROT: Output protocol configuration of the USB interface
# Output protocol enable flags of the USB interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=218&zoom=auto,-70,517
CFG_USBOUTPROT = {
    "CFG-USBOUTPROT-UBX": 0x10780001.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if UBX should be an output protocol on USB
    "CFG-USBOUTPROT-NMEA": 0x10780002.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if NMEA should be an output protocol on USB
    "CFG-USBOUTPROT-RTCM3X": 0x10780004.to_bytes(4, "little", signed=False),  # L - - Flag to indicate if RTCM3X should be an output protocol on USB
}
