'''
https://www.codewars.com/kata/5b64334ab1788374fb0000c8/train/python

明
这个卡塔的目的是找到一种方法，在返回语句之后做一些操作。

你的任务
你需要首先和最后调用两个函数。你必须在你的函数中按这个顺序调用它们。

问题是，你的函数必须返回第一个函数所返回的内容。

另外，你不能在你的函数中声明任何变量。

Bug函数控制流程基本语言特征基础知识
'''
#not good
def solution(first,last):
    ''' Find a way to make this work without declaring any variables'''
    def s(last):
        return first
    return last + s(last)
first ,last = 1,2
print(solution(first,last))


#1st
def solution(first, last):
    return (first(), last())[0]


#2nd
def solution(first, last):
    try:
        return first()
    finally:
        last()

#3rd

def solution(*fs):
    return [f() for f in fs][0]


#4th
def solution(first,last):
    def f():
        setattr(f,'f',first())
    f()
    last()
    return f.f

#5th
def solution(first, last):
    class A:
        def __call__(self, a, b):
            return a
    return A()(first(), last())

def inner(x, f):
    f()
    return x

def solution(first, last):
    return inner(first(), last)