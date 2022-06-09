'''
https://www.codewars.com/kata/57b71a89b69bfc92c7000170/train/python

Write a function getNumberOfSquares (C, F#, Haskell) / get_number_of_squares
(Python, Ruby) that will return how many integer (starting from 1, 2...)
numbers raised to power of 2 and then summed up are less than some number given as a parameter.

E.g 1: For n = 6 result should be 2 because 1^2 + 2^2 = 1 + 4 = 5 and 5 < 6 E.g 2:
For n = 15 result should be 3 because 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14 and 14 < 15

FUNDAMENTALSNUMBERS
'''

#17th solve by ericlee
def get_number_of_squares(n):
    i = 0
    s = 0
    while s < n:  #18和19的次序不同，结果不同，同学们多感受！！！
        i += 1
        s += i**2
    return i-1
n = 15
print(get_number_of_squares(n))