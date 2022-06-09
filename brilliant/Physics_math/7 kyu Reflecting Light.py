'''
https://www.codewars.com/kata/5eaf88f92b679f001423cc66/train/python
有两种满足要求的顶点，A'和 D'
x,y的公倍数恰好落在 odd * x 或者 even * x

'''
def reflections(n, m):
    x = y = 0
    dx = dy = 1
    while 1:
        x += dx
        y += dy
        if x == y == 0 or x == n and y == m: return 1
        if 0 in (x, y) and (x == n or y == m): return 0
        if x in (0, n): dx *= -1
        if y in (0, m): dy *= -1


from math import gcd
def reflections(x,y):
    g=gcd(x,y)
    return (x//g+y//g)%2 == 0

import math
def reflections(x, y):
    #bench = x*y/math.gcd(x,y)
    if (max(x,y)/min(x,y))%2 == 1:return True
    bench = [1] + [i for i in range(3,100,4)] + [i for i in range(2,100,4)]
    s = min(x,y)
    print(sorted(bench),s)
    #while bench % (2*i*x) !=0 or bench % ((2*i+1)*x) !=0:
    for i in range(1,1000):
        if (i*y) % x == 0:
            step = (i*y) % x
            if step in bench:
                return True,i,i*y,x,step
    return False
x,y = 12,23
x,y = 5,25
print(reflections(x,y))


# not enough to solve
def reflections(max_x, max_y):
    return (max(max_x,max_y) / min(max_x,max_y)) % 2 == 1

def reflections(max_x, max_y):
    x, y = max_x, max_y
    if max_x == max_y: return True
    #x,y = 0,0
    #x = y = min(x,y)
    #while [x,y] != [0,0] and [x,y] != [X,Y]:
    #while x <= X and y <= Y:
    i = 0
    while (2*i+1)*x % y != 0 and 2*i*x % y != 0:
        i += 1
    return True

