from functools import reduce
import struct

# https://stackoverflow.com/a/56243296
class DataView:
    def __init__(self, array, bytes_per_element=1):
        """
        bytes_per_element is the size of each element in bytes.
        By default we are assume the array is one byte per element.
        """
        self.array = array
        self.bytes_per_element = bytes_per_element

    def __get_binary(self, start_index, byte_count, signed=False):
        integers = [self.array[start_index + x] for x in range(byte_count)]
        bytes = [integer.to_bytes(self.bytes_per_element, byteorder='little', signed=signed) for integer in integers]
        return reduce(lambda a, b: a + b, bytes)

    def get_uint_16(self, start_index):
        bytes_to_read = 2
        return int.from_bytes(self.__get_binary(start_index, bytes_to_read), byteorder='little')

    def get_uint_8(self, start_index):
        bytes_to_read = 1
        return int.from_bytes(self.__get_binary(start_index, bytes_to_read), byteorder='little')

    def get_float_32(self, start_index):
        bytes_to_read = 4
        binary = self.__get_binary(start_index, bytes_to_read)
        return struct.unpack('<f', binary)[0] # <f for little endian


def parse(byte_array):
    d = DataView(byte_array)
    return [d.get_uint_8(x) for x in range(10)]


# result = parse([8, 96, 0, 0, 2, 0, 1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# import json
# print(json.dumps(result, indent=2))

# d = DataView([111, 62, 163, 36])
# d.get_float_32(0)