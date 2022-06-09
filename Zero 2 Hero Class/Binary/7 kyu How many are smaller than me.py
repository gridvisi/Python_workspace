'''
https://www.codewars.com/kata/56a1c074f87bc2201200002e/train/python

Write

smaller(arr)
that given an array arr, you have to return the amount of numbers that are smaller than
arr[i] to the right.

For example:

smaller([5, 4, 3, 2, 1]) == [4, 3, 2, 1, 0]
smaller([1, 2, 0]) == [1, 1, 0]
If you've completed this one and you feel like testing your performance tuning of this
same kata, head over to the much tougher version How many are

Test.describe("Basic Tests")
Test.assert_equals(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])
Test.assert_equals(smaller([1, 2, 3]), [0, 0, 0])
Test.assert_equals(smaller([1, 2, 0]), [1, 1, 0])
Test.assert_equals(smaller([1, 2, 1]), [0, 1, 0])
Test.assert_equals(smaller([1, 1, -1, 0, 0]), [3, 3, 0, 0, 0])
Test.assert_equals(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]), [4, 1, 5, 5, 0, 0, 0, 0, 0])
'''

#16th solve by ericlee
def smaller(arr):
    print([[e > j for j in arr[i+1:]] for i,e in enumerate(arr[:-1])])
    return [sum([int(e > j) for j in arr[i+1:]]) for i,e in enumerate(arr)]
arr = [5, 4, 7, 9, 2, 4, 4, 5, 6]
print(smaller(arr))

#1st
def smaller(arr):
    return [len([a for a in arr[i:] if a < arr[i]]) for i in range(0, len(arr))]