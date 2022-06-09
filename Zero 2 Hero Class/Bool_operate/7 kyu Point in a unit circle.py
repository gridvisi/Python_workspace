'''
https://www.codewars.com/kata/58da7ae9b340a2440500009c/solutions/python
'''

def point_in_circle(x, y):
    return (x*x + y*y) < 1

point_in_circle=lambda*I:sum(i*i for i in I)<1

import math

def point_in_circle(x, y):
    return math.hypot(x, y) < 1