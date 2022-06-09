'''
https://www.codewars.com/kata/5a55f04be6be383a50000187/train/python
0, 1, 2, 3, 4 or 5

A number is a Special Number if it’s digits only consist 0, 1, 2, 3, 4 or 5

Given a number determine if it special number or not .
Test.describe("Sample Tests")
Test.it("Check Single Digit Number")
test.assert_equals(special_number(2), "Special!!")
test.assert_equals(special_number(5), "Special!!")
test.assert_equals(special_number(9), "NOT!!")
test.assert_equals(special_number(7), "NOT!!")

Test.it("Check Two Digit Number")
test.assert_equals(special_number(23), "Special!!")
test.assert_equals(special_number(79), "NOT!!")
test.assert_equals(special_number(39), "NOT!!")
test.assert_equals(special_number(55), "Special!!")

Test.it("Larger Special Number")
test.assert_equals(special_number(513)     , "Special!!")
test.assert_equals(special_number(709)     , "NOT!!")
test.assert_equals(special_number(970569)  , "NOT!!")
test.assert_equals(special_number(11350224), "Special!!")
'''

def special_number(number):
    return all([int(i) in {0, 1, 2, 3, 4,5} for i in str(number)])

def special_number(n):
    return "Special!!" if max(str(n)) <= "5" else "NOT!!"

def special_number(number):
    return ('Special' if set(str(number)) <= set('012345') else 'NOT') + '!!'

import re
def special_number(number):
    return "Special!!" if re.match(r'^[0-5]+$', str(number)) else "NOT!!"