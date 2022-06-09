'''
https://www.codewars.com/kata/5729c30961cecadc4f001878/train/python

Write a function that takes one or more arrays and returns a new array of unique values
in the order of the original provided arrays.

In other words, all values present from all arrays should be included in their original
order, but with no duplicates in the final array.

The unique numbers should be sorted by their original order, but the final array should
not be sorted in numerical order.

Check the assertion tests for examples.

Courtesy of FreeCodeCamp, a great place to learn web-dev; plus, its founder Quincy
Larson is pretty cool and amicable. I made the original one slightly more tricky ;)

Test.describe("Basic tests")
Test.assert_equals(unite_unique([1, 2], [3, 4]),[1, 2, 3, 4])
Test.assert_equals(unite_unique([1, 3, 2], [5, 2, 1, 4], [2, 1]),[1, 3, 2, 5, 4])
Test.assert_equals(unite_unique([4, 3, 2, 2]),[4, 3, 2])
Test.assert_equals(unite_unique([4, "a", 2], []),[4, "a", 2])
Test.assert_equals(unite_unique([], [4, "a", 2]),[4, "a", 2])
Test.assert_equals(unite_unique([], [4, "a", 2], []),[4, "a", 2])
Test.assert_equals(unite_unique([]),[])
Test.assert_equals(unite_unique([],[]),[])
Test.assert_equals(unite_unique([],[1, 2]),[1, 2])
Test.assert_equals(unite_unique([],[1, 2, 1, 2],[2, 1, 1, 2, 1]),[1, 2])

编写一个函数，接受一个或多个数组，并按照原来提供的数组的顺序返回一个
新的唯一值数组。

换句话说，所有数组中的所有值都应该按照原来的顺序被包含，但最终数组中
没有重复的值。

唯一的数字应该按照它们的原始顺序排序，但最后的数组不应该按照数字顺序
排序。

检查断言测试的例子。

由FreeCodeCamp提供，这是一个学习web-dev的好地方；另外，
它的创始人Quincy Larson相当酷，而且很和蔼。我把原来的那个稍稍做得
更棘手了;)
'''

def unite_unique(*args):
    init =[]
    for x in args:
        init.extend([i for i in x if i not in init])
    return sorted(set(init),key=init.index)  #sorted(init),set(init)

print(unite_unique([],[1, 2, 1, 2],[2, 1, 1, 2, 1]))
print(unite_unique([1, 3, 2], [5, 2, 1, 4], [2, 1]))
#print(sum([[1,2],[1, 2, 1, 2]],[2, 1, 1, 2, 1]))
'''
def unite_unique(*args):
    init = set()
    for x in args:
        print(init,set(x),init|set(x),x)
        init |= set(x)
    return init,sorted(init),set(init)
'''

#1st

def unite_unique(*arg):
    res = []
    for arr in arg:
        for val in arr:
            if not val in res: res.append(val)
    return res

from itertools import chain
def unite_unique(*args):
    return list(dict.fromkeys(chain.from_iterable(args)))


def unite_unique(*args):
    return list({x:'' for arg in args for x in arg}.keys())

#2nd
from collections import OrderedDict
def unite_unique(*xss):
    return list(OrderedDict.fromkeys(x for xs in xss for x in xs))

#3rd
from collections import OrderedDict
from itertools import chain

def unite_unique(*args):
    return OrderedDict.fromkeys(chain.from_iterable(args)).keys()

#4th
from itertools import chain
def unite_unique(*arrs):
    r = list()

    for item in chain(*arrs):
        if item not in r:
            r.append(item)
    return r
from collections import OrderedDict
from itertools import chain


def unite_unique(*arrs):
    return OrderedDict((n, None) for n in chain(*arrs)).keys()
#5th
def unite_unique(*arrays):
    output = []
    for arr in arrays:
        for i in arr:
            if i not in output: output.append(i)
    return output

#6th
from itertools import chain

def unite_unique(*lists):
    cache = set()
    result = list()
    for elem in chain(*lists):
        if elem not in cache:
            result.append(elem)
        cache.add(elem)
    return result

#7th
def unite_unique(*args):
    init =[]
    for x in args:
        init.extend([i for i in x if i not in init])
    return sorted(set(init),key=init.index)

#8th
def unite_unique(*inp):
    a = []
    for i in inp:
        for c in i:
            if c not in a:
                a.append(c)
    return a

