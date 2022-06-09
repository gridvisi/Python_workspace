'''
https://www.codewars.com/kata/57cf50a7eca2603de0000090/train/python

Move every letter in the provided string forward 10 letters through the alphabet.
If it goes past 'z', start again at 'a'.
Input will be a string with length > 0.

FUNDAMENTALSSTRINGSARRAYS

import codewars_test as test
from solution import move_ten

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(move_ten("testcase"), "docdmkco")
        test.assert_equals(move_ten("codewars"), "mynogkbc")
'''

import string
def move_ten(st):
    strs = string.ascii_lowercase
    return ''.join([strs[(strs.index(i)+10)%26] for i in st])

st = "codewars"
print(move_ten(st))

print(string.ascii_lowercase)
s = string.ascii_lowercase
print(s.index('c'),len(s))
print(s[s.index('c')+10])
print(s[(s.index('c')+10)%26])