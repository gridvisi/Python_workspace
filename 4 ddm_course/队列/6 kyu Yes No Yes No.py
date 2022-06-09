#https://www.codewars.com/kata/573c84bf0addf9568d001299/train/python
'''
var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 // returns [1, 3, 5, 7, 9, 2, 6, 10, 8, 4]

var arr = ['this', 'code', 'is', 'right', 'the']
 // returns ['this', 'is', 'the', 'right', 'code']
'''
from collections import deque

def yes_no(arr):
    d, result = deque(arr), []
    while d:
        result.append(d.popleft())
        d.rotate(-1)
    return result

def yes_no(arr):  # S2
    result, i = [], 0
    while arr:
        result.extend(arr[i::2])
        print(result,i)
        j = i != len(arr) % 2
        print(j,i)
        arr = arr[1-i::2]
        i = j
    return result
arr = [1,2,3,4,5]
print('s2',yes_no(arr))

def yes_no(arr):
    result = []
    while arr:
        result.append(arr.pop(0))
        if arr:
            arr.append(arr.pop(0))
    return result


import itertools
def yes_no(arr):
    re = itertools.cycle(arr)
    return list(itertools.islice(re,0,10,2))
arr = ['this', 'code', 'is', 'right', 'the']
print(yes_no(arr))

def yes_no(arr):
    re,index = [],[]
    arrn = arr[:]
    i = 1
    if len(arr) <= 2:
        return arr
    else:
        while len(arrn) > 0:
            #if len(arrn) == 2: arrn = arrn[::-1]
            i = 0
            while i < len(arrn):
                re.append(arrn[i])
                i += 2
            arrn = [i for i in arr if i not in re]
    re[-1],re[-2] = re[-2],re[-1]
    return re

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr = []
arr = ['a']
arr = ['a','b']
arr = ['this', 'code', 'is', 'right', 'the']
print(yes_no(arr))


'''
[3, 'you', 'testing', '!', 'villains', 2, 5, 'out', [], 0, 8, 'big', 'pippi', 4, 'cat'] 
[3, 'you', 'testing', '!', 'villains', 2, 5, 'out', 'pippi', 4, 'cat', [], 8, 0, 'big']
'''

#It should work for random inputs too:
#[1, 'out', 'beware', 2, '!', 'testing', 3, 8, 'pippi', 'watch', 'mighty', 6, 5, 'is']
#[1, 'out', 'beware', 2, '!', 'testing', 3, 8, 'pippi', 'watch', 'mighty', 'is', 6, 5]