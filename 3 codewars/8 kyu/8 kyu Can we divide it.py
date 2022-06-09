'''
https://www.codewars.com/kata/5a2b703dc5e2845c0900005a/train/python

Test.describe("Basic Tests")
Test.it("should pass basic tests")
Test.assert_equals(is_divide_by(-12, 2, -6), True)
Test.assert_equals(is_divide_by(-12, 2, -5), False)
Test.assert_equals(is_divide_by(45, 1, 6), False)
Test.assert_equals(is_divide_by(45, 5, 15), True)
Test.assert_equals(is_divide_by(4, 1, 4), True)
Test.assert_equals(is_divide_by(15, -5, 3), True)
'''
def is_divide_by(number, a, b):
    return all([number % x == 0 for x in (a,b)])

number, a, b = -12, 2, -6

print(is_divide_by(number, a, b))