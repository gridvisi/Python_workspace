'''
https://www.codewars.com/kata/5d6f49d85e45290016bf4718/train/python

Assume that:

x is an unsigned, 32-bit integer;
the bits are zero-indexed (the least significant bit is position 0)
Examples
  2  -->  1 (true) because at least one odd bit is 1 (2 = 0b10)
  5  -->  0 (false) because none of the odd bits are 1 (5 = 0b101)
170  -->  1 (true) because all of the odd bits are 1 (170 = 0b10101010)
'''

def any_odd(x):
    print(str(bin(x)))
    return int(any([b =='1' for i,b in enumerate(str(bin(x))[::-1]) if i%2]))

x = 170
#x = 2
print(any_odd(x))

#1st solution
MATCH = int('10'*16,2)
def any_odd(x): return bool(MATCH & x)


def any_odd(n):
    return 1 if '1' in bin(n)[2:][-2::-2] else 0

def any_odd(x):
    return x & 0xaaaaaaaa != 0

def any_odd(x):
    return '1' in f'0{x:b}'[-2::-2]

def any_odd(x):
    return '1' in list(bin(x)[-2::-2])