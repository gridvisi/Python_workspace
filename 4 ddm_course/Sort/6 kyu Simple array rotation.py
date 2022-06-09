'''
https://www.codewars.com/kata/5a16cab2c9fc0e09ce000097/train/python

solve([1,2,3,4,5,7]) = "A" -- Ascending
solve([7,1,2,3,4,5]) = "RA" -- Rotated ascending
solve([4,5,6,1,2,3]) = "RA" -- Rotated ascending
solve([9,8,7,6]) = "D" -- Descending
solve([5,9,8,7,6]) = "RD" -- Rotated Descending
solve([1,2,3,4,5,7])="A"--升序排列。
solve([7,1,2,3,4,5])="RA"--旋转升序。
solve([4,5,6,1,2,3])="RA"--旋转升序。
solve([9,8,7,6])="D"--降序排列
solve([5,9,8,7,6])="RD"--旋转降序。

Test.it("Basic tests")
Test.assert_equals(solve([1,2,3,4,5,7]),"A")
Test.assert_equals(solve([7,1,2,3,4,5]),"RA")
Test.assert_equals(solve([2,3,4,5,7,12]),"A")
Test.assert_equals(solve([7,12,1,2,3,4,5]),"RA")
Test.assert_equals(solve([4,5,6,1,2,3]),"RA")
Test.assert_equals(solve([9,8,7,6,5]),"D")
Test.assert_equals(solve([5,9,8,7,6]),"RD")
Test.assert_equals(solve([6,5,9,8,7]),"RD")
Test.assert_equals(solve([9,6,7]),"RA")
'''

def solve(arr):
    for i in range(len(arr)-1):
        if i == 0:
            if arr[i:] == sorted(arr[i:]):
                return "A"
            elif arr[i:] == sorted(arr[i:],reverse=True):
                return "D"

        elif i > 0:
            if arr[:i] == sorted(arr[:i],reverse=True) and arr[i:] == sorted(arr[i:]):
                return "RA"

            elif arr[:i] == sorted(arr[:i]) and arr[i:] == sorted(arr[i:]):
                return "RA"

            elif arr[:i] == sorted(arr[:i]) and arr[i:] == sorted(arr[i:],reverse=True):
                return "RD"

            elif arr[:i] == sorted(arr[:i],reverse=True) and arr[i:] == sorted(arr[i:], reverse=True):
                return "RD"


arr = [5,9,8,7,6]
arr = [7,12,1,2,3,4,5]
print(solve(arr))

print([7] == sorted([7],reverse=True))
print([7] == sorted([7]))
print(arr[2:] == sorted(arr[2:]))


#1st solution
def solve(lst):
    a, b, c = lst[0] < lst[1], lst[1] < lst[2], lst[-1] < lst[0]
    m = a if a == b else c
    return ('R' if c == m else '') + ('A' if m else 'D')

def solve(arr):
    if sorted(arr) == arr:
        return "A"
    if sorted(arr)[::-1] == arr:
        return "D"
    return "RA" if arr[0] > arr[-1] else "RD"