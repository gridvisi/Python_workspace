'''
https://www.codewars.com/kata/59de795c289ef9197f000c48/train/python

import codewars_test as test
# TODO Write tests
import solution # or from solution import example

# test.assert_equals(actual, expected, [optional] message)
@test.describe("Example")
def test_group():
    test.assert_equals(remove_bmw("bmwvolvoBMW"), "volvo")
    test.assert_equals(remove_bmw("blablahblah"), "lalahlah")
'''

strng = "blablahblah"

def remove_bmw(strng):
    try:      #strng.isalpha()
        return ''.join([i for i in strng if i.lower() not in 'bmw'])
    except:
        return "This program only works for text."

strng = 2
strng = {}
strng = "bmwvolvoBMW"
print(remove_bmw(strng))

#1st solution
def remove_bmw(string):
    try:
        return string.translate(str.maketrans('','',"BMWbmw"))
    except AttributeError:
        raise TypeError("This program only works for text.")

#2nd solution
def remove_bmw(string):
    if not isinstance(string,str):
        raise TypeError("This program only works for text.")
    return ''.join(item for item in string if item not in "bBmMwW")