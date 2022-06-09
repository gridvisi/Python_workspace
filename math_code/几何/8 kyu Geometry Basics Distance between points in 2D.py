'''
https://www.codewars.com/kata/58dced7b702b805b200000be/train/python
'''

from math import hypot

def distance_between_points(a, b):
    return hypot(a.x - b.x, a.y - b.y)

def distance_between_points(a, b):
    return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** 0.5

class D:
  def __init__(self, a, b):
    self.x = a.x - b.x
    self.y = a.y - b.y
    self.d = (self.x ** 2 + self.y ** 2) ** .5
distance_between_points = lambda a, b: D(a, b).d

from itertools import starmap
from math import hypot
from operator import sub

Point.__iter__ = lambda self: iter((self.x, self.y))
def distance_between_points(a, b):
    return hypot(*starmap(sub, zip(a, b)))