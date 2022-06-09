'''
https://www.geeksforgeeks.org/python-make-pair-from-two-list-such-that-elements-are-not-same-in-pairs/?ref=rp

Input : list1 = [100, 20, 30, 400]
        list2 = [400, 2, 30]
Output:
[[100, 400], [100, 2], [100, 30],
 [20, 400], [20, 2], [20, 30],
 [30, 400], [30, 2], [400, 2], [400, 30]]

Input: list1 = [10,20,30,40]
       list2 = [60, 10, 20]
Output:
[[10, 60], [10, 20], [20, 60], [20, 10],
 [30, 60], [30, 10], [30, 20],
 [40, 60], [40, 10], [40, 20]]

'''

# Python code to create pair of element
# from two list such that element
# in pairs are not equal.

# List initialization
list1 = [10, 20, 30, 40]
list2 = [40, 50, 60]

# using list comprehension
output = [[a, b] for a in list1
          for b in list2 if a != b]

# printing output
print(output)

# Python code to create pair of element
# from two list such that element
# in pairs are not equal.


# Method #2: Using itertools and iteration
# Importing
import itertools

# List initialization
list1 = [11, 22, 33, 44]
list2 = [22, 44, 66]

# using itertools
temp = list(itertools.product(list1, list1))

# output list initialization
out = []

# iteration
for elem in temp:
    if elem[0] != elem[1]:
        out.append(elem)

# printing output
print(out)