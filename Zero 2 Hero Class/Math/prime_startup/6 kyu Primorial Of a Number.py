'''
https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124/train/python

Test.describe("Basic tests")
Test.assert_equals(num_primorial(3),30)
Test.assert_equals(num_primorial(4),210)
Test.assert_equals(num_primorial(5),2310)
Test.assert_equals(num_primorial(8),9699690)
Test.assert_equals(num_primorial(9),223092870)
print("<COMPLETEDIN::>")
'''
# next prime function
# n = perior prime
# 21st rank solve by ericlee
import math
def num_primorial(n):
    def isPrime(x):
        if x == 1:return False
        else:
            for i in range(2,int(math.sqrt(x))+1):
                if x % i == 0:return False
            return True
    primeMul = 2
    st = 2
    for _ in range(n-1):
        x = 1
        while not isPrime(st+x):
            x += 1
        st = st+x
        primeMul *= st
    return primeMul
n = 2
n = 3
n = 5
n = 7
n = 9
print(num_primorial(n))


#1ST
def num_primorial(n):
    primorial, x, n = 2, 3, n-1
    while n:
        if all(x % d for d in range(3, int(x ** .5) + 1, 2)):
            primorial *= x
            n -= 1
        x += 2
    return primorial

#2ND
from gmpy2 import next_prime


def num_primorial(n: int) -> int:
    p = prev = 1
    for _ in range(n):
        prev = next_prime(prev)
        p *= prev
    return p

