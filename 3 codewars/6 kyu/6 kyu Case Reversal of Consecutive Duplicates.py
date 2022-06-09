'''
https://www.codewars.com/kata/case-reversal-of-consecutive-duplicates/train/python
The aim of this Kata is to write a function which will reverse the case of all consecutive duplicate letters in a string. That is, any letters that occur one after the other and are identical.

If the duplicate letters are lowercase then they must be set to uppercase, and if they are uppercase then they need to be changed to lowercase.

Examples:
reverse_case("puzzles")    Expected Result: "puZZles"
reverse_case("massive")    Expected Result: "maSSive"
reverse_case("LITTLE")     Expected Result: "LIttLE"
reverse_case("shhh")       Expected Result: "sHHH"
https://www.codewars.com/kata/577c2d68311a24132a0002a5/solutions
'''
str = "LITTTLE"
print(str.swapcase())
#str = 'sxxdxcsxxzy'

import re

def reverse(s):
    return re.sub(r'(.)\1+', lambda m: m.group().swapcase(), s)

import re
def reverse(strng): return re.sub(r'(\w)\1+', lambda m: m.group().swapcase(), strng)

from functools import partial
from re import compile

reverse = partial(compile(r"(.)\1+").sub, lambda s: s.group().swapcase())


reverse=lambda s:__import__('re').sub(r'(.)\1+',lambda x:x.group(0).swapcase(),s)

def reverse(s):
    index, l = 0, [[]]
    for x in s:
        if x in l[index]:
            l[index].append(x)
        elif not l[index]:
            l[index].append(x)
        else:
            l.append([x])
            index += 1
    return "".join(''.join(c.swapcase()for c in x)if len(x)>1 else x.pop()for x in l)


from itertools import groupby
def reverse(str):
    result = ''
    for k, g in groupby(str):
        l = sum(1 for _ in g)
        result += k if l==1 else k.swapcase()*l
    return result

import re
def reverse(_str):
    r=''
    for w in re.findall(r'((.)\2*)',_str):
        if len(w[0])>1:
            r+=w[0].swapcase()
        else:
            r+=w[0]
    return r

def reverse(str):
    result = []
    l = len(str)
    for i, c in enumerate(str):
        if (i < l - 1 and c == str[i + 1]) or (i > 0 and c == str[i - 1]):
            result.append(c.swapcase())
        else:
            result.append(c)
    return ''.join(result)

from itertools import groupby
def reverse(str):
    a = [list(y) for x,y in groupby(str)]
    return ''.join(y.swapcase() if len(x)>1 else y for x in a for y in x)

from re import findall
def reverse(s):
    return ''.join([m.swapcase() if len(m) > 1 else m for m, c in findall(r'((.)\2*)', s)])