'''
https://www.codewars.com/kata/556196a6091a7e7f58000018/train/python

Given a sequence of numbers, find the largest pair sum in the sequence.

For example

[10, 14, 2, 23, 19] -->  42 (= 23 + 19)
[99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
'''

#1st solution by ericlee
def largest_pair_sum(numbers):
    return sum(sorted(numbers)[-2:])


#2nd solution
from heapq import nlargest
def largest_pair_sum(a):
    return sum(nlargest(2, a))