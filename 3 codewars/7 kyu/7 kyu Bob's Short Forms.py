'''
https://www.codewars.com/kata/570cbe88f616a8f4f50011ac/solutions/python
'''

def short_form(s):
    return '{}{}{}'.format(s[0], s[1:-1].translate(None, 'aeiouAEIOU'), s[-1])

from re import *
def short_form(s):
    return sub(r"(?<!^)[aeiou](?=.)", '', s, flags=I)

def short_form(s):
    return s[0] + s[1:-1].translate(None, "aeiouAEIOU") + s[-1]

import re
def short_form(s):
    return s[0] + re.sub(r'[aeiou]', '', s[1:-1], flags=re.I) + s[-1]

