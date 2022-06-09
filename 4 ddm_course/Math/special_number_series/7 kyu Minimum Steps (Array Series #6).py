'''
https://www.codewars.com/kata/5a91a7c5fd8c061367000002/train/python

Test.describe("Basic tests")
Test.assert_equals(minimum_steps([4,6,3], 7), 1)
Test.assert_equals(minimum_steps([10,9,9,8], 17), 1)
Test.assert_equals(minimum_steps([8,9,10,4,2], 23), 3)
Test.assert_equals(minimum_steps([19,98,69,28,75,45,17,98,67], 464), 8)
Test.assert_equals(minimum_steps([4,6,3], 2), 0)
print("<COMPLETEDIN::>")
'''

#17 solution by ericlee

def minimum_steps(numbers, value):
    ans,t = 0,0
    for i in sorted(numbers):
        ans += i
        t += 1
        if ans > value:
            return t

#1st solution
def minimum_steps(arr, n):
    arr = sorted(arr)
    s = 0
    for i,v in enumerate(arr):
        s += v
        if s >= n: return i