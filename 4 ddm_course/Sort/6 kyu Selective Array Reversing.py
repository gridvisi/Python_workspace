'''
https://www.codewars.com/kata/58f6000bc0ec6451960000fd/train/python
selReverse([2,4,6,8,10,12,14,16], 3)
 //=> [6,4,2, 12,10,8, 16,14]

 selReverse([1,2,3,4,5,6], 2)
 //=> [2,1, 4,3, 6,5]
'''
arr,l = [2,4,6,8,10,12,14,16], 3
def sel_reverse(arr,l):
    if l == 0:return arr
    ans = [arr[i:i+l][::-1] for i in range(0,len(arr),l)]
    return [x for arr in ans for x in arr]
print(sel_reverse(arr,l))

#1st solution
def sel_reverse(arr,l):
    return [ elt for i in range(0, len(arr), l) for elt in arr[i:i+l][::-1] ] if l != 0 else arr

#2nd solution
from itertools import chain

def gen(arr, l):
    for i in range(0, len(arr), l):
        yield arr[i:i+l][::-1]

def sel_reverse(arr,l):
    return list(chain.from_iterable(gen(arr, l or 1)))

#3rd solution
def sel_reverse(lst, k):
    return sum((lst[i:i+k][::-1] for i in range(0, len(lst), k)), []) if k else lst

#4th solution
def sel_reverse(arr, l):
    l = l or 1
    return [
        x
        for i in range(0, len(arr), l)
        for x in reversed(arr[i:i+l])
    ]

print(sum([[i] for i in range(10)],[]))
print(sum([arr[i:i+l][::-1] for i in range(0,len(arr),l)],[]) if l>0 else arr)
print([arr[i:i + l][::-1] for i in range(0, len(arr), l)])
print(sum([arr[i:i + l][::-1] for i in range(0, len(arr), l)], []))

print('([[3]]+[]',sum([[[3]]],[[1]]))
print('([3]+[1]',sum([[3]],[1])) # not work
print(sum([3]),sum([3]))