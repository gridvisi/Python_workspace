'''
https://www.codewars.com/kata/5ae64f28d2ee274164000118/train/python
("I like it!",1234),"iitkIl !e "
https://blog.csdn.net/liangguohuan/article/details/7088265

from random import randint
@test.describe("Fixed tests")
def tests():
    Test.assert_equals(string_func("This is a string exemplification!",0),"This is a string exemplification!")

    Test.assert_equals(string_func("String for test: incommensurability",1),"ySttirliinbga rfuosrn etmemsotc:n i")

    Test.assert_equals(string_func("Ohh Man God Damn",7)," nGOnmohaadhMD  ")

    Test.assert_equals(string_func("Ohh Man God Damnn",19),"haG mnad MhO noDn")
'''
s = "I like it!"
s = "String for test: incommensurability"
from collections import deque
def func(s):
    d = deque()
    res = deque()
    for i in s:
        d.append(i)
    while d:
        if len(d) == 1:
            res.append(d.pop())
            break
        res.append(d.pop())
        res.append(d.popleft())
    return ''.join(res)

r = "ySttirliinbga rfuosrn etmemsotc:n i"
c = "ySttirliinbga rfuosrn etmemsotc:n i"

def string_func(s,x):
    while x > 0:
        res = func(s)
        s = res
        x -= 1
    return res

s,x = "Ohh Man God Damn",7
print(string_func(s,x))  #" nGOnmohaadhMD  ")

def flip(s):
    front, tail = [],list(s)
    for i in range(len(s)):
        front,tail = front+[tail[-1]],tail[:len(s)-i-1]
        re,tail = front + tail[::-1],tail[::-1]
    return ''.join(re)

def string_func(s,x):
    if x > 0:
        s = flip(s)
        x -= 1
        return string_func(s,x)
    elif x == 0:return ''.join(s)