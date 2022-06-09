'''
https://www.codewars.com/kata/5566b0dd450172dfc4000005/train/python

Test.assert_equals(length_of_sequence([1, 1], 1), 2, 'Returns two when there are only two elements in the array')
Test.assert_equals(length_of_sequence([1, 2, 3, 1], 1), 4, 'Returns four for an array of length four and the number to be searched at the boundaries')
Test.assert_equals(length_of_sequence([-7, 5, 0, 2, 9, 5], 10), 0, 'Returns zero if element is missing from the array')
Test.assert_equals(length_of_sequence([-7, 5, 0, 2, 9, 5], 5), 5, 'Returns five')
Test.assert_equals(length_of_sequence([-7, 6, 2, -7, 4], -7), 4, 'Returns four')
'''

def length_of_sequence(arr,n):
    ans = [i for i,e in enumerate(arr) if e == n]
    print(ans)
    return ans[1] + 1 - ans[0] if len(ans) > 1 and len(ans)<=2 else 0

arr,n = [-7, 5, 0, 2, 9, 5], 2
#arr,n = [-7, 5, 0, 2, 9, 5], 5
print(length_of_sequence(arr,n))

#1st solution
def length_of_sequence(arr, n):
    if arr.count(n) != 2:
        return 0
    a = arr.index(n)
    b = arr.index(n, a + 1)
    return b - a + 1