'''
https://www.codewars.com/kata/5a3e1319b6486ac96f000049/train/python

Test.it("Basic tests")
Test.assert_equals(pairs([1,2,5,8,-4,-3,7,6,5]),3)
Test.assert_equals(pairs([21, 20, 22, 40, 39, -56, 30, -55, 95, 94]),2)
Test.assert_equals(pairs([81, 44, 80, 26, 12, 27, -34, 37, -35]),0)
Test.assert_equals(pairs([-55, -56, -7, -6, 56, 55, 63, 62]),4)
Test.assert_equals(pairs([73, 72, 8, 9, 73, 72]),3)
'''

arr = [1,2,5,8,-4,-3,7,6,5]
def pairs(arr):
    cunt = 0
    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) == 1:
            cunt += 1
    return cunt

print(pairs(arr))