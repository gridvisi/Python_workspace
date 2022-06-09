'''
https://www.codewars.com/kata/57a4d500e298a7952100035d/train/python

omplete the function which converts hex number (given as a string) to a decimal number.

'''

print(sum(list(range(123456))))
print()
def hex_to_dec(s):
    return int(s,16)

from functools import partial
hex_to_dec = partial(int, base=16)