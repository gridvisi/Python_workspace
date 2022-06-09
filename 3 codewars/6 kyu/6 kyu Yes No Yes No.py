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

from collections import deque
def yes_no(arr):
    d = deque(reversed(arr))
    result = []
    while d:
        result.append(d.pop())
        d.rotate()
    return result

def yes_no(arr):
    new = []
    take = True
    while arr:
        if take:
            some = arr.pop(0)
            new.append(some)
            take = False
        else:
            some = arr.pop(0)
            arr.append(some) # 偶数地址移动到数组尾部
            take = True
    return new

def yes_no(arr):
    counter = 0
    out = []
    _in = []
    while arr:
        for i in arr:
            if counter % 2 == 0:
                out.append(i)
            else:
                _in.append(i)
            counter += 1
        arr = _in
        _in = []
    return out

def yes_no(a):
    if len(a)<=1: return a
    a.append(a.pop(1))
    return [a.pop(0)] + yes_no(a)

def yes_no(arr):
    for r in range(1, len(arr)- 1):
        arr.append(arr.pop(r))
    return arr


def yes_no(arr, x=0):
    if len(arr) <= 1: return arr
    return arr[x::2] + yes_no(arr[1-x::2], x+len(arr)&1)

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
有100个人，环成一圈开始报数，从1数起，
数到7就枪毙一个，然后继续从1数起，数到7就枪毙一个，直到所有枪毙。求所有人的死亡顺序。
'''

def dead_live(person,nth):
    circle = [i for i in range(7,person)]+[i for i in range(7)]
    #print(circle)
    d, result = deque(circle), []
    while d:
        result.append(d.popleft())
        d.rotate(-(nth-1))
    return result
person,nth = 100,7
print('sequence：',dead_live(person,nth))

def  dead_live(person,nth):
    seq = [i for i in range(person)]
    result = []
    while seq:
        result.append(seq.pop(7))
        if seq:
            result.append(seq.pop(7))
    return result,seq

print('sq：',dead_live(person,nth))
#It should work for random inputs too:
#[1, 'out', 'beware', 2, '!', 'testing', 3, 8, 'pippi', 'watch', 'mighty', 6, 5, 'is']
#[1, 'out', 'beware', 2, '!', 'testing', 3, 8, 'pippi', 'watch', 'mighty', 'is', 6, 5]

