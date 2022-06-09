#https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/python

'''
Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""

'''
s = "abc#d##c"
s = "abc##d######"
from collections import deque
def clean_string(s):
    sq,re = deque(),list(s)
    for i,e in enumerate(re):
        if e != '#':
            sq.append(e)
        else:
            if len(sq) != 0:
                sq.pop()
    return ''.join(list(sq))
print(clean_string(s))

def clean_string(s):
    stk = []
    for c in s:
        if c=='#' and stk: stk.pop()
        elif c!='#':       stk.append(c)
    return ''.join(stk)

import re

def clean_string(s):
  while '#' in s:
    s = re.sub('.?#', '', s, count=1)
  return s

import regex
def clean_string(s):
    return regex.sub(r'[^#]((?R)*)#+|\A#+', '', s)

from functools import reduce

def clean_string(s):
  return reduce(lambda x, y: x[:-1] if y == '#' else x+y, s, "")