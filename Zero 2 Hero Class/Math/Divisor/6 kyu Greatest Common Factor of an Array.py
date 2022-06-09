'''
https://www.codewars.com/kata/5849169a6512c5964000016e/train/python

prove x = m*d, y = n*d
y/x = n/m
y = x * (y//x) + y%x
y = m*d * (n*d//m*d) + y%x
y = m*d * n//m + y%x

d = y - y%x

(n*d - m*d + m*d)/m*d = (n - m)/m + 1
so that
(n - m)/m

'''

import math
def gcd(x,y):
    a,b = min(x,y),max(x,y)
    while a != 0:
        a,b = b%a,a
    return b
print(gcd(27,12))

def greatest_common_factor(seq):
    res = gcd(seq[0], seq[1])
    for i in seq[2:]:
        res = gcd(res,i)
    return res
seq = [46, 14, 20, 88]
print(greatest_common_factor(seq))


#1st
from functools import reduce
from math import gcd

def greatest_common_factor(seq):
    return reduce(gcd, seq)