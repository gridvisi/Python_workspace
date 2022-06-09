'''
https://www.codewars.com/kata/5a090c4e697598d0b9000004/train/python

In this Kata, you will be given an array of unique elements, and your task is to
rerrange the values so that the first max value is followed by the first minimum,
followed by second max value then second min value, etc.

For example:

solve([15,11,10,7,12]) = [15,7,12,10,11]
The first max is 15 and the first min is 7. The second max is 12 and the second min
is 10 and so on.

More examples in the test cases.

Good luck!

FUNDAMENTALSARRAYS

Test.it("Basic tests")
Test.assert_equals(solve([15,11,10,7,12]),[15,7,12,10,11])
Test.assert_equals(solve([91,75,86,14,82]),[91,14,86,75,82])
Test.assert_equals(solve([84,79,76,61,78]),[84,61,79,76,78])
Test.assert_equals(solve([52,77,72,44,74,76,40]),[77,40,76,44,74,52,72])
Test.assert_equals(solve([1,6,9,4,3,7,8,2]),[9,1,8,2,7,3,6,4])
Test.assert_equals(solve([78,79,52,87,16,74,31,63,80]),[87,16,80,31,79,52,78,63,74])
'''

def solve(arr):
    ans,l,r = [],0,len(arr)-1
    arrs = sorted(arr)
    while r - l >= 1:
        ans.append(arrs[r])
        ans.append(arrs[l])
        l += 1
        r -= 1
    if len(arr)%2==1:
        ans.extend(arrs[l:r+1])
        #ans.append(sum(arrs[l:r+1]))
        return ans
    else:
        return ans


arr = [1,6,9,4,3,7,8,2] #[9,1,8,2,7,3,6,4]
#arr = [78,79,52,87,16,74,31,63,80] #out = [87,16,80,31,79,52,78,63,74]
print(solve(arr))

#1st solution
def solve(arr):
    arr = sorted(arr, reverse=True)
    res = []
    while len(arr):
        res.append(arr.pop(0))
        if len(arr):
            res.append(arr.pop())
    return res

def solve(arr):
    lst, n = sorted(arr), len(arr)
    return [lst[i // 2 if i % 2 else n - i // 2 - 1] for i in range(n)]


