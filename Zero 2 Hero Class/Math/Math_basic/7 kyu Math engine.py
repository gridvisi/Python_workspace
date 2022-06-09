'''
https://www.codewars.com/kata/587854330594a6fb7e000057/train/python
The product of all the non-negative numbers
The sum of all the negative numbers
Edge cases
If there are no non-negative numbers, assume the product of them to be 1.
Similarly, if there are no negative numbers, assume the sum of them to be 0.
If the array is null, result should be 0.
For example:
math_engine([1, 2, 3, -4, -5]) # should return -3
FUNDAMENTALS
'''
# key point: non-negative numbers

#3rd solve by ericlee
def math_engine(arr):
    if arr == None:return 0
    ans,res = 1,[]
    flag = 0
    for n in arr:
        if n >= 0:
            ans *= n
            flag = 1
        else:
            res.append(n)
    return ans*flag + sum(res) + (1 if flag==0 else 0)

arr = [1, 2, 3, -4, -5]
arr = []
print(math_engine(arr))

#1st
def math_engine(arr):
    a= 1
    b = 0
    if arr is None:
        return 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            a *= arr[i]
        else:
            b += arr[i]
    return a+b


#2nd
from operator import mul
from functools import reduce

def math_engine(arr):
    if arr == []:
        return 1
    elif not arr:
        return 0
    pro = reduce(mul, filter(lambda x: x >= 0, arr), 1)
    tot = sum(filter(lambda y: y < 0, arr))
    return pro + tot

