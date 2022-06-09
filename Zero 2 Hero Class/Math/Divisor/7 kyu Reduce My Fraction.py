'''
https://www.codewars.com/kata/576400f2f716ca816d001614/train/python
'''

#8th solve by ericlee
def reduce_fraction(fraction):
    g,d = max(fraction),1
    total_g = g * d
    while total_g % min(fraction) != 0:
        total_g = g * d
        d += 1
    return (total_g//(fraction[1]),total_g//(fraction[0]))

#1st
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def reduce_fraction(fraction):
    num, denom = fraction
    gcd_num_denom = gcd(num, denom)
    return (num // gcd_num_denom, denom // gcd_num_denom)

#2nd
from fractions import Fraction
def reduce_fraction(fraction):
    t = Fraction(*fraction)
    return (t.numerator, t.denominator)

#3rd
from math import gcd

def reduce_fraction(fraction):
    g = gcd(*fraction)
    return tuple(n // g for n in fraction)

#4th
from math import gcd


def reduce_fraction(fraction):
    numerator, denominator = fraction
    greatest_common_divisor = gcd(numerator, denominator)
    return numerator // greatest_common_divisor, denominator // greatest_common_divisor

