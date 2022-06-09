#https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-in-python-taking-union-o

import timeit
import itertools
from collections import ChainMap
from string import ascii_uppercase as up, ascii_lowercase as lo

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

def merge_two_dicts(x, y):
    """Given two dictionaries, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

print(min(timeit.repeat(lambda: {**x, **y})))
#0.4094954460160807

#print(min(timeit.repeat(dict(x.items() | y.items()))))

print(min(timeit.repeat(lambda: merge_two_dicts(x, y))))
#0.7881555100320838

print(min(timeit.repeat(lambda: {k: v for d in (x, y) for k, v in d.items()} )))
#1.4525277839857154

print(min(timeit.repeat(lambda: dict(itertools.chain(x.items(), y.items())))))
#2.3143140770262107

print(min(timeit.repeat(lambda: dict((k, v) for d in (x, y) for k, v in d.items()))))
#3.2069112799945287

'''
0.16867379999999998
0.3397424
0.7155157000000001
0.6476766999999999
1.1597363000000005
'''

from collections import ChainMap
from string import ascii_uppercase as up, ascii_lowercase as lo
x = dict(zip(lo, up))
y = dict(zip(up, lo))
chainmap_dict = ChainMap(y, x)
union_dict = dict(x.items() | y.items())
#print('dict(x.items() | y.items()):',min(timeit.repeat(lambda: dict(x.items() | y.items()))))
#dict(x.items() | y.items()): 4.094819599999999

print('ChainMap(y, x):',min(timeit.repeat(lambda:ChainMap(y, x))))

#100000 loops, best of 3: 2.15 µs per loop
#timeit for k in chainmap_dict: chainmap_dict[k]
#10000 loops, best of 3: 27.1 µs per loop


import timeit

def in_(s, other):
    return other in s

def contains(s, other):
    return s.__contains__(other)

def find(s, other):
    return s.find(other) != -1

def index(s, other):
    try:
        s.index(other)
    except ValueError:
        return False
    else:
        return True



perf_dict = {
'in:True': min(timeit.repeat(lambda: in_('superstring', 'str'))),
'in:False': min(timeit.repeat(lambda: in_('superstring', 'not'))),
'__contains__:True': min(timeit.repeat(lambda: contains('superstring', 'str'))),
'__contains__:False': min(timeit.repeat(lambda: contains('superstring', 'not'))),
'find:True': min(timeit.repeat(lambda: find('superstring', 'str'))),
'find:False': min(timeit.repeat(lambda: find('superstring', 'not'))),
'index:True': min(timeit.repeat(lambda: index('superstring', 'str'))),
'index:False': min(timeit.repeat(lambda: index('superstring', 'not'))),
}

print('perf_dict:',perf_dict)

'''
perf_dict: 
{'in:True': 0.14055830000000036, 
'in:False': 0.14288459999999858, 
'__contains__:True': 0.21399359999999845, 
'__contains__:False': 0.20630039999999994, 
'find:True': 0.2552975999999987, 
'find:False': 0.24854670000000212, 
'index:True': 0.28346939999999776, 
'index:False': 0.5126667000000005}
'''

from collections import ChainMap
x = {'a':1, 'b': 2}
y = {'b':10, 'c': 11}
z = dict(ChainMap({}, y, x))
for k, v in z.items():
    print(k, '-->', v)

from itertools import chain
x = {'a':1, 'b': 2}
y = {'b':10, 'c': 11}

'''
dict(chain(x.iteritems(), y.iteritems()))
在Python 3.x 里面，iteritems()方法已经废除了。在3.x里用 items()替换iteritems() ，
可以用于 for 来循环遍历。
'''

dict(chain(x.items(), y.items()))


def deepupdate(original, update):
    """
    Recursively update a dict.
    Subdict's won't be overwritten but also updated.
    """
    for key, value in original.items():
        if key not in update:
            update[key] = value
        elif isinstance(value, dict):
            deepupdate(value, update[key])
    return update
pluto_original = {
    'name': 'Pluto',
    'details': {
        'tail': True,
        'color': 'orange'
    }
}

pluto_update = {
    'name': 'Pluutoo',
    'details': {
        'color': 'blue'
    }
}

print(deepupdate(pluto_original, pluto_update))


'''
我在试图解决一个图相关问题的时候，就有这个疑问。我遇到的问题是我需要定义一个空的邻接列表，
并希望用一个空列表初始化所有的节点，这时我就想不如我检查一下是否足够快，我的意思是是否值得
做一个zip操作而不是简单的赋值键值对。毕竟大多数时候，时间因素是一个重要的破冰因素。
所以我对两种方法都进行了timeit操作。
'''


import timeit
def dictionary_creation(n_nodes):
    dummy_dict = dict()
    for node in range(n_nodes):
        dummy_dict[node] = []
    return dummy_dict


def dictionary_creation_1(n_nodes):
    keys = list(range(n_nodes))
    values = [[] for i in range(n_nodes)]
    graph = dict(zip(keys, values))
    return graph


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

iteration = wrapper(dictionary_creation, n_nodes)
shorthand = wrapper(dictionary_creation_1, n_nodes)

for trail in range(1, 8):
    print(f'Itertion: {timeit.timeit(iteration, number=trails)}\n'
          f'Shorthand: {timeit.timeit(shorthand, number=trails)}')



