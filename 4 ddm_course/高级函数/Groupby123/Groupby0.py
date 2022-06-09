from operator import itemgetter
from itertools import groupby

# 通过country进行分组
data.sort(key=itemgetter('country'))  # 需要先排序，然后才能groupby

lstg = groupby(data, itemgetter('country'))
for key, group in lstg:
    for g in group:  # group是一个迭代器，包含了所有的分组列表
        print(key, g)

"""
China {'country': 'China', 'age': 20, 'name': 'zhangsan'}
China {'country': 'China', 'age': 22, 'name': 'lijiu'}
JP {'country': 'JP', 'age': 22, 'name': 'lisi'}
USA {'country': 'USA', 'age': 19, 'name': 'wangwu'}
USA {'country': 'USA', 'age': 22, 'name': 'zhaoliu'}
USA {'country': 'USA', 'age': 22, 'name': 'pengqi'}
"""

# 返回每个分组的个数
res = dict([(key, len(list(group))) for key, group in lstg])

"""
{'JP': 1, 'China': 2, 'USA': 3}
"""


data = [
    {'name': 'zhangsan', 'age': 20, 'country': 'China'},
    {'name': 'lisi', 'age': 19, 'country': 'USA'},
    {'name': 'wangwu', 'age': 22, 'country': 'JP'},
    {'name': 'zhaoliu', 'age': 21, 'country': 'USA'},
    {'name': 'maqi', 'age': 22, 'country': 'USA'},
    {'name': 'yangba', 'age': 18, 'country': 'China'}
]

# 通过country进行分组
data.sort(key=itemgetter('country'))  # 需要先排序，然后才能groupby

lstg = groupby(data, itemgetter('country'))
for key, group in lstg:
    for g in group:  # group是一个迭代器，包含了所有的分组列表
        print(key, g)

"""
China {'country': 'China', 'age': 20, 'name': 'zhangsan'}
China {'country': 'China', 'age': 22, 'name': 'lijiu'}
JP {'country': 'JP', 'age': 22, 'name': 'lisi'}
USA {'country': 'USA', 'age': 19, 'name': 'wangwu'}
USA {'country': 'USA', 'age': 22, 'name': 'zhaoliu'}
USA {'country': 'USA', 'age': 22, 'name': 'pengqi'}
"""

# 返回每个分组的个数
res = dict([(key, len(list(group))) for key, group in lstg])

"""
{'JP': 1, 'China': 2, 'USA': 3}
"""

from itertools import groupby

lst = [2, 8, 11, 25, 43, 6, 9, 29, 51, 66]

def gb(num):
    if num <= 10:
        return 'less'
    elif num >= 30:
        return 'great'
    else:
        return 'middle'

print([(k, list(g)) for k, g in groupby(sorted(lst), key=gb)])

"""
[('less', [2, 6, 8, 9]), ('middle', [11, 25, 29]), ('great', [43, 51, 66])]
"""