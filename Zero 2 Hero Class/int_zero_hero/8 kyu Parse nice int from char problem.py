'''
https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1/solutions/python

Test.describe("Basic tests")
Test.assert_equals(get_age("2 years old"), 2)
Test.assert_equals(get_age("4 years old"), 4)
Test.assert_equals(get_age("5 years old"), 5)
Test.assert_equals(get_age("7 years old"), 7)
'''

def get_age(age):
    return int(age[0])

import re
def get_age(age):
    return int(re.search(r"\d+", age).group())