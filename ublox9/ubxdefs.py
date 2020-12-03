# Section 3.8, UBX messages overview
# extracted verbatim from https://www.u-blox.com/en/docs/UBX-18010854#page=49&zoom=auto,-74,575

# UBX-ACK – Acknowledgement and negative acknowledgement messages
UBX_ACK_ACK = ("UBX-ACK-ACK", b"\x05\x01")  # Message acknowledged (Output)
UBX_ACK_NAK = ("UBX-ACK-NAK", b"\x05\x00")  # Message not acknowledged (Output)

# UBX-CFG – Configuration and command messages
UBX_CFG_ANT = ("UBX-CFG-ANT", b"\x06\x13")  # Antenna control settings (Get/set)
UBX_CFG_CFG = ("UBX-CFG-CFG", b"\x06\x09")  # Clear, save and load configurations (Command)
UBX_CFG_DAT = ("UBX-CFG-DAT", b"\x06\x06")  # Set user-defined datum (Set) • Get currently defined datum (Get)
UBX_CFG_DGNSS = ("UBX-CFG-DGNSS", b"\x06\x70")  # DGNSS configuration (Get/set)
UBX_CFG_GEOFENCE = ("UBX-CFG-GEOFENCE", b"\x06\x69")  # Geofencing configuration (Get/set)
UBX_CFG_GNSS = ("UBX-CFG-GNSS", b"\x06\x3e")  # GNSS system configuration (Get/set)
UBX_CFG_INF = ("UBX-CFG-INF", b"\x06\x02")  # Poll configuration for one protocol (Poll request) • Information message configuration (Get/set)
UBX_CFG_ITFM = ("UBX-CFG-ITFM", b"\x06\x39")  # Jamming/interference monitor configuration (Get/set)
UBX_CFG_LOGFILTER = ("UBX-CFG-LOGFILTER", b"\x06\x47")  # Data logger configuration (Get/set)
UBX_CFG_MSG = ("UBX-CFG-MSG", b"\x06\x01")  # Poll a message configuration (Poll request) • Set message rate(s) (Get/set) • Set message rate (Get/set)
UBX_CFG_NAV5 = ("UBX-CFG-NAV5", b"\x06\x24")  # Navigation engine settings (Get/set)
UBX_CFG_NAVX5 = ("UBX-CFG-NAVX5", b"\x06\x23")  # Navigation engine expert settings (Get/set)
UBX_CFG_NMEA = ("UBX-CFG-NMEA", b"\x06\x17")  # Extended NMEA protocol configuration V1 (Get/set)
UBX_CFG_ODO = ("UBX-CFG-ODO", b"\x06\x1e")  # Odometer, low-speed COG engine settings (Get/set)
UBX_CFG_PRT = ("UBX-CFG-PRT", b"\x06\x00")  # Polls the configuration for one I/O port (Poll request) • Port configuration for UART ports (Get/set) • Port configuration for USB port (Get/set) • Port configuration for SPI port (Get/set) • Port configuration for I2C (DDC) port (Get/set)
UBX_CFG_PWR = ("UBX-CFG-PWR", b"\x06\x57")  # Put receiver in a defined power state (Set)
UBX_CFG_RATE = ("UBX-CFG-RATE", b"\x06\x08")  # Navigation/measurement rate settings (Get/set)
UBX_CFG_RINV = ("UBX-CFG-RINV", b"\x06\x34")  # Contents of remote inventory (Get/set)
UBX_CFG_RST = ("UBX-CFG-RST", b"\x06\x04")  # Reset receiver / Clear backup data structures (Command)
UBX_CFG_SBAS = ("UBX-CFG-SBAS", b"\x06\x16")  # SBAS configuration (Get/set)
UBX_CFG_TMODE3 = ("UBX-CFG-TMODE3", b"\x06\x71")  # Time mode settings 3 (Get/set)
UBX_CFG_TP5 = ("UBX-CFG-TP5", b"\x06\x31")  # Time pulse parameters (Get/set)
UBX_CFG_USB = ("UBX-CFG-USB", b"\x06\x1b")  # USB configuration (Get/set)
UBX_CFG_VALDEL = ("UBX-CFG-VALDEL", b"\x06\x8c")  # Delete configuration item values (Set) • Delete configuration item values (with transaction) (Set)
UBX_CFG_VALGET = ("UBX-CFG-VALGET", b"\x06\x8b")  # Get configuration items (Poll request) • Configuration items (Polled)
UBX_CFG_VALSET = ("UBX-CFG-VALSET", b"\x06\x8a")  # Set configuration item values (Set) • Set configuration item values (with transaction) (Set)

# UBX-INF – Information messages
UBX_INF_DEBUG = ("UBX-INF-DEBUG", b"\x04\x04")  # ASCII output with debug contents (Output)
UBX_INF_ERROR = ("UBX-INF-ERROR", b"\x04\x00")  # ASCII output with error contents (Output)
UBX_INF_NOTICE = ("UBX-INF-NOTICE", b"\x04\x02")  # ASCII output with informational contents (Output)
UBX_INF_TEST = ("UBX-INF-TEST", b"\x04\x03")  # ASCII output with test contents (Output)
UBX_INF_WARNING = ("UBX-INF-WARNING", b"\x04\x01")  # ASCII output with warning contents (Output)

# UBX-LOG – Logging messages
UBX_LOG_CREATE = ("UBX-LOG-CREATE", b"\x21\x07")  # Create log file (Command)
UBX_LOG_ERASE = ("UBX-LOG-ERASE", b"\x21\x03")  # Erase logged data (Command)
UBX_LOG_FINDTIME = ("UBX-LOG-FINDTIME", b"\x21\x0e")  # Find index of a log entry based on a given time (Input) • Response to FINDTIME request (Output)
UBX_LOG_INFO = ("UBX-LOG-INFO", b"\x21\x08")  # Poll for log information (Poll request) • Log information (Output)
UBX_LOG_RETRIEVE = ("UBX-LOG-RETRIEVE", b"\x21\x09")  # Request log data (Command) 
UBX_LOG_RETRIEVEPOS = ("UBX-LOG-RETRIEVEPOS", b"\x21\x0b")  # Position fix log entry (Output)
UBX_LOG_RETRIEVEPOSEXTRA = ("UBX-LOG-RETRIEVEPOSEXTRA", b"\x21\x0f")  # Odometer log entry (Output)
UBX_LOG_RETRIEVESTRING = ("UBX-LOG-RETRIEVESTRING", b"\x21\x0d")  # Byte string log entry (Output)
UBX_LOG_STRING = ("UBX-LOG-STRING", b"\x21\x04")  # Store arbitrary string in on-board flash (Command) 

# UBX-MGA – GNSS assistance (A-GNSS) messages 
UBX_MGA_ACK = ("UBX-MGA-ACK", b"\x13\x60")  # Multiple GNSS acknowledge message (Output)
UBX_MGA_BDS = ("UBX-MGA-BDS", b"\x13\x03")  # BeiDou ephemeris assistance (Input) • BeiDou almanac assistance (Input) • BeiDou health assistance (Input) • BeiDou UTC assistance (Input) • BeiDou ionosphere assistance (Input)
UBX_MGA_DBD = ("UBX-MGA-DBD", b"\x13\x80")  # Poll the navigation database (Poll request) • Navigation database dump entry (Input/output)
UBX_MGA_GAL = ("UBX-MGA-GAL", b"\x13\x02")  # Galileo ephemeris assistance (Input) • Galileo almanac assistance (Input) • Galileo GPS time offset assistance (Input) • Galileo UTC assistance (Input)
UBX_MGA_GLO = ("UBX-MGA-GLO", b"\x13\x06")  # GLONASS ephemeris assistance (Input) • GLONASS almanac assistance (Input) • GLONASS auxiliary time offset assistance (Input)
UBX_MGA_GPS = ("UBX-MGA-GPS", b"\x13\x00")  # GPS ephemeris assistance (Input) • GPS almanac assistance (Input) • GPS health assistance (Input) • GPS UTC assistance (Input) • GPS ionosphere assistance (Input)
UBX_MGA_INI = ("UBX-MGA-INI", b"\x13\x40")  # Initial position assistance (Input) • Initial time assistance (Input) • Initial clock drift assistance (Input) • Initial frequency assistance (Input) 
UBX_MGA_QZSS = ("UBX-MGA-QZSS", b"\x13\x05")  # QZSS ephemeris assistance (Input) • QZSS almanac assistance (Input) • QZSS health assistance (Input)

# UBX-MON – Monitoring messages
UBX_MON_COMMS = ("UBX-MON-COMMS", b"\x0a\x36")  # Communication port information (Periodic/polled) 
UBX_MON_GNSS = ("UBX-MON-GNSS", b"\x0a\x28")  # Information message major GNSS selection (Polled)
UBX_MON_HW = ("UBX-MON-HW", b"\x0a\x09")  # Hardware status (Periodic/polled) 
UBX_MON_HW2 = ("UBX-MON-HW2", b"\x0a\x0b")  # Extended hardware status (Periodic/polled)
UBX_MON_HW3 = ("UBX-MON-HW3", b"\x0a\x37")  # I/O pin status (Periodic/polled) 
UBX_MON_IO = ("UBX-MON-IO", b"\x0a\x02")  # I/O system status (Periodic/polled)
UBX_MON_MSGPP = ("UBX-MON-MSGPP", b"\x0a\x06")  # Message parse and process status (Periodic/polled)
UBX_MON_PATCH = ("UBX-MON-PATCH", b"\x0a\x27")  # Installed patches (Polled)
UBX_MON_RF = ("UBX-MON-RF", b"\x0a\x38")  # RF information (Periodic/polled)
UBX_MON_RXBUF = ("UBX-MON-RXBUF", b"\x0a\x07")  # Receiver buffer status (Periodic/polled)
UBX_MON_RXR = ("UBX-MON-RXR", b"\x0a\x21")  # Receiver status information (Output)
UBX_MON_SPAN = ("UBX-MON-SPAN", b"\x0a\x31")  # Signal characteristics (Periodic/polled)
UBX_MON_TXBUF = ("UBX-MON-TXBUF", b"\x0a\x08")  # Transmitter buffer status (Periodic/polled)
UBX_MON_VER = ("UBX-MON-VER", b"\x0a\x04")  # Receiver and software version (Polled)

# UBX-NAV – Navigation solution messages
UBX_NAV_CLOCK = ("UBX-NAV-CLOCK", b"\x01\x22")  # Clock solution (Periodic/polled) 
UBX_NAV_DOP = ("UBX-NAV-DOP", b"\x01\x04")  # Dilution of precision (Periodic/polled)
UBX_NAV_EOE = ("UBX-NAV-EOE", b"\x01\x61")  # End of epoch (Periodic) 
UBX_NAV_GEOFENCE = ("UBX-NAV-GEOFENCE", b"\x01\x39")  # Geofencing status (Periodic/polled)
UBX_NAV_HPPOSECEF = ("UBX-NAV-HPPOSECEF", b"\x01\x13")  # High precision position solution in ECEF (Periodic/polled)
UBX_NAV_HPPOSLLH = ("UBX-NAV-HPPOSLLH", b"\x01\x14")  # High precision geodetic position solution (Periodic/polled)
UBX_NAV_ODO = ("UBX-NAV-ODO", b"\x01\x09")  # Odometer solution (Periodic/polled)
UBX_NAV_ORB = ("UBX-NAV-ORB", b"\x01\x34")  # GNSS orbit database info (Periodic/polled)
UBX_NAV_POSECEF = ("UBX-NAV-POSECEF", b"\x01\x01")  # Position solution in ECEF (Periodic/polled)
UBX_NAV_POSLLH = ("UBX-NAV-POSLLH", b"\x01\x02")  # Geodetic position solution (Periodic/polled)
UBX_NAV_PVT = ("UBX-NAV-PVT", b"\x01\x07")  # Navigation position velocity time solution (Periodic/polled)
UBX_NAV_RELPOSNED = ("UBX-NAV-RELPOSNED", b"\x01\x3c")  # Relative positioning information in NED frame (Periodic/polled)
UBX_NAV_RESETODO = ("UBX-NAV-RESETODO", b"\x01\x10")  # Reset odometer (Command)
UBX_NAV_SAT = ("UBX-NAV-SAT", b"\x01\x35")  # Satellite information (Periodic/polled)
UBX_NAV_SBAS = ("UBX-NAV-SBAS", b"\x01\x32")  # SBAS status data (Periodic/polled) 
UBX_NAV_SIG = ("UBX-NAV-SIG", b"\x01\x43")  # Signal information (Periodic/polled)
UBX_NAV_SLAS = ("UBX-NAV-SLAS", b"\x01\x42")  # QZSS L1S SLAS status data (Periodic/polled)
UBX_NAV_STATUS = ("UBX-NAV-STATUS", b"\x01\x03")  # Receiver navigation status (Periodic/polled)
UBX_NAV_SVIN = ("UBX-NAV-SVIN", b"\x01\x3b")  # Survey-in data (Periodic/polled) 
UBX_NAV_TIMEBDS = ("UBX-NAV-TIMEBDS", b"\x01\x24")  # BeiDou time solution (Periodic/polled)
UBX_NAV_TIMEGAL = ("UBX-NAV-TIMEGAL", b"\x01\x25")  # Galileo time solution (Periodic/polled) 
UBX_NAV_TIMEGLO = ("UBX-NAV-TIMEGLO", b"\x01\x23")  # GLONASS time solution (Periodic/polled)
UBX_NAV_TIMELS = ("UBX-NAV-TIMELS", b"\x01\x26")  # Leap second event information (Periodic/polled) 
UBX_NAV_TIMEQZSS = ("UBX-NAV-TIMEQZSS", b"\x01\x27")  # QZSS time solution (Periodic/polled)
UBX_NAV_TIMEUTC = ("UBX-NAV-TIMEUTC", b"\x01\x21")  # UTC time solution (Periodic/polled) 
UBX_NAV_VELECEF = ("UBX-NAV-VELECEF", b"\x01\x11")  # Velocity solution in ECEF (Periodic/polled)
UBX_NAV_VELNED = ("UBX-NAV-VELNED", b"\x01\x12")  # Velocity solution in NED frame (Periodic/polled) 

# UBX-RXM – Receiver manager messages
UBX_RXM_MEASX = ("UBX-RXM-MEASX", b"\x02\x14")  # Satellite measurements for RRLP (Periodic/polled) 
UBX_RXM_PMREQ = ("UBX-RXM-PMREQ", b"\x02\x41")  # Power management request (Command)
UBX_RXM_RAWX = ("UBX-RXM-RAWX", b"\x02\x15")  # Multi-GNSS raw measurements (Periodic/polled) 
UBX_RXM_RLM = ("UBX-RXM-RLM", b"\x02\x59")  # Galileo SAR short-RLM report (Output) • Galileo SAR long-RLM report (Output)
UBX_RXM_RTCM = ("UBX-RXM-RTCM", b"\x02\x32")  # RTCM input status (Output) 
UBX_RXM_SFRBX = ("UBX-RXM-SFRBX", b"\x02\x13")  # Broadcast navigation data subframe (Output)

# UBX-SEC – Security messages
UBX_SEC_UNIQID = ("UBX-SEC-UNIQID", b"\x27\x03")  # Unique chip ID (Output) 

# UBX-TIM – Timing messages
UBX_TIM_TM2 = ("UBX-TIM-TM2", b"\x0d\x03")  # Time mark data (Periodic/polled) 
UBX_TIM_TP = ("UBX-TIM-TP", b"\x0d\x01")  # Time pulse time data (Periodic/polled)
UBX_TIM_VRFY = ("UBX-TIM-VRFY", b"\x0d\x06")  # Sourced time verification (Periodic/polled) 

# UBX-UPD – Firmware update messages
UBX_UPD_SOS = ("UBX-UPD-SOS", b"\x09\x14")  # Poll backup restore status (Poll request) • Create backup in flash (Command) • Clear backup in flash (Command) • Backup creation acknowledge (Output) • System restored from backup (Output)


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
CFG-INFMSG Information message configuration
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
CFG-TP Timepulse configuration
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

# CFG-MSGOUT: Message output configuration
# For each message and port a separate output rate (per second, per epoch) can be configured.
# https://www.u-blox.com/en/docs/UBX-18010854#page=186&zoom=auto,-70,208
CFG_MSGOUT = {
    "CFG-MSGOUT-NMEA_ID_DTM_I2C": b"\x20\x91\x00\xa6",  # U1 - - Output rate of the NMEA-GX-DTM message on port I2C
    "CFG-MSGOUT-NMEA_ID_DTM_SPI": b"\x20\x91\x00\xaa",  # U1 - - Output rate of the NMEA-GX-DTM message on port SPI
    "CFG-MSGOUT-NMEA_ID_DTM_UART1": b"\x20\x91\x00\xa7",  # U1 - - Output rate of the NMEA-GX-DTM message on port UART1
    "CFG-MSGOUT-NMEA_ID_DTM_UART2": b"\x20\x91\x00\xa8",  # U1 - - Output rate of the NMEA-GX-DTM message on port UART2
    "CFG-MSGOUT-NMEA_ID_DTM_USB": b"\x20\x91\x00\xa9",  # U1 - - Output rate of the NMEA-GX-DTM message on port USB
    "CFG-MSGOUT-NMEA_ID_GBS_I2C": b"\x20\x91\x00\xdd",  # U1 - - Output rate of the NMEA-GX-GBS message on port I2C
    "CFG-MSGOUT-NMEA_ID_GBS_SPI": b"\x20\x91\x00\xe1",  # U1 - - Output rate of the NMEA-GX-GBS message on port SPI
    "CFG-MSGOUT-NMEA_ID_GBS_UART1": b"\x20\x91\x00\xde",  # U1 - - Output rate of the NMEA-GX-GBS message on port UART1
    "CFG-MSGOUT-NMEA_ID_GBS_UART2": b"\x20\x91\x00\xdf",  # U1 - - Output rate of the NMEA-GX-GBS message on port UART2
    "CFG-MSGOUT-NMEA_ID_GBS_USB": b"\x20\x91\x00\xe0",  # U1 - - Output rate of the NMEA-GX-GBS message on port USB
    "CFG-MSGOUT-NMEA_ID_GGA_I2C": b"\x20\x91\x00\xba",  # U1 - - Output rate of the NMEA-GX-GGA message on port I2C
    "CFG-MSGOUT-NMEA_ID_GGA_SPI": b"\x20\x91\x00\xbe",  # U1 - - Output rate of the NMEA-GX-GGA message on port SPI
    "CFG-MSGOUT-NMEA_ID_GGA_UART1": b"\x20\x91\x00\xbb",  # U1 - - Output rate of the NMEA-GX-GGA message on port UART1
    "CFG-MSGOUT-NMEA_ID_GGA_UART2": b"\x20\x91\x00\xbc",  # U1 - - Output rate of the NMEA-GX-GGA message on port UART2
    "CFG-MSGOUT-NMEA_ID_GGA_USB": b"\x20\x91\x00\xbd",  # U1 - - Output rate of the NMEA-GX-GGA message on port USB
    "CFG-MSGOUT-NMEA_ID_GLL_I2C": b"\x20\x91\x00\xc9",  # U1 - - Output rate of the NMEA-GX-GLL message on port I2C
    "CFG-MSGOUT-NMEA_ID_GLL_SPI": b"\x20\x91\x00\xcd",  # U1 - - Output rate of the NMEA-GX-GLL message on port SPI
    "CFG-MSGOUT-NMEA_ID_GLL_UART1": b"\x20\x91\x00\xca",  # U1 - - Output rate of the NMEA-GX-GLL message on port UART1
    "CFG-MSGOUT-NMEA_ID_GLL_UART2": b"\x20\x91\x00\xcb",  # U1 - - Output rate of the NMEA-GX-GLL message on port UART2
    "CFG-MSGOUT-NMEA_ID_GLL_USB": b"\x20\x91\x00\xcc",  # U1 - - Output rate of the NMEA-GX-GLL message on port USB
    "CFG-MSGOUT-NMEA_ID_GNS_I2C": b"\x20\x91\x00\xb5",  # U1 - - Output rate of the NMEA-GX-GNS message on port I2C
    "CFG-MSGOUT-NMEA_ID_GNS_SPI": b"\x20\x91\x00\xb9",  # U1 - - Output rate of the NMEA-GX-GNS message on port SPI
    "CFG-MSGOUT-NMEA_ID_GNS_UART1": b"\x20\x91\x00\xb6",  # U1 - - Output rate of the NMEA-GX-GNS message on port UART1
    "CFG-MSGOUT-NMEA_ID_GNS_UART2": b"\x20\x91\x00\xb7",  # U1 - - Output rate of the NMEA-GX-GNS message on port UART2
    "CFG-MSGOUT-NMEA_ID_GNS_USB": b"\x20\x91\x00\xb8",  # U1 - - Output rate of the NMEA-GX-GNS message on port USB
    "CFG-MSGOUT-NMEA_ID_GRS_I2C": b"\x20\x91\x00\xce",  # U1 - - Output rate of the NMEA-GX-GRS message on port I2C
    "CFG-MSGOUT-NMEA_ID_GRS_SPI": b"\x20\x91\x00\xd2",  # U1 - - Output rate of the NMEA-GX-GRS message on port SPI
    "CFG-MSGOUT-NMEA_ID_GRS_UART1": b"\x20\x91\x00\xcf",  # U1 - - Output rate of the NMEA-GX-GRS message on port UART1
    "CFG-MSGOUT-NMEA_ID_GRS_UART2": b"\x20\x91\x00\xd0",  # U1 - - Output rate of the NMEA-GX-GRS message on port UART2
    "CFG-MSGOUT-NMEA_ID_GRS_USB": b"\x20\x91\x00\xd1",  # U1 - - Output rate of the NMEA-GX-GRS message on port USB
    "CFG-MSGOUT-NMEA_ID_GSA_I2C": b"\x20\x91\x00\xbf",  # U1 - - Output rate of the NMEA-GX-GSA message on port I2C
    "CFG-MSGOUT-NMEA_ID_GSA_SPI": b"\x20\x91\x00\xc3",  # U1 - - Output rate of the NMEA-GX-GSA message on port SPI
    "CFG-MSGOUT-NMEA_ID_GSA_UART1": b"\x20\x91\x00\xc0",  # U1 - - Output rate of the NMEA-GX-GSA message on port UART1
    "CFG-MSGOUT-NMEA_ID_GSA_UART2": b"\x20\x91\x00\xc1",  # U1 - - Output rate of the NMEA-GX-GSA message on port UART2
    "CFG-MSGOUT-NMEA_ID_GSA_USB": b"\x20\x91\x00\xc2",  # U1 - - Output rate of the NMEA-GX-GSA message on port USB
    "CFG-MSGOUT-NMEA_ID_GST_I2C": b"\x20\x91\x00\xd3",  # U1 - - Output rate of the NMEA-GX-GST message on port I2C
    "CFG-MSGOUT-NMEA_ID_GST_SPI": b"\x20\x91\x00\xd7",  # U1 - - Output rate of the NMEA-GX-GST message on port SPI
    "CFG-MSGOUT-NMEA_ID_GST_UART1": b"\x20\x91\x00\xd4",  # U1 - - Output rate of the NMEA-GX-GST message on port UART1
    "CFG-MSGOUT-NMEA_ID_GST_UART2": b"\x20\x91\x00\xd5",  # U1 - - Output rate of the NMEA-GX-GST message on port UART2
    "CFG-MSGOUT-NMEA_ID_GST_USB": b"\x20\x91\x00\xd6",  # U1 - - Output rate of the NMEA-GX-GST message on port USB
    "CFG-MSGOUT-NMEA_ID_GSV_I2C": b"\x20\x91\x00\xc4",  # U1 - - Output rate of the NMEA-GX-GSV message on port I2C
    "CFG-MSGOUT-NMEA_ID_GSV_SPI": b"\x20\x91\x00\xc8",  # U1 - - Output rate of the NMEA-GX-GSV message on port SPI
    "CFG-MSGOUT-NMEA_ID_GSV_UART1": b"\x20\x91\x00\xc5",  # U1 - - Output rate of the NMEA-GX-GSV message on port UART1
    "CFG-MSGOUT-NMEA_ID_GSV_UART2": b"\x20\x91\x00\xc6",  # U1 - - Output rate of the NMEA-GX-GSV message on port UART2
    "CFG-MSGOUT-NMEA_ID_GSV_USB": b"\x20\x91\x00\xc7",  # U1 - - Output rate of the NMEA-GX-GSV message on port USB
    "CFG-MSGOUT-NMEA_ID_RLM_I2C": b"\x20\x91\x04\x00",  # U1 - - Output rate of the NMEA-GX-RLM message on port I2C
    "CFG-MSGOUT-NMEA_ID_RLM_SPI": b"\x20\x91\x04\x04",  # U1 - - Output rate of the NMEA-GX-RLM message on port SPI
    "CFG-MSGOUT-NMEA_ID_RLM_UART1": b"\x20\x91\x04\x01",  # U1 - - Output rate of the NMEA-GX-RLM message on port UART1
    "CFG-MSGOUT-NMEA_ID_RLM_UART2": b"\x20\x91\x04\x02",  # U1 - - Output rate of the NMEA-GX-RLM message on port UART2
    "CFG-MSGOUT-NMEA_ID_RLM_USB": b"\x20\x91\x04\x03",  # U1 - - Output rate of the NMEA-GX-RLM message on port USB
    "CFG-MSGOUT-NMEA_ID_RMC_I2C": b"\x20\x91\x00\xab",  # U1 - - Output rate of the NMEA-GX-RMC message on port I2C
    "CFG-MSGOUT-NMEA_ID_RMC_SPI": b"\x20\x91\x00\xaf",  # U1 - - Output rate of the NMEA-GX-RMC message on port SPI
    "CFG-MSGOUT-NMEA_ID_RMC_UART1": b"\x20\x91\x00\xac",  # U1 - - Output rate of the NMEA-GX-RMC message on port UART1
    "CFG-MSGOUT-NMEA_ID_RMC_UART2": b"\x20\x91\x00\xad",  # U1 - - Output rate of the NMEA-GX-RMC message on port UART2
    "CFG-MSGOUT-NMEA_ID_RMC_USB": b"\x20\x91\x00\xae",  # U1 - - Output rate of the NMEA-GX-RMC message on port USB
    "CFG-MSGOUT-NMEA_ID_VLW_I2C": b"\x20\x91\x00\xe7",  # U1 - - Output rate of the NMEA-GX-VLW message on port I2C
    "CFG-MSGOUT-NMEA_ID_VLW_SPI": b"\x20\x91\x00\xeb",  # U1 - - Output rate of the NMEA-GX-VLW message on port SPI
    "CFG-MSGOUT-NMEA_ID_VLW_UART1": b"\x20\x91\x00\xe8",  # U1 - - Output rate of the NMEA-GX-VLW message on port UART1
    "CFG-MSGOUT-NMEA_ID_VLW_UART2": b"\x20\x91\x00\xe9",  # U1 - - Output rate of the NMEA-GX-VLW message on port UART2
    "CFG-MSGOUT-NMEA_ID_VLW_USB": b"\x20\x91\x00\xea",  # U1 - - Output rate of the NMEA-GX-VLW message on port USB
    "CFG-MSGOUT-NMEA_ID_VTG_I2C": b"\x20\x91\x00\xb0",  # U1 - - Output rate of the NMEA-GX-VTG message on port I2C
    "CFG-MSGOUT-NMEA_ID_VTG_SPI": b"\x20\x91\x00\xb4",  # U1 - - Output rate of the NMEA-GX-VTG message on port SPI
    "CFG-MSGOUT-NMEA_ID_VTG_UART1": b"\x20\x91\x00\xb1",  # U1 - - Output rate of the NMEA-GX-VTG message on port UART1
    "CFG-MSGOUT-NMEA_ID_VTG_UART2": b"\x20\x91\x00\xb2",  # U1 - - Output rate of the NMEA-GX-VTG message on port UART2
    "CFG-MSGOUT-NMEA_ID_VTG_USB": b"\x20\x91\x00\xb3",  # U1 - - Output rate of the NMEA-GX-VTG message on port USB
    "CFG-MSGOUT-NMEA_ID_ZDA_I2C": b"\x20\x91\x00\xd8",  # U1 - - Output rate of the NMEA-GX-ZDA message on port I2C
    "CFG-MSGOUT-NMEA_ID_ZDA_SPI": b"\x20\x91\x00\xdc",  # U1 - - Output rate of the NMEA-GX-ZDA message on port SPI
    "CFG-MSGOUT-NMEA_ID_ZDA_UART1": b"\x20\x91\x00\xd9",  # U1 - - Output rate of the NMEA-GX-ZDA message on port UART1
    "CFG-MSGOUT-NMEA_ID_ZDA_UART2": b"\x20\x91\x00\xda",  # U1 - - Output rate of the NMEA-GX-ZDA message on port UART2
    "CFG-MSGOUT-NMEA_ID_ZDA_USB": b"\x20\x91\x00\xdb",  # U1 - - Output rate of the NMEA-GX-ZDA message on port USB
    "CFG-MSGOUT-PUBX_ID_POLYP_I2C": b"\x20\x91\x00\xec",  # U1 - - Output rate of the NMEA-GX-PUBX00 message on port I2C
    "CFG-MSGOUT-PUBX_ID_POLYP_SPI": b"\x20\x91\x00\xf0",  # U1 - - Output rate of the NMEA-GX-PUBX00 message on port SPI
    "CFG-MSGOUT-PUBX_ID_POLYP_UART1": b"\x20\x91\x00\xed",  # U1 - - Output rate of the NMEA-GX-PUBX00 message on port UART1
    "CFG-MSGOUT-PUBX_ID_POLYP_UART2": b"\x20\x91\x00\xee",  # U1 - - Output rate of the NMEA-GX-PUBX00 message on port UART2
    "CFG-MSGOUT-PUBX_ID_POLYP_USB": b"\x20\x91\x00\xef",  # U1 - - Output rate of the NMEA-GX-PUBX00 message on port USB
    "CFG-MSGOUT-PUBX_ID_POLYS_I2C": b"\x20\x91\x00\xf1",  # U1 - - Output rate of the NMEA-GX-PUBX03 message on port I2C
    "CFG-MSGOUT-PUBX_ID_POLYS_SPI": b"\x20\x91\x00\xf5",  # U1 - - Output rate of the NMEA-GX-PUBX03 message on port SPI
    "CFG-MSGOUT-PUBX_ID_POLYS_UART1": b"\x20\x91\x00\xf2",  # U1 - - Output rate of the NMEA-GX-PUBX03 message on port UART1
    "CFG-MSGOUT-PUBX_ID_POLYS_UART2": b"\x20\x91\x00\xf3",  # U1 - - Output rate of the NMEA-GX-PUBX03 message on port UART2
    "CFG-MSGOUT-PUBX_ID_POLYS_USB": b"\x20\x91\x00\xf4",  # U1 - - Output rate of the NMEA-GX-PUBX03 message on port USB
    "CFG-MSGOUT-PUBX_ID_POLYT_I2C": b"\x20\x91\x00\xf6",  # U1 - - Output rate of the NMEA-GX-PUBX04 message on port I2C
    "CFG-MSGOUT-PUBX_ID_POLYT_SPI": b"\x20\x91\x00\xfa",  # U1 - - Output rate of the NMEA-GX-PUBX04 message on port SPI
    "CFG-MSGOUT-PUBX_ID_POLYT_UART1": b"\x20\x91\x00\xf7",  # U1 - - Output rate of the NMEA-GX-PUBX04 message on port UART1
    "CFG-MSGOUT-PUBX_ID_POLYT_UART2": b"\x20\x91\x00\xf8",  # U1 - - Output rate of the NMEA-GX-PUBX04 message on port UART2
    "CFG-MSGOUT-PUBX_ID_POLYT_USB": b"\x20\x91\x00\xf9",  # U1 - - Output rate of the NMEA-GX-PUBX04 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1005_I2C": b"\x20\x91\x02\xbd",  # U1 - - Output rate of the RTCM-3X-TYPE1005 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1005_SPI": b"\x20\x91\x02\xc1",  # U1 - - Output rate of the RTCM-3X-TYPE1005 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1005_UART1": b"\x20\x91\x02\xbe",  # U1 - - Output rate of the RTCM-3X-TYPE1005 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1005_UART2": b"\x20\x91\x02\xbf",  # U1 - - Output rate of the RTCM-3X-TYPE1005 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1005_USB": b"\x20\x91\x02\xc0",  # U1 - - Output rate of the RTCM-3X-TYPE1005 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1074_I2C": b"\x20\x91\x03\x5e",  # U1 - - Output rate of the RTCM-3X-TYPE1074 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1074_SPI": b"\x20\x91\x03\x62",  # U1 - - Output rate of the RTCM-3X-TYPE1074 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1074_UART1": b"\x20\x91\x03\x5f",  # U1 - - Output rate of the RTCM-3X-TYPE1074 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1074_UART2": b"\x20\x91\x03\x60",  # U1 - - Output rate of the RTCM-3X-TYPE1074 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1074_USB": b"\x20\x91\x03\x61",  # U1 - - Output rate of the RTCM-3X-TYPE1074 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1077_I2C": b"\x20\x91\x02\xcc",  # U1 - - Output rate of the RTCM-3X-TYPE1077 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1077_SPI": b"\x20\x91\x02\xd0",  # U1 - - Output rate of the RTCM-3X-TYPE1077 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1077_UART1": b"\x20\x91\x02\xcd",  # U1 - - Output rate of the RTCM-3X-TYPE1077 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1077_UART2": b"\x20\x91\x02\xce",  # U1 - - Output rate of the RTCM-3X-TYPE1077 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1077_USB": b"\x20\x91\x02\xcf",  # U1 - - Output rate of the RTCM-3X-TYPE1077 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1084_I2C": b"\x20\x91\x03\x63",  # U1 - - Output rate of the RTCM-3X-TYPE1084 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1084_SPI": b"\x20\x91\x03\x67",  # U1 - - Output rate of the RTCM-3X-TYPE1084 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1084_UART1": b"\x20\x91\x03\x64",  # U1 - - Output rate of the RTCM-3X-TYPE1084 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1084_UART2": b"\x20\x91\x03\x65",  # U1 - - Output rate of the RTCM-3X-TYPE1084 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1084_USB": b"\x20\x91\x03\x66",  # U1 - - Output rate of the RTCM-3X-TYPE1084 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1087_I2C": b"\x20\x91\x02\xd1",  # U1 - - Output rate of the RTCM-3X-TYPE1087 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1087_SPI": b"\x20\x91\x02\xd5",  # U1 - - Output rate of the RTCM-3X-TYPE1087 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1087_UART1": b"\x20\x91\x02\xd2",  # U1 - - Output rate of the RTCM-3X-TYPE1087 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1087_UART2": b"\x20\x91\x02\xd3",  # U1 - - Output rate of the RTCM-3X-TYPE1087 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1087_USB": b"\x20\x91\x02\xd4",  # U1 - - Output rate of the RTCM-3X-TYPE1087 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1094_I2C": b"\x20\x91\x03\x68",  # U1 - - Output rate of the RTCM-3X-TYPE1094 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1094_SPI": b"\x20\x91\x03\x6c",  # U1 - - Output rate of the RTCM-3X-TYPE1094 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1094_UART1": b"\x20\x91\x03\x69",  # U1 - - Output rate of the RTCM-3X-TYPE1094 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1094_UART2": b"\x20\x91\x03\x6a",  # U1 - - Output rate of the RTCM-3X-TYPE1094 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1094_USB": b"\x20\x91\x03\x6b",  # U1 - - Output rate of the RTCM-3X-TYPE1094 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1097_I2C": b"\x20\x91\x03\x18",  # U1 - - Output rate of the RTCM-3X-TYPE1097 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1097_SPI": b"\x20\x91\x03\x1c",  # U1 - - Output rate of the RTCM-3X-TYPE1097 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1097_UART1": b"\x20\x91\x03\x19",  # U1 - - Output rate of the RTCM-3X-TYPE1097 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1097_UART2": b"\x20\x91\x03\x1a",  # U1 - - Output rate of the RTCM-3X-TYPE1097 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1097_USB": b"\x20\x91\x03\x1b",  # U1 - - Output rate of the RTCM-3X-TYPE1097 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1124_I2C": b"\x20\x91\x03\x6d",  # U1 - - Output rate of the RTCM-3X-TYPE1124 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1124_SPI": b"\x20\x91\x03\x71",  # U1 - - Output rate of the RTCM-3X-TYPE1124 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1124_UART1": b"\x20\x91\x03\x6e",  # U1 - - Output rate of the RTCM-3X-TYPE1124 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1124_UART2": b"\x20\x91\x03\x6f",  # U1 - - Output rate of the RTCM-3X-TYPE1124 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1124_USB": b"\x20\x91\x03\x70",  # U1 - - Output rate of the RTCM-3X-TYPE1124 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1127_I2C": b"\x20\x91\x02\xd6",  # U1 - - Output rate of the RTCM-3X-TYPE1127 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1127_SPI": b"\x20\x91\x02\xda",  # U1 - - Output rate of the RTCM-3X-TYPE1127 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1127_UART1": b"\x20\x91\x02\xd7",  # U1 - - Output rate of the RTCM-3X-TYPE1127 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1127_UART2": b"\x20\x91\x02\xd8",  # U1 - - Output rate of the RTCM-3X-TYPE1127 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1127_USB": b"\x20\x91\x02\xd9",  # U1 - - Output rate of the RTCM-3X-TYPE1127 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE1230_I2C": b"\x20\x91\x03\x03",  # U1 - - Output rate of the RTCM-3X-TYPE1230 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE1230_SPI": b"\x20\x91\x03\x07",  # U1 - - Output rate of the RTCM-3X-TYPE1230 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE1230_UART1": b"\x20\x91\x03\x04",  # U1 - - Output rate of the RTCM-3X-TYPE1230 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE1230_UART2": b"\x20\x91\x03\x05",  # U1 - - Output rate of the RTCM-3X-TYPE1230 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE1230_USB": b"\x20\x91\x03\x06",  # U1 - - Output rate of the RTCM-3X-TYPE1230 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE4072_0_I2C": b"\x20\x91\x02\xfe",  # U1 - - Output rate of the RTCM-3X-TYPE4072_0 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE4072_0_SPI": b"\x20\x91\x03\x02",  # U1 - - Output rate of the RTCM-3X-TYPE4072_0 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE4072_0_UART1": b"\x20\x91\x02\xff",  # U1 - - Output rate of the RTCM-3X-TYPE4072_0 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE4072_0_UART2": b"\x20\x91\x03\x00",  # U1 - - Output rate of the RTCM-3X-TYPE4072_0 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE4072_0_USB": b"\x20\x91\x03\x01",  # U1 - - Output rate of the RTCM-3X-TYPE4072_0 message on port USB
    "CFG-MSGOUT-RTCM_3X_TYPE4072_1_I2C": b"\x20\x91\x03\x81",  # U1 - - Output rate of the RTCM-3X-TYPE4072_1 message on port I2C
    "CFG-MSGOUT-RTCM_3X_TYPE4072_1_SPI": b"\x20\x91\x03\x85",  # U1 - - Output rate of the RTCM-3X-TYPE4072_1 message on port SPI
    "CFG-MSGOUT-RTCM_3X_TYPE4072_1_UART1": b"\x20\x91\x03\x82",  # U1 - - Output rate of the RTCM-3X-TYPE4072_1 message on port UART1
    "CFG-MSGOUT-RTCM_3X_TYPE4072_1_UART2": b"\x20\x91\x03\x83",  # U1 - - Output rate of the RTCM-3X-TYPE4072_1 message on port UART2
    "CFG-MSGOUT-RTCM_3X_TYPE4072_1_USB": b"\x20\x91\x03\x84",  # U1 - - Output rate of the RTCM-3X-TYPE4072_1 message on port USB
    "CFG-MSGOUT-UBX_LOG_INFO_I2C": b"\x20\x91\x02\x59",  # U1 - - Output rate of the UBX-LOG-INFO message on port I2C
    "CFG-MSGOUT-UBX_LOG_INFO_SPI": b"\x20\x91\x02\x5d",  # U1 - - Output rate of the UBX-LOG-INFO message on port SPI
    "CFG-MSGOUT-UBX_LOG_INFO_UART1": b"\x20\x91\x02\x5a",  # U1 - - Output rate of the UBX-LOG-INFO message on port UART1
    "CFG-MSGOUT-UBX_LOG_INFO_UART2": b"\x20\x91\x02\x5b",  # U1 - - Output rate of the UBX-LOG-INFO message on port UART2
    "CFG-MSGOUT-UBX_LOG_INFO_USB": b"\x20\x91\x02\x5c",  # U1 - - Output rate of the UBX-LOG-INFO message on port USB
    "CFG-MSGOUT-UBX_MON_COMMS_I2C": b"\x20\x91\x03\x4f",  # U1 - - Output rate of the UBX-MON-COMMS message on port I2C
    "CFG-MSGOUT-UBX_MON_COMMS_SPI": b"\x20\x91\x03\x53",  # U1 - - Output rate of the UBX-MON-COMMS message on port SPI
    "CFG-MSGOUT-UBX_MON_COMMS_UART1": b"\x20\x91\x03\x50",  # U1 - - Output rate of the UBX-MON-COMMS message on port UART1
    "CFG-MSGOUT-UBX_MON_COMMS_UART2": b"\x20\x91\x03\x51",  # U1 - - Output rate of the UBX-MON-COMMS message on port UART2
    "CFG-MSGOUT-UBX_MON_COMMS_USB": b"\x20\x91\x03\x52",  # U1 - - Output rate of the UBX-MON-COMMS message on port USB
    "CFG-MSGOUT-UBX_MON_HW2_I2C": b"\x20\x91\x01\xb9",  # U1 - - Output rate of the UBX-MON-HW2 message on port I2C
    "CFG-MSGOUT-UBX_MON_HW2_SPI": b"\x20\x91\x01\xbd",  # U1 - - Output rate of the UBX-MON-HW2 message on port SPI
    "CFG-MSGOUT-UBX_MON_HW2_UART1": b"\x20\x91\x01\xba",  # U1 - - Output rate of the UBX-MON-HW2 message on port UART1
    "CFG-MSGOUT-UBX_MON_HW2_UART2": b"\x20\x91\x01\xbb",  # U1 - - Output rate of the UBX-MON-HW2 message on port UART2
    "CFG-MSGOUT-UBX_MON_HW2_USB": b"\x20\x91\x01\xbc",  # U1 - - Output rate of the UBX-MON-HW2 message on port USB
    "CFG-MSGOUT-UBX_MON_HW3_I2C": b"\x20\x91\x03\x54",  # U1 - - Output rate of the UBX-MON-HW3 message on port I2C
    "CFG-MSGOUT-UBX_MON_HW3_SPI": b"\x20\x91\x03\x58",  # U1 - - Output rate of the UBX-MON-HW3 message on port SPI
    "CFG-MSGOUT-UBX_MON_HW3_UART1": b"\x20\x91\x03\x55",  # U1 - - Output rate of the UBX-MON-HW3 message on port UART1
    "CFG-MSGOUT-UBX_MON_HW3_UART2": b"\x20\x91\x03\x56",  # U1 - - Output rate of the UBX-MON-HW3 message on port UART2
    "CFG-MSGOUT-UBX_MON_HW3_USB": b"\x20\x91\x03\x57",  # U1 - - Output rate of the UBX-MON-HW3 message on port USB
    "CFG-MSGOUT-UBX_MON_HW_I2C": b"\x20\x91\x01\xb4",  # U1 - - Output rate of the UBX-MON-HW message on port I2C
    "CFG-MSGOUT-UBX_MON_HW_SPI": b"\x20\x91\x01\xb8",  # U1 - - Output rate of the UBX-MON-HW message on port SPI
    "CFG-MSGOUT-UBX_MON_HW_UART1": b"\x20\x91\x01\xb5",  # U1 - - Output rate of the UBX-MON-HW message on port UART1
    "CFG-MSGOUT-UBX_MON_HW_UART2": b"\x20\x91\x01\xb6",  # U1 - - Output rate of the UBX-MON-HW message on port UART2
    "CFG-MSGOUT-UBX_MON_HW_USB": b"\x20\x91\x01\xb7",  # U1 - - Output rate of the UBX-MON-HW message on port USB
    "CFG-MSGOUT-UBX_MON_IO_I2C": b"\x20\x91\x01\xa5",  # U1 - - Output rate of the UBX-MON-IO message on port I2C
    "CFG-MSGOUT-UBX_MON_IO_SPI": b"\x20\x91\x01\xa9",  # U1 - - Output rate of the UBX-MON-IO message on port SPI
    "CFG-MSGOUT-UBX_MON_IO_UART1": b"\x20\x91\x01\xa6",  # U1 - - Output rate of the UBX-MON-IO message on port UART1
    "CFG-MSGOUT-UBX_MON_IO_UART2": b"\x20\x91\x01\xa7",  # U1 - - Output rate of the UBX-MON-IO message on port UART2
    "CFG-MSGOUT-UBX_MON_IO_USB": b"\x20\x91\x01\xa8",  # U1 - - Output rate of the UBX-MON-IO message on port USB
    "CFG-MSGOUT-UBX_MON_MSGPP_I2C": b"\x20\x91\x01\x96",  # U1 - - Output rate of the UBX-MON-MSGPP message on port I2C
    "CFG-MSGOUT-UBX_MON_MSGPP_SPI": b"\x20\x91\x01\x9a",  # U1 - - Output rate of the UBX-MON-MSGPP message on port SPI
    "CFG-MSGOUT-UBX_MON_MSGPP_UART1": b"\x20\x91\x01\x97",  # U1 - - Output rate of the UBX-MON-MSGPP message on port UART1
    "CFG-MSGOUT-UBX_MON_MSGPP_UART2": b"\x20\x91\x01\x98",  # U1 - - Output rate of the UBX-MON-MSGPP message on port UART2
    "CFG-MSGOUT-UBX_MON_MSGPP_USB": b"\x20\x91\x01\x99",  # U1 - - Output rate of the UBX-MON-MSGPP message on port USB
    "CFG-MSGOUT-UBX_MON_RF_I2C": b"\x20\x91\x03\x59",  # U1 - - Output rate of the UBX-MON-RF message on port I2C
    "CFG-MSGOUT-UBX_MON_RF_SPI": b"\x20\x91\x03\x5d",  # U1 - - Output rate of the UBX-MON-RF message on port SPI
    "CFG-MSGOUT-UBX_MON_RF_UART1": b"\x20\x91\x03\x5a",  # U1 - - Output rate of the UBX-MON-RF message on port UART1
    "CFG-MSGOUT-UBX_MON_RF_UART2": b"\x20\x91\x03\x5b",  # U1 - - Output rate of the UBX-MON-RF message on port UART2
    "CFG-MSGOUT-UBX_MON_RF_USB": b"\x20\x91\x03\x5c",  # U1 - - Output rate of the UBX-MON-RF message on port USB
    "CFG-MSGOUT-UBX_MON_RXBUF_I2C": b"\x20\x91\x01\xa0",  # U1 - - Output rate of the UBX-MON-RXBUF message on port I2C
    "CFG-MSGOUT-UBX_MON_RXBUF_SPI": b"\x20\x91\x01\xa4",  # U1 - - Output rate of the UBX-MON-RXBUF message on port SPI
    "CFG-MSGOUT-UBX_MON_RXBUF_UART1": b"\x20\x91\x01\xa1",  # U1 - - Output rate of the UBX-MON-RXBUF message on port UART1
    "CFG-MSGOUT-UBX_MON_RXBUF_UART2": b"\x20\x91\x01\xa2",  # U1 - - Output rate of the UBX-MON-RXBUF message on port UART2
    "CFG-MSGOUT-UBX_MON_RXBUF_USB": b"\x20\x91\x01\xa3",  # U1 - - Output rate of the UBX-MON-RXBUF message on port USB
    "CFG-MSGOUT-UBX_MON_RXR_I2C": b"\x20\x91\x01\x87",  # U1 - - Output rate of the UBX-MON-RXR message on port I2C
    "CFG-MSGOUT-UBX_MON_RXR_SPI": b"\x20\x91\x01\x8b",  # U1 - - Output rate of the UBX-MON-RXR message on port SPI
    "CFG-MSGOUT-UBX_MON_RXR_UART1": b"\x20\x91\x01\x88",  # U1 - - Output rate of the UBX-MON-RXR message on port UART1
    "CFG-MSGOUT-UBX_MON_RXR_UART2": b"\x20\x91\x01\x89",  # U1 - - Output rate of the UBX-MON-RXR message on port UART2
    "CFG-MSGOUT-UBX_MON_RXR_USB": b"\x20\x91\x01\x8a",  # U1 - - Output rate of the UBX-MON-RXR message on port USB
    "CFG-MSGOUT-UBX_MON_SPAN_I2C": b"\x20\x91\x03\x8b",  # U1 - - Output rate of the UBX-MON-SPAN message on port I2C
    "CFG-MSGOUT-UBX_MON_SPAN_SPI": b"\x20\x91\x03\x8f",  # U1 - - Output rate of the UBX-MON-SPAN message on port SPI
    "CFG-MSGOUT-UBX_MON_SPAN_UART1": b"\x20\x91\x03\x8c",  # U1 - - Output rate of the UBX-MON-SPAN message on port UART1
    "CFG-MSGOUT-UBX_MON_SPAN_UART2": b"\x20\x91\x03\x8d",  # U1 - - Output rate of the UBX-MON-SPAN message on port UART2
    "CFG-MSGOUT-UBX_MON_SPAN_USB": b"\x20\x91\x03\x8e",  # U1 - - Output rate of the UBX-MON-SPAN message on port USB
    "CFG-MSGOUT-UBX_MON_TXBUF_I2C": b"\x20\x91\x01\x9b",  # U1 - - Output rate of the UBX-MON-TXBUF message on port I2C
    "CFG-MSGOUT-UBX_MON_TXBUF_SPI": b"\x20\x91\x01\x9f",  # U1 - - Output rate of the UBX-MON-TXBUF message on port SPI
    "CFG-MSGOUT-UBX_MON_TXBUF_UART1": b"\x20\x91\x01\x9c",  # U1 - - Output rate of the UBX-MON-TXBUF message on port UART1
    "CFG-MSGOUT-UBX_MON_TXBUF_UART2": b"\x20\x91\x01\x9d",  # U1 - - Output rate of the UBX-MON-TXBUF message on port UART2
    "CFG-MSGOUT-UBX_MON_TXBUF_USB": b"\x20\x91\x01\x9e",  # U1 - - Output rate of the UBX-MON-TXBUF message on port USB
    "CFG-MSGOUT-UBX_NAV_CLOCK_I2C": b"\x20\x91\x00\x65",  # U1 - - Output rate of the UBX-NAV-CLOCK message on port I2C
    "CFG-MSGOUT-UBX_NAV_CLOCK_SPI": b"\x20\x91\x00\x69",  # U1 - - Output rate of the UBX-NAV-CLOCK message on port SPI
    "CFG-MSGOUT-UBX_NAV_CLOCK_UART1": b"\x20\x91\x00\x66",  # U1 - - Output rate of the UBX-NAV-CLOCK message on port UART1
    "CFG-MSGOUT-UBX_NAV_CLOCK_UART2": b"\x20\x91\x00\x67",  # U1 - - Output rate of the UBX-NAV-CLOCK message on port UART2
    "CFG-MSGOUT-UBX_NAV_CLOCK_USB": b"\x20\x91\x00\x68",  # U1 - - Output rate of the UBX-NAV-CLOCK message on port USB
    "CFG-MSGOUT-UBX_NAV_DOP_I2C": b"\x20\x91\x00\x38",  # U1 - - Output rate of the UBX-NAV-DOP message on port I2C
    "CFG-MSGOUT-UBX_NAV_DOP_SPI": b"\x20\x91\x00\x3c",  # U1 - - Output rate of the UBX-NAV-DOP message on port SPI
    "CFG-MSGOUT-UBX_NAV_DOP_UART1": b"\x20\x91\x00\x39",  # U1 - - Output rate of the UBX-NAV-DOP message on port UART1
    "CFG-MSGOUT-UBX_NAV_DOP_UART2": b"\x20\x91\x00\x3a",  # U1 - - Output rate of the UBX-NAV-DOP message on port UART2
    "CFG-MSGOUT-UBX_NAV_DOP_USB": b"\x20\x91\x00\x3b",  # U1 - - Output rate of the UBX-NAV-DOP message on port USB
    "CFG-MSGOUT-UBX_NAV_EOE_I2C": b"\x20\x91\x01\x5f",  # U1 - - Output rate of the UBX-NAV-EOE message on port I2C
    "CFG-MSGOUT-UBX_NAV_EOE_SPI": b"\x20\x91\x01\x63",  # U1 - - Output rate of the UBX-NAV-EOE message on port SPI
    "CFG-MSGOUT-UBX_NAV_EOE_UART1": b"\x20\x91\x01\x60",  # U1 - - Output rate of the UBX-NAV-EOE message on port UART1
    "CFG-MSGOUT-UBX_NAV_EOE_UART2": b"\x20\x91\x01\x61",  # U1 - - Output rate of the UBX-NAV-EOE message on port UART2
    "CFG-MSGOUT-UBX_NAV_EOE_USB": b"\x20\x91\x01\x62",  # U1 - - Output rate of the UBX-NAV-EOE message on port USB
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_I2C": b"\x20\x91\x00\xa1",  # U1 - - Output rate of the UBX-NAV-GEOFENCE message on port I2C
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_SPI": b"\x20\x91\x00\xa5",  # U1 - - Output rate of the UBX-NAV-GEOFENCE message on port SPI
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_UART1": b"\x20\x91\x00\xa2",  # U1 - - Output rate of the UBX-NAV-GEOFENCE message on port UART1
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_UART2": b"\x20\x91\x00\xa3",  # U1 - - Output rate of the UBX-NAV-GEOFENCE message on port UART2
    "CFG-MSGOUT-UBX_NAV_GEOFENCE_USB": b"\x20\x91\x00\xa4",  # U1 - - Output rate of the UBX-NAV-GEOFENCE message on port USB
    "CFG-MSGOUT-UBX_NAV_HPPOSECEF_I2C": b"\x20\x91\x00\x2e",  # U1 - - Output rate of the UBX-NAV-HPPOSECEF message on port I2C
    "CFG-MSGOUT-UBX_NAV_HPPOSECEF_SPI": b"\x20\x91\x00\x32",  # U1 - - Output rate of the UBX-NAV-HPPOSECEF message on port SPI
    "CFG-MSGOUT-UBX_NAV_HPPOSECEF_UART1": b"\x20\x91\x00\x2f",  # U1 - - Output rate of the UBX-NAV-HPPOSECEF message on port UART1
    "CFG-MSGOUT-UBX_NAV_HPPOSECEF_UART2": b"\x20\x91\x00\x30",  # U1 - - Output rate of the UBX-NAV-HPPOSECEF message on port UART2
    "CFG-MSGOUT-UBX_NAV_HPPOSECEF_USB": b"\x20\x91\x00\x31",  # U1 - - Output rate of the UBX-NAV-HPPOSECEF message on port USB
    "CFG-MSGOUT-UBX_NAV_HPPOSLLH_I2C": b"\x20\x91\x00\x33",  # U1 - - Output rate of the UBX-NAV-HPPOSLLH message on port I2C
    "CFG-MSGOUT-UBX_NAV_HPPOSLLH_SPI": b"\x20\x91\x00\x37",  # U1 - - Output rate of the UBX-NAV-HPPOSLLH message on port SPI
    "CFG-MSGOUT-UBX_NAV_HPPOSLLH_UART1": b"\x20\x91\x00\x34",  # U1 - - Output rate of the UBX-NAV-HPPOSLLH message on port UART1
    "CFG-MSGOUT-UBX_NAV_HPPOSLLH_UART2": b"\x20\x91\x00\x35",  # U1 - - Output rate of the UBX-NAV-HPPOSLLH message on port UART2
    "CFG-MSGOUT-UBX_NAV_HPPOSLLH_USB": b"\x20\x91\x00\x36",  # U1 - - Output rate of the UBX-NAV-HPPOSLLH message on port USB
    "CFG-MSGOUT-UBX_NAV_ODO_I2C": b"\x20\x91\x00\x7e",  # U1 - - Output rate of the UBX-NAV-ODO message on port I2C
    "CFG-MSGOUT-UBX_NAV_ODO_SPI": b"\x20\x91\x00\x82",  # U1 - - Output rate of the UBX-NAV-ODO message on port SPI
    "CFG-MSGOUT-UBX_NAV_ODO_UART1": b"\x20\x91\x00\x7f",  # U1 - - Output rate of the UBX-NAV-ODO message on port UART1
    "CFG-MSGOUT-UBX_NAV_ODO_UART2": b"\x20\x91\x00\x80",  # U1 - - Output rate of the UBX-NAV-ODO message on port UART2
    "CFG-MSGOUT-UBX_NAV_ODO_USB": b"\x20\x91\x00\x81",  # U1 - - Output rate of the UBX-NAV-ODO message on port USB
    "CFG-MSGOUT-UBX_NAV_ORB_I2C": b"\x20\x91\x00\x10",  # U1 - - Output rate of the UBX-NAV-ORB message on port I2C
    "CFG-MSGOUT-UBX_NAV_ORB_SPI": b"\x20\x91\x00\x14",  # U1 - - Output rate of the UBX-NAV-ORB message on port SPI
    "CFG-MSGOUT-UBX_NAV_ORB_UART1": b"\x20\x91\x00\x11",  # U1 - - Output rate of the UBX-NAV-ORB message on port UART1
    "CFG-MSGOUT-UBX_NAV_ORB_UART2": b"\x20\x91\x00\x12",  # U1 - - Output rate of the UBX-NAV-ORB message on port UART2
    "CFG-MSGOUT-UBX_NAV_ORB_USB": b"\x20\x91\x00\x13",  # U1 - - Output rate of the UBX-NAV-ORB message on port USB
    "CFG-MSGOUT-UBX_NAV_POSECEF_I2C": b"\x20\x91\x00\x24",  # U1 - - Output rate of the UBX-NAV-POSECEF message on port I2C
    "CFG-MSGOUT-UBX_NAV_POSECEF_SPI": b"\x20\x91\x00\x28",  # U1 - - Output rate of the UBX-NAV-POSECEF message on port SPI
    "CFG-MSGOUT-UBX_NAV_POSECEF_UART1": b"\x20\x91\x00\x25",  # U1 - - Output rate of the UBX-NAV-POSECEF message on port UART1
    "CFG-MSGOUT-UBX_NAV_POSECEF_UART2": b"\x20\x91\x00\x26",  # U1 - - Output rate of the UBX-NAV-POSECEF message on port UART2
    "CFG-MSGOUT-UBX_NAV_POSECEF_USB": b"\x20\x91\x00\x27",  # U1 - - Output rate of the UBX-NAV-POSECEF message on port USB
    "CFG-MSGOUT-UBX_NAV_POSLLH_I2C": b"\x20\x91\x00\x29",  # U1 - - Output rate of the UBX-NAV-POSLLH message on port I2C
    "CFG-MSGOUT-UBX_NAV_POSLLH_SPI": b"\x20\x91\x00\x2d",  # U1 - - Output rate of the UBX-NAV-POSLLH message on port SPI
    "CFG-MSGOUT-UBX_NAV_POSLLH_UART1": b"\x20\x91\x00\x2a",  # U1 - - Output rate of the UBX-NAV-POSLLH message on port UART1
    "CFG-MSGOUT-UBX_NAV_POSLLH_UART2": b"\x20\x91\x00\x2b",  # U1 - - Output rate of the UBX-NAV-POSLLH message on port UART2
    "CFG-MSGOUT-UBX_NAV_POSLLH_USB": b"\x20\x91\x00\x2c",  # U1 - - Output rate of the UBX-NAV-POSLLH message on port USB
    "CFG-MSGOUT-UBX_NAV_PVT_I2C": b"\x20\x91\x00\x06",  # U1 - - Output rate of the UBX-NAV-PVT message on port I2C
    "CFG-MSGOUT-UBX_NAV_PVT_SPI": b"\x20\x91\x00\x0a",  # U1 - - Output rate of the UBX-NAV-PVT message on port SPI
    "CFG-MSGOUT-UBX_NAV_PVT_UART1": b"\x20\x91\x00\x07",  # U1 - - Output rate of the UBX-NAV-PVT message on port UART1
    "CFG-MSGOUT-UBX_NAV_PVT_UART2": b"\x20\x91\x00\x08",  # U1 - - Output rate of the UBX-NAV-PVT message on port UART2
    "CFG-MSGOUT-UBX_NAV_PVT_USB": b"\x20\x91\x00\x09",  # U1 - - Output rate of the UBX-NAV-PVT message on port USB
    "CFG-MSGOUT-UBX_NAV_RELPOSNED_I2C": b"\x20\x91\x00\x8d",  # U1 - - Output rate of the UBX-NAV-RELPOSNED message on port I2C
    "CFG-MSGOUT-UBX_NAV_RELPOSNED_SPI": b"\x20\x91\x00\x91",  # U1 - - Output rate of the UBX-NAV-RELPOSNED message on port SPI
    "CFG-MSGOUT-UBX_NAV_RELPOSNED_UART1": b"\x20\x91\x00\x8e",  # U1 - - Output rate of the UBX-NAV-RELPOSNED message on port UART1
    "CFG-MSGOUT-UBX_NAV_RELPOSNED_UART2": b"\x20\x91\x00\x8f",  # U1 - - Output rate of the UBX-NAV-RELPOSNED message on port UART2
    "CFG-MSGOUT-UBX_NAV_RELPOSNED_USB": b"\x20\x91\x00\x90",  # U1 - - Output rate of the UBX-NAV-RELPOSNED message on port USB
    "CFG-MSGOUT-UBX_NAV_SAT_I2C": b"\x20\x91\x00\x15",  # U1 - - Output rate of the UBX-NAV-SAT message on port I2C
    "CFG-MSGOUT-UBX_NAV_SAT_SPI": b"\x20\x91\x00\x19",  # U1 - - Output rate of the UBX-NAV-SAT message on port SPI
    "CFG-MSGOUT-UBX_NAV_SAT_UART1": b"\x20\x91\x00\x16",  # U1 - - Output rate of the UBX-NAV-SAT message on port UART1
    "CFG-MSGOUT-UBX_NAV_SAT_UART2": b"\x20\x91\x00\x17",  # U1 - - Output rate of the UBX-NAV-SAT message on port UART2
    "CFG-MSGOUT-UBX_NAV_SAT_USB": b"\x20\x91\x00\x18",  # U1 - - Output rate of the UBX-NAV-SAT message on port USB
    "CFG-MSGOUT-UBX_NAV_SBAS_I2C": b"\x20\x91\x00\x6a",  # U1 - - Output rate of the UBX-NAV-SBAS message on port I2C
    "CFG-MSGOUT-UBX_NAV_SBAS_SPI": b"\x20\x91\x00\x6e",  # U1 - - Output rate of the UBX-NAV-SBAS message on port SPI
    "CFG-MSGOUT-UBX_NAV_SBAS_UART1": b"\x20\x91\x00\x6b",  # U1 - - Output rate of the UBX-NAV-SBAS message on port UART1
    "CFG-MSGOUT-UBX_NAV_SBAS_UART2": b"\x20\x91\x00\x6c",  # U1 - - Output rate of the UBX-NAV-SBAS message on port UART2
    "CFG-MSGOUT-UBX_NAV_SBAS_USB": b"\x20\x91\x00\x6d",  # U1 - - Output rate of the UBX-NAV-SBAS message on port USB
    "CFG-MSGOUT-UBX_NAV_SIG_I2C": b"\x20\x91\x03\x45",  # U1 - - Output rate of the UBX-NAV-SIG message on port I2C
    "CFG-MSGOUT-UBX_NAV_SIG_SPI": b"\x20\x91\x03\x49",  # U1 - - Output rate of the UBX-NAV-SIG message on port SPI
    "CFG-MSGOUT-UBX_NAV_SIG_UART1": b"\x20\x91\x03\x46",  # U1 - - Output rate of the UBX-NAV-SIG message on port UART1
    "CFG-MSGOUT-UBX_NAV_SIG_UART2": b"\x20\x91\x03\x47",  # U1 - - Output rate of the UBX-NAV-SIG message on port UART2
    "CFG-MSGOUT-UBX_NAV_SIG_USB": b"\x20\x91\x03\x48",  # U1 - - Output rate of the UBX-NAV-SIG message on port USB
    "CFG-MSGOUT-UBX_NAV_SLAS_I2C": b"\x20\x91\x03\x36",  # U1 - - Output rate of the UBX-NAV-SLAS message on port I2C
    "CFG-MSGOUT-UBX_NAV_SLAS_SPI": b"\x20\x91\x03\x3a",  # U1 - - Output rate of the UBX-NAV-SLAS message on port SPI
    "CFG-MSGOUT-UBX_NAV_SLAS_UART1": b"\x20\x91\x03\x37",  # U1 - - Output rate of the UBX-NAV-SLAS message on port UART1
    "CFG-MSGOUT-UBX_NAV_SLAS_UART2": b"\x20\x91\x03\x38",  # U1 - - Output rate of the UBX-NAV-SLAS message on port UART2
    "CFG-MSGOUT-UBX_NAV_SLAS_USB": b"\x20\x91\x03\x39",  # U1 - - Output rate of the UBX-NAV-SLAS message on port USB
    "CFG-MSGOUT-UBX_NAV_STATUS_I2C": b"\x20\x91\x00\x1a",  # U1 - - Output rate of the UBX-NAV-STATUS message on port I2C
    "CFG-MSGOUT-UBX_NAV_STATUS_SPI": b"\x20\x91\x00\x1e",  # U1 - - Output rate of the UBX-NAV-STATUS message on port SPI
    "CFG-MSGOUT-UBX_NAV_STATUS_UART1": b"\x20\x91\x00\x1b",  # U1 - - Output rate of the UBX-NAV-STATUS message on port UART1
    "CFG-MSGOUT-UBX_NAV_STATUS_UART2": b"\x20\x91\x00\x1c",  # U1 - - Output rate of the UBX-NAV-STATUS message on port UART2
    "CFG-MSGOUT-UBX_NAV_STATUS_USB": b"\x20\x91\x00\x1d",  # U1 - - Output rate of the UBX-NAV-STATUS message on port USB
    "CFG-MSGOUT-UBX_NAV_SVIN_I2C": b"\x20\x91\x00\x88",  # U1 - - Output rate of the UBX-NAV-SVIN message on port I2C
    "CFG-MSGOUT-UBX_NAV_SVIN_SPI": b"\x20\x91\x00\x8c",  # U1 - - Output rate of the UBX-NAV-SVIN message on port SPI
    "CFG-MSGOUT-UBX_NAV_SVIN_UART1": b"\x20\x91\x00\x89",  # U1 - - Output rate of the UBX-NAV-SVIN message on port UART1
    "CFG-MSGOUT-UBX_NAV_SVIN_UART2": b"\x20\x91\x00\x8a",  # U1 - - Output rate of the UBX-NAV-SVIN message on port UART2
    "CFG-MSGOUT-UBX_NAV_SVIN_USB": b"\x20\x91\x00\x8b",  # U1 - - Output rate of the UBX-NAV-SVIN message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_I2C": b"\x20\x91\x00\x51",  # U1 - - Output rate of the UBX-NAV-TIMEBDS message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_SPI": b"\x20\x91\x00\x55",  # U1 - - Output rate of the UBX-NAV-TIMEBDS message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_UART1": b"\x20\x91\x00\x52",  # U1 - - Output rate of the UBX-NAV-TIMEBDS message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_UART2": b"\x20\x91\x00\x53",  # U1 - - Output rate of the UBX-NAV-TIMEBDS message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEBDS_USB": b"\x20\x91\x00\x54",  # U1 - - Output rate of the UBX-NAV-TIMEBDS message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_I2C": b"\x20\x91\x00\x56",  # U1 - - Output rate of the UBX-NAV-TIMEGAL message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_SPI": b"\x20\x91\x00\x5a",  # U1 - - Output rate of the UBX-NAV-TIMEGAL message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_UART1": b"\x20\x91\x00\x57",  # U1 - - Output rate of the UBX-NAV-TIMEGAL message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_UART2": b"\x20\x91\x00\x58",  # U1 - - Output rate of the UBX-NAV-TIMEGAL message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEGAL_USB": b"\x20\x91\x00\x59",  # U1 - - Output rate of the UBX-NAV-TIMEGAL message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_I2C": b"\x20\x91\x00\x4c",  # U1 - - Output rate of the UBX-NAV-TIMEGLO message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_SPI": b"\x20\x91\x00\x50",  # U1 - - Output rate of the UBX-NAV-TIMEGLO message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_UART1": b"\x20\x91\x00\x4d",  # U1 - - Output rate of the UBX-NAV-TIMEGLO message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_UART2": b"\x20\x91\x00\x4e",  # U1 - - Output rate of the UBX-NAV-TIMEGLO message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEGLO_USB": b"\x20\x91\x00\x4f",  # U1 - - Output rate of the UBX-NAV-TIMEGLO message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_I2C": b"\x20\x91\x00\x47",  # U1 - - Output rate of the UBX-NAV-TIMEGPS message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_SPI": b"\x20\x91\x00\x4b",  # U1 - - Output rate of the UBX-NAV-TIMEGPS message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_UART1": b"\x20\x91\x00\x48",  # U1 - - Output rate of the UBX-NAV-TIMEGPS message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_UART2": b"\x20\x91\x00\x49",  # U1 - - Output rate of the UBX-NAV-TIMEGPS message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEGPS_USB": b"\x20\x91\x00\x4a",  # U1 - - Output rate of the UBX-NAV-TIMEGPS message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMELS_I2C": b"\x20\x91\x00\x60",  # U1 - - Output rate of the UBX-NAV-TIMELS message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMELS_SPI": b"\x20\x91\x00\x64",  # U1 - - Output rate of the UBX-NAV-TIMELS message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMELS_UART1": b"\x20\x91\x00\x61",  # U1 - - Output rate of the UBX-NAV-TIMELS message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMELS_UART2": b"\x20\x91\x00\x62",  # U1 - - Output rate of the UBX-NAV-TIMELS message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMELS_USB": b"\x20\x91\x00\x63",  # U1 - - Output rate of the UBX-NAV-TIMELS message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_I2C": b"\x20\x91\x03\x86",  # U1 - - Output rate of the UBX-NAV-TIMEQZSS message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_SPI": b"\x20\x91\x03\x8a",  # U1 - - Output rate of the UBX-NAV-TIMEQZSS message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_UART1": b"\x20\x91\x03\x87",  # U1 - - Output rate of the UBX-NAV-TIMEQZSS message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_UART2": b"\x20\x91\x03\x88",  # U1 - - Output rate of the UBX-NAV-TIMEQZSS message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEQZSS_USB": b"\x20\x91\x03\x89",  # U1 - - Output rate of the UBX-NAV-TIMEQZSS message on port USB
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_I2C": b"\x20\x91\x00\x5b",  # U1 - - Output rate of the UBX-NAV-TIMEUTC message on port I2C
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_SPI": b"\x20\x91\x00\x5f",  # U1 - - Output rate of the UBX-NAV-TIMEUTC message on port SPI
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_UART1": b"\x20\x91\x00\x5c",  # U1 - - Output rate of the UBX-NAV-TIMEUTC message on port UART1
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_UART2": b"\x20\x91\x00\x5d",  # U1 - - Output rate of the UBX-NAV-TIMEUTC message on port UART2
    "CFG-MSGOUT-UBX_NAV_TIMEUTC_USB": b"\x20\x91\x00\x5e",  # U1 - - Output rate of the UBX-NAV-TIMEUTC message on port USB
    "CFG-MSGOUT-UBX_NAV_VELECEF_I2C": b"\x20\x91\x00\x3d",  # U1 - - Output rate of the UBX-NAV-VELECEF message on port I2C
    "CFG-MSGOUT-UBX_NAV_VELECEF_SPI": b"\x20\x91\x00\x41",  # U1 - - Output rate of the UBX-NAV-VELECEF message on port SPI
    "CFG-MSGOUT-UBX_NAV_VELECEF_UART1": b"\x20\x91\x00\x3e",  # U1 - - Output rate of the UBX-NAV-VELECEF message on port UART1
    "CFG-MSGOUT-UBX_NAV_VELECEF_UART2": b"\x20\x91\x00\x3f",  # U1 - - Output rate of the UBX-NAV-VELECEF message on port UART2
    "CFG-MSGOUT-UBX_NAV_VELECEF_USB": b"\x20\x91\x00\x40",  # U1 - - Output rate of the UBX-NAV-VELECEF message on port USB
    "CFG-MSGOUT-UBX_NAV_VELNED_I2C": b"\x20\x91\x00\x42",  # U1 - - Output rate of the UBX-NAV-VELNED message on port I2C
    "CFG-MSGOUT-UBX_NAV_VELNED_SPI": b"\x20\x91\x00\x46",  # U1 - - Output rate of the UBX-NAV-VELNED message on port SPI
    "CFG-MSGOUT-UBX_NAV_VELNED_UART1": b"\x20\x91\x00\x43",  # U1 - - Output rate of the UBX-NAV-VELNED message on port UART1
    "CFG-MSGOUT-UBX_NAV_VELNED_UART2": b"\x20\x91\x00\x44",  # U1 - - Output rate of the UBX-NAV-VELNED message on port UART2
    "CFG-MSGOUT-UBX_NAV_VELNED_USB": b"\x20\x91\x00\x45",  # U1 - - Output rate of the UBX-NAV-VELNED message on port USB
    "CFG-MSGOUT-UBX_RXM_MEASX_I2C": b"\x20\x91\x02\x04",  # U1 - - Output rate of the UBX-RXM-MEASX message on port I2C
    "CFG-MSGOUT-UBX_RXM_MEASX_SPI": b"\x20\x91\x02\x08",  # U1 - - Output rate of the UBX-RXM-MEASX message on port SPI
    "CFG-MSGOUT-UBX_RXM_MEASX_UART1": b"\x20\x91\x02\x05",  # U1 - - Output rate of the UBX-RXM-MEASX message on port UART1
    "CFG-MSGOUT-UBX_RXM_MEASX_UART2": b"\x20\x91\x02\x06",  # U1 - - Output rate of the UBX-RXM-MEASX message on port UART2
    "CFG-MSGOUT-UBX_RXM_MEASX_USB": b"\x20\x91\x02\x07",  # U1 - - Output rate of the UBX-RXM-MEASX message on port USB
    "CFG-MSGOUT-UBX_RXM_RAWX_I2C": b"\x20\x91\x02\xa4",  # U1 - - Output rate of the UBX-RXM-RAWX message on port I2C
    "CFG-MSGOUT-UBX_RXM_RAWX_SPI": b"\x20\x91\x02\xa8",  # U1 - - Output rate of the UBX-RXM-RAWX message on port SPI
    "CFG-MSGOUT-UBX_RXM_RAWX_UART1": b"\x20\x91\x02\xa5",  # U1 - - Output rate of the UBX-RXM-RAWX message on port UART1
    "CFG-MSGOUT-UBX_RXM_RAWX_UART2": b"\x20\x91\x02\xa6",  # U1 - - Output rate of the UBX-RXM-RAWX message on port UART2
    "CFG-MSGOUT-UBX_RXM_RAWX_USB": b"\x20\x91\x02\xa7",  # U1 - - Output rate of the UBX-RXM-RAWX message on port USB
    "CFG-MSGOUT-UBX_RXM_RLM_I2C": b"\x20\x91\x02\x5e",  # U1 - - Output rate of the UBX-RXM-RLM message on port I2C
    "CFG-MSGOUT-UBX_RXM_RLM_SPI": b"\x20\x91\x02\x62",  # U1 - - Output rate of the UBX-RXM-RLM message on port SPI
    "CFG-MSGOUT-UBX_RXM_RLM_UART1": b"\x20\x91\x02\x5f",  # U1 - - Output rate of the UBX-RXM-RLM message on port UART1
    "CFG-MSGOUT-UBX_RXM_RLM_UART2": b"\x20\x91\x02\x60",  # U1 - - Output rate of the UBX-RXM-RLM message on port UART2
    "CFG-MSGOUT-UBX_RXM_RLM_USB": b"\x20\x91\x02\x61",  # U1 - - Output rate of the UBX-RXM-RLM message on port USB
    "CFG-MSGOUT-UBX_RXM_RTCM_I2C": b"\x20\x91\x02\x68",  # U1 - - Output rate of the UBX-RXM-RTCM message on port I2C
    "CFG-MSGOUT-UBX_RXM_RTCM_SPI": b"\x20\x91\x02\x6c",  # U1 - - Output rate of the UBX-RXM-RTCM message on port SPI
    "CFG-MSGOUT-UBX_RXM_RTCM_UART1": b"\x20\x91\x02\x69",  # U1 - - Output rate of the UBX-RXM-RTCM message on port UART1
    "CFG-MSGOUT-UBX_RXM_RTCM_UART2": b"\x20\x91\x02\x6a",  # U1 - - Output rate of the UBX-RXM-RTCM message on port UART2
    "CFG-MSGOUT-UBX_RXM_RTCM_USB": b"\x20\x91\x02\x6b",  # U1 - - Output rate of the UBX-RXM-RTCM message on port USB
    "CFG-MSGOUT-UBX_RXM_SFRBX_I2C": b"\x20\x91\x02\x31",  # U1 - - Output rate of the UBX-RXM-SFRBX message on port I2C
    "CFG-MSGOUT-UBX_RXM_SFRBX_SPI": b"\x20\x91\x02\x35",  # U1 - - Output rate of the UBX-RXM-SFRBX message on port SPI
    "CFG-MSGOUT-UBX_RXM_SFRBX_UART1": b"\x20\x91\x02\x32",  # U1 - - Output rate of the UBX-RXM-SFRBX message on port UART1
    "CFG-MSGOUT-UBX_RXM_SFRBX_UART2": b"\x20\x91\x02\x33",  # U1 - - Output rate of the UBX-RXM-SFRBX message on port UART2
    "CFG-MSGOUT-UBX_RXM_SFRBX_USB": b"\x20\x91\x02\x34",  # U1 - - Output rate of the UBX-RXM-SFRBX message on port USB
    "CFG-MSGOUT-UBX_TIM_TM2_I2C": b"\x20\x91\x01\x78",  # U1 - - Output rate of the UBX-TIM-TM2 message on port I2C
    "CFG-MSGOUT-UBX_TIM_TM2_SPI": b"\x20\x91\x01\x7c",  # U1 - - Output rate of the UBX-TIM-TM2 message on port SPI
    "CFG-MSGOUT-UBX_TIM_TM2_UART1": b"\x20\x91\x01\x79",  # U1 - - Output rate of the UBX-TIM-TM2 message on port UART1
    "CFG-MSGOUT-UBX_TIM_TM2_UART2": b"\x20\x91\x01\x7a",  # U1 - - Output rate of the UBX-TIM-TM2 message on port UART2
    "CFG-MSGOUT-UBX_TIM_TM2_USB": b"\x20\x91\x01\x7b",  # U1 - - Output rate of the UBX-TIM-TM2 message on port USB
    "CFG-MSGOUT-UBX_TIM_TP_I2C": b"\x20\x91\x01\x7d",  # U1 - - Output rate of the UBX-TIM-TP message on port I2C
    "CFG-MSGOUT-UBX_TIM_TP_SPI": b"\x20\x91\x01\x81",  # U1 - - Output rate of the UBX-TIM-TP message on port SPI
    "CFG-MSGOUT-UBX_TIM_TP_UART1": b"\x20\x91\x01\x7e",  # U1 - - Output rate of the UBX-TIM-TP message on port UART1
    "CFG-MSGOUT-UBX_TIM_TP_UART2": b"\x20\x91\x01\x7f",  # U1 - - Output rate of the UBX-TIM-TP message on port UART2
    "CFG-MSGOUT-UBX_TIM_TP_USB": b"\x20\x91\x01\x80",  # U1 - - Output rate of the UBX-TIM-TP message on port USB
    "CFG-MSGOUT-UBX_TIM_VRFY_I2C": b"\x20\x91\x00\x92",  # U1 - - Output rate of the UBX-TIM-VRFY message on port I2C
    "CFG-MSGOUT-UBX_TIM_VRFY_SPI": b"\x20\x91\x00\x96",  # U1 - - Output rate of the UBX-TIM-VRFY message on port SPI
    "CFG-MSGOUT-UBX_TIM_VRFY_UART1": b"\x20\x91\x00\x93",  # U1 - - Output rate of the UBX-TIM-VRFY message on port UART1
    "CFG-MSGOUT-UBX_TIM_VRFY_UART2": b"\x20\x91\x00\x94",  # U1 - - Output rate of the UBX-TIM-VRFY message on port UART2
    "CFG-MSGOUT-UBX_TIM_VRFY_USB": b"\x20\x91\x00\x95",  # U1 - - Output rate of the UBX-TIM-VRFY message on port USB
}

# CFG-NAVHPG: High precision navigation configuration
# This group configures items related to the operation of the receiver in high precision, for example Differential correction and other related features.
# https://www.u-blox.com/en/docs/UBX-18010854#page=201&zoom=auto,-70,370
CFG_NAVHPG = {
    "CFG-NAVHPG-DGNSSMODE", b"\x20\x14\x00\x11",  # E1 - - Differential corrections mode. See Table 18 below for a list of possible constants for this item.
}
CFG_NAVHPG_DGNSSMODE = {  # Table 18
    RTK_FLOAT: 2,  # No attempts made to fix ambiguities
    RTK_FIXED: 3,  # Ambiguities are fixed whenever possible
}

# CFG-NAVSPG: Standard precision navigation configuration
# This group contains configuration items related to the operation of the receiver at standard. precision, including configuring postition fix mode, ionospheric model selection and other related items.
# https://www.u-blox.com/en/docs/UBX-18010854#page=201&zoom=auto,-70,187
CFG_NAVSPG = {
    "CFG-NAVSPG-FIXMODE", b"\x20\x11\x00\x11",  # E1 - - Position fix mode. See Table 20 below for a list of possible constants for this item.
    "CFG-NAVSPG-INIFIX3D", b"\x10\x11\x00\x13",  # L - - Initial fix must be a 3D fix.
    "CFG-NAVSPG-WKNROLLOVER", b"\x30\x11\x00\x17",  # U2 - - GPS week rollover number. GPS week numbers will be set correctly from this week up to 1024 weeks after this week. Range is from 1 to 4096.
    "CFG-NAVSPG-UTCSTANDARD", b"\x20\x11\x00\x1c",  # E1 - - UTC standard to be used. See also the section GNSS time base in the Integration manual. See Table 21 below for a list of possible constants for this item.
    "CFG-NAVSPG-DYNMODEL", b"\x20\x11\x00\x21",  # E1 - - Dynamic platform model. See Table 22 below for a list of possible constants for this item.
    "CFG-NAVSPG-ACKAIDING", b"\x10\x11\x00\x25",  # L - - Acknowledge assistance input messages.
    "CFG-NAVSPG-USE_USRDAT", b"\x10\x11\x00\x61",  # L - - Use user geodetic datum parameters. This must be set together with all CFG-NAVSPG-USERDAT_* parameters.
    "CFG-NAVSPG-USRDAT_MAJA", b"\x50\x11\x00\x62",  # R8 - m Geodetic datum semi-major axis. Accepted range is from 6,300,000.0 to 6,500,000.0 meters. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_FLAT", b"\x50\x11\x00\x63",  # R8 - - Geodetic datum 1.0 / flattening. Accepted range is 0.0 to 500.0. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_DX", b"\x40\x11\x00\x64",  # R4 - m Geodetic datum X axis shift at the origin. Accepted range is +/- 5000.0 meters. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_DY", b"\x40\x11\x00\x65",  # R4 - m Geodetic datum Y axis shift at the origin. Accepted range is +/- 5000.0 meters. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_DZ", b"\x40\x11\x00\x66",  # R4 - m Geodetic datum Z axis shift at the origin. Accepted range is +/- 5000.0 meters. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_.. parameters.
    "CFG-NAVSPG-USRDAT_ROTX", b"\x40\x11\x00\x67",  # R4 - arcsec Geodetic datum rotation about the X axis. Accepted range is +/- 20.0 milli arc seconds. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_ROTY", b"\x40\x11\x00\x68",  # R4 - arcsec Geodetic datum rotation about the Y axis (). Accepted range is +/- 20.0 milli-arc seconds. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_*. parameters.
    "CFG-NAVSPG-USRDAT_ROTZ", b"\x40\x11\x00\x69",  # R4 - arcsec Geodetic datum rotation about the Z axis. Accepted range is +/- 20.0 milli-arc seconds. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-USRDAT_SCALE", b"\x40\x11\x00\x6a",  # R4 - ppm Geodetic datum scale factor. Accepted range is 0.0 to 50.0 parts per million. This will only be used if CFG-NAVSPG-USE_USERDAT is set. It must be set together with all other CFG-NAVSPGUSERDAT_... parameters.
    "CFG-NAVSPG-INFIL_MINSVS", b"\x20\x11\x00\xa1",  # U1 - - Minimum number of satellites for navigation.
    "CFG-NAVSPG-INFIL_MAXSVS", b"\x20\x11\x00\xa2",  # U1 - - Maximum number of satellites for navigation.
    "CFG-NAVSPG-INFIL_MINCNO", b"\x20\x11\x00\xa3",  # U1 - dBHz Minimum satellite signal level for navigation.
    "CFG-NAVSPG-INFIL_MINELEV", b"\x20\x11\x00\xa4",  # I1 - deg Minimum elevation for a GNSS satellite to be. used in navigation.
    "CFG-NAVSPG-INFIL_NCNOTHRS", b"\x20\x11\x00\xaa",  # U1 - - Number of satellites required to have C/N0. above CFG-NAVSPG-INFIL_CNOTHRS for a fix to. be attempted.
    "CFG-NAVSPG-INFIL_CNOTHRS", b"\x20\x11\x00\xab",  # U1 - - C/N0 threshold for deciding whether to attempt. a fix.
    "CFG-NAVSPG-OUTFIL_PDOP", b"\x30\x11\x00\xb1",  # U2 0.1 - Output filter position DOP mask (threshold).
    "CFG-NAVSPG-OUTFIL_TDOP", b"\x30\x11\x00\xb2",  # U2 0.1 - Output filter time DOP mask (threshold).
    "CFG-NAVSPG-OUTFIL_PACC", b"\x30\x11\x00\xb3",  # U2 - m Output filter position accuracy mask (threshold).
    "CFG-NAVSPG-OUTFIL_TACC", b"\x30\x11\x00\xb4",  # U2 - m Output filter time accuracy mask (threshold).
    "CFG-NAVSPG-OUTFIL_FACC", b"\x30\x11\x00\xb5",  # U2 0.01 m/s Output filter frequency accuracy mask. (threshold).
    "CFG-NAVSPG-CONSTR_ALT", b"\x40\x11\x00\xc1",  # I4 0.01 m Fixed altitude (mean sea level) for 2D fix mode.
    "CFG-NAVSPG-CONSTR_ALTVAR", b"\x40\x11\x00\xc2",  # U4 0.0001 m^2 Fixed altitude variance for 2D mode.
    "CFG-NAVSPG-CONSTR_DGNSSTO", b"\x20\x11\x00\xc4",  # U1 - s DGNSS timeout
}
CFG_NAVSPG_FIXMODE = {  #Table 20
    2DONLY: 1,  # 2D only
    3DONLY: 2,  # 3D only
    AUTO: 3,  # Auto 2D/3D
}
CFG_NAVSPG_UTCSTANDARD = {  #Table 21
    AUTO: 0,  # Automatic; receiver selects based on GNSS configuration
    USNO: 3,  # UTC as operated by the U.S. Naval Observatory (USNO); derived from GPS time
    EU: 5,  # UTC as combined from multiple European laboratories; derived from Galileo time
    SU: 6,  # UTC as operated by the former Soviet Union (SU); derived from GLONASS time
    NTSC: 7,  # UTC as operated by the National Time Service Center (NTSC), China; derived from BeiDou time
}
CFG_NAVSPG_DYNMODEL = {  # Table 22
    PORT: 0,  # Portable
    STAT: 2,  # Stationary
    PED: 3,  # Pedestrian
    AUTOMOT: 4,  # Automotive
    SEA: 5,  # Sea
    AIR1: 6,  # Airborne with <1g acceleration
    AIR2: 7,  # Airborne with <2g acceleration
    AIR4: 8,  # Airborne with <4g acceleration
    WRIST: 9,  # Wrist-worn watch (not available in all products)
}

# CFG-NMEA: NMEA protocol configuration
# This group configures the NMEA protocol. See section NMEA protocol configuration for a detailed description of the configuration effects on NMEA output.
# https://www.u-blox.com/en/docs/UBX-18010854#page=204&zoom=auto,-70,631
CFG_NMEA = {
    "CFG-NMEA-PROTVER", b"\x20\x93\x00\x01",  # E1 - - NMEA protocol version - - See Table 24 below for a list of possible constants for this item.
    "CFG-NMEA-MAXSVS", b"\x20\x93\x00\x02",  # E1 - - Maximum number of SVs to report per Talker ID - - See Table 25 below for a list of possible constants for this item.
    "CFG-NMEA-COMPAT", b"\x10\x93\x00\x03",  # L - - Enable compatibility mode - - This might be needed for certain applications, e.g. for an NMEA parser that expects a fixed number of digits in position coordinates.
    "CFG-NMEA-CONSIDER", b"\x10\x93\x00\x04",  # L - - Enable considering mode. This will affect NMEA output used satellite count. If set, also considered satellites (e.g. RAIMED) are counted as used satellites as well.
    "CFG-NMEA-LIMIT82", b"\x10\x93\x00\x05",  # L - - Enable strict limit to 82 characters maximum NMEA message length
    "CFG-NMEA-HIGHPREC", b"\x10\x93\x00\x06",  # L - - Enable high precision mode - - This flag cannot be set in conjunction with either CFG-NMEA-COMPAT or CFG-NMEA-LIMIT82 mode.
    "CFG-NMEA-SVNUMBERING", b"\x20\x93\x00\x07",  # E1 - - Display configuration for SVs that do not have value defined in NMEA. Configures the display of satellites that do not have an NMEA-defined value. Note: this does not apply to satellites with an unknown ID. See also Satellite Numbering. See Table 26 below for a list of possible constants for this item.
    "CFG-NMEA-FILT_GPS", b"\x10\x93\x00\x11",  # L - - Disable reporting of GPS satellites
    "CFG-NMEA-FILT_SBAS", b"\x10\x93\x00\x12",  # L - - Disable reporting of SBAS satellites
    "CFG-NMEA-FILT_GAL", b"\x10\x93\x00\x13",  # L - - Disable reporting of Galileo satellites
    "CFG-NMEA-FILT_QZSS", b"\x10\x93\x00\x15",  # L - - Disable reporting of QZSS satellites
    "CFG-NMEA-FILT_GLO", b"\x10\x93\x00\x16",  # L - - Disable reporting of GLONASS satellites
    "CFG-NMEA-FILT_BDS", b"\x10\x93\x00\x17",  # L - - Disable reporting of BeiDou satellites
    "CFG-NMEA-OUT_INVFIX", b"\x10\x93\x00\x21",  # L - - Enable position output for failed or invalid fixes
    "CFG-NMEA-OUT_MSKFIX", b"\x10\x93\x00\x22",  # L - - Enable position output for invalid fixes
    "CFG-NMEA-OUT_INVTIME", b"\x10\x93\x00\x23",  # L - - Enable time output for invalid times
    "CFG-NMEA-OUT_INVDATE", b"\x10\x93\x00\x24",  # L - - Enable date output for invalid dates
    "CFG-NMEA-OUT_ONLYGPS", b"\x10\x93\x00\x25",  # L - - Restrict output to GPS satellites only
    "CFG-NMEA-OUT_FROZENCOG", b"\x10\x93\x00\x26",  # L - - Enable course over ground output even if it is frozen
    "CFG-NMEA-MAINTALKERID", b"\x20\x93\x00\x31",  # E1 - - Main Talker ID. By default the main Talker ID (i.e. the Talker ID used for all messages other than GSV) is determined by the GNSS assignment of the receiver's channels (see CFG-SIGNAL). This field enables the main Talker ID to be overridden. See Table 27 below for a list of possible constants for this item.
    "CFG-NMEA-GSVTALKERID", b"\x20\x93\x00\x32",  # E1 - - Talker ID for GSV NMEA messages. By default the Talker ID for GSV messages is GNSS-specific (as defined by NMEA). This field enables the GSV Talker ID to be overridden. See Table 28 below for a list of possible constants for this item.
    "CFG-NMEA-BDSTALKERID", b"\x30\x93\x00\x33",  # U2 - - BeiDou Talker ID. Sets the two ASCII characters that should be used for the BeiDou Talker ID. If these are set to zero, the default BeiDou Talker ID will be used.
}
CFG_NMEA_PROTVER = {  # Table 24
    V21: 21,  # NMEA protocol version 2.1
    V23: 23,  # NMEA protocol version 2.3
    V40: 40,  # NMEA protocol version 4.0 (not available in all products)
    V41: 41,  # NMEA protocol version 4.10 (not available in all products)
    V411: 42,  # NMEA protocol version 4.11 (not available in all products)
}
CFG_NMEA_MAXSVS = { Table 25
    UNLIM: 0,  # Unlimited
    8SVS: 8,  # 8 SVs
    12SVS: 12,  # 12 SVs
    16SVS: 16,  # 16 SVs
}
CFG_NMEA_SVNUMBERING = {  # Table 26
    STRICT: 0,  # Strict - satellites are not output
    EXTENDED: 1,  # Extended - use proprietary numbering
}
CFG_NMEA_MAINTALKERID = {  # Table 27
    AUTO: 0,  # Main Talker ID is not overridden
    GP: 1,  # Set main Talker ID to 'GP'
    GL: 2,  # Set main Talker ID to 'GL'
    GN: 3,  # Set main Talker ID to 'GN'
    GA: 4,  # Set main Talker ID to 'GA' (not available in all products)
    GB: 5,  # Set main Talker ID to 'GB' (not available in all products)
    GQ: 7,  # Set main Talker ID to 'GQ' (not available in all products)
}
CFG_NMEA_GSVTALKERID = {  # Table 28
    GNSS: 0,  # Use GNSS-specific Talker ID (as defined by NMEA)
    MAIN: 1,  # Use the main Talker ID
}

# CFG-RATE: Navigation and measurement rate configuration
# The configuration items in this group allow the user to alter the rate at which navigation solutions (and the measurements that they depend on) are generated by the receiver. The calculation of the navigation solution will always be aligned to the top of a second zero (first second of the week) of the configured reference time system. The navigation period is an integer multiple of the measurement period.
# https://www.u-blox.com/en/docs/UBX-18010854#page=207&zoom=auto,-70,676
CFG_RATE = {
    "CFG-RATE-MEAS", b"\x30\x21\x00\x01",  # U2 0.001 s Nominal time between GNSS measurements. E.g. 100 ms results in 10 Hz measurement rate, 1000 ms = 1 Hz measurement rate.
    "CFG-RATE-NAV", b"\x30\x21\x00\x02",  # U2 - - Ratio of number of measurements to number of navigation solutions. E.g. 5 means five measurements for every navigation solution. The maximum value is 128.
    "CFG-RATE-TIMEREF", b"\x20\x21\x00\x03",  # E1 - - Time system to which measurements are aligned. See Table 33 below for a list of possible constants for this item.
}
CFG_RATE_TIMEREF = {  # Table 33
    UTC : 0,  # Align measurements to UTC time
    GPS : 1,  # Align measurements to GPS time
    GLO : 2,  # Align measurements to GLONASS time
    BDS : 3,  # Align measurements to BeiDou time
    GAL : 4,  # Align measurements to Galileo time
}

# CFG-TMODE: Time mode configuration
# Configuration for operation of the receiver in Time mode. The position referred to in the configuration items is that of the Antenna Reference Point (ARP).
# https://www.u-blox.com/en/docs/UBX-18010854#page=211&zoom=auto,-70,301
CFG_TMODE = {
    "CFG-TMODE-MODE", b"\x20\x03\x00\x01",  # E1 - - Receiver mode. See Table 44 below for a list of possible constants for this item.
    "CFG-TMODE-POS_TYPE", b"\x20\x03\x00\x02",  # E1 - - Determines whether the ARP position is given in. ECEF or LAT/LON/HEIGHT?. See Table 45 below for a list of possible constants for this item.
    "CFG-TMODE-ECEF_X", b"\x40\x03\x00\x03",  # I4 - cm ECEF X coordinate of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-ECEF_Y", b"\x40\x03\x00\x04",  # I4 - cm ECEF Y coordinate of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-ECEF_Z", b"\x40\x03\x00\x05",  # I4 - cm ECEF Z coordinate of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-ECEF_X_HP", b"\x20\x03\x00\x06",  # I1 0.1 mm High-precision ECEF X coordinate of the ARP. position.. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-ECEF_Y_HP", b"\x20\x03\x00\x07",  # I1 0.1 mm High-precision ECEF Y coordinate of the ARP. position.. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-ECEF_Z_HP", b"\x20\x03\x00\x08",  # I1 0.1 mm High-precision ECEF Z coordinate of the ARP. position.. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=ECEF.
    "CFG-TMODE-LAT", b"\x40\x03\x00\x09",  # I4 1e-7 deg Latitude of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-LON", b"\x40\x03\x00\x0a",  # I4 1e-7 deg Longitude of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-HEIGHT", b"\x40\x03\x00\x0b",  # I4 - cm Height of the ARP position.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-LAT_HP", b"\x20\x03\x00\x0c",  # I1 1e-9 deg High-precision latitude of the ARP position. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-LON_HP", b"\x20\x03\x00\x0d",  # I1 1e-9 deg High-precision longitude of the ARP position.. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-HEIGHT_HP", b"\x20\x03\x00\x0e",  # I1 0.1 mm High-precision height of the ARP position.. Accepted range is -99 to +99.. This will only be used if CFG-TMODE-MODE=FIXED and CFG-TMODE-POS_TYPE=LLH.
    "CFG-TMODE-FIXED_POS_ACC", b"\x40\x03\x00\x0f",  # U4 0.1 mm Fixed position 3D accuracy. CFG-TMODE-SVIN_MIN_DUR", b"\x40\x03\x00\x10",  # U4 - s Survey-in minimum duration. This will only be used if CFG-TMODE-MODE=SURVEY_IN.
    "CFG-TMODE-SVIN_ACC_LIMIT", b"\x40\x03\x00\x11",  # U4 0.1 mm Survey-in position accuracy limit. This will only be used if CFG-TMODE-MODE=SURVEY_IN.
}
CFG_TMODE_MODE = { # Table 44
    DISABLED: 0,  # Disabled
    SURVEY_IN: 1,  # Survey in
    FIXED: 2,  # Fixed mode (true ARP position information required)
}
CFG_TMODE_POS_TYPE = {  # Table 45
    ECEF: 0,  # Position is ECEF
    LLH: 1,  # Position is Lat/Lon/Height
}

# CFG-UART1: Configuration of the UART1 interface
# Settings needed to configure the UART1 communication interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=215&zoom=auto,-70,678
CFG_UART1 = {
    "CFG-UART1-BAUDRATE", b"\x40\x52\x00\x01"  # U4 - - The baud rate that should be configured on the UART1 
    "CFG-UART1-STOPBITS", b"\x20\x52\x00\x02"  # E1 - - Number of stopbits that should be used on UART1 See  Table 53  below for a list of possible constants for this item. 
    "CFG-UART1-DATABITS", b"\x20\x52\x00\x03"  # E1 - - Number of databits that should be used on UART1 See  Table 54  below for a list of possible constants for this item. 
    "CFG-UART1-PARITY", b"\x20\x52\x00\x04"  # E1 - - Parity mode that should be used on UART1 See  Table 55  below for a list of possible constants for this item. 
    "CFG-UART1-ENABLED", b"\x10\x52\x00\x05"  # L - - Flag to indicate if the UART1 should be enabled
}
CFG_UART1_STOPBITS = {  # Table 53, Table 59
    HALF: 0,  # 0.5 stopbits
    ONE: 1,  # 1.0 stopbits
    ONEHALF: 2,  # 1.5 stopbits
    TWO: 3,  # 2.0 stopbits
}
CFG_UART1_DATABITS = {  # Table 54, Table 60
    EIGHT: 0,  # 8 databits
    SEVEN: 1,  # 7 databits
}
CFG_UART1_PARITY = {  # Table 55, Table 61
    NONE: 0  # No parity bit
    ODD: 1,  # Add an odd parity bit
    EVEN: 2,  # Add an even parity bit
}

# CFG-UART1INPROT: Input protocol configuration of the UART1 interface
# Input protocol enable flags of the UART1 interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=215&zoom=auto,-70,211
CFG_UART1INPROT = {
    "CFG-UART1INPROT-UBX", b"\x10\x73\x00\x01",  # L - - Flag to indicate if UBX should be an input protocol on UART1
    "CFG-UART1INPROT-NMEA", b"\x10\x73\x00\x02",  # L - - Flag to indicate if NMEA should be an input protocol on UART1
    "CFG-UART1INPROT-RTCM3X", b"\x10\x73\x00\x04"  # L - - Flag to indicate if RTCM3X should be an input protocol on UART1
}

# CFG-UART1OUTPROT: Output protocol configuration of the UART1 interface
# Output protocol enable flags of the UART1 interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=216&zoom=auto,-70,685
CFG_UART1OUTPROT = {
    "CFG-UART1OUTPROT-UBX", b"\x10\x74\x00\x01",  # L - - Flag to indicate if UBX should be an output protocol on UART1
    "CFG-UART1OUTPROT-NMEA", b"\x10\x74\x00\x02",  # L - - Flag to indicate if NMEA should be an output protocol on UART1
    "CFG-UART1OUTPROT-RTCM3X", b"\x10\x74\x00\x04"  # L - - Flag to indicate if RTCM3X should be an output protocol on UART1
}

# CFG-UART2: Configuration of the UART2 interface
# Settings needed to configure the UART2 communication interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=216&zoom=auto,-70,524
CFG_UART2 = {
    "CFG-UART2-BAUDRATE", b"\x40\x53\x00\x01",  # U4 - - The baud rate that should be configured on the UART2
    "CFG-UART2-STOPBITS", b"\x20\x53\x00\x02",  # E1 - - Number of stopbits that should be used on UART2 See  Table 59  below for a list of possible constants for this item. 
    "CFG-UART2-DATABITS", b"\x20\x53\x00\x03",  # E1 - - Number of databits that should be used on UART2 See  Table 60  below for a list of possible constants for this item. 
    "CFG-UART2-PARITY", b"\x20\x53\x00\x04",  # E1 - - Parity mode that should be used on UART2 See  Table 61  below for a list of possible constants for this item. 
    "CFG-UART2-ENABLED", b"\x10\x53\x00\x05",  # L - - Flag to indicate if the UART2 should be enabled
    "CFG-UART2-REMAP", b"\x10\x53\x00\x06"  # L - - UART2 Remapping
}
# contants tables are defined at CFG_UART1

# CFG-UART2INPROT: Input protocol configuration of the UART2 interface
# Input protocol enable flags of the UART2 interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=217&zoom=auto,-70,678
CFG_UART2INPROT = {
    "CFG-UART2INPROT-UBX", b"\x10\x75\x00\x01",  # L - - Flag to indicate if UBX should be an input protocol on UART2
    "CFG-UART2INPROT-NMEA", b"\x10\x75\x00\x02",  # L - - Flag to indicate if NMEA should be an input protocol on UART2
    "CFG-UART2INPROT-RTCM3X", b"\x10\x75\x00\x04"  # L - - Flag to indicate if RTCM3X should be an input protocol on UART2
}

# CFG-UART2OUTPROT: Output protocol configuration of the UART2 interface
# Output protocol enable flags of the UART2 interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=217&zoom=auto,-70,532
CFG_UART2OUTPROT = {
    "CFG-UART2OUTPROT-UBX", b"\x10\x76\x00\x01",  # L - - Flag to indicate if UBX should be an output protocol on UART2
    "CFG-UART2OUTPROT-NMEA", b"\x10\x76\x00\x02",  # L - - Flag to indicate if NMEA should be an output protocol on UART2
    "CFG-UART2OUTPROT-RTCM3X", b"\x10\x76\x00\x04"  # L - - Flag to indicate if RTCM3X should be an output protocol on UART2
}

# CFG-USB: Configuration of the USB interface
# Settings needed to configure the USB communication interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=217&zoom=auto,-70,371
CFG_USB = {
    "CFG-USB-ENABLED", b"\x10\x65\x00\x01",  # L - - Flag to indicate if the USB interface should be enabled 
    "CFG-USB-SELFPOW", b"\x10\x65\x00\x02",  # L - - Self-powered device 
    "CFG-USB-VENDOR_ID", b"\x30\x65\x00\x0a",  # U2 - - Vendor ID 
    "CFG-USB-PRODUCT_ID", b"\x30\x65\x00\x0b",  # U2 - - Vendor ID 
    "CFG-USB-POWER", b"\x30\x65\x00\x0c",  # U2 - mA Power consumption 
    "CFG-USB-VENDOR_STR0", b"\x50\x65\x00\x0d",  # X8 - - Vendor string characters 0-7 
    "CFG-USB-VENDOR_STR1", b"\x50\x65\x00\x0e",  # X8 - - Vendor string characters 8-15 
    "CFG-USB-VENDOR_STR2", b"\x50\x65\x00\x0f",  # X8 - - Vendor string characters 16-23 
    "CFG-USB-VENDOR_STR3", b"\x50\x65\x00\x10",  # X8 - - Vendor string characters 24-31 
    "CFG-USB-PRODUCT_STR0", b"\x50\x65\x00\x11",  # X8 - - Product string characters 0-7 
    "CFG-USB-PRODUCT_STR1", b"\x50\x65\x00\x12",  # X8 - - Product string characters 8-15 
    "CFG-USB-PRODUCT_STR2", b"\x50\x65\x00\x13",  # X8 - - Product string characters 16-23 
    "CFG-USB-PRODUCT_STR3", b"\x50\x65\x00\x14",  # X8 - - Product string characters 24-31 
    "CFG-USB-SERIAL_NO_STR0", b"\x50\x65\x00\x15",  # X8 - - Serial number string characters 0-7 
    "CFG-USB-SERIAL_NO_STR1", b"\x50\x65\x00\x16",  # X8 - - Serial number string characters 8-15 
    "CFG-USB-SERIAL_NO_STR2", b"\x50\x65\x00\x17",  # X8 - - Serial number string characters 16-23 
    "CFG-USB-SERIAL_NO_STR3", b"\x50\x65\x00\x18",  # X8 - - Serial number string characters 24-31
}

# CFG-USBINPROT: Input protocol configuration of the USB interface
# Input protocol enable flags of the USB interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=218&zoom=auto,-70,662
CFG_USBINPROT = {
    "CFG-USBINPROT-UBX", b"\x10\x77\x00\x01",  # L - - Flag to indicate if UBX should be an input protocol on USB 
    "CFG-USBINPROT-NMEA", b"\x10\x77\x00\x02",  # L - - Flag to indicate if NMEA should be an input protocol on USB 
    "CFG-USBINPROT-RTCM3X", b"\x10\x77\x00\x04",  # L - - Flag to indicate if RTCM3X should be an input protocol on USB
}

# CFG-USBOUTPROT: Output protocol configuration of the USB interface
# Output protocol enable flags of the USB interface.
# https://www.u-blox.com/en/docs/UBX-18010854#page=218&zoom=auto,-70,517
CFG_USBOUTPROT = {
    "CFG-USBOUTPROT-UBX", b"\x10\x78\x00\x01",  # L - - Flag to indicate if UBX should be an output protocol on USB
    "CFG-USBOUTPROT-NMEA", b"\x10\x78\x00\x02",  # L - - Flag to indicate if NMEA should be an output protocol on USB
    "CFG-USBOUTPROT-RTCM3X", b"\x10\x78\x00\x04",  # L - - Flag to indicate if RTCM3X should be an output protocol on USB
}