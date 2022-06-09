'''
https://www.codewars.com/kata/5d6f49d85e45290016bf4718/train/python

Return true when any odd bit of x equals 1; false otherwise.

Assume that:

x is an unsigned, 32-bit integer;
the bits are zero-indexed (the least significant bit is position 0)
Examples
  2  -->  1 (true) because at least one odd bit is 1 (2 = 0b10)
  5  -->  0 (false) because none of the odd bits are 1 (5 = 0b101)
170  -->  1 (true) because all of the odd bits are 1 (170 = 0b10101010)
'''

def any_odd(x):
    # Write code here...
    return any([int(e) == 1 for i,e in enumerate(bin(x)[2:][::-1]) if i%2 == 1])

#1st
MATCH = int('10'*16,2)
print(MATCH)
def any_odd(x): return bool(MATCH & x)

#2nd
def any_odd(n):
    return 1 if '1' in bin(n)[2:][-2::-2] else 0

#3rd
def any_odd(x):
    return x & 0xaaaaaaaa != 0

#4th
def any_odd(x):
    return int("1" in f"{x:032b}"[::2])


