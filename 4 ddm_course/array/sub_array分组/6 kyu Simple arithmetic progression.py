'''
https://www.codewars.com/kata/5a903c0557c562cd7500026f/train/python

In this Kata, you will be given an array of integers and your task is to return the number of arithmetic progressions of size 3 that are possible from that list. In each progression, the differences between the elements must be the same.

[1, 2, 3, 5, 7, 9] ==> 5
// [1, 2, 3], [1, 3, 5], [1, 5, 9], [3, 5, 7], and [5, 7, 9]
All inputs will be sorted. More examples in test cases.

Good luck!

Test.it("Basic tests")
Test.assert_equals(solve([1,2,3,4,5]),4)
Test.assert_equals(solve([1,2,3,5,7,9]),5)
Test.assert_equals(solve([0,5,8,9,11,13,14,16,17,19]),10)
Test.assert_equals(solve([0,1,2,3,5,6,7,11,13,15,17,19]),17)
Test.assert_equals(solve([0,1,4,5,7,9,10,13,15,16,18,19]),15)
Test.assert_equals(solve([0,1,2,3,5,8,11,13,14,16,18,19]),13)
'''

#1st solution
def solve(arr):
    return sum(y-x == z-y for i,x in enumerate(arr[:-2])
                           for j,y in enumerate(arr[i+1:-1])
                           for _,z in enumerate(arr[j+1:]))

#2nd solution
from itertools import combinations
def solve(xs):
    return sum(1 for a, b, c in combinations(xs, 3) if a - b == b - c)

from itertools import combinations
def solve(xs):
    return sum(a - b == b - c for a, b, c in combinations(xs, 3))
#3rd solution
def solve(arr):
    return sum(x<y and y*2-x in arr for x in arr for y in arr)


#6th

from itertools import combinations
def help67(arr):
    S = set(arr)
    for a, b in combinations(arr, 2):
        if 2 * b - a in S:
            yield a, b, 2 * b - a

def solve(arr):
    c = 0
    for i in help67(arr):
        c += 1
    return c

#9th solution
def solve(arr):
    res = []
    for n in arr:
        for k in range(1, max(arr)//2+1):
            if n+k in arr and n+2*k in arr:
                res.append([n, n+k, n+2*k])
    return len(res)
arr = [1,2,3,4,5]
print(solve(arr))
