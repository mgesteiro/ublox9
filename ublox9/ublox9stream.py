"""
Ublox9Stream class.

Created on 27 Nov 2020

@author: mgesteiro
"""
from serial import Serial, SerialException, SerialTimeoutException
from ublox9 import UBXMessage, UBX_SEC


class Ublox9Stream:
    """
    Read, write and handle data from a u-blox gen 9 module (e.g. ZED-F9P).
    Supports any base stream that offers read(n)/readline(n)/write() methods.
    """

    def __init__(self, stream):
        """
        Constructor.

        :params stream: stream with read()/readline()/write() methods
        """
        self._stream = stream
        self._id = b''

    def __iter__(self):
        """
        Iterator.
        """
        return self

    def __next__(self) -> bytes:
        """
        Returns next item in iteration.
        """
        mdata = self.read_message()
        if mdata: return mdata
        raise StopIteration

    @property
    def stream(self):
        """
        Getter for the base stream object
        """
        return self._stream

    @property
    def id(self) -> bytes:
        """
        Getter for the stream identifier. The first time it's read, it is
        requested to the module via the get_uniqid() method.
        """
        if not self._id:
            self._id = self.get_uniqid()
        return self._id

    @id.setter
    def id(self, newid: bytes):
        """
        Setter for the stream identifier
        """
        self._id = newid

    def get_uniqid(self) -> bytes:
        """
        Request the UNIQID identifier from the u-blox module

        :return: the UNIQID of the module, empty if it fails
        """
        # try to obtain u-blox uniqid via UBX-SEC-UNIQID message
        muniqid = UBXMessage(UBX_SEC["UBX-SEC-UNIQID"])
        try:
            self.write_message(muniqid.message_bytes())
            bansw = self.read_ubxmessage(discardlimit=30, maxsearchbytes=100)
            answ = UBXMessage.parse_bytes(bansw)
            if answ and (answ['message'] == 'UBX-SEC-UNIQID'):
                return answ['uniqueId']
        except (SerialException, SerialTimeoutException, ValueError):
            return b''

    def read_message(self, maxsearchbytes=128) -> bytes:
        """
        Reads data from the stream and returns the next available message.
        This method assumes that every message is complete and atomic (i.e. no
        interleaving supported).

        :param maxsearchbytes: max number of non-expected bytes to ignore/skip. 128 by default.
        :return: the message read. Empty if EOF or any other problem.
        """
        rembytes = maxsearchbytes  # remaining bytes to read
        read_byte = self._stream.read(1)  # first byte
        while (rembytes > 0) and read_byte:

            if read_byte == b"$":
                # possible NMEA message
                # https://www.u-blox.com/en/docs/UBX-18010854#page=19
                # TT - Talker identifier (2) GP, GL, GA, GB, GQ, GN
                #   https://www.u-blox.com/en/docs/UBX-18010854#page=21&zoom=auto,-74,345
                # SSS - Sentence formatter (3)
                # field,field,field...
                # *HH - checksum '*' + 2 hex digits
                # \r\n - ending
                return read_byte + self._stream.readline(255)

            if read_byte == b"\xb5":
                # possible UBX message
                # https://www.u-blox.com/en/docs/UBX-18010854#page=44
                # \x62
                # Class(1)
                # ID(1)
                # Length(2)
                # payload (Length)
                # CKACKB(2)
                header = read_byte + self._stream.read(5)
                plen = int.from_bytes(header[-2:], byteorder="little", signed=False)
                rest = self._stream.read(plen + 2)
                return header + rest

            if read_byte == b"\xd3":
                # possible RTCM3 message
                # https://www.u-blox.com/en/docs/UBX-18010854#page=161
                # 0 U1 preamble 0xd3
                # 1 X2 bitfield0: numData=10 bits(0..9), res1=6 bits (10..15) all 0
                # 3 U1*numData data
                # 3+numData U1[3] crc
                blen = self._stream.read(2)
                plen = int.from_bytes(blen, byteorder="big", signed=False)
                if plen > 1023:
                    read_byte = blen[1:2]  # try to continue with the last read byte
                    rembytes -= 2  # discard already read bytes
                    continue
                rest = self._stream.read(plen + 3)
                return read_byte + blen + rest

            # unknown or unexpected byte: ignore it
            read_byte = self._stream.read(1)  # read next
            rembytes -= 1

        # if we reach here, no valid message was found
        return b""

    def read_ubxmessage(self, discardlimit=16, maxsearchbytes=128) -> bytes:
        """
        Gets the next UBX message from the stream, discarding all previous non
        UBX messages up to the provided limit. This method invoques internally
        the read_message() method and discards the non-UBX messages.

        :param discardlimit: max non-UBX messages to discard before returning.
            16 by default, use 0 to remove this limit.
        :param maxsearchbytes: as needed by read_message(). 128 by default.
        :return: the following UBX message or empty if any limit is reached or
            there are no more messages available.
        """
        discarded = 0
        message = self.read_message(maxsearchbytes=maxsearchbytes)
        while message and (message[0:1] != b"\xb5"):
            discarded += 1
            if (discardlimit > 0) & (discarded >= discardlimit):
                return b""
            message = self.read_message(maxsearchbytes=maxsearchbytes)
        return message

    def write_message(self, message: bytes):
        """
        Writes the bytes directly to the stream. No checks performed.

        :param message: the bytes to be sent
        """
        self._stream.write(message)

    def close(self):
        """
        Closes the underlying stream. No checks.
        """
        self._stream.close()

    def clear_input(self):
        """
        Empties input buffer by reading all of it
        """
        while self._stream.read(256):
            pass
