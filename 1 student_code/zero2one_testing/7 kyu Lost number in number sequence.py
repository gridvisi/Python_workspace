'''
https://www.codewars.com/kata/595aa94353e43a8746000120/train/python

# These are some of the methods available:
#   test.expect(boolean, [optional] message)
#   test.assert_equals(actual, expected, [optional] message)
#   test.assert_not_equals(actual, expected, [optional] message)

Test.assert_equals(find_deleted_number([1,2,3,4,5], [3,4,1,5]), 2, 'Deletion')
Test.assert_equals(find_deleted_number([1,2,3,4,5,6,7,8,9], [1,9,7,4,6,2,3,8]), 5, 'Deletion')
Test.assert_equals(find_deleted_number([1,2,3,4,5,6,7,8,9], [5,7,6,9,4,8,1,2,3]), 0, 'No deletion')
'''

arr,mixed_arr = [1,2,3,4,5,6,7,8,9], [5,7,6,9,4,8,1,2,3]
def find_deleted_number(arr, mixed_arr):
    ans = [i for i in arr if i not in mixed_arr]
    if len(ans) > 0:
        return ans[0]
    elif len(ans) == 0:return 0
print(find_deleted_number(arr, mixed_arr))

#1st
def find_deleted_number(arr, mixed_arr):
    return sum(arr)-sum(mixed_arr)