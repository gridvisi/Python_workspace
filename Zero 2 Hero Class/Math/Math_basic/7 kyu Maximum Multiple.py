'''
https://www.codewars.com/kata/5aba780a6a176b029800041c/train/python

Test.describe("Basic tests")
Test.assert_equals(max_multiple(2,7),6)
Test.assert_equals(max_multiple(3,10),9)
Test.assert_equals(max_multiple(7,17),14)
Test.assert_equals(max_multiple(10,50),50)
Test.assert_equals(max_multiple(37,200),185)
Test.assert_equals(max_multiple(7,100),98)
'''

def max_multiple(divisor, bound):
    return (bound//divisor) * divisor

def max_multiple(divisor, bound):
    return bound - (bound % divisor)