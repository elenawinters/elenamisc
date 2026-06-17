import struct

# from .. import testutils
# PatternTest(sample).sieve_of_winters

# arg1 = 25DAB1B9
# arg2 = 25
# arg3 = 2

# numeric_packet = 446329225

# EAX = 0x19
# EDX = 0x2

print(bin(0x708))


# packet = 0x25DAB1B9  # 1800 world id (0x708)
packet = 0x25DAB1B9
length = 0x19
arg3 = 0x2

bpacket = 0x53.to_bytes(32, 'big')
# bpacket += packet.to_bytes(32, 'big')

print(bpacket)

load_zone_struct = struct.unpack('HHII?cfffI', bpacket)
print(load_zone_struct)





# target = 0x708
# print(bin(packet))
# print(packet)
# print(len(bin(packet)))

# test = list(map(int, str(packet)))
# print(test)

# bytes = []
# for x in test:
#     # val = bin(x)[2:]
#     val = bin(x)[2:].zfill(4)
#     # bytes.insert(0, val)
#     bytes.append(val)


# print(bytes)
# m = ''.join(bytes)
# print(m)
# print(len(m))


