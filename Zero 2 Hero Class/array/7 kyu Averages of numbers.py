'''
https://www.codewars.com/kata/57d2807295497e652b000139/train/python

Get the averages of these numbers

Write a method, that gets an array of integer-numbers and return an array of the averages of each integer-number and his follower, if there is one.

Example:

Input:  [ 1, 3, 5, 1, -10]
Output:  [ 2, 4, 3, -4.5]
If the array has 0 or 1 values or is null, your method should return an empty array.

Have fun coding it and please don't forget to vote and rank this kata! :-)

ALGORITHMSFUNDAMENTALSBASIC LANGUAGE FEATURES

None, Empty, Single ElementTests
Unexpected exception raised
Traceback (most recent call last):
  File "/workspace/default/src/codewars-test/codewars_test/test_framework.py", line 111, in wrapper
    func()
  File "tests.py", line 27, in _
    test.assert_equals(averages(inp), exp)
  File "/workspace/default/solution.py", line 2, in averages
    return [sum(n)/2 for n in zip(arr[:-1],arr[1:])]
TypeError: 'NoneType' object is not subscriptable
'''

def averages(arr):
    if not arr and not isinstance(arr,list):return None
    return [sum(n)/2 for n in zip(arr[:-1],arr[1:])]
arr =  [ 1, 3, 5, 1, -10]
arr = []
arr = ''
arr = [1,2,3]
arr = None

#solve by ericlee
def averages(arr):
    if not arr: return []
    return [sum(n) / 2 for n in zip(arr[:-1], arr[1:])]
print(averages(arr))

def averages(arr):
    return [i/2 for i in list(map(sum,zip(arr[1:],arr[:-1])))] if arr else []
#1st
def averages(arr):
    return [(arr[x]+arr[x+1])/2 for x in range(len(arr or [])-1)]

