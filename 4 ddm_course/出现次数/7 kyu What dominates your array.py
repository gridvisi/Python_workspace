'''
https://www.codewars.com/kata/559e10e2e162b69f750000b4/train/python

A zero-indexed array arr consisting of n integers is given. The dominator of array arr is the value that occurs in more than half of the elements of arr.
For example, consider array arr such that arr = [3,4,3,2,3,1,3,3]
The dominator of arr is 3 because it occurs in 5 out of 8 elements of arr and 5 is more than a half of 8.
Write a function dominator(arr) that, given a zero-indexed array arr consisting of n integers, returns the dominator of arr. The function should return −1 if array does not have a dominator. All values in arr will be >=0.

Test.assert_equals(dominator([3,4,3,2,3,1,3,3]),3)
Test.assert_equals(dominator([1,2,3,4,5]),-1)
Test.assert_equals(dominator([1,1,1,2,2,2]),-1)
Test.assert_equals(dominator([1,1,1,2,2,2,2]),2)
Test.assert_equals(dominator([]),-1)
'''
arr = [3,4,3,2,3,1,3,3]

#21th solution by ericlee
from collections import Counter
def dominator(arr):
    arrCunt = Counter(arr)
    print(arrCunt)
    prim = [k for k,v in arrCunt.items() if v > len(arr)* 0.5]  #== max(arrCunt.values())
    if prim:return prim[0]
    return -1
print(dominator(arr))

def dominator(arr):
    for x in set(arr):
        if arr.count(x) > len(arr)/2.0:
            return x
    return -1

from collections import Counter
def dominator(arr):
    if not arr:
        return -1
    k, v = Counter(arr).most_common(1)[0]
    return k if v > len(arr) / 2 else -1

def dominator(arr):
    for el in arr:
        if arr.count(el) > len(arr) / 2:
            return el
    return -1


