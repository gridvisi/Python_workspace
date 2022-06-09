'''
https://www.codewars.com/kata/57a5c31ce298a7e6b7000334/train/python

test.assert_equals(bin_to_decimal("0"), 0)
test.assert_equals(bin_to_decimal("1"), 1)
test.assert_equals(bin_to_decimal("10"), 2)
test.assert_equals(bin_to_decimal("11"), 3)
test.assert_equals(bin_to_decimal("101010"), 42)
test.assert_equals(bin_to_decimal("1001001"), 73)
'''


def bin_to_decimal(inp):
    return int(inp, 2)

def bin_to_decimal(inp):
    return sum([int(e) * 2**i for i,e in enumerate(inp[::-1])])

inp = '10001101100100011010110'
print(type(bin(3)),bin(3) + "end")

#print(int(bin(0) +inp))
#print(int('0b'+'01'))
#print(int(''.join(['0b','01'])))

#print(bin_to_decimal(inp))

def bin_to_decimal(inp):
    return int(inp)
inp = '10001101100100011010110'

print(bin_to_decimal(inp))
'''
Test Passed
Test Passed

1001001 should equal 73
Random Tests
10001101100100011010110 should equal 4638934
10001111111011101110 should equal 589550
10010000001101011001000 should equal 4725448
1101001011111111010011 should equal 3456979
'''