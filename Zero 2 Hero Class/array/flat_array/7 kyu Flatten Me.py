'''
https://www.codewars.com/kata/55a5bef147d6be698b0000cd/solutions/python
'''

#ericlee
def flatten_me(arr):
    ans = []
    for i in arr:
        if type(i) == list:
            for j in i:
                ans.append(j)
        else:ans.append(i)
    return ans

#brilliant_idea
def flatten(lst):
    try:return sum(map(list, lst), [])
    except:return lst

#1st
def flatten_me(lst):
    res = []
    for l in lst:
        if isinstance(l, list):
            res.extend(l)
        else:
            res.append(l)
    return res

#2nd
def flatten_me(nput):
    output = []
    for itm in nput:
        if isinstance(itm, list):
            output += flatten_me(itm)
        else:
            output += [itm]
    return output

#3rd
from collections import Iterable
from itertools import chain

def flatten_me(lst):
    return list(chain(*(x if isinstance(x,Iterable) else [x] for x in lst)))

#4th
def flatten(lst):
    r = []
    for x in lst:
       if type(x) is list:
          r.extend(x)
       else:
          r.append(x)
    return r