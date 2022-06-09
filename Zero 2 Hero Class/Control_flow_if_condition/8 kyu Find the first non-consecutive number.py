'''
https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python

Test.describe("Basic tests")
Test.assert_equals(first_non_consecutive([1,2,3,4,6,7,8]), 6)
Test.assert_equals(first_non_consecutive([1,2,3,4,5,6,7,8]), None)
Test.assert_equals(first_non_consecutive([4,6,7,8,9,11]), 6)
Test.assert_equals(first_non_consecutive([4,5,6,7,8,9,11]), 11)
Test.assert_equals(first_non_consecutive([31,32]), None)
Test.assert_equals(first_non_consecutive([-3,-2,0,1]), 0)
Test.assert_equals(first_non_consecutive([-5,-4,-3,-1]), -1)
'''

def first_non_consecutive(arr):
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] > 1:
            return arr[i+1]

#1st
def first_non_consecutive(arr):
    if not arr: return 0
    for i, x in enumerate(arr[:-1]):
        if x + 1 != arr[i + 1]:
            return arr[i + 1]