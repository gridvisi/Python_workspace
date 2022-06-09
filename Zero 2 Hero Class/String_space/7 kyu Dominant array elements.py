'''
https://www.codewars.com/kata/5a04133e32b8b998dc000089/train/python
An element in an array is dominant if it is greater than all elements to its right. You will be given an array and your task will be to return a list of all dominant elements. For example:

solve([1,21,4,7,5]) = [21,7,5] because 21, 7 and 5 are greater than elments to their right.
solve([5,4,3,2,1]) = [5,4,3,2,1]

Notice that the last element is always included. All numbers will be greater than 0.
More examples in the test cases.

Good luck!

Test.it("Basic tests")
Test.assert_equals(solve([16,17,14,3,14,5,2]),[ 17,14,5,2])
Test.assert_equals(solve([ 92,52,93,31,89,87,77,105]),[105])
Test.assert_equals(solve([ 75,47,42,56,13,55]), [75,56,55])
Test.assert_equals(solve([ 67,54,27,85,66,88,31,24,49]),[88,49])
Test.assert_equals(solve([ 76,17,25,36,29]),[76,36,29])
Test.assert_equals(solve([ 104,18,37,9,36,47,28]),[104,47,28]
'''

def solve(arr):
    ans = []
    for i in range(len(arr)-1):
        if arr[i] > max(arr[i+1:]):
            ans.append(arr[i])
    ans.append(arr[-1])
    return ans
arr = [ 104,18,37,9,36,47,28]
print(solve(arr))

#1st
def solve(arr):
    r = []
    for v in arr[::-1]:
        if not r or r[-1] < v: r.append(v)
    return r[::-1]