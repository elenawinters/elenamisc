from functools import reduce
import struct

# this was me trying to parse incomplete data. honestly, just ignore



# test_data = [258, 9986, 16642, 108802, 68610, 22018, 40962, 19714]
test_data = [701698]
# test = 258
# victim = 701698


for x in test_data:
    # btest = x.to_bytes(68, 'little')
    btest = bin(x)[2:]
    print(btest)
    # print(type(btest))
    ctest = bytes(int(btest[i:i+8], 2) for i in range(0, len(btest), 8))
    # ctest = parse(btest)
    print(ctest)

    
    bstrut = struct.unpack('qqqqqfqfff', ctest)
    # print(bstrut)
