'''
https://www.codewars.com/kata/53da6a7e112bd15cbc000012/train/python
Python dictionaries are inherently unsorted. So what do you
do if you need to sort the contents of a dictionary?

Create a function that returns a sorted list of (key, value)
tuples (Javascript: arrays of 2 items).

The list must be sorted by the value and be sorted largest
to smallest.

Examples
sort_dict({3:1, 2:2, 1:3}) == [(1,3), (2,2), (3,1)]
sort_dict({1:2, 2:4, 3:6}) == [(3,6), (2,4), (1,2)]
'''

def sort_dict(d):
    return sorted(d,key= lambda x:d[x],reverse=True)
d = {3:1, 2:2, 1:3}
d = {1:5, 3:10, 2:2, 6:3, 8:8}
print(sort_dict(d))

def sort_dict(d):
    return sorted(d.items())
d = {3:1, 2:2, 1:3}
d = {1:5, 3:10, 2:2, 6:3, 8:8}
print(sort_dict(d))

def sort_dict(d):
    return sorted([(k,v) for k,v in d.items()],key=lambda x:x[1],reverse=True)
d = {3:1, 2:2, 1:3}
d = {1:5, 3:10, 2:2, 6:3, 8:8}
print(sort_dict(d))

#1st
def sort_dict(d):
  return sorted(d.items(), key=lambda x: x[1], reverse=True)

#3rd
def sort_dict(d):
    'return a sorted list of tuples from the dictionary'
    return sorted(d.items(), key=lambda x: -x[1])