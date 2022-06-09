'''
https://www.codewars.com/kata/59f3178e3640cef6d90000d5/train/python

Consider the array [3,6,9,12]. If we generate all the combinations with repetition
that sum to 12, we get 5 combinations: [12], [6,6], [3,9], [3,3,6], [3,3,3,3].
The length of the sub-arrays (such as [3,3,3,3] should be less than or equal to the
length of the initial array ([3,6,9,12]).

Given an array of positive integers and a number n, count all combinations with
repetition of integers that sum to n. For example:

find([3,6,9,12],12) = 5.
More examples in the test cases.
Test.it("Basic tests")
Test.assert_equals(find([1,2,3],10),0)
Test.assert_equals(find([1,2,3],7),2)
Test.assert_equals(find([1,2,3],5),3)
Test.assert_equals(find([3,6,9,12],12),5)
Test.assert_equals(find([1,4,5,8],8),3)
Test.assert_equals(find([3,6,9,12],15),5)
Test.assert_equals(find([3,6,9,12,14,18],30),21)
Good luck!
'''
from itertools import combinations_with_replacement
def find(arr,n):
    return sum( sum(c) == n for x in range(1,len(arr)+1) for c in combinations_with_replacement(arr, x) )

from itertools import combinations_with_replacement as comb
# Brute force!
def find(arr, n):
    return sum(sum(L) == n for i in range(1, len(arr)+1) for L in comb(arr, i))

from itertools import combinations_with_replacement as c

def find(arr, n):
    return sum(
        sum(xs) == n
        for i in range(len(arr))
        for xs in c(arr, i + 1)
    )


def find(arr, n):
    def helper(current):
        nonlocal count
        if len(current) > len(arr):
            return
        if sum(current) == n:
            count += 1
            return
        for m in arr:
            if not current or current[-1] <= m:
                current.append(m)
                if sum(current) <= n:
                    helper(current)
                current.pop()

    count = 0
    helper([])
    return count