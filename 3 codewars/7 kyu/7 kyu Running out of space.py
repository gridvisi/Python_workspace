'''
https://www.codewars.com/kata/56576f82ab83ee8268000059/solutions/python

import codewars_test as test
import solution # or from solution import example

test.assert_equals(spacey(['kevin', 'has','no','space']), [ 'kevin', 'kevinhas', 'kevinhasno', 'kevinhasnospace'])
test.assert_equals(spacey(['this','cheese','has','no','holes']), ['this','thischeese','thischeesehas','thischeesehasno','thischeesehasnoholes'])

'''

def spacey(array):
    return [''.join(array[:i]) for i in range(1,len(array)+1)]

from itertools import accumulate
def spacey(a):
    return list(accumulate(a))