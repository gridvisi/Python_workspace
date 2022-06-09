'''
https://www.codewars.com/kata/5340298112fa30e786000688/train/python
The objective is to return all pairs of integers from a given collection of integers
that have a difference of 2.
The result should be sorted in ascending order.
The input will consist of unique values. The order of the integers in the input
collection should not matter.

Examples
[1, 2, 3, 4]      -->  [[1, 3], [2, 4]]
[4, 1, 2, 3]      -->  [[1, 3], [2, 4]]
[1, 23, 3, 4, 7]  -->  [[1, 3]]
[4, 3, 1, 5, 6]   -->  [[1, 3], [3, 5], [4, 6]]
'''
lst = [4, 3, 1, 5, 6]
def twos_difference(lst):
    re = []
    res = [[x,x+2] for x in lst if x+2 in lst]
    return sorted(res)

def twos_difference(a):
    s = set(a)
    return sorted((x, x + 2) for x in a if x + 2 in s)
print(twos_difference(lst))