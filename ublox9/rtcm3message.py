"""
RTCM3 classes

@author: mgesteiro
"""
import bitstruct


class RTCM3Message:
    """
    Class to manage RTCM3 messages. Basic support only.
    """

    SIGNATURE = b"\xd3"

    def __init__(self, payload: bytes = b""):
        """
        Constructor
        Creates a RTCM3Message object with the provided data.
        Reference at https://www.u-blox.com/en/docs/UBX-18010854#page=161

        :param payload: content of the message
        """
        self._payload = payload
        if len(payload) > 1024: raise RTCM3Exception("Payload size too big (> 1024)")
        self._plen = len(payload).to_bytes(2, byteorder="big", signed=False)

    def message_bytes(self) -> bytes:
        """
        Returns the binary representation of the message.

        :return: the message bytes
        """
        base = self._plen + self._payload
        return self.SIGNATURE + base + self.calc_checksum(base)

    @staticmethod
    def calc_checksum(content: bytes):
        """
        Calculates and returns the checksum bytes for the content.

        :param content: bytes:
        :return: the checksum
        """
        crc = 0x0
        for octet in content:
            crc ^= (octet << 16)
            for i in range(8):
                crc <<= 1
                if crc & 0x1000000: crc ^= 0x1864cfb
        return (crc & 0xffffff).to_bytes(3, byteorder="big", signed=False)

    @staticmethod
    def parse_bytes(content: bytes) -> dict:
        """
        Parse the UBX message in content. Only simple validations.

        :param content: the complete message bytes
        :return: the parsed message in a dict, empty if fails/invalid
        """
        result = {}
        if type(content) != bytes: return result
        if content[0:1] != RTCM3Message.SIGNATURE: return result
        length = int.from_bytes(content[1:3], byteorder="big", signed=False)
        result['length'] = length
        result['type'], = bitstruct.unpack('u12', content[3:5])
        result['payload'] = content[3: 3+length]
        result['crc'] = content[3+length: 3+length+3]
        if RTCM3Message.calc_checksum(content[0:length+3]) != result['crc']:
            return {}  # raise RTCM3Exception("Invalid CRC")
        return result


class RTCM3Exception(Exception):
    """
    Exception raised for errors in the RTCM3 messages handling.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
