#https://www.codewars.com/kata/5bc052f93f43de7054000188/train/python

'''

You will be given two strings a and b consisting of lower case letters, but a will have at most
 one asterix character. The asterix (if any) can be replaced with an arbitrary sequence (possibly empty) 
 of lowercase letters. No other character of string a can be replaced. If it is possible to replace 
 the asterix in a to obtain string b, then string b matches the pattern.

If the string matches, return true else false.

For example:
solve("code*s","codewars") = true, because we can replace the asterix(*) with "war" to match the second 
string.
solve("codewar*s","codewars") = true, because we can replace the asterix(*) with "" to match the second 
string. 
solve("codewars","codewars") = true, because the strings already match.
solve("a","b") = false
solve("*", "codewars") = true
'''

#1st solution
from fnmatch import fnmatch
def solve(a, b):
    return fnmatch(b, a)

import re
def solve(a,b):
    return bool(re.fullmatch(a.replace('*', '.*'), b))


def solve(a, b):
    if a == b: return True
    if "*" not in a: return False

    sides = a.split("*")
    missing = b[len(sides[0]):len(b) - len(sides[1])]
    c = a.replace("*", missing)
    return c == b