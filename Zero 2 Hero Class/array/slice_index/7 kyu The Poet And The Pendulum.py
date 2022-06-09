# https://www.codewars.com/kata/5bd776533a7e2720c40000e5/train/python
#17th by eric
def pendulum(values):
    vsort = sorted(values)
    left,right = vsort[::2][::-1],vsort[1::2]
    return left + right

values = [1,2,3,4,5]
print(pendulum(values))
#1st
def pendulum(a):
    a = sorted(a)
    return a[::2][::-1] + a[1::2]


#2nd
from collections import deque
def pendulum(values):
    x = deque()
    v = sorted(values)
    for i, n in enumerate(v):
        x.append(n) if i%2 else x.appendleft(n)
    return list(x)