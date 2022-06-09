'''
Implement a method power_set(s) that takes a set s and returns its power set: a set of all subsets of s including s and the empty set.

Example
If S is the set [x, y, z], then the subsets of S are:

[] # the empty set
[x]
[y]
[z]
[x, y]
[x, z]
[y, z]
[x, y, z] # S
'''

def powers(lst):
    n = len(lst)
    return 2**n