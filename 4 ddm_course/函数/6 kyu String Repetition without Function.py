'''
https://www.codewars.com/kata/57a110eee298a737e2000283/train/python

test.describe("Example Tests")
test.assert_equals(str_repeat('a', 4), 'aaaa')
test.assert_equals(str_repeat('hello ', 3), 'hello hello hello ')
test.assert_equals(str_repeat('abc', 2), 'abcabc')
'''

from operator import mul as str_repeat

str_repeat=str.__mul__

class str_repeat:
    def __new__(cls, s, r):
        return s * r

class Repit():

    def __call__(self, st, r):
        return st * r
str_repeat = Repit()

from operator import mul as str_repeat
str_repeat = str.__mul__

def isinstance(a, b):
    return False
str_repeat = lambda x, y: x*y