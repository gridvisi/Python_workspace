'''
https://www.codewars.com/kata/5932c94f6aa4d1d786000028/train/python

In mathematics, an nth root of a number x, where n is usually assumed to be a positive
integer, is a number r which, when raised to the power n, yields x:

r^n=x,
Given number n, such that n > 1, find if its 2nd root, 4th root and 8th root are all
integers (fractional part is 0), return true if it exists, false if not.

# 2nd root of 256 is 16
# 4th root of 256 is 4
# 8th root of 256 is 2
perfect_roots(256) # returns True
'''


import math
def perfect_roots(n):
    # your code here
    return all([math.pow(n,1/i)==int(math.pow(n,1/i)) for i in [2,4,8]])

#1st
def perfect_roots(n):
    return (n ** 0.125) % 1 == 0