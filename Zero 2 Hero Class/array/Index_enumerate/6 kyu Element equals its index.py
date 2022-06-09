'''
https://www.codewars.com/kata/5b7176768adeae9bc9000056/train/python

Given a sorted array of distinct integers, write a function index_equals_value that
returns the lowest index for which array[index] == index.
Return -1 if there is no such index.

Your algorithm should be very performant.

[input] array of integers ( with 0-based nonnegative indexing )
[output] integer

Examples:
input: [-8,0,2,5]
output: 2 # since array[2] == 2

input: [-1,0,3,6]
output: -1 # since no index in array satisfies array[index] == index
Random Tests Constraints:
Array length: 200 000

Amount of tests: 1 000

Time limit: 1.5 s
'''
#1st
def index_equals_value(arr):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + hi >> 1
        if arr[mid] >= mid:
            hi = mid
        else:
            lo = mid + 1
    return lo if lo < len(arr) and arr[lo] == lo else -1


def index_equals_value(arr):
    ie = [(i,e) for i,e in enumerate(arr)]
    return ie
arr = (-3,0,1,3,10)
print(index_equals_value(arr))


#Not success try
def index_equals_value(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return arr[i]
    return -1
'''
Test Results:
Fixed Tests
Small array
Array with multiple matches
Completed in 0.05ms
Edge Cases
No match
One Element Array
Completed in 0.03ms
Random Test
Exceeded time limit of 1.500 seconds
Completed in 1714.87ms
'''
#Not success try
def index_equals_value(arr):
    for i,e in enumerate(arr):
        if i == e:
            return e
    return -1
'''
Test Results:
Fixed Tests
Small array
Array with multiple matches
Completed in 0.05ms
Edge Cases
No match
One Element Array
Completed in 0.03ms
Random Test
Exceeded time limit of 1.500 seconds
Completed in 1688.88ms

'''
# Not success try
def index_equals_value(arr):
    return [i for i,e in enumerate(arr) if i==e][0]
'''
Fixed Tests
Small array
-1 should equal 3
Completed in 0.01ms
Array with multiple matches
-1 should equal 1
Completed in 0.01ms
Completed in 0.09ms
Edge Cases
No match
One Element Array
Completed in 0.03ms
Random Test
Exceeded time limit of 1.500 seconds
Completed in 1694.73ms
'''

