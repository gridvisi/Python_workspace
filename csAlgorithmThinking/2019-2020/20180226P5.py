__author__ = 'Administrator'
'''
How many ways can a 2×10 rectangle be filled 1×1 and 2×1 with and tiles?
一个2×10的矩形可以用1×1 and 2×1瓷砖 多少种方式填充和平铺？

One such possible tiling is shown below.
一种可能的瓷砖如下所示。
'''

def f(n):    #f(n) = f(n-1) + f(n-2)+g(n-1)+g(n)

    if n == 0:
        return 1
    if n == 1:
        return 2
    return 2*f(n-1) + f(n-2) + 2*g(n-1)

def g(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return f(n-1) + g(n-1)

print(f(3))
print(f(10))