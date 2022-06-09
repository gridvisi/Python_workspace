'''
https://www.codewars.com/kata/5a55f04be6be383a50000187/train/python

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
    return "Special!!" if max([int(i) for i in str(number)]) <= 5 else "NOT!!"