'''
https://www.codewars.com/kata/minimize-sum-of-array-array-series-number-1/train/python
Given an array of intgers , Find the minimum sum which is obtained from summing each Two integers product .
Notes  Array/list will contain positives only .
Array/list will always has even size   Input >> Output Examples
minSum({5,4,2,3}) ==> return (22)
Explanation:
The minimum sum obtained from summing each two integers product , 5*2 + 3*4 = 22
升序Ascending order, 降序 descending order
'''

arr = [12,6,10,26,3,24]
arr = [9,2,8,7,5,4,0,6]
def min_sum(arr):
    s = 0
    arr_asc = sorted(arr)
    for i in range(int(len(arr)/2)):
        s += arr_asc[i]*arr_asc[len(arr)-i-1]
        print(arr_asc[i],arr_asc[len(arr)-i-1],arr_asc)
    return s

def min_sum(arr):
    arr = sorted(arr)
    return sum(arr[i]*arr[-i-1] for i in range(len(arr)//2))

def min_sum(arr):
    arr.sort()
    left, right, res = 0, len(arr) - 1, 0
    while left < right:
        res += arr[left] * arr[right]
        left += 1
        right -= 1
    return res

def min_sum(arr):
    return sum(x * y for x, y in zip(sorted(arr)[::2], sorted(arr)[-1::-2]))
print(min_sum(arr))