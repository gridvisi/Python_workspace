'''
https://www.codewars.com/kata/5913152be0b295cf99000001/train/python
'''
import math
def divisions(n, divisor):
    return int(math.log(n,divisor))

n, divisor = 9999, 3
print(divisions(n, divisor))
from math import log, floor
def divisions(m, n):
    return floor(log(m, n))

#1st
def divisions(n, divisor):
    c=0
    while divisor<=n:
        n/=divisor
        c+=1
    return c

def divisions(n, divisor):
    l = 0
    while n >= divisor > 1:
        n, m = divmod(n, divisor)
        l += 1
    return l

def divisions(n, divisor):
    summa = 0
    while n >= divisor:
        n = n // divisor
        summa += 1
    return summa   