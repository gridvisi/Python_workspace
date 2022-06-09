# https://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-whilst-preserving-order/39835527#39835527
# for hashable sequence
def remove_duplicates(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
list(remove_duplicates(a))
# [1, 5, 2, 9, 10]

sequence = ['1', '2', '3', '3', '6', '4', '5', '6']
unique = []
print([unique.append(item) for item in sequence if item not in unique])

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
'''
为什么要把 seen.add 分配给 seen_add，而不是直接调用 seen.add？Python 是一种动态语言，每次迭代解析 
seen.add 比解析一个局部变量的成本更高。 seen.add 可能在迭代之间发生了变化，而运行时没有足够的智能来排除这种可能性。
为了安全起见，它必须每次都检查对象。
如果你打算在同一个数据集上经常使用这个函数，也许你最好使用一个有序的集合：
http://code.activestate.com/recipes/528878/。
O(1)每次操作的插入、删除和成员检查。
(额外的小说明： seen.add()总是返回None，所以上面的or只是作为尝试集更新的一种方式，而不是作为逻辑测试的一个组成部分。)
'''

# for unhashable sequence
def remove_duplicates(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
list(remove_duplicates(a, key=lambda d: (d['x'],d['y'])))
# [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]


#%matplotlib notebook

from iteration_utilities import unique_everseen
from collections import OrderedDict
from more_itertools import unique_everseen as mi_unique_everseen

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def iteration_utilities_unique_everseen(seq):
    return list(unique_everseen(seq))

def more_itertools_unique_everseen(seq):
    return list(mi_unique_everseen(seq))

def odict(seq):
    return list(OrderedDict.fromkeys(seq))

#from simple_benchmark import benchmark
#b = benchmark([f7, iteration_utilities_unique_everseen, more_itertools_unique_everseen, odict],
#              {2**i: list(range(2**i)) for i in range(1, 20)},
#              'list size (no duplicates)')
#b.plot()

def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element

#In Python 3.7, the regular dict is guaranteed to both ordered across all implementations.
# So, the shortest and fastest solution is:
print(list(dict.fromkeys('abracadabra')))
#['a', 'b', 'r', 'c', 'd']


import pandas as pd

my_list = [0, 1, 2, 3, 4, 1, 2, 3, 5]
pd.Series(my_list).drop_duplicates().tolist()
# Output:
# [0, 1, 2, 3, 4, 5]

sortedList = [0, 1, 2, 3, 4, 1, 2, 3, 5]
from itertools import groupby
print([key for key,_ in groupby(sortedList)])

import pandas as pd
lst = [1, 2, 1, 3, 3, 2, 4]
pd.unique(lst)
#array([1, 2, 3, 4])

import pandas as pd
import numpy as np

uniquifier = lambda alist: pd.Series(alist).drop_duplicates().tolist()

# from the chosen answer
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

alist = np.random.randint(low=0, high=1000, size=10000).tolist()

print (uniquifier(alist) == f7(alist))  # True
'''
Timing: 
    In [104]: %timeit f7(alist)
    1000 loops, best of 3: 1.3 ms per loop
    In [110]: %timeit uniquifier(alist)
    100 loops, best of 3: 4.39 ms per loop
'''

'''
this will preserve order and run in O(n) time. basically the idea is to create a hole 
wherever there is a duplicate found and sink it down to the bottom. makes use of a read 
and write pointer. whenever a duplicate is found only the read pointer advances and write 
pointer stays on the duplicate entry to overwrite it.

'''