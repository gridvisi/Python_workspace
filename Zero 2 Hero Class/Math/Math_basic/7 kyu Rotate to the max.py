'''
https://www.codewars.com/kata/579fa665bb9944f9340005d2/train/python

Task
Given a number, return the maximum value by rearranging its digits.
Examples:

(123) => 321 (786) => 876 ("001") => 100 (999) => 999 (10543) => 54310
^Note the number may be given as a string
FUNDAMENTALSNUMBERS

import codewars_test as test
from solution import rotate_to_max

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(rotate_to_max(123), 321)
        test.assert_equals(rotate_to_max(786), 876)
        test.assert_equals(rotate_to_max('001'), 100)
        test.assert_equals(rotate_to_max(999), 999)
        test.assert_equals(rotate_to_max(10543), 54310)
'''

def rotate_to_max(n):
    return int(''.join(sorted(list(str(n)))[::-1]))
n = 123
print(rotate_to_max(n))
inp = ['001',999,10543,786]
print([rotate_to_max(n) for n in inp])