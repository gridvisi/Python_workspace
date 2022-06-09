# https://www.codewars.com/kata/5d10d53a4b67bb00211ca8af/train/python

#return the minimum required waterbombs to extinguish the fires in the array
'''
"xxYxx" and w = 3      -->  2 waterbombs needed
"xxYxx" and w = 1      -->  4
"xxxxYxYx" and w = 5   -->  3
"xxxxxYxYx" and w = 2  -->  5
'''
print("xxxxxYxYx".split('Y'))
def waterbombs(fire, w):  # false since
    res = 0
    f = fire.split('Y')
    for s in f:
        res += (len(s)//w) + 1
    return res


fire, w = "xxYxx", 3
fire, w = "xxxxYxYx", 4
fire, w = "xxxxYxYx" ,5
fire, w = "xxxxxYxYx", 2
def waterbombs(fire, w):
    return sum([len(i)//w if len(i)%w == 0 else 1+len(i)//w for i in fire.split('Y')])
    #return sum([len(i)//w + 1 for i in fire.split('Y')])
print(waterbombs(fire, w))

#1st solution
waterbombs = lambda fire, w: sum([(len(i)+w-1)//w for i in fire.split('Y')])

from math import ceil
def waterbombs(fire, w):
  return sum(ceil(len(l)/w) for l in fire.split('Y'))

import re
def waterbombs(xs, w):
    return len(re.findall(f'x{{1,{w}}}', ''.join(xs)))

from math import ceil
def waterbombs(fire, w):
  return sum(ceil(len(f)/w) for f in fire.split('Y'))

from itertools import groupby
def waterbombs(fire, w):
    return sum((len(list(grp)) + w - 1)//w for key, grp in groupby(fire) if key == 'x')