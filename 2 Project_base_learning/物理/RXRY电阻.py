__author__ = 'Administrator'
'''
Parallel connection:20170807intermediatep4
This resistive network forms an infinite binary tree--every branch splits into two new branches, where the new branch that goes to the left has a resistance of , and the one that goes to the right has a resistance of .
Suppose that after going down  levels, all of the branches are connected to a single node, . As  approaches infinity, what will be the equivalent resistance between nodes  and
这个电阻网络形成一个无限的二叉树——每个分支分成两个新的分支，其中左边的新分支具有.
假设在下一级之后，所有分支都连接到一个节点。当接近无穷大时，节点之间的等效电阻是什么？
'''
'''
x = float(input("电阻X的值："))
y = float(input("电阻Y的值："))
counter = input("二叉树的层数：")

class Parallel_R():
    def __init__(self,resistance_x,resistance_y,counter):  # 类包含两个参数
        self.resistance_x = resistance_x
        self.resistance_y = resistance_y
        self.counter = counter

    def Parallel(self):
        if self.counter > 1 :
            cache = self.resistance_x*self.resistance_y/(self.resistance_x+self.resistance_y)   # 1/(1/x + 1/y)
            x = cache + self.resistance_x
            y = cache + self.resistance_y
            self.counter -= 1
            #print('counter',counter,':',X,Y,x,y,cache)
            if self.counter == 1:
            #RR = 1/(1/x + 1/y)*
            #x = RR*(counter-1)+x
            #y = RR*(counter-1)+y
                R = 1/(1/(2+cache) + 1/(2+cache))
                return Parallel(self),R

def Parallel(x,y,counter):
    #global cache
    if counter > 1 :
        cache = x*y/(x+y)   # 1/(1/x + 1/y)
        x = cache + 1
        y = cache + 1
        counter -= 1
        print('counter',counter,':',x,y,cache)
        return Parallel(x,y,counter),cache

print(Parallel(1,1,100))
'''
'''
def Parallel(x,y,i):
    #global cache
    cache = []
    X = x
    Y = y
    cache.append(x*y/(x+y))     # 1/(1/x + 1/y)
    print(cache)
    x = cache[i] + X
    y = cache[i] + Y
    i += 1
    return x,y

i = 0
x = float(input("电阻X的值："))
y = float(input("电阻Y的值："))
counter = int(input("二叉树的层数："))

while counter >= 0:
    Parallel(x,y,i)
    counter -= 1
    print(Parallel(x,y,i))
# x = rx,y = ry
# 错误案例之一：x =2, y = 2  4c层二叉树 R = 17/12  执笔演算
'''
import math
print(math.sqrt(17*13))
'''
import sys
sys.setrecursionlimit(450000)
import sys
class TailRecurseException:
   def __init__(self, args, kwargs):
     self.args = args
     self.kwargs = kwargs

def tail_call_optimized(g):
   def func(*args, **kwargs):
     f = sys._getframe()
     if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
       raise TailRecurseException(args, kwargs)
     else:
       while 1:
         try:
           return g(*args, **kwargs)
         except TailRecurseException, e:
           args = e.args
           kwargs = e.kwargs
   func.__doc__ = g.__doc__
   return func
@tail_call_optimized
'''

def Parallel(x, y, counter, a, b):
    # global cache
    global cache
    if counter > 1:
        cache = x * y / (x + y)  # 1/(1/x + 1/y)
        x = cache + a
        y = cache + b
        counter -= 1
        print('counter', counter, ':', x, y, cache)
        return Parallel(x, y, counter, a, b), cache
x = int(input("电阻X的值："))
y = int(input("电阻Y的值："))
a = x
b = y
counter = int(input("二叉树的层数："))
Parallel(x, y, counter, a, b)
print("R =", cache)
import math
print(math.sqrt(1*2))
'''
# 题目：定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0 的两个解
import math
def quadratic(a,b,c):
    if not (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float))):
        raise TypeError('a,b,c只能为数字')
    if a==0:
        return '请输入不等于0的a值'
    else:
        d=b*b-4*a*c
        if d<0:
            return '无实根'
        elif d==0:
            x=-b/(2*a)
            return x
        else:
            x1=(-b+math.sqrt(d))/(2*a)
            x2=(-b-math.sqrt(d))/(2*a)
            return x1,x2
#测试
print(quadratic(1,2,1))
print(quadratic(1,1,1))
print(quadratic(1,3,1))

# R**2 + (RX + RY - 2RX*RY)*R - RX*RY = 0  a = 1,b = RX + RY - 2RX*RY,c = - RX*RY
print(quadratic(1,RX + RY - 2RX*RY,- RX*RY))
'''