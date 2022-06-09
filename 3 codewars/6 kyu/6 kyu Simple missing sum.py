#https://www.codewars.com/kata/5a941f3a4a6b34edf900006f/train/python
'''
Test.it("Basic tests")
Test.assert_equals(solve([1,2,8,7]),4)
Test.assert_equals(solve([2,12,3,1]),7)
Test.assert_equals(solve([4,2,8,3,1]),19)
Test.assert_equals(solve([4,2,7,3,1]),18)
Test.assert_equals(solve([1,2,8,7]),4)
Test.assert_equals(solve([4,2,12,3]),1)
'''
def solve(xs):
    m = 0
    for x in sorted(xs):
        if x > m + 1:
            break
        m += x
    return m + 1

from itertools import accumulate
def solve(arr):
    arr = sorted(arr)
    return next((x+1 for x, i in zip(accumulate([0]+arr), arr+[0]) if i > x + 1), sum(arr)+1)

def solve(arr):
    arr.sort()
    res = 1
    for i in range(len(arr)):
        if arr[i] <= res:
            res += arr[i]
    return res

def solve(arr):
    re = []
    arr = sorted(arr)
    for j in range(len(arr)):
        sub = [e + arr[j] for i,e in enumerate(arr) if i != j]
        re.append(sub)

    return re
arr = [4,2,12,3]
print(solve(arr))
