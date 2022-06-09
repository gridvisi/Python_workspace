'''
https://www.codewars.com/kata/55eea63119278d571d00006a/train/python

Test.assert_equals(next_id([0,1,2,3,4,5,6,7,8,9,10]), 11)
Test.assert_equals(next_id([5,4,3,2,1]), 0)
Test.assert_equals(next_id([0,1,2,3,5]), 4)
Test.assert_equals(next_id([0,0,0,0,0,0]), 1)
Test.assert_equals(next_id([]), 0)

嘿，厉害的程序员!

你有很多数据需要管理，当然，你使用基于零的和非负的ID来使每个数据项都是独一无二的！因此，你需要一个方法，
为你的下一个新数据项返回最小的未使用ID。

因此，你需要一个方法，为你的下一个新数据项返回最小的未使用ID......
注意：给定的已使用ID数组可能是未排序的。出于测试的原因，可能会有重复的ID，但你不需要找到或删除它们。

去吧，编写一些纯粹的神奇代码吧
'''
#ascending order：升序
#descending order：降序


def next_id(arr):
    if not arr:return 0
    for i in range(len(arr)):
        if i not in sorted(arr):
            return i
    return max(arr)+1

arr = [0,1,2,3,5]
arr = [5,4,3,2,1] #0
print(next_id(arr))

#1st solution
def next_id(arr):
    t = 0
    while t in arr:
        t +=1
    return t


'''

       if not i and sorted(arr) == [i for i in range(len(arr)-1)]:
            return 0
        else:
            if sorted(arr) == [i for i in range(len(arr)-1)]:
                return max(arr) + 1
            else:
                for i in range(len(arr) - 1):
                    if i not in sorted(arr):
                        return i
'''