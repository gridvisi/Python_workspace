'''
https://www.codewars.com/kata/5afd81d0de4c7f45f4000239/train/python

Given a list of integers (possibly including duplicates) and a positive integer k (> 0),
find the minimum and maximum possible product of k elements taken from the list.

If you cannot take enough elements from the list (k > list size), return None/nil.

Examples
numbers = [1, -2, -3, 4, 6, 7]

k = 1  ==>  -3, 7
k = 2  ==>  -21, 42    # -3*7, 6*7
k = 3  ==>  -126, 168  # -3*6*7, 4*6*7
k = 7  ==>  None       # there are only 6 elements in the list
Note: the test lists are sufficiently small (up to 20 elements) for a simple approach.

arr = [1, -2, -3, 4, 6, 7]

# k = 1: -3, 7
Test.assert_equals(find_min_max_product(arr, 1), (-3, 7))

# k = 2: -3 * 7 = -21, 6 * 7 = 42
Test.assert_equals(find_min_max_product(arr, 2), (-21, 42))

# k = 3: -3 * 6 * 7 = -126, 4 * 6 * 7 = 168
Test.assert_equals(find_min_max_product(arr, 3), (-126, 168))

# k = 7: None (there are only 6 elements in the array)
Test.assert_equals(find_min_max_product(arr, 7), None)
'''

from functools import reduce
from itertools import combinations
from operator import mul

def find_min_max_product(arr, k):
    if k <= len(arr):
        prods = [ reduce(mul, nums) for nums in combinations(arr, k) ]
        return min(prods), max(prods)