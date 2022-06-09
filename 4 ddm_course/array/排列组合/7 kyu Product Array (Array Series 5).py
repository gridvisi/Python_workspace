'''
https://www.codewars.com/kata/5a905c2157c562994900009d/train/python
Explanation:
The first element 10 is the product of all array's elements except the first element *1***
The second element 2 is the product of all array's elements except the second element 5
The Third element 5 is the product of all array's elements except the Third element 2.

Test.describe("Basic Tests")
Test.assert_equals(product_array([12,20]), [20,12])
Test.assert_equals(product_array([12,20]), [20,12])
Test.assert_equals(product_array([3,27,4,2]), [216,24,162,324])
Test.assert_equals(product_array([13,10,5,2,9]), [900,1170,2340,5850,1300])
Test.assert_equals(product_array([16,17,4,3,5,2]), [2040,1920,8160,10880,6528,16320])
print("<COMPLETEDIN::")

product (of multiplication)
product (of vectors)
'''

def product_array(numbers):
    ans = []
    mul = 1
    for n in numbers:
        mul *= n
        s = 1
    print(mul)
    for i in numbers:
        ans.append(mul/i)
    return ans
numbers = [16,17,4,3,5,2]
print(product_array(numbers))

#1st solution
from operator import mul
from functools import reduce

def product_array(numbers):
    tot = reduce(mul,numbers)
    return [tot//n for n in numbers]

from numpy import prod
def product_array(numbers):
    p = prod(numbers)
    return [p // i for i in numbers]

def product_array(numbers):
    prod = eval("*".join(map(str, numbers)))
    return [ prod / x for x in numbers ]

def product_array(n):
    prod = eval("*".join(map(str,n)))
    return [prod//i for i in n]

import numpy
def product_array(numbers):
    p = numpy.prod(numbers)
    return [p / i for i in numbers]

import numpy
def product_array(numbers):
    return [numpy.prod(numbers)/i for i in numbers]

product_array = lambda n: map(reduce(int.__mul__, n).__div__, n)