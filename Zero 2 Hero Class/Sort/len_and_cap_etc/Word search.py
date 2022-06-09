'''
https://www.codewars.com/kata/5f05e334a0a6950011e72a3a/train/python

You are given a word target and list of sorted(by length(increasing), number of upper case letters(decreasing), natural order) unique words words which always contains target, your task is to find the index(0 based) of target in words,which would always be in the list.

Examples:
words = ['JaCk', 'Jack', 'jack', 'jackk', 'COdewars', 'codeWars', 'abcdefgh', 'codewarsss']
'''
#(list is sorted by length(small to big), then by number of uppercase letters(maximum to minimum)
# and then by natural order)
'''
target = 'codewars'
#result should be 7

#Another example:
words = ['cP', 'rE', 'sZ', 'am', 'bt', 'ev', 'hq', 'rx', 'yi', 'akC', 'nrcVpx', 'iKMVqsj']
target = 'akC'
#result should be 9
Constraints:
python
4 < len(words) <= 200000
1 < len(search) <= 10
Number of random tests are around 6000.
Reference solution passes in 8s.
Javascript
Your solution must pass in lss than ref.solution-10ms speed.
This is because generating long list of unique words in js is slow.
If you think you've got an correct approach and timing test is not passing then submit again.

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(index_of(['JaCk', 'Jack', 'jack', 'jackk', 'COdewars', 'codeWars', 'abcdefgh', 'codewars', 'codewarsss'], 'codewars'), 7)
    test.assert_equals(index_of(['cP', 'rE', 'sZ', 'am', 'bt', 'ev', 'hq', 'rx', 'yi', 'akC', 'nrcVpx', 'iKMVqsj'], 'akC'), 9)
'''
def index_of(words, target):
    words = [w for w in words if len(w) <= len(target)]
    return sorted(words,key=len).index(target)
'''
Example Tests
Test Passed
Test Passed
Completed in 0.04ms
random tests
Small random tests for verifying solution (349 of 349 Assertions)
STDERR
Execution Timed Out (12000 ms)
'''
#sorted(lendict,key=lambda x:lendict.values()) sorted(words,key=len).index(target)
words, target = ['JaCk', 'Jack', 'jack', 'jackk', 'COdewars', 'codeWars', 'abcdefgh', 'codewars', 'codewarsss'], 'codewars'
print(index_of(words, target))


def index_of(words, target):
    words = [w for w in words if len(w) <= target]
    return sorted(words,key=len).index(target)
'''
Test Results:
Example Tests
Test Passed
Test Passed
Completed in 0.02ms
random tests
Small random tests for verifying solution (349 of 349 Assertions)
STDERR
Execution Timed Out (12000 ms)
'''

#1st
def keyer(w): return (len(w), -sum(map(str.isupper, w)), w)


w = ['ABC','Abc']
print('keyer',keyer(w))


def index_of(words, target):
    def cmp(i, base=keyer(target)):
        o = keyer(words[i])
        print('o:',o,words[i],base,(o > base) - (o < base))
        return (o > base) - (o < base)

    l, h = 0, len(words)
    while l < h:
        m = h + l >> 1
        v = cmp(m)
        if not v: return m
        if v < 0:
            l = m
        else:
            h = m
w, target = ['JaCk', 'Jack', 'jack', 'jackk', 'COdewars', 'codeWars', 'abcdefgh',
             'codewars', 'codewarsss'], 'codewars'
print(index_of(w,target))
#2
from bisect import bisect_left

class OrderedStr:
    def __init__(self, s):
        self.key = (len(s), -sum(map(str.isupper, s)), s)
        print(self.key)
    def __gt__(self, other):
        return self.key > OrderedStr(other).key

def index_of(words, target):
    #print( bisect_left(words, OrderedStr(target)))
    return bisect_left(words, OrderedStr(target))

w, target = ['JaCk', 'Jack', 'jack', 'jackk', 'COdewars', 'codeWars', 'abcdefgh',
             'codewars', 'codewarsss'], 'codewars'
print(index_of(w,target))


# TESTING sorted
a = [3, -1, 'aBc']
b = [3, 0, 'abc']
c = [3, -3,'ABC']

print(sorted([a,b,c]))

a =  'aBc'
b = 'abc'
c = 'ABC'

print(sorted([a,b,c]))
'''
bisect 模块

Python 有一个 bisect 模块，用于维护有序列表。bisect 模块实现了一个算法用于插入元素到有序列表。
在一些情况下，这比反复排序列表或构造一个大的列表再排序的效率更高。

Bisect 是二分法的意思，这里使用二分法来排序，它会将一个元素插入到一个有序列表的合适位置，这使得不需
要每次调用 sort 的方式维护有序列表。

Bisect模块提供的函数有：

bisect.bisect_left(a,x, lo=0, hi=len(a)) :

查找在有序列表 a 中插入 x 的index。
lo 和 hi 用于指定列表的区间，默认是使用整个列表。
如果 x 已经存在，在其左边“模拟”插入（不进行实际的插入！！！），返回值为 index。

bisect.bisect_right(a,x, lo=0, hi=len(a))
bisect.bisect(a, x,lo=0, hi=len(a)) ：
这2个函数和 bisect_left 类似，但如果 x 已经存在，在其右边插入。
bisect.insort_left(a,x, lo=0, hi=len(a)) ：
在有序列表 a 中插入 x。和 a.insert(bisect.bisect_left(a,x, lo, hi), x) 的效果相同。
bisect.insort_right(a,x, lo=0, hi=len(a))
bisect.insort(a, x,lo=0, hi=len(a)) :

和 insort_left 类似，但如果 x 已经存在，在其右边插入。
Bisect 模块提供的函数可以分两类： 
bisect* 只用于查找 index， 不进行实际的插入；
而 insort* 则用于实际插入。

该模块比较典型的应用是计算分数等级：

'''

import bisect
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

# -》['F', 'A', 'C', 'C', 'B', 'A', 'A']
sl = [2,46,3,6,123,45,95,4,34,62,22,46]
n = 123
print(sorted(sl).index(n))
print(bisect.bisect(sl,n))