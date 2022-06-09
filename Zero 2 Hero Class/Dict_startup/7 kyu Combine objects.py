'''
https://www.codewars.com/kata/56bd9e4b0d0b64eaf5000819/train/python
'''
objA = { 'a': 10, 'b': 20, 'c': 30 }
objB = { 'a': 3, 'c': 6, 'd': 3 }

def combine(*bs):
    c = {}
    for b in bs:
        for k, v in b.items():
            c[k] = v + c.get(k, 0)
    return c

#2nd
from collections import Counter
def combine(*args):
    return sum((Counter(a) for a in args), Counter())
print(combine({'a': 10, 'b': 20, 'c': 30},{'a': 3, 'c': 6, 'd': 3}))

keys = ['a','b','c']
values = [2,3,4]
print(Counter({'a': 10, 'b': 20, 'c': 30}))
#print(sum(('a','b','c'),))
#3rd
from collections import defaultdict
def combine(*dicts):
    ret = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            ret[k] += v
    return dict(ret)