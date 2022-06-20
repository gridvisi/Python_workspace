'''
https://www.codewars.com/kata/lazy-repeater/solutions?show-solutions=1

门诊排队叫号系统设计
Design of "line up to call the number" system of the outpatien
ITERTOOLS模块小结: https://www.jianshu.com/p/73b17486ef8c

def make_looper(customer):
    def generator():
        while True:
            for char in customer:
                yield char
    return generator().next
line = make_looper(customer)

'''
import itertools
from itertools import cycle
from itertools import *

customer = [1,2,3,4,5,6,7,8]
g = iter(customer)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print('*'*30)

customer = (1,2,3,4,5,6,7,8)
def make_looper(customer):
    #it = iter(customer)
    g = itertools.cycle(customer)
    return lambda: next(g)
print(make_looper(customer))
print(make_looper(customer))
print(make_looper(customer))

print('*'*30)

from itertools import cycle
class make_looper(cycle):
    def __call__(self):
        return self.__next__()

#print(line)
print(make_looper(customer))
print(make_looper(customer))
print(make_looper(customer))
print(make_looper(customer))


from itertools import cycle
def make_looper(string):
    return cycle(string).__next__
string = ['apple','banana','carrot']
string = [i for i in range(7)]
line = make_looper(string)

print(line)
print(make_looper(string))
print(make_looper(string))
print(make_looper(string))
print(make_looper(string))

print('*'*30)

customer = 8
def make_looper(customer):
    g = cycle(customer)
    yield next(g) #return next(g)
line = make_looper(customer)

print(line)
print(make_looper(customer))
print(make_looper(customer))

print('*'*30)

def line_up_call(n):
    i = 0
    while i <= n:
        yield i
        i += 1
line = line_up_call(8)
print(next(line))
print(next(line))
print(next(line))
print(next(line))