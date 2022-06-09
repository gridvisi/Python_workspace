'''
https://www.codewars.com/kata/59f38b033640ce9fc700015b/train/python

Test.it("Basic tests")
Test.assert_equals(total([]),0)
Test.assert_equals(total([1,2,3,4]),7)
Test.assert_equals(total([1,2,3,4,5,6]),13)
Test.assert_equals(total([1,2,3,4,5,6,7,8]),21)
Test.assert_equals(total([1,2,3,4,5,6,7,8,9,10,11]),21)
Test.assert_equals(total([1,2,3,4,5,6,7,8,9,10,11,12,13]),33)
Test.assert_equals(total([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]),47)
'''

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#16th solution by ericlee
import math
def isPrime(x):
    if x == 0 or x == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x % i == 0:
                return False
    return True

def total(arr):
    return sum([e for i,e in enumerate(arr) if isPrime(i)])
print(total(arr))


#1st solution
def is_prime(n):
    return n >= 2 and all(n % i for i in range(2, 1 + int(n ** .5)))


def total(arr):
    return sum(n for i, n in enumerate(arr) if is_prime(i))

#nth
import itertools
import numpy as np

s = np.ones(100000)
s[:2] = s[4::2] = 0
for i in range(3, int(len(s)**0.5)+1, 2):
    if s[i]:
        s[i*i::i] = 0

def total(arr):
    return sum(itertools.compress(arr, s))


def total(arr):
    total = 0
    for c in range(2,len(arr)):
        for i in range (2,c):
            if c%i==0:
                break
        else:
            total += arr[c]
    return total
