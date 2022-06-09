# https://morioh.com/p/4f4b74ba17cc?f=5c21fb01c16e2556b555ab32
my_string = "aavvccccddddeee"

# converting the string to a set
temp_set = set(my_string)

# stitching set into a string using join
new_string = ''.join(temp_set)

print(new_string)

my_string = "my name is chaitanya baweja"

# using the title() function of string class
new_string = my_string.title()

print(new_string)

# Output
# My Name Is Chaitanya Baweja


# Reversing a string using slicing

my_string = "ABCDE"
reversed_string = my_string[::-1]

print(reversed_string)

# Output
# EDCBA

n = 3  # number of repetitions

my_string = "abcd"
my_list = [1, 2, 3]

print(my_string * n)
# abcdabcdabcd

print(my_list * n)
# [1,2,3,1,2,3,1,2,3]

n = 4
my_list = [0] * n  # n denotes the length of the required list
# [0, 0, 0, 0]

list_of_strings = ['My', 'name', 'is', 'Chaitanya', 'Baweja']

# Using join with the comma separator
print(','.join(list_of_strings))

# Output
# My,name,is,Chaitanya,Baweja


a = 1
b = 2

a, b = b, a

print(a)  # 2
print(b)  # 1


string_1 = "My name is Chaitanya Baweja"
string_2 = "sample/ string 2"

# default separator ' '
print(string_1.split())
# ['My', 'name', 'is', 'Chaitanya', 'Baweja']

# defining separator as '/'
print(string_2.split('/'))
# ['sample', ' string 2']



# Multiplying each element in a list by 2

original_list = [1, 2, 3, 4]

new_list = [2 * x for x in original_list]

print(new_list)
# [2,4,6,8]


my_string = "abcba"

if my_string == my_string[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# Output
# palindrome



my_list = ['a', 'b', 'c', 'd', 'e']

for index, value in enumerate(my_list):
    print('{0}: {1}'.format(index, value))

# 0: a
# 1: b
# 2: c
# 3: d
# 4: e


from collections import Counter

str_1, str_2, str_3 = "acbde", "abced", "abcda"
cnt_1, cnt_2, cnt_3 = Counter(str_1), Counter(str_2), Counter(str_3)

if cnt_1 == cnt_2:
    print('1 and 2 anagram')
if cnt_1 == cnt_3:
    print('1 and 3 anagram')



a, b = 1, 0

try:
    print(a / b)
    # exception raised when b is 0
except ZeroDivisionError:
    print("division by zero")
else:
    print("no exceptions raised")
finally:
    print("Run this always")






#with elements as keys and frequency as values.



# finding frequency of each element in a list
from collections import Counter

my_list = ['a', 'a', 'b', 'b', 'b', 'c', 'd', 'd', 'd', 'd', 'd']
count = Counter(my_list)  # defining a counter object

print(count)  # Of all elements
# Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})

print(count['b'])  # of individual element
# 3

print(count.most_common(1))  # most frequent element
# [('d', 5)]



import sys

num = 21

print(sys.getsizeof(num))

# In Python 2, 24
# In Python 3, 28



import random

my_list = ['a', 'b', 'c', 'd', 'e']
num_samples = 2

samples = random.sample(my_list, num_samples)
print(samples)
# [ 'a', 'e'] this will have any 2 random values

import secrets  # imports secure module.

secure_random = secrets.SystemRandom()  # creates a secure random object.

my_list = ['a', 'b', 'c', 'd', 'e']
num_samples = 2

samples = secure_random.sample(my_list, num_samples)

print(samples)
# [ 'e', 'd'] this will have any 2 random values



import time

start_time = time.time()
# Code to check follows
a, b = 1, 2
c = a + b
# Code to check ends
end_time = time.time()
time_taken_in_micro = (end_time - start_time) * (10 ** 6)

print(" Time taken in micro_seconds: {0} ms").format(time_taken_in_micro)


from iteration_utilities import deepflatten


# if you only have one depth nested_list, use this
def flatten(l):
    return [item for sublist in l for item in sublist]


l = [[1, 2, 3], [3]]
print(flatten(l))
# [1, 2, 3, 3]

# if you don't know how deep the list is nested
l = [[1, 2, 3], [4, [5], [6, 7]], [8, [9, [10]]]]

print(list(deepflatten(l, depth=3)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


dict_1 = {'apple': 9, 'banana': 6}
dict_2 = {'banana': 4, 'orange': 8}

combined_dict = {**dict_1, **dict_2}

print(combined_dict)
# Output
# {'apple': 9, 'banana': 4, 'orange': 8}
