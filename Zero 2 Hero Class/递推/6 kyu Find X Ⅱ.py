'''
https://www.codewars.com/kata/5d339b01496f8d001054887f/train/python

This kata is the part two version of the Find X kata, if you haven't solved it you should try solving it, it's pretty easy.

In this version you're given the following function

def find_x(n):
      if n == 0: return 0
      x = 0
      for i in range(1, n+1):
            x += find_x(i-1) + 3*i
      return x
Since this computation is exponential, it gets very slow quickly as n increases,
your task is to optimize the function so it works well for large numbers.

find_x(2) #=> 12
find_x(3) #=> 33
find_x(5) #=> 171
'''

# optimize
def find_x(n):
    if n == 0: return 0
    x,sumx = 0,0
    #y = 3
    for i in range(1, n+1):
        sumx += x
        x = 3*i + sumx
        #sumx += x
        #x += find_x(i-1) + 3*i
    return sumx+x
n = 3
print([find_x(n) for n in (9,12,15)]) #[3039, 24534, 196557]
'''
Execution Timed Out
STDERR
Execution Timed Out (12000 ms)
'''
#1st
M = 10 ** 9 + 7
def find_x(n):
    return 3 * (pow(2, n + 1, M) - n - 2) % M
'''
是个质数。其他就没有了。答案太大，mod一个数可以让你不用麻烦的写高精度。

Python中pow()，里面可以有两个或三个参数，它们的意义是完全不同的。
1、pow(x,y):这个是表示x的y次幂。
      >>> pow(2,4)
             16
      >>> 

2、pow(x,y,z)：这个是表示x的y次幂后除以z的余数。
    >>> pow(2,4,5)
           1
    >>>
'''

def find_x(n):
    if n == 0: return 0
    x = 0
    for i in range(1, n + 1):
        x += find_x(i - 1) + 3 * i
    return x
print(find_x(n))