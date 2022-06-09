'''
https://www.codewars.com/kata/586beb5ba44cfc44ed0006c3/train/python

Write a function named sumEvenNumbers, taking a sequence of numbers as single parameter.
Your function must return the sum of the even values of this sequence.

Only numbers without decimals like 4 or 4.0 can be even.

Input
sequence of numbers: those numbers could be integers and/or floats.
For example, considering this input value : [4,3,1,2,5,10,6,7,9,8], then your function
should return 30 (because 4 + 2 + 10 + 6 + 8 = 30).

@test.describe("Simple integers input.")
def example_tests():
    test.assert_equals(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
    test.assert_equals(sum_even_numbers([]), 0)
'''

#1st solution by ericlee
def sum_even_numbers(seq):
    return sum([n for n in seq if not n%2])