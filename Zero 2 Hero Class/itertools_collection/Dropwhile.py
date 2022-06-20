#https://www.geeksforgeeks.org/python-itertools-dropwhile/
#Dropwhile
# Python code to demonstrate the working of
# dropwhile()


# Function to be passed
# as an argument
from itertools import dropwhile
import itertools
def is_positive(n):
    return n > 0


value_list = [5, 6, -8, -4, 2]
result = list(itertools.dropwhile(is_positive, value_list))

print(result)


#2
# Python code to demonstrate the working of
# dropwhile()


import itertools

# initializing list
li = [2, 4, 5, 7, 8]

# using dropwhile() to start displaying after condition is false
print("The values after condition returns false : ", end="")
print(list(itertools.dropwhile(lambda x: x % 2 == 0, li)))