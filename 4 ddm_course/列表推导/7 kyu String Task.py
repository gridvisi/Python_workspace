'''
https://www.codewars.com/kata/598ab63c7367483c890000f4/train/python

import codewars_test as test
from solution import string_task

# test.assert_equals(actual, expected, [optional] message)
@test.describe("Example")
def test_group():
    test.assert_equals(string_task("Tour"), ".t.r")
    test.assert_equals(string_task("Codewars"), ".c.d.w.r.s")
    test.assert_equals(string_task("aBAcAba"), ".b.c.b")

'''

#1st solution by eric
s = "Tour"
def string_task(s):
    return ''.join([f".{i}" for i in s.lower() if i not in 'aeiou'])
print(string_task(s))

#2nd solution
def string_task(s):
    Vowels = ["A", "O", "Y", "E", "U", "I"]
    return "".join(["." + char.lower() for char in s if char.upper() not in Vowels])

#3rd solution
import re
def string_task(s):
    return re.sub(r"(.)", '.\\1' ,re.sub(r"[aeiouy]", '', s.lower(), flags = re.I))

