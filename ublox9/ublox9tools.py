"""
ublox9 tools

Based on the ZED-F9P u-blox GNSS receiver documentation:
https://www.u-blox.com/en/docs/UBX-18010854

Created on 9 Dec 2020

@author: mgesteiro
"""
import socket
import time
from ublox9 import Ublox9Stream, UBXMessage
from ublox9.ubxdefs import UBX_CFG
from serial import Serial, SerialException, SerialTimeoutException


class StreamToTCP:
    """docstring for StreamToSocket"""

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
    try to open serialport with different baudrates and check that there is
    valid communication with the ublox module using the UBX-SEC-UNIQID message.

    if a valid connection is achieved, the id property of the resulting object
    is populated with the u-blox module UNIQID.

    returns: an Ublox9Stream if successfull, None otherwise
    """
    unique = b"\xB5\x62\x27\x03\x00\x00\x2A\xA5"
    for baudrate in baudrates:
        try:
            sport = Serial(serialport, baudrate, timeout=timeout)
            ub9stream = Ublox9Stream(sport)
            ub9stream.write_message(unique)
            answ = ub9stream.read_ubxmessage(discardlimit=12, maxsearchbytes=90)
            if answ[1]:
                ub9stream.id = answ[1][10:15]
                return ub9stream
            else:
                sport.close()
                time.sleep(0.250)
        except (SerialException, SerialTimeoutException, ValueError):
            pass
    return None


def gen_valset_message(layers: bytes, cfgData: bytes) -> bytes:
    """
    creates an UBX-VALSET message with the specified values/keys of cfgData
    to be written to the specified layers

    param: layers: which layers should be written the config to
    param: cfgData: the bundle of keys and values
    returns: the VALSET message ready to be sent
    """
    VERSION = b"\x00"
    RESERVED0 = b"\x00\x00"
    payload = VERSION + layers + RESERVED0 + cfgData
    return UBXMessage(UBX_CFG["UBX-CFG-VALSET"], payload).message_bytes()
