#https://www.codewars.com/kata/row-weights/train/python
'''
Scenario
Several people are standing in a row divided into two teams.
The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

Task
Given an array of positive integers (the weights of the people), return a new array/tuple of two integers, where the first one is the total weight of team 1, and the second one is the total weight of team 2.

Notes
Array size is at least 1.
All numbers will be positive.
Input >> Output Examples
'''

array = [70,58,75,34,91]
array = [50,60,70,80]
array = [100,50]
array = [80]
def row_weights(array):
    return sum(array[0:len(array):2]),sum(array[1:len(array):2])


def row_weights(array):
    return sum(array[::2]), sum(array[1::2])

print(row_weights(array))