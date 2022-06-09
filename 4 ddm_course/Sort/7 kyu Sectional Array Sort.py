'''
https://www.codewars.com/kata/58ef87dc4db9b24c6c000092/train/python

In this kata you are given an array to sort but you're expected to start sorting from
a specific position of the array (in ascending order) and optionally you're given the
number of items to sort.

Examples:
sect_sort([1, 2, 5, 7, 4, 6, 3, 9, 8], 2) //=> [1, 2, 3, 4, 5, 6, 7, 8, 9]
sect_sort([9, 7, 4, 2, 5, 3, 1, 8, 6], 2, 5) //=> [9, 7, 1, 2, 3, 4, 5, 8, 6]
Documentation:
sect_sort(array, start, length);
array - array to sort
start - position to begin sorting
length - number of items to sort (optional)
if the length argument is not passed or is zero, you sort all items to the right of
the start postiton in the array

Test.describe("Basic tests")
Test.assert_equals(sect_sort([1, 2, 5, 7, 4, 6, 3, 9, 8], 2), [1, 2, 3, 4, 5, 6, 7, 8, 9])
Test.assert_equals(sect_sort([1, 2, 5, 7, 4, 6, 3, 9, 8], 8), [1, 2, 5, 7, 4, 6, 3, 9, 8])
Test.assert_equals(sect_sort([9, 7, 4, 2, 5, 3, 1, 8, 6], 2, 5), [9, 7, 1, 2, 3, 4, 5, 8, 6])
Test.assert_equals(sect_sort([1, 2, 5, 7, 4, 6, 3, 9, 8], 8, 3), [1, 2, 5, 7, 4, 6, 3, 9, 8])
Test.assert_equals(sect_sort([], 0), [])
'''
arr = [9, 7, 4, 2, 5, 3, 1, 8, 6], 2, 5
def sect_sort(*arr):
    print(arr,arr[0],arr[-1])
    if len(arr) == 3:
        start,lenth = arr[-2],arr[-1]
    elif len(arr) == 2:
        start,lenth = arr[-1],len(arr[0]) - arr[-1]
    print(start)
    return arr[0][:start] + sorted(arr[0][start:start+lenth]) + arr[0][start+lenth:]
print(sect_sort(*arr))

#1st solution
def sect_sort(lst, start, length=0):
    end = start + length if length else len(lst)
    return lst[:start] + sorted(lst[start:end]) + lst[end:]
