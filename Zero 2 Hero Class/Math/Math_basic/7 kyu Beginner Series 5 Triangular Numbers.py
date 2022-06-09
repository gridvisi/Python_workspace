'''
https://www.codewars.com/kata/56d0a591c6c8b466ca00118b/train/python

Triangular number is the amount of points that can fill equilateral triangle.

Example: the number 6 is a triangular number because all sides of a triangle
has the same amount of points.

alt text

Hint!
T(n) = n * (n + 1) / 2,
n - is the size of one side.
T(n) - is the triangular number.
Given a number 'T' from interval [1; 2147483646], find if it is triangular number or not.
三角形数是指能填满等边三角形的点的数量。

例：数字6是一个三角形数，因为三角形的所有边都有相同的点数。

alt text

提示!
T(n) = n * (n + 1) / 2,
n--是一边的大小。
T(n)--是三角形数。
给定区间[1；2147483646]中的一个数'T'，求它是否是三角形数。
    *  *  *
   *  *  *
  *  *  *

Appreciate the feedback!
'''
import math
def is_triangular(t):
    root = int(math.sqrt(2*t))
    return root*(root+1) == 2*t
t = 10
print(is_triangular(t))

#2nd
def is_triangular(t):
    x = int((t*2)**0.5)
    return t == x*(x+1)/2