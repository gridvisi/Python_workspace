__author__ = 'Administrator'
import math

print(math.sqrt(144444))
x = 4
y = 1

def time(i):

    m = 4*10**(i-1)
    return m
i = 10
while True:
    i = 10
    if i > 0:
        a = time(i-1)
        b = time(i-2)
        a,b = b,a+b
        i -= 1
    print(b)
    break
