"""
UBXMessage class

@author: mgesteiro
"""
from ublox9.ubxdefs import *
from ublox9.ubxpayloads import UBX_PAYLOADS


class UBXMessage:
    """Class to fiddle with UBX messages"""

    SIGNATURE = b"\xb5\x62"

    def __init__(self, class_id: bytes, payload: bytes =b""):
        """
        Constructor
        Creates an UBXMessage object with the provided data.
        Reference at https://www.u-blox.com/en/docs/UBX-18010854#page=44
        :param class_id: message Class and ID
        :param payload: content of the message
        """
        self._class_id = class_id
        self._payload = payload
        self._plen = len(payload).to_bytes(2, byteorder="little", signed=False)

    def message_bytes(self) -> bytes:
        """
        Returns the binary representation of the message, ready to be sent.
        :return: the message bytes
        """
        base = self._class_id + self._plen + self._payload
        return self.SIGNATURE + base + self.calc_checksum(base)

    @staticmethod
    def calc_checksum(content: bytes) -> bytes:
        """
        Calculates and returns the checksum bytes for the content.
        :param content: bytes:
        :return: the checksum
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
    def get_classid_def(class_id: bytes) -> (str, dict):
        """
        Retrieves the definition (name/key and container) corresponding to
        the provided classid.
        :param class_id: the ubx message bytes of the Class and ID
        returns: (name,dict), ("", None) if not found
        """
        for mclass in UBX_CLASSID_SET:
            for name in mclass:
                if mclass[name] == class_id: return name, mclass
        return "", None

    @staticmethod
    def parse_bytes(content: bytes) -> dict:
        """
        Parse the UBX message in content. Only simple validations.
        :param content: the complete message bytes
        :return: the parsed message in a dict, empty if fails/invalid
        """
        result = {}
        if type(content) != bytes: return result
        if content[0:2] != UBXMessage.SIGNATURE: return result
        mdef = UBXMessage.get_classid_def(content[2:4])
        if mdef[0] == "": return result  # unrecognized message definition
        index = 6  # start from the payload initial byte
        for attribute, size in UBX_PAYLOADS[mdef[0]].items():
            if type(size) == int:
                # simple type
                result[attribute] = content[index: index + size]
                index += size
            elif type(size) == tuple:
                # groups
                if size[0] == "N":
                    # fixed width fields of size[1] size
                    for i in range(int((len(content)-2-index)/size[1])):
                        result[attribute+f"{i}"] = content[index: index + size[1]]
                        index += size[1]
                elif size[0] == "R":
                    # rest of the payload
                    result[attribute] = content[index: len(content)-2]
        return result
