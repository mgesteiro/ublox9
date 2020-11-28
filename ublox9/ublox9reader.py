"""
ublox9Reader class.

Reads and handles data from a u-blox gen 9 module (e.g. ZED-F9P).
Deals with any stream that supports a read(n) -> bytes method.

Created on 27 Nov 2020

@author: mgesteiro
"""

import ublox9

class ublox9Reader:
    """
    ublox9Reader class.
    """

    def __init__(self, stream):
        """
        Constructor.
        :params stream: stream:
        """
        self._stream = stream

    def __iter__(self):
        """Iterator."""
        return self

    def __next__(self) -> (int, bytes):
        """Returns next item in iteration."""
        (type, message) = self.readMessage()
        if type is not None:
            return (type, message)
        raise StopIteration

    def readMessage(self) -> (int, bytes):
        """
        Reads data from the stream and returns the next available message,
        in a tuple with format (type, data).
        If no more items are available (EOF) a (None, None) message is returned.
        This method assumes a couple of pre-conditions:
        1. we start from the beginning (i.e. not in the middle of a message)
        2. every message is complete and atomic (i.e. no interleaving supported)
        Non-expected data is ignored and skipped
        :return (type:, message:)
        """

        s = self._stream

        b = s.read(1) # first byte
        while len(b) > 0:
            if b == b'$':
                # possible NMEA message
                # https://www.u-blox.com/en/docs/UBX-18010854#page=19
                # TT - Talker identifier (2) GP, GL, GA, GB, GQ, GN
                #     https://www.u-blox.com/en/docs/UBX-18010854#page=21&zoom=auto,-74,345
                # SSS - Sentence formatter (3)
                # field,field,field
                # *HH - checksum '*' + 2 hex digits
                # \r\n - ending
                return (ublox9.MSG_NMEA, b + s.readline())
            elif b == b'\xb5':
                # possible UBX message
                # https://www.u-blox.com/en/docs/UBX-18010854#page=44
                # \x62
                # Class(1)
                # ID(1)
                # Length(2)
                # payload (Length)
                # CKACKB(2)
                header = b + s.read(5)
                plen = int.from_bytes(header[-2:], "little", signed=False)
                rest = s.read(plen + 2)
                return (ublox9.MSG_UBX, header + rest )
            elif b == b'\xf5':
                # possible RTCM message
                # https://www.u-blox.com/en/docs/UBX-18010854#page=161
                # ID(1)
                # preamble(1)
                # bitfield0(2) (includes numData)
                # data(numData)
                # crc(3)
                b = s.read(1) # not handled yet
            else:
                # unknown or unexpected byte
                b = s.read(1)  # read next
                # return (ublox9.MSG_RTCM, xxx)

        # if we reach here, no valid message was found
        return (None, None)

    def readUBXMessage(self, discardlimit=10) -> (int, bytes):
        """
        Gets the next UBX message from the stream, discarding all
        previous messages up to a limit of discardlimit.
        Returns an UBX message or (None, None) if the limit is reached
        or there are no more messages available.
        discardlimit is 10 by default, use 0 to remove this limit.
        :params discardlimit: int:
        :return (type:, message:)
        """
        discarded = 0
        m = self.readMessage()
        while m[0] not in {None, ublox9.MSG_UBX}:
            discarded += 1
            if (discardlimit > 0) & (discarded >= discardlimit):
                return (None, None)
            m = self.readMessage()

        return m
