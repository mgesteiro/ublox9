"""
UBXMessage class

@author: mgesteiro
"""
from ublox9.ubxdefs import *
from ublox9.ubxpayloads import UBX_PAYLOADS, UBX_GENERIC


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
    def get_classid_name(class_id: bytes) -> str:
        """
        Retrieves the name corresponding to the provided classid.
        :param class_id: the ubx message bytes of the Class and ID
        :return: (name,dict), ("", None) if not found
        """
        for group in UBX_CLASSIDS.values():
            for name, value in group.items():
                if value == class_id: return name
        return ""

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
        name = UBXMessage.get_classid_name(content[2:4])
        if not name: return result  # unrecognized message definition
        result['message'] = name.encode()  # bytes format as the other fields
        index = 6  # start from the payload initial byte
        try:
            ubx_payload = UBX_PAYLOADS[name]
        except KeyError:
            ubx_payload = UBX_PAYLOADS[UBX_GENERIC]
        for attribute, specs in ubx_payload.items():
            if type(specs) == int:
                # simple type
                size = specs
                result[attribute] = content[index: index + size]
                index += size
            elif type(specs) == tuple:
                # repeating groups

                if specs[0] == "PN":
                    # predetermined number of groups
                    numfield, subattribes = specs[1]
                    numofg = int.from_bytes(result[numfield], byteorder="little", signed=False)
                    for i in range(numofg):
                        group = {}
                        for subattrib, size in subattribes.items():
                            group[subattrib] = content[index: index + size]
                            index += size
                        result[attribute+f"{i}"] = group

                elif specs[0] == "FL":
                    # fixed length groups, as many as possible fit in the payload
                    size = specs[1]
                    for i in range(int((len(content)-2-index)/size)):
                        result[attribute+f"{i}"] = content[index: index + size]
                        index += size

                elif specs[0] == "RP":
                    # rest of the payload
                    result[attribute] = content[index: len(content)-2]

        return result
