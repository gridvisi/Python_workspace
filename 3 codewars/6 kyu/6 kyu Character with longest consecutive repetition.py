'''
https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/python

tests = [
    # [input, expected],
    ["aaaabb", ('a', 4)],
    ["bbbaaabaaaa", ('a', 4)],
    ["cbdeuuu900", ('u', 3)],
    ["abbbbb", ('b', 5)],
    ["aabb", ('a', 2)],
    ["ba", ('b', 1)],
    ["", ('', 0)],
'''
chars = "ba"  #('b', 1)
chars = "bbbaaabaaaa"
#chars = "cbdeuuu900"
#chars = "aabb"
#chars = 'ba'

from itertools import groupby
def longest_repetition(chars):
    if not chars:return '',0
    res = []
    for c, group in groupby(chars):
        res.append((c, len(list(group))))
        print(res)
    return max(res,key=lambda x:x[1])
    #sorted(res,key=lambda x:x[1])[-1]
print('-1: ',longest_repetition(chars))

from itertools import groupby

def longest_repetition(chars):
  return max([(x, len(list(gp))) for x, gp in groupby(chars)], key = lambda x: x[1], default = ('', 0))

#1st solution
def longest_repetition(chars):
    max_char, max_count = '', 0
    char, count = '', 0
    for c in chars:
        if c != char:
            count, char = 0, c
        count += 1
        if count > max_count:
            max_char, max_count = char, count
    return max_char, max_count

#2 solution
def longest_repetition(chars):
    from itertools import groupby
    return max(((char, len(list(group))) for char, group in groupby(chars)),
               key=lambda char_group: char_group[1], default=("", 0))

#3 solution
import re


def longest_repetition(chars):
    if not chars: return ("", 0)

    longest = max(re.findall(r"((.)\2*)", chars), key=lambda x: len(x[0]))
    return (longest[1], len(longest[0]))

from itertools import groupby
def longest_repetition(chars):
    if not chars:return ''
    res = []
    for c, group in groupby(chars):
        res.append((c, len(list(group))))
    #print(sorted(res,reverse=True))
    res.sort(reverse=True)
    print(res,sorted(res,key=lambda x:x[1]))
    return sorted(res,key=lambda x:x[1])[-1]
    #sorted(res,key=lambda x:x[1])[-1]
print('0 ',longest_repetition(chars))

res = []
for c, group in groupby(chars):
    #print(c,list(group))
    res.append((c,len(list(group))))
print(res)
print(sorted(res))
print(sorted(res,key=lambda x:x[1]))

print('test:',max(chars.split('b'),key=len))
print('test:',max(chars.split(f"{'b'}"),key=len))



from collections import Counter
def longest_repetition(chars):
    #d = sorted(Counter(chars),key=lambda x:x[values]
    #d = sorted(Counter(chars), key=lambda x:Counter(chars).values())
    chars_d = Counter(chars)
    d,mx = sorted(chars_d,reverse=True),chars_d[max(chars_d)]

    return d,mx

chars = "cbdeuuu900"
print('1 ',longest_repetition(chars))

def longest_repetition(chars):
    k = set(list(chars))
    print(k)
    long,bench = 0,''
    for i in k:
        l = len(chars) - len(chars.split(f"{i}"))
        #print(chars,chars.split(f"{i}"),max(chars.split(f"{i}"),key=len))
        re = max(chars.split(f"{i}"),key=len)
        print(chars.split(f"{i}"))
        if len(re) >= len(bench):
        #if l > long:
            bench = re
    return bench,len(bench)
chars = "aaaabb"  # ('a', 4)
chars = 'bdeuuu900'
print('2:',longest_repetition(chars))

def longest_repetition(chars):
    k = set(list(chars))
    mxlen = 0
    for i in k:
        sl = [i for i in chars.split(i) if i == '']
        if len(sl) > mxlen:
            mxlen = len(sl)
    return mxlen
chars = "aaaabb"  # ('a', 4)
print(longest_repetition(chars))

from collections import Counter
def longest_repetition(chars):
    return max(Counter(chars)),
chars = "ba" # ('b', 1)
chars = "bbbaaabaaaa"
print(longest_repetition(chars))


def longest_repetition(chars):
    i,j,mx,re = 0,1,0,[]
    for i in range(len(chars)):
        while j < len(chars):
            if chars[i] == chars[j]:
                j += 1
                if j - i > mx:
                    mx = j - i
                    re.append((chars[i],mx))
            else:
                i += 1
    return re,re[-1]
print(longest_repetition(chars))