'''
https://www.codewars.com/kata/596f28fd9be8ebe6ec0000c1/train/python

A list of integers is sorted in “Wave” order if alternate items are not less than their
immediate neighbors (thus the other alternate items are not greater than their immediate
neighbors).

Thus, the array [4, 1, 7, 5, 6, 2, 3] is in Wave order because 4 >= 1, then 1 <= 7, then
7 >= 5, then 5 <= 6, then 6 >= 2, and finally 2 <= 3.

The wave-sorted lists has to begin with an element not less than the next, so [1, 4, 5, 3]
 is not sorted in Wave because 1 < 4

Your task is to implement a function that takes a list of integers and sorts it into wave
order in place; your function shouldn't return anything.

Note:

The resulting array shouldn't necessarily match anyone in the tests, a function just checks
if the array is now wave sorted.
ALGORITHMSARRAYS
'''


def wave_sort(a):
    if len(a) > 1 and a[0] < a[1]:
        return False
    return all(a[i-1] >= a[i] <= a[i+1] for i in range(1, len(a) - 1, 2))

a = [1, 2]
print(wave_sort(a))