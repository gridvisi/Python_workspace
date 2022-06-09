'''
https://www.geeksforgeeks.org/python-program-to-convert-camel-case-string-to-snake-case/?ref=rp

Given a string in camel case, write a Python program to convert the given string from camel case to snake case.
Examples:

Input : GeeksForGeeks
Output : geeks_for_geeks

Input : ThisIsInCamelCase
Output : this_is_in_camel_case
Let’s see the different ways we can do this task.
Method #1 : Naive Approach
This is a naive implementation to convert camel case to snake case. First, we initialize a variable ‘res’ with an empty list and append first character (in lower case) to it. Now, Each time we encounter a Capital alphabet, we append ‘_’ and the alphabet (in lower case) to ‘res’, otherwise, just append the alphabet only.


'''


# Python3 program to convert string
# from camel case to snake case

def change_case(str):
    res = [str[0].lower()]
    for c in str[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)

    return ''.join(res)
#1
str = "GeeksForGeeks"
print(change_case(str))

#Method #2 : List comprehension
# Python3 program to convert string
# from camel case to snake case

def change_case(str):
    return ''.join(['_' + i.lower() if i.isupper()
                    else i for i in str]).lstrip('_')
#2 Driver code
str = "GeeksForGeeks"
print(change_case(str))

'''
Method #3 : Python reduce()
Python reduce() method applies a function to all the string alphabets, 
that wherever it find uppercase alphabet, it add ‘_’ in front of it and 
replace the uppercase alphabet with lowercase alphabet. 
'''
# Python3 program to convert string
# from camel case to snake case
from functools import reduce


def change_case(str):
    return reduce(lambda x, y: x + ('_' if y.isupper() else '') + y, str).lower()

#3 Driver code
str = "GeeksForGeeks"
print(change_case(str))

#Method #4 : Python Regex
# Python3 program to convert string
# from camel case to snake case
import re


def change_case(str):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


# Driver code
str = "GeeksForGeeks"
print(change_case(str))
