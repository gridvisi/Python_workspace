'''
https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python

Challenge:

Given a two-dimensional array of integers, return the flattened version of the array
with all the integers in the sorted (ascending) order.

Example:

Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return
[1, 2, 3, 4, 5, 6, 7, 8, 9].

FUNDAMENTALSARRAYSSORTINGALGORITHMSLAMBDASFUNCTIONAL PROGRAMMINGFUNCTIONSDECLARATIVE
PROGRAMMINGCONTROL FLOWBASIC LANGUAGE FEATURES

Test.it("should work for some simple example test cases")
test.assert_equals(flatten_and_sort([]), [])
test.assert_equals(flatten_and_sort([[], [1]]), [1])
test.assert_equals(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
test.assert_equals(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]), [1, 2, 3, 4, 5, 6, 100])
'''

# NOT workable code!!!
def flatten_and_sort(array):
    arr = []
    return [arr.extend(a) for a in array]
array = [[1, 3, 5], [100,1], [2, 4, 6]]

print(flatten_and_sort(array))

def flatten_and_sort(array):
    arr = []
    for sl in array:
        arr.extend(sl)
    return sorted(arr)

array = [[1, 3, 5], [100,1], [2, 4, 6]]
array = [[1,2,3],[1]]

#print(max(array))
print(flatten_and_sort(array))

#1st
from itertools import chain
def flatten_and_sort(array):
    return sorted((chain(*array)))

#2nd
def flatten_and_sort(array):
    return sorted([j for i in array for j in i])

#3rd
def flatten_and_sort(array):
    return sorted(sum(array, []))

#4th
def flatten_and_sort(array):
    newList = []
    for item in array:
        newList += item
    return sorted(newList)