'''

Difficulty Level : Basic
Last Updated : 13 Nov, 2018
range() : Python range function generates a list of numbers
which are generally used in many situation for iteration as
in for loop or in many other cases.

In python range objects are not iterators. range is a class
of a list of immutable objects. The iteration behavior of
range is similar to iteration behavior of list in list and
range we can not directly call next function. We can call
next if we get an iterator using iter.

难度等级：基本
最后更新：2018年11月13日
range()：Python range函数生成一个数字列表，通常在许多情况下用于迭代，
如for循环或许多其他情况。在Python中，range对象不是迭代器。range是一
个不可改变的对象的列表类。range 的迭代行为类似于 list 的迭代行为，在
list 和 range 中我们不能直接调用 next 函数。如果我们使用 iter 得到
一个迭代器，我们可以调用 next。
'''

id = range(10)
#print(next(id))
#TypeError: 'range' object is not an iterator

it = iter(id)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Python program to understand range
# this creates a list of 0 to 5
# integers

demo = range(6)

# print the demo
print(demo)

# it will generate error
#print(next(demo))

# Python program to understand range

# creates an iterator
demo = iter(range(6))

# print iterator
print(demo)

# use next
print(next(demo))

# Python program to understand range

# creates a demo range
demo = range(1, 31, 2)

# print the range
print(demo)

# print the start of range
print(demo.start)

# print step of range
print(demo.step)

# print the index of element 23
print(demo.index(23))

# since 30 is not present it will give error
print(demo.index(29))