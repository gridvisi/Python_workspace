'''
https://www.codewars.com/kata/557a2c136b19113912000010/train/python

You have to create a function named reverseIt.

Write your function so that in the case a string or a number is passed
in as the data , you will return the data in reverse order.
If the data is any other type, return it as it is.

Examples of inputs and subsequent outputs:

"Hello" -> "olleH"

"314159" -> "951413"

[1,2,3] -> [1,2,3]


'''

# not good try due to isdigt
def reverse_it(data):
    if not data or type(data)==bool:return data
    elif isinstance(data,int):
        return int(str(data)[::-1])
    elif isinstance(data,str):
        return data[::-1]
    elif isinstance(data,float):
        return float(str(data)[::-1])
# AttributeError: 'int' object has no attribute 'isdigit'
data = 'True'
data = True
print(reverse_it(data))

#1st
def reverse_it(data):
    if type(data) in [int, str, float]:
        return type(data)(str(data)[::-1])
    return data

#2nd
def reverse_it(data):
    t = type(data)
    return t(''.join(reversed(str(data)))) if t in [str, int, float] else data

#3rd
def reverse_it(data):
    t = type(data)
    if t not in (str, float, int):
        return data
    return t(str(data)[::-1])