'''
https://www.codewars.com/kata/57741d8f10a0a66915000001/train/python

Write a function that accepts two arguments: an array/list of integers and another integer (n).

Determine the number of times where two integers in the array have a difference of n.

For example:

[1, 1, 5, 6, 9, 16, 27], n=4  -->  3  # (1,5), (1,5), (5,9)
[1, 1, 3, 3], n=2             -->  4  # (1,3), (1,3), (1,3), (1,3)
'''

def int_diff(lst, n):
    exp,lst = [],sorted(lst)
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i]-lst[j]==-n:
                exp.append([lst[i],lst[j]])

    return len(exp)
lst, n = [1, 1, 5, 6, 9, 16, 27], 4
print(int_diff(lst, n))


#1st
import itertools

def int_diff(arr, n):
    return sum(abs(a-b) == n for a, b in itertools.combinations(arr, 2))

#2nd
int_diff=lambda l,n:sum(n==abs(a-b)for i,a in enumerate(l)for b in l[:i])







# Not good so fail!
def int_diff(lst, n):
    res,i,j = [],0,0
    lst = sorted(lst)
    while i < len(lst)-1:

        if lst[i] - lst[j] == -n:
            res.append([lst[i],lst[j]])
        #j += 1
        else:
            if i < len(lst)-1 and j == len(lst)-1:
                i += 1
            elif i < len(lst)-1 and j < len(lst)-1:
                j += 1
            elif i == j == len(lst)-1:
                return len(res),res



