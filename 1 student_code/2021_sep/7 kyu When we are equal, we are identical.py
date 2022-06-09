'''
https://www.codewars.com/kata/60c47b07f24d000019f722a2/train/python

在Python中，==测试的是相等，而is测试的是相同。两个相等的字符串也可能是相同的，但这并不保证，
而是一个实现细节。给定一个计算的表达式，通过完成make_identical函数来确保它与相应的相等的字
符串字面是相同的。请看测试案例以了解清楚。(注意，如果你知道这个概念，这很容易）。)

import codewars_test as test
from solution import make_identical

@test.describe("Basic tests")
def _():
    @test.it("Example Test")
    def _():
        test.assert_equals("abc" is make_identical("abcd"[:-1]), True)
'''

#1st
from sys import intern as make_identical
print('abc' == 'abcd'[:-1])
print('1st make_identical:','abc' is make_identical('abcd'[:-1]))

#2nd
make_identical = __import__('sys').intern
print('abc' == 'abcd'[:-1])
print('2nd make_identical:','abc' is make_identical('abcd'[:-1]))


#3rd
def make_identical(strng):
    return eval(f'"{strng}"')
print('abc' == 'abcd'[:-1])
print('3rd make_identical:','abc' is make_identical('abcd'[:-1]))

#4
def make_identical(strng):
    # Code here
    if strng is strng:
        return eval(repr(strng))

print('abc' == 'abcd'[:-1])
print('4th make_identical:','abc' is make_identical('abcd'[:-1]))

#NOT good!!!
#tran = eval(f"{'abcd'[:-1]}")
#print('abc' is tran)


print(id('abc'),id('abcd'[:-1]))

# 2039381927408 2039384603120

#out = 'abcd'[::-1]
#print('abc' is out)



print(['a','b','c'] == ['a','b','c','d'][:-1])
print(['a','b','c'] is ['a','b','c','d'][:-1])

def make_identical(strng):
    # Code here
    pass


print('#'*100)
import copy

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = copy.copy(a)
    c = copy.deepcopy(a)
    print(a == b)
    print(a is b)
    print(a == c)
    print(a is c)
    print([id(i) for i in (a,b,c)])