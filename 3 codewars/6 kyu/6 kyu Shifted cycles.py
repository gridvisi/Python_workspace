'''
https://www.codewars.com/kata/shifted-cycles/train/python
'''

import itertools
from itertools import cycle
n = 3
iterable = [i for i in range(5)]
def gen(n, iterable):
    iter, r = cycle(iterable), ()

    while True:
        while len(r) < n:
            r += (next(iter),)
        yield r
        r = r[1:]
print(gen(n, iterable))

from itertools import cycle, islice, tee

def gen(n, iterable):
    iterators = tee(cycle(iterable), n)
    for i, it in enumerate(iterators):
        list(islice(it, i))
    return list(zip(*iterators))


print(gen(n, iterable))
'''
def gen(n, iterable):
    count = 0
    res = []
    for item in cycle(iterable):
        if count > 100:
            break
        res.append(item)
        count += 1
    return res
print(gen(n, iterable))

def gen(n, iterable):
    res = []
    for item in zip(start,cycle(iterable)):
        #res.append(iterable[0:n])
        res.append((item))
    return res
print(gen(n, iterable))
'''