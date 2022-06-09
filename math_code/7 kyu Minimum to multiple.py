'''

https://www.codewars.com/kata/5e030f77cec18900322c535d/train/python

Given two integers a and x, return the minimum non-negative number to add to / subtract from a to make it a multiple of x.

minimum(10, 6)  #= 2
10+2 = 12 which is a multiple of 6
Note:
0 is always a multiple of x
Constraints
1 <= a <= 106
1 <= x <= 105

FUNDAMENTALSNUMBERS
'''

def minimum(a, x):
    return x - a % x if (x-a%x) < a%x else a % x

#1st solution
def minimum(a, x):
    return min(a % x, -a % x)

