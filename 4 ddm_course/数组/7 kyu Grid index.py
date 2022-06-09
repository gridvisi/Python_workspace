'''
https://www.codewars.com/kata/5f5802bf4c2cc4001a6f859e/train/python

[['m', 'y', 'e'],
 ['x', 'a', 'm'],
 ['p', 'l', 'e']]

 [1, 3, 5, 8]

 [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

 'meal'
'''
from numpy import *
grid = [['h', 'e', 'l', 'l'], ['o', 'c', 'o', 'd'], ['e', 'w', 'a', 'r'], ['r', 'i', 'o', 'r']]
indexes = [5, 7, 9, 3, 6, 6, 8, 8, 16, 13]
a = array(grid)
a.flatten()
print(a)
def grid_index(grid, indexes):
    a = array(grid)
    print(a.flatten())
    return ''.join([e for i,e in enumerate(a.flatten()) if i+1 in indexes])

def grid_index(grid, indexes):
    a = array(grid)
    print(a.flatten())
    return ''.join([a.flatten()[i-1] for i in indexes])
print(grid_index(grid, indexes))

grid = [['m', 'y', 'e'],
        ['x', 'a', 'm'],
        ['p', 'l', 'e']]
indexes = [1, 3, 5, 8]
print(grid_index(grid, indexes))

#1st solution
def grid_index(grid, indexes):
    flat = sum(grid, [])
    return "".join( flat[i-1] for i in indexes )

#2nd solution
def grid_index(grid, indexes):
    flat = sum(grid, [''])
    return ''.join(flat[i] for i in indexes)

def grid_index(grid, indexes):
    flat = tuple(x for e in grid for x in e)
    return ''.join(flat[e-1] for e in indexes)