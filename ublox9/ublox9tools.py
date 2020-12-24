"""
ublox9 tools

Based on the ZED-F9P u-blox GNSS receiver documentation:
https://www.u-blox.com/en/docs/UBX-18010854

Created on 9 Dec 2020

@author: mgesteiro
"""
import socket
import time
from ublox9 import Ublox9Stream, UBXMessage, UBX_CFG, UBX_ACK
from ublox9.ublox9defs import MSG_NMEA, MSG_UBX, MSG_RTCM
from serial import Serial, SerialException, SerialTimeoutException


class StreamToTCP:
    """docstring for StreamToTCP"""

    def __init__(self, address, timeout=1):
        # super(StreamToSocket, self).__init__()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.settimeout(timeout)
        self._socket.connect(address)

    def read(self, amount=1) -> bytes:
        return self._socket.recv(amount)

    def write(self, data: bytes):
        return self._socket.send(data)

    def readline(self, amount=0) -> bytes:
        return self._socket.recv(amount)

    def close(self):
        self._socket.close()


def open_serial(serialport, baudrates, timeout=1) -> Ublox9Stream:
    """
    try to open a serial port with different baudrates and check that there is
    a valid communication with the ublox module (sending UBX-SEC-UNIQID message)
    if a valid connection is achieved, the id property of the resulting object
    is populated with the u-blox module UNIQID.
    :param serialport: the device port to open
    :param baudrates: a list of baudrates to try
    :param timeout: timeout in seconds
    :return: an Ublox9Stream if successfull, None otherwise
    """
    unique = b"\xB5\x62\x27\x03\x00\x00\x2A\xA5"
    for baudrate in baudrates:
        try:
            sport = Serial(serialport, baudrate, timeout=timeout)
            ub9stream = Ublox9Stream(sport)
            ub9stream.write_message(unique)
            answ = ub9stream.read_ubxmessage(discardlimit=12, maxsearchbytes=90)
            if answ:
                ub9stream.id = answ[10:15]
                return ub9stream
            else:
                sport.close()
                time.sleep(0.250)
        except (SerialException, SerialTimeoutException, ValueError):
            pass


UBX_ACK_VALSET = UBXMessage(
    UBX_ACK["UBX-ACK-ACK"],
    UBX_CFG["UBX-CFG-VALSET"]
).message_bytes()


def gen_valset_message(layers: bytes, cfg_data: bytes) -> bytes:
    """
    creates an UBX-VALSET message with the specified values/keys of cfgData
    to be written to the specified layers
    :param layers: which layers should be written the config to
    :param cfg_data: the bundle of keys and values
    :return: the VALSET message ready to be sent
    """
    version = b"\x00"
    reserved0 = b"\x00\x00"
    payload = version + layers + reserved0 + cfg_data
    return UBXMessage(UBX_CFG["UBX-CFG-VALSET"], payload).message_bytes()


def get_message_type(message: bytes) -> int:
    """
    Returns the type of the message
    :param message: the message to classify
    :return: the message type
    """
    firstbye = message[0:1]
    if firstbye == b"$": return MSG_NMEA
    if firstbye == b"\xb5": return MSG_UBX
    if firstbye == b"\xf5": return MSG_RTCM
