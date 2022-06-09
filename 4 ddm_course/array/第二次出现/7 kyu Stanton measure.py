'''
https://www.codewars.com/kata/59a1cdde9f922b83ee00003b/train/python

The Stanton measure of an array is computed as follows: count the number of 1s in
the array. Let this count be n. The Stanton measure is the number of times that n
appears in the array.

Write a function which takes an integer array and returns its Stanton measure.

Example
The Stanton measure of [1, 4, 3, 2, 1, 2, 3, 2] is 3, because 1 occurs 2 times in
the array and 2 occurs 3 times.

FUNDAMENTALSARRAYS
'''

def stanton_measure(arr):
    return max([arr.index(e) for e in arr])
arr = [1, 4, 3, 2, 1, 2, 3, 2]
print(stanton_measure(arr))

from collections import Counter
def stanton_measure(arr):
    arrCunt = Counter(arr).items()
    return [v for k,v in arr if k == v]

from collections import Counter
def stanton_measure(arr):
    arrCunt = Counter(arr).items()
    return max(arrCunt)
arr = [1, 4, 3, 2, 1, 2, 3, 2]
print(stanton_measure(arr))