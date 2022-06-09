'''
https://www.codewars.com/kata/596c6eb85b0f515834000049/train/python

import codewars_test as test
from solution import replace_dots

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(replace_dots(""), "")
        test.assert_equals(replace_dots("no dots"), "no dots")
        test.assert_equals(replace_dots("one.two.three"), "one-two-three")
        test.assert_equals(replace_dots("........"), "--------")
'''

import re
import re
def replace_dots(str):
    return re.sub(r"\.", "-", str)
    # literally I had to only add a \ infront of the dot.
    # this challenge is super hard for noobs and super easy
    # for pros. it's not fair.

def replace_dots(string):
    return string.replace('.', '-')
s = "one.two.three"
print(replace_dots(s))

def replace_dots(s):
    return ''.join(['-' if i == '.' else i for i in s ])
s = "one.two.three"
print(replace_dots(s))