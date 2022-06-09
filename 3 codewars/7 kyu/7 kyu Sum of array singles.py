'''
https://www.codewars.com/kata/59f11118a5e129e591000134/train/python

Test.it("Basic tests")
Test.assert_equals(repeats([4,5,7,5,4,8]),15)
Test.assert_equals(repeats([9, 10, 19, 13, 19, 13]),19)
Test.assert_equals(repeats([16, 0, 11, 4, 8, 16, 0, 11]),12)
Test.assert_equals(repeats([5, 17, 18, 11, 13, 18, 11, 13]),22)
Test.assert_equals(repeats([5, 10, 19, 13, 10, 13]),24)
'''

def repeats(arr):
    ans,dup = [],[]
    for i in arr:
        if i not in ans:
            ans.append(i)
        else:
            dup.append(i)
    return sum([i for i in ans if i not in dup])
'''
Time: 4885ms Passed: 105 Failed: 0
Test Results:
 Basic tests (5 of 5 Assertions)
 Random tests (100 of 100 Assertions)
'''
arr = [5, 10, 19, 13, 10, 13]

#1st solution
from collections import Counter
def repeats(arr):
    return sum(k for k, v in Counter(arr).items() if v == 1)
'''
Time: 2415ms Passed: 105 Failed: 0
Test Results:
 Basic tests (5 of 5 Assertions)
 Random tests (100 of 100 Assertions)
You have passed all of the tests! :)
'''
#2nd solution
def repeats(arr):
    return sum([x for x in arr if arr.count(x) == 1])
'''
Time: 8552ms Passed: 105 Failed: 0
Test Results:
 Basic tests (5 of 5 Assertions)
 Random tests (100 of 100 Assertions)
You have passed all of the tests! :)
'''
print(repeats(arr))