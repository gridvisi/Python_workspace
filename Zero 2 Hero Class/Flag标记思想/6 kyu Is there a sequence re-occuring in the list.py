'''
https://www.codewars.com/kata/5a7e6bd576c0e2f27d00237a/train/python

Examples
[0, 0, 1, 1, 0, 0]       ==> True   # 0 is re-occuring
[0, 0, 'a', 0]           ==> True   # 0 is re-occuring
[0, 0, 1, 1, 2, 2, 1, 1] ==> True   # 1 is re-occuring
[0, 0, 0]                ==> False  # no sequence re-occurs
[0, 0, 1, 1, 2, 2]       ==> False  # no sequence re-occurs
'''


#1st
from itertools import groupby
def is_reoccuring(xs):
    cs = [k for k, _ in groupby(xs)]
    return len(cs) != len(set(cs))

items = [0, 0, 1, 1, 2, 2, 1, 1]
#items = [0, 0, 1, 1, 2, 2]
print(is_reoccuring(items))

#2
from collections import Counter
from itertools import groupby
def is_reoccuring(arr):
    return any( v>1 for v in Counter(k for k,g in groupby(arr)).values() )


#3rd
def is_reoccuring(items):
    seen = set()
    last = ''

    for i in items:
        if i not in seen:
            seen.add(i)
        elif i != last:
            return True
        last = i
    return False

# ericlee first try time out
def is_reoccuring(items):
    s = set(items)
    #print(s)
    res = []
    for elem in s:
        res = [i for i,e in enumerate(items) if e == elem]
        #print(res)
        if any([j-i > 1 for i,j in zip(res[:-1],res[1:])]):
            return True
    return False
'''
Test Results:
Execution Timed Out
STDERR
Execution Timed Out (12000 ms)
'''
items = [0, 0, 1, 1, 2, 2, 1, 1]
items = [0, 0, 1, 1, 2, 2]
print(is_reoccuring(items))
