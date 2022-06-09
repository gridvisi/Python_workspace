'''
https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python

Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
'''

def grow(arr):
    ans = 1
    for i in arr:
        ans *= i
    return ans

from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)

from functools import reduce
from operator import mul

def grow(arr):
    return reduce(mul, arr, 1)

import math
def grow(arr):
    return math.prod(arr)

def grow(arr):
    return eval('*'.join([str(i) for i in arr]))