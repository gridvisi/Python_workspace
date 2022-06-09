'''
https://www.codewars.com/kata/sum-of-cubes/python
Write a function that takes a positive integer n, sums all the cubed
values from 1 to n, and returns that sum.

Assume that the input n will always be a positive integer.
Examples:
sum_cubes(2)
> 9
# sum of the cubes of 1 and 2 is 1 + 8
FUNDAMENTALSCONTROL FLOWBASIC LANGUAGE FEATURES
'''

def sum_cubes(n):
    s = 0
    for i in range(n+1):
        s += i*i*i
    return s
n = 4
print(sum_cubes(n))

def sum_cubes(n):
    return (n*(n+1)/2)**2
