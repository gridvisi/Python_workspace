'''
https://www.codewars.com/kata/60908bc1d5811f0025474291/train/python

import codewars_test as test
from solution import find_squares
# TODO Write tests

# test.assert_equals(actual, expected, [optional] message)
@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(find_squares(9), '25-16')
    @test.it("Random Tests")
    def test_case():
        test.assert_equals(find_squares(5), '9-4')
        test.assert_equals(find_squares(7), '16-9')
'''

import math
def find_squares(num):
    i = 1
    while math.sqrt(num + i**2) != int(math.sqrt(num + i**2)):
        i += 1
    return f"{num + i**2}-{i**2}"
num = 9
num = 187
num = 77
print(find_squares(num))

'''
Numbers > 100
'196-9' should equal '8836-8649'
'961-784' should equal '7921-7744'
'''
print(math.sqrt(196),196-9)

print(math.sqrt(8836),math.sqrt(8649),8836-8649)

#1st
def find_squares(n):
    m = (n-1)//2
    return f'{(m+1)**2}-{m**2}'