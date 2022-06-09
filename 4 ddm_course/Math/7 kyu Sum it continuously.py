'''
https://www.codewars.com/kata/59b44d00bf10a439dd00006f/train/python

add [1,2,3,4,5] == [1, 3, 6, 10, 15], because it's calculated like
this : [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4, 1 + 2 + 3 + 4 + 5]
'''
def add(l):
    ans,s = [],0
    for i in l:
        s += i
        ans.append(s)
    return ans
l = [1,4,9,16,25,36]
print(add(l))

from itertools import accumulate
def add(lst):
    return list(accumulate(lst))


