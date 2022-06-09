'''
https://www.codewars.com/kata/55aea0a123c33fa3400000e7/train/python

Sort array by last character

Complete the function to sort a given array or list by last character of elements.

Element can be an integer or a string.

Example:
['acvd', 'bcc']  -->  ['bcc', 'acvd']
The last characters of the strings are d and c. As c comes before d, sorting by last character will give ['bcc', 'acvd'].

If two elements don't differ in the last character, then they should be sorted by the order they come in the array.
'''

def sort_me(arr):
    return sorted(arr,key=lambda x:x[-1])

#1st
def sort_me(arr):
    return sorted(arr, key=lambda elem: str(elem)[-1])