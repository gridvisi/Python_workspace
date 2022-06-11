'''
https://www.codewars.com/kata/54f9c37106098647f400080a/train/python
'''


def drop_while(arr, pred):
    # your code here
    res = []
    for i, x in enumerate(arr):
        if pred(x):
            pass
        else:
            return arr[i:]
    return []

#1st
from itertools import dropwhile

def drop_while(arr, pred):
    return list(dropwhile(pred, arr))


#2nd
def drop_while(arr, pred):
    for i, v in enumerate(arr):
        if pred(v):
            continue
        else:
            return arr[i:]
    return []

# relate case_study

from itertools import takewhile

def take_while(arr, pred_fun):
    return list(takewhile(pred_fun, arr))

def take_while(arr, pred_fun):
    res = []
    for x in arr:
        if pred_fun(x):
            res.append(x)
        else:
            break
    return res
