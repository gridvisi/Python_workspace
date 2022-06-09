'''
https://brilliant.org/daily-problems/circle-fill-12/
'''

## using brute force: x is the '?', y is the bottom circle
import itertools
for x,y in itertools.product(range(1,15), repeat=2):
    if (x*(x-y)*(x+y+3)==42):
        print("x={}".format(x))