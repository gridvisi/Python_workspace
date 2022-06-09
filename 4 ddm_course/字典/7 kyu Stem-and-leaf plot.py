'''
https://www.codewars.com/kata/5cc80fbe701f0d001136e5eb/train/python

stem | leaf
-----------
  0  | 9
  1  | 1 4
  2  | 3
  3  | 5 5 9
'''
data = [11, 35, 14, 9, 39, 23, 35]
output = {0: [9], 1: [1, 4], 2: [3], 3: [5, 5, 9]}

def stem_and_leaf(data):
    ans = {}
    data = sorted(['0'+str(i) if len(str(i)) == 1 else str(i) for i in data])
    print(data)
    #res = [(0,i) if len(i) == 1 else (i[0],i[1]) for i in data]
    key,value = [int(i[0]) for i in data],[int(i[1:]) for i in data]
    for k,v in list(zip(key,value)):
        if k not in ans:
            ans[k] = [v]
        else:
            ans[k].append(v)

    return ans


#1 solution

from collections import defaultdict

def stem_and_leaf(a):
    d = defaultdict(list)
    for x in a:
        d[x//10].append(x % 10)
    return {x: sorted(y) for x, y in d.items()}

#2 solution
from collections import defaultdict
def stem_and_leaf(data):
    result = defaultdict(list)
    for n in sorted(data):
        stem, leaf = divmod(n, 10)
        result[stem].append(leaf)
    return result

#3 solution
from collections import defaultdict
from bisect import insort

def stem_and_leaf(data):
    res = defaultdict(list)
    for x in data:
        q, r = divmod(x, 10)
        insort(res[q], r)
    return res

#4 solution
def stem_and_leaf(data):
    plot = {}
    data = sorted(data)
    for x in data:
        if x//10 in plot:
            plot[x//10].append(x%10)
        else:
            plot[x//10] = [x%10]
    return plot


print(stem_and_leaf(data))