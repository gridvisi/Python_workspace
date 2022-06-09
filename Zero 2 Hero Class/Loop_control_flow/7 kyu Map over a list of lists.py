#https://www.codewars.com/kata/606b43f4adea6e00425dff42/train/python
'''
x = [[1,2,3],
     [4,5,6]]

grid_map(x, lambda x: x + 1)
-- returns [[2,3,4],[5,6,7]]

grid_map(x, lambda x: x ** 2)
-- returns [[1,4,9],[16,25,36]]
Example 2

x = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]
grid_map(x, lambda x: x.upper())
-- returns [['H', 'E', 'L', 'L', 'O'], ['W', 'O', 'R', 'L', 'D']]
'''
def grid_map(inp, op):
    return [list(map(op,i)) for i in inp]

inp = [[1,2,3],
     [4,5,6]]
op = lambda x: x + 1
print(grid_map(inp,op))

#1st
def grid_map(lst, op):
    return [[*map(op,x)] for x in lst]