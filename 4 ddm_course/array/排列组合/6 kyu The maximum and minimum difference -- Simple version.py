'''
https://www.codewars.com/kata/583c5469977933319f000403/train/python
说明：给定两个整数组(arr1,arr2)。
给定两个整数数组(arr1,arr2)。你的任务是找到一对数组(一个元素在arr1中，另一个元素在arr2中)，
它们的差值越大越好(绝对值)；同样，你应该找到一对数组，它们的差值越小越好。用一个数组返回最大和最小的差值。
[ 最大差值，最小差值 ]
Some Examples
 maxAndMin([3,10,5],[20,7,15,8]) === [17,2]
 maxAndMin([3],[20]) === [17,17]
 maxAndMin([3,10,5],[3,10,5]) === [7,0]
 maxAndMin([1,2,3,4,5],[6,7,8,9,10]) === [9,1]
'''

def max_and_min(arr1,arr2):
    mx,minx = -1,float("inf")
    for i in arr1:
        submx = max([abs(i-j) for j in arr2])
        subminx = min([abs(i-j) for j in arr2])
        if submx > mx:   mx = submx
        if subminx < minx: minx = subminx
    return mx,minx
arr1,arr2 = [1,2,3,4,5],[6,7,8,9,10]
print(max_and_min(arr1,arr2))

#1st solution
def max_and_min(arr1,arr2):
    diffs = [abs(x-y) for x in arr1 for y in arr2]
    print(diffs)
    return [max(diffs), min(diffs)]
arr1,arr2 = [1,2,3,4,5],[6,7,8,9,10]
print(max_and_min(arr1,arr2))