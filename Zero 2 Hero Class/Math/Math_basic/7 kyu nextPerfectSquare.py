'''
https://www.codewars.com/kata/599f403119afacf9f1000051/train/python
Write a function name nextPerfectSquare / next_perfect_square that returns the first perfect square that is greater than its integer argument. A perfect square is a integer that is equal to some integer squared. For example 16 is a perfect square because 16=4*4.

example

n   next perfect square

6    9
36   49
0    1
-5   0
'''

import math
def next_perfect_square(n):
    return math.ceil(math.sqrt(n + 1)) ** 2 if n >= 0 else 0
n = 36
print(next_perfect_square(n))

#1st
def next_perfect_square(n):
    return n>=0 and (int(n**0.5)+1)**2

