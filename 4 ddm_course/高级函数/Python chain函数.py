'''
https://blog.csdn.net/u013300049/article/details/79313979
https://blog.csdn.net/y472360651/article/details/78387815
'''

import itertools
from itertools import chain
def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element

x = itertools.cycle('ABC')
print(list(itertools.islice(x, 0, 10, 1)))

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)

listone = ['a','b','c']
listtwo = ['11','22','abc']
for item in itertools.chain(listone,listtwo):
    print(item)

import itertools

listone = ['a', 'b', 'c']
listtwo = ['11', '22', 'abc']


for item in itertools.islice("abcdefg", 0, 5, 2):
    print(item)

'''
for item in itertools.cycle(listone):
    step = 10
    while step > 0:
        step -= 1
        print(item)
'''
