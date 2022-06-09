'''
https://www.codewars.com/kata/56d344c7fd3a52566700124b/train/python

Write a function that adds from two invocations.

All inputs will be integers.
编写一个函数，从两个调用中进行加法。

所有的输入将是整数。
'''


add=lambda a:lambda b:a+b


def add(a):
    def number(x):
        return a+x
    return number

class add(int):
    '''
    This works for infinite calls.
    e.g. add(1)(2)(3)(4)(5)(6)(7)(8)(9)(10) --> 55
    '''
    def __call__(self, other):
        return add(self + other)

add=lambda a:a.__add__


class add(int):
    '''
    This works for infinite calls.
    e.g. add(1)(2)(3)(4)(5)(6)(7)(8)(9)(10) --> 55
    '''
    def __call__(self, value):
        return add(self + value)


class add:
    def __init__(self, num):
        self.total = num

    def __call__(self, num):
        return self.total + num

def add(n):
    return n.__add__