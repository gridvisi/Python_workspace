'''
https://www.codewars.com/kata/59c5f4e9d751df43cf000035/train/python
'''
def solve(s):
    s = ''.join([i if i in 'aeiou' else ' ' for i in s])
    print(s)
    return len(max(s.split(' '),key=len))
s = "chrononhotonthuooaos"
print(solve(s))



#1st solution
def solve(s):
    return max(map(len, ''.join(c if c in 'aeiou' else ' ' for c in s).split()))

#2nd solution
import re
def solve(s):
    return max(len(x.group(0)) for x in re.finditer(r'[aeiou]+', s))

#3rd solution
from re import findall
def solve(s):
    return max(map(len, findall("[aeiou]+", s)))

from re import compile
r = compile("[aeiou]+")
def solve(s: str):
    return max(map(len, r.findall(s)))


from itertools import groupby
def solve(s):
  return max(len(list(gp)) for p, gp in groupby(s, key = lambda x: x in 'aeiou') if p)


def solve(s):
    re = ''
    vow = 'aeiou'
    for i in s:
        if i in 'aeiou':
            re += i
        else:
            re += ' '
    return len(max(re.split(' '),key=len))

'[(k,list(group)) for k,group in groupby(s) if k in vow]'

s = "chrononhotonthuooaos"
print(solve(s))


def solve(s):
    re = []
    for i in range(len(s)):
        j, w = 0,''
        if s[i+j] in 'aeiou':
            w += s[i + j]
            j += 1
        re.append(''.join(w))
        #print(re)
    return re
