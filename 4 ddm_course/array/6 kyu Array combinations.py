'''
https://www.codewars.com/kata/59e66e48fc3c499ec5000103/train/python

Test.it("Basic tests")
Test.assert_equals(solve([[1,2],[4],[5,6]]),4)
Test.assert_equals(solve([[1,2],[4,4],[5,6,6]]),4)
Test.assert_equals(solve([[1,2],[3,4],[5,6]]),8)
Test.assert_equals(solve([[1,2,3],[3,4,6,6,7],[8,9,10,12,5,6]]),72)
'''

#18th solution by ericlee
def solve(arr):
    ans = 1
    setArr = [len(set(a)) for a in arr]
    for i in setArr:
        ans *= i
    return ans

arr = [[1,2,3],[3,4,6,6,7],[8,9,10,12,5,6]]
print(solve(arr))