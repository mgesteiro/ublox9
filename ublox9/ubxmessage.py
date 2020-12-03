"""
UBXMessage class

@author: mgesteiro
"""


class UBXMessage:
    """Class to fiddle with UBX messages"""

    SIGNATURE = b"\xb5\x62"

    def __init__(self, Class, ID, payload=b""):
        """
        Constructor
        Creates an UBXMessage object with the provided data
        :param Class: bytes: message Class
        :param ID: bytes: message ID
        :param payload: bytes: content of the message
        reference at https://www.u-blox.com/en/docs/UBX-18010854#page=44
        """
        # super(UBXMessage, self).__init__()
        self._class = Class
        self._id = ID
        self._payload = payload
        self._plen = len(payload).to_bytes(2, byteorder="little", signed=False)

    def message_bytes(self) -> bytes:
        """
        Returns the binary (bytes) representation of the message, ready to
        be sent through any stream.
        :return message: bytes:
        """
        base =  self._class + self._id + self._plen + self._payload
        return self.SIGNATURE + base + self.calc_checksum(base)

    @staticmethod
    def calc_checksum(content: bytes) -> bytes:
        """
        Calculates and returns the checksum bytes for the content
        :param content: bytes:
        :return checksum: bytes:
        """
        check_a = 0
        check_b = 0

        for char in content:
            check_a += char
            check_a &= 0xFF
            check_b += check_a
            check_b &= 0xFF

        return bytes((check_a, check_b))
