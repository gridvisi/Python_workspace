# https://realpython.com/quizzes/python-split-strings/viewer/
# https://realpython.com/quizzes/

#1
'''

In Python, strings are…


changeable


immutable

Correct

char arrays


str objects
'''

#2
'''
The minsplit parameter to split() specifies the minimum number of splits to make to the input string.


False

Incorrect

True

Incorrect

split() takes in two parameters: sep, the delimiter 
string, and maxsplit, which specifies the maximum number 
of splits to make on the input string.
'''

#3
'''
Which of the following would separate a string input_string on the first 2 occurences of the letter “e”?


'e'.split(input_string, 2)


'e'.split(input_string, maxsplit=2)


input_string.split('e', 2)

Correct

input_string.split('e', maxsplit=2)
'''
input_string = 'chineeeeseee'
print(input_string.split('e', maxsplit=2))
print(input_string.split('e', maxsplit=5))
print(input_string.split('e', 2))
print(input_string.split('e'))
#4
'''
Write the code for a Python function expand(x) that takes a list of strings, concatenates them, and returns the resulting string repeated three times.

Example 1:

Input: ['string1', 'string2']
Output: 'string1string2string1string2string1string2'
Example 2:

Input: ['a', 'b', 'c']
Output: 'abcabcabc'
''.join(input)*3
Incorrect
TypeError: 'builtin_function_or_method' object is not iterable

This is what we expected to see:
def expand(x):
    return ''.join(x) * 3
'''
def expand(x):
    return ''.join(x) * 3

#5
'''
Python strings have a property called “immutability.” 
What does this mean?

You can update a string in Python with concatenation
Strings in Python can be represented as arrays of chars


Strings in Python can’t be changed

Correct

Strings can’t be divided by numbers


Immutability is a key property of strings as implemented 
in Python. While it is true that strings can’t be divided 
by numbers, that is not the meaning of immutability. 

Instead, immutability means that strings can not be 
changed.

不变性是Python中实现的字符串的一个关键属性。虽然字符串确实不能被数字分割，
但这并不是不变性的含义。相反，不可变性意味着字符串不能被改变。
'''

#6
'''
If you want to transform a list of strings input_list into a single string with 
a comma between each item, which of the following would you give as the input to join()?


input_list
Incorrect
string
','
Incorrect
str

The list to join is always the sole input to join(), 
which is called on the string you want to join with.

>>> input_list = ['a', 'b', 'c']
>>> ','.join(input_list)
'a,b,c'
'''

input_list = ['a', 'b', 'c']
print(','.join(input_list))
'a,b,c'
print(','.join(['a', 'b', 'c']))

#7
'''
Which of the following mathematical operators can be used to concatenate strings:


/


*

Incorrect

+

Correct

-


Concatenation is an additive operation, so you can not 
subtract or divide strings from each other.
'''

print('string')