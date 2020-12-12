"""
UBXMessage class

@author: mgesteiro
"""
from ublox9.ubxdefs import *
from ublox9.ubxpayloads import UBX_PAYLOADS

class UBXMessage:
    """Class to fiddle with UBX messages"""

    SIGNATURE = b"\xb5\x62"

    def __init__(self, Class_ID, payload=b""):
        """
        Constructor
        Creates an UBXMessage object with the provided data
        :param Class_ID: bytes: message Class and ID
        :param payload: bytes: content of the message
        reference at https://www.u-blox.com/en/docs/UBX-18010854#page=44
        """
        self._class_id = Class_ID
        self._payload = payload
        self._plen = len(payload).to_bytes(2, byteorder="little", signed=False)

    def message_bytes(self) -> bytes:
        """
        Returns the binary (bytes) representation of the message, ready to
        be sent through any stream.
        :return message: bytes:
        """
        base =  self._class_id + self._plen + self._payload
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

    @staticmethod
    def get_classid_def(classid: bytes) -> (str, dict):
        """
        Retrieves the definition (name/key and container) corresponding to
        the provided classid

        params: classid: the ubx message bytes of the Class and ID
        returns: (name,dict), ("", None) if not found
        """
        for mclass in UBX_CLASSID_SET:
            for name in mclass:
                if mclass[name] == classid: return (name, mclass)
        return ("", None)

    @staticmethod
    def parse_bytes(content: bytes) -> bytes:
        if type(content) != bytes: return None
        if content[0:2] != UBXMessage.SIGNATURE: return None
        mdef = UBXMessage.get_classid_def(content[2:4])
        if mdef[0] == "": return None
        result = {}
        index = 6  # start from the payload initial byte
        for attribute, size in UBX_PAYLOADS[mdef[0]].items():
            result[attribute] = content[index : index + size]
            index += size
        return result
