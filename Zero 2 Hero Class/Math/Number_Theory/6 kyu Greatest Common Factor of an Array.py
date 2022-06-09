'''
https://www.codewars.com/kata/5849169a6512c5964000016e/train/python
'''

#9th solve by ericlee
def greatest_common_factor(seq):
    i = min(seq)
    while True:
        if all([e%i ==0 for e in seq]):
            return i
        else:
            i -= 1


#1st
from functools import reduce
from math import gcd
def greatest_common_factoseq(seq):
    return reduce(gcd,seq)


#2nd
gcd = lambda a, b: gcd(b, a % b) if b else a

def greatest_common_factor(seq):
    divisor = seq[0]
    for num in seq:
        divisor = gcd(divisor, num)
    return divisor

#3rd
greatest_common_factor = __import__('numpy').gcd.reduce

#4th
def greatest_common_factor(seq):
    return max([i if all(v%i == 0 for v in seq) else 0 for i in range(1, min(seq)+1)])

#5th
from math import gcd
from functools import reduce
greatest_common_factor = lambda N: reduce(gcd, N)


