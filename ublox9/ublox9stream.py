"""
Ublox9Stream class.

Created on 27 Nov 2020

@author: mgesteiro
"""


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
        Getter for the stream identifier
        """
        return self._id

    @id.setter
    def id(self, newid: bytes):
        """
        Setter for the stream identifier
        """
        self._id = newid

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
                plen = int.from_bytes(header[-2:], "little", signed=False)
                rest = self._stream.read(plen + 2)
                return header + rest

            if read_byte == b"\xf5":
                # possible RTCM message
                # https://www.u-blox.com/en/docs/UBX-18010854#page=161
                # ID(1)
                # preamble(1)
                # bitfield0(2) (includes numData)
                # data(numData)
                # crc(3)
                # return (MSG_RTCM, xxx)
                pass  # not handled yet

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
