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
    """
    Simple stream wrapper of a TCP connection
    """

    def __init__(self, address, timeout: float = 1.0):
        """
        Constructor.

        :param address: TCP/IP address to connect to
        :param timeout: timeout in seconds. 1 by default.
        """
        # super(StreamToSocket, self).__init__()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.settimeout(timeout)
        self._socket.connect(address)

    def read(self, amount: int = 1) -> bytes:
        """
        read from the stream the specified amount of bytes

        :param amount: amount of bytes to read. 1 by default.
        :return: bytes read
        """
        return self._socket.recv(amount)

    def write(self, data: bytes):
        """
        write to the stream

        :param data: bytes to write to the stream
        """
        self._socket.send(data)

    def readline(self, amount=0) -> bytes:
        """
        read a line from the stream.

        :param amount: max amount of bytes to read
        :return: bytes read
        """
        return self._socket.recv(amount)

    def close(self):
        """
        close the stream
        """
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
    unique = b"\xb5\x62\x27\x03\x00\x00\x2a\xa5"
    for baudrate in baudrates:
        try:
            sport = Serial(serialport, baudrate, timeout=timeout)
            ub9stream = Ublox9Stream(sport)
            ub9stream.write_message(unique)
            answ = ub9stream.read_ubxmessage(discardlimit=30, maxsearchbytes=100)
            if answ and (answ[:6] == b'\xb5\x62\x27\x03\x09\x00'):
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


def gen_valget_message(layer: bytes, keys: bytes) -> bytes:
    """
    creates an UBX-VALGET message with the specified keys of cfgData
    to be written to the specified layers

    :param layer: which layer should be queried
    :param keys: the bundle of keys to be queried
    :return: the VALGET message ready to be sent
    """
    version = b"\x00"
    position = b"\x00\x00"
    payload = version + layer + position + keys
    return UBXMessage(UBX_CFG["UBX-CFG-VALGET"], payload).message_bytes()


def get_message_type(message: bytes) -> int:
    """
    Returns the type of the message.

    :param message: the message to classify
    :return: the message type
    """
    firstbye = message[0:1]
    if firstbye == b"$": return MSG_NMEA
    if firstbye == b"\xb5": return MSG_UBX
    if firstbye == b"\xf5": return MSG_RTCM
