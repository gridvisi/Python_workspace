'''
https://www.codewars.com/kata/5ff22b6e833a9300180bb953/train/python

Given a list of numbers of all types, find the positive difference between each
consecutive pair of numbers, and put this into a new list of differences.
Then, find the differences between consecutive pairs in this new list, and repeat
until the list has a length of 1. Then, return the single value.

The list will only contain numbers. If it is empty, return 0.

For example:

differences([1, 2, 3]) => [1, 1] => [0] => 0
differences([1, 5, 2, 7, 8, 9, 0]) => [4, 3, 5, 1, 1, 9] => [1, 2, 4, 0, 8] => ... => 1
differences([1.5, 2.5, 1]) => [1, 1.5] => 0.5
'''

#7th solve by ericlee
def differences(lst):
    if len(lst) <= 1: return 0
    while len(lst) > 1:
        lst = [abs(x - y) for x, y in zip(lst[:-1], lst[1:])]
    return lst[0]


lst = [1, 5, 2, 7, 8, 9, 0]
print(differences(lst))

#1st
def differences(lst):
    if len(lst)<2: return lst[0] if lst else 0
    return differences([abs(b-a) for a,b in zip(lst, lst[1:])])

