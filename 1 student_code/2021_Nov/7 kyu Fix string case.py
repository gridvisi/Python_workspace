'''
https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python
'''

import string
print([ord(i) for i in string.ascii_letters])
def solve(s):
    supper = len([i for i in s if ord(i) <= 90])
    #slower = [i for i in s if ord(i) > 90]
    return s.lower() if 2*supper <= len(s) else s.upper()

#2
def solve(s):
    return s.upper() if sum(map(str.isupper, s)) * 2 > len(s) else s.lower()