
'''

https://www.codewars.com/kata/5902ea9b378a92a990000016/train/python

Test.assert_equals(sum_primes(4, 20), 72)
Test.assert_equals(sum_primes(20, 4), 0)
Test.assert_equals(sum_primes(2, 7), 17)
Test.assert_equals(sum_primes(1, 30), 129)

'''

# TypeError: can't convert complex to int
# python 不支持复数转换为整数或浮点数

import math


def isPrime(n):
    return n == 2 or n != 1 and n % 2 and all(n % p for p in range(3, int(math.sqrt(n)) + 1, 2))

def isPrime(n):
    return n==2 or n%2 and all(n%p for p in range(3,int(n**.5)+1,2))

def sum_primes(lower, upper):
    if lower > upper: return 0

    return sum([i for i in range(lower, upper + 1) if i > 0 and isPrime(i)])


#
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def sum_primes(lower, upper):
    return sum(i for i in range(lower, upper + 1) if is_prime(i))

'''
>>> float(4.5+0j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    float(4.5+0j)
TypeError: can't convert complex to float

>>> int(4+0j)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(4+0j)
TypeError: can't convert complex to int
>>>
针对前面有人提到复数不能强转为int或者float的问题：

其实在Python中，复数提供了2个函数，一个函数是real，返回复数的实数部分，另一个函数是imag，
返回复数的虚数部分。因为实数跟复数是差异很大的类型，所以不支持强制转换是可以理解的。因为在强制转换过程中，
虚数部分到底该怎么转换，是没有定义的，而int和float只有实数部分，虚数部分该如何取舍？

>>> a = 4.1+0.3j
>>> a
(4.1+0.3j)
>>> a.real
4.1
>>> a.imag
0.3
'''