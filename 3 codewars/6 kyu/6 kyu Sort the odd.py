'''
https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/python
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example
sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
'''
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]

def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]

def sort_array(arr):
    odds = iter(sorted((n for n in arr if n & 1)))
    return [next(odds) if n & 1 else n for n in arr]

import numpy as np
def sort_array(source_array):
    arr = np.array(source_array)
    arr[arr % 2 == 1] = np.sort(arr[arr % 2 == 1])
    return arr.tolist()

def sort_array(source_array):
    odds = []
    answer = []
    for i in source_array:
        if i % 2 > 0:
            odds.append(i)
            answer.append("X")
        else:
            answer.append(i)

    odds.sort()
    for i in odds:
        x = answer.index("X")
        answer[x] = i
    return answer

from collections import deque

def sort_array(array):
    odd = deque(sorted(x for x in array if x % 2))
    return [odd.popleft() if x % 2 else x for x in array]

def sort_array(source_array):
    odd = sorted(list(filter(lambda x: x % 2, source_array)))
    l, c = [], 0
    for i in source_array:
        if i in odd:
            l.append(odd[c])
            c += 1
        else:
            l.append(i)
    return l

def sort_array(source_array):
    result = sorted([l for l in source_array if l % 2 == 1])
    for index, item in enumerate(source_array):
        if item % 2 == 0:
            result.insert(index, item)
    return result

def sort_array(source_array):
    odd_list = sorted([x for x in source_array if x%2 != 0], reverse=False)
    return [odd_list.pop(0) if x%2 != 0 else x for x in source_array]

