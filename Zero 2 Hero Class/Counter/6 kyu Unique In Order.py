'''
https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
Implement the function unique_in_order which takes as argument a sequence
and returns a list of items without any elements with the same value next
to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
'''

def unique_in_order(iterable):
    try:
        flag = iterable[0]
        ans = [flag]
        for c in iterable[1:]:
            if flag == c:
                pass
            elif flag != c:
                ans.append(c)
                flag = c
    except:ans = []
    return ans
iterable = 'AAAABBBCCDAABBB'
iterable = ''
print(unique_in_order(iterable))

#1st
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

#2nd
from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]

#3rd
unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]



#4th
def unique_in_order(iterable):
    r = []
    for x in iterable:
        x in r[-1:] or r.append(x)
    return r

print('AAAABBBCCDAABBB'[-1:])
print('AAAABBBCCDAABBB'[-1])


print(list('AAAABBBCCDAABBB')[-1:])
print(list('AAAABBBCCDAABBB')[-1])



from collections import Counter
def unique_in_order(iterable):
    it = Counter(iterable)
    return it.keys()
iterable = 'AAAABBBCCDAABBB'
print(unique_in_order(iterable))