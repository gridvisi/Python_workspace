'''
https://www.codewars.com/kata/59f08f89a5e129c543000069/train/python
'''

arr = ["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]

from itertools import groupby
def dup(arr):
    re = []
    for w in arr:
        re.append(''.join([k for k, group in groupby(w)]))
    return re

from itertools import groupby
def dup(arry):
    return ["".join(c for c, grouper in groupby(i)) for i in arry]

import re
def dup(arry):
    return list(map(lambda s: re.sub(r'(\w)\1+', r'\1', s), arry))
print(dup(arr))


from itertools import groupby
lst = [2,8,11,25,43,6,9,29,51,66]


def gb(num):
    if num <= 20:
        return 'less'
    elif num >= 30:
        return 'great'
    else:
        return 'middle'

print(sorted(lst,key=gb))
print([(k,list(group)) for k,group in groupby(sorted(lst),key=gb)])
print(dict([(k,list(group)) for k,group in groupby(sorted(lst),key=gb)]))

# [('less', [2, 6, 8, 9]), ('middle', [11, 25, 29]), ('great', [43, 51, 66])]

rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in list(items):
        print(' ', i)



'''
def dup(arr):
    ans,res = '',[]
    k = [set(w) for w in arr]
    re = [list(w) for w in arr]
    for ls in re:
        ans = ''
        for i in ls:
            if i not in ans:
                ans += i
        res.append(ans)
    return res

'''