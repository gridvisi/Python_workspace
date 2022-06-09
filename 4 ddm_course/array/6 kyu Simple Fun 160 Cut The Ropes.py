'''
https://www.codewars.com/kata/58ad388555bf4c80e800001e/train/python

Test.describe("Basic Tests")
Test.assert_equals(cut_the_ropes([3, 3, 2, 9, 7]),[5, 4, 2, 1])
Test.assert_equals(cut_the_ropes([1, 2, 3, 4, 3, 3, 2, 1]),[8, 6, 4, 1])
Test.assert_equals(cut_the_ropes([13035, 6618, 13056, 20912, 1119, 13035, 6618, 6618, 8482, 13056]),[10, 9, 6, 5, 3, 1])
Test.assert_equals(cut_the_ropes([9, 9, 9, 9, 7]),[5, 4])
Test.assert_equals(cut_the_ropes([3, 3, 2, 9, 7]),[5, 4, 2, 1])

For a = [3, 3, 2, 9, 7], the result should be [5, 4, 2, 1]

You have 5 ropes: 3 3 2 9 7 ( 5 left)
step 1: 1 1 0 7 5 ( 4 left)
step 2: 0 0 0 6 4 ( 2 left)
step 3: 0 0 0 0 2 ( 1 left)
step 4: 0 0 0 0 0
Hence the result is [5, 4, 2, 1]
'''
arr = [1, 2, 3, 4, 3, 3, 2, 1]  #[8, 6, 4, 1]

def cut_the_ropes(arr):
    step = []
    #count = 0
    while sum(arr) > 0:
        arrs = [i for i in arr if i > 0]
        count = len(arrs)
        step.append(count)
        reduce = min(arrs)
        arr = [i - reduce for i in arr if i - reduce>=0]
        print(arr)
    return step

print(cut_the_ropes(arr))