'''
https://www.codewars.com/kata/5a262cfb8f27f217f700000b/train/python

n this Kata, you will be given two strings a and b and your task will be to return the characters that are not common in the two strings.

For example:

solve("xyab","xzca") = "ybzc"
--The first string has 'yb' which is not in the second string.
--The second string has 'zc' which is not in the first string.
Notice also that you return the characters from the first string concatenated with
those from the second string.

More examples in the tests cases.

Test.it("Basic tests")
Test.assert_equals(solve("xyab","xzca"),"ybzc")
Test.assert_equals(solve("xyabb","xzca"),"ybbzc")
Test.assert_equals(solve("abcd","xyz"),"abcdxyz")
Test.assert_equals(solve("xxx","xzca"),"zca")
'''

def solve(a,b):
    return "".join([i for i in a if i not in b] + [i for i in b if i not in a])

def solve(a,b):
    s = set(a)&set(b)
    return ''.join(c for c in a+b if c not in s)

import re
def solve(a,b):
    return re.sub('|'.join(set(a) & set(b)), '', a+b)

def solve(a,b):
    return "".join(c for c in a if c not in b) \
         + "".join(c for c in b if c not in a)