'''
https://www.codewars.com/kata/5a4ea304b3bfa89a9900008e/train/python

Test.describe("Basic tests")
Test.assert_equals(max_number(213), 321)
Test.assert_equals(max_number(7389), 9873)
Test.assert_equals(max_number(63792), 97632)
Test.assert_equals(max_number(566797), 977665)
Test.assert_equals(max_number(1000000), 1000000)
print("<COMPLETEDIN::>")
'''

def max_number(n):
    return int(''.join(sorted(list(str(n)),reverse=True)))

#lambda
max_number = lambda n: int("".join(sorted(str(n)))[::-1])