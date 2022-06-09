'''
https://www.codewars.com/kata/57c18a16c82ce75f4b000020/train/python
Preconditions
2 <= m <= 36
2 <= n <= 36
xm is always a valid non-negative m-based number.
d is always a valid digit for base n

base = 2: 0, 1
base = 3: 0, 1, 2
...
base = 10: 0, 1, ... 8, 9
base = 11: 0 ... , 8, 9, a
base = 12: 0 ... , 8, 9, a, b
...
base = 16: 0 ... , 8, 9, a, ..., e, f
base = 36: 0 ..., 8, 9, a, ..., y, z

# 十进制 to 八进制: oct()
# 十进制 to 十六进制: hex()
'''

#7th solution by ericlee
import string

def convert(n,x,ans):   #n为待转换的十进制数，x为进制，取值为2-32
    basefull = string.digits + string.ascii_lowercase
    if (n>=0) and (n<x):
        ans = basefull[n]+ans
        return ans
    else:
        ans = basefull[n % x] + ans
        return convert(n//x,x,ans)
n,x = 100,17
print(convert(n,x,ans=''))
print('hex:',hex(n))


def count_digit(number, digit, base, from_base):
    #basefull = string.digits + string.ascii_lowercase
    baseTen = int(number,from_base)
    #remainder = basefull[:base][baseTen%base]
    ans = ''
    return convert(baseTen,base,ans).count(digit)
number, digit, base, from_base = "1100101110101", "d", 15, 2
print(count_digit(number, digit, base, from_base))


#1st solution
from numpy import base_repr
def count_digit(number, digit, base=10, from_base=10):
    return base_repr(int(number, from_base), base).lower().count(digit)

'''
#2nd solution
from gmpy2 import mpz
def count_digit(number, digit, base=10, from_base=10):
    return mpz(number, base=from_base).digits(base).count(digit)
'''

import string
def count_digit(number, digit, base=10, from_base=10):
    digs = string.digits + string.ascii_lowercase
    num = int(number, from_base)
    out = ''

    while num:
        out = digs[num % base] + out
        num = num // base
    if not out:
        out = '0'
    return out.count(digit)