'''
https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

FUNDAMENTALSSTRINGSASCIICHARACTER ENCODINGSFORMATS
'''
from collections import Counter
def count(s):
    cuntstr = Counter(s)
    return Counter(s)

def count(string):
    r = {}
    for c in string:
        if c in r:
            r[c] += 1
        else:
            r[c] = 1
    return r

def count(s):
    return {x:s.count(x) for x in set(s)}

from collections import Counter as count