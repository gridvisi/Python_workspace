'''
https://www.codewars.com/kata/5dae2599a8f7d90025d2f15f/train/python

Positive integers have so many gorgeous features. Some of them could be expressed
as a sum of two or more consecutive positive numbers.

Consider an Example :
10 , could be expressed as a sum of 1 + 2 + 3 + 4.
'''

import math
def consecutive_ducks(n):
    i = 2
    while i <= int(math.sqrt(n))+1:
        s = sum([j for j in range(i)])
        #print(s)
        if (n - s) % i == 0:
            #print(n-s)
            return True
        else:i += 1
    return False
n = 5263987
n = 10
#n = 15
print(consecutive_ducks(n))


#1st
from math import log2

def consecutive_ducks(n):
    return not log2(n).is_integer()

#2nd
def consecutive_ducks(n):
    while n % 2 == 0:
        n //= 2
    return n > 1

#3rd
def consecutive_ducks(n):
    '''
    find x + (x + 1) = n thus x exists if (n-1) % 2 == 0
    if not, find x + (x + 1) + (x + 2) = n
    4*x + 1+2+3+4
    5*x + 1+2+3+4+5
    '''
    sum = 0
    for i in range(1,n//2):
        sum += i
        if sum > n:
            continue
        if (n-sum) % (i+1) == 0:
            return True
    return False

#4th
def consecutive_ducks(n):
    return bool(n & (n - 1))


