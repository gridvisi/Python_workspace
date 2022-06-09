'''
https://www.codewars.com/kata/5747fcfce2fab91f43000697/train/python

Given an Array and an Example-Array to sort to, write a
function that sorts the Array
following the Example-Array.

Assume Example Array catalogs all elements possibly seen
in the input Array. However,
the input Array does not necessarily have to have all
elements seen in the Example.

Example:

Arr: [1,3,4,4,4,4,5]

Example Arr: [4,1,2,3,5]

Result: [4,4,4,4,1,3,5]

FUNDAMENTALSARRAYSSORTINGALGORITHMS
'''

def example_sort(arr, example_arr):
    return sorted(arr,key=lambda x:example_arr.index(x))

arr,example_arr = [1,2,3,3,3,5],[3,4,5,6,9,11,12,13,1,7,8,2,10]
print(example_sort(arr, example_arr))

#1st
def example_sort(arr, example_arr):
    return sorted(arr, key=example_arr.index)