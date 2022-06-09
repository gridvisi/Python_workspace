#Python dict

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key)

'blue'
'apple'
'dog'

'color'
'fruit'
'pet'

'blue'
'apple'
'dog'

'color'
'fruit'
'pet'

#2
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
d_items = a_dict.items()
print(d_items)

#1 ('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')
#Incorrect
#2 [('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')]
#3 dict_items([('color'), ('fruit'), ('pet')])
#4 dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])

for item in a_dict.items():
   print(item)

#1 ('color', 'blue')
#2 ('fruit', 'apple')
#3 ('pet', 'dog')

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
keys = a_dict.keys()
print(keys)
#dict_keys(['color', 'fruit', 'pet'])

#Three problem
'''
Consider the following statement:
If you just need to work with the keys of a dictionary, then you can use .keys(), 
which is a method that returns a new view object containing the dictionary’s keys.
Is this statement True or False?
False
True
Correct
'''

# The fourth problem
#Consider the following code snippet:
# Python 3. dict.keys() returns a view object, not a list
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for key in prices.keys():
    if key == 'orange':
        del prices[key]

'''
You need to check if the key deletion is successful. What would be the console 
output of this program?
1:RuntimeError: dictionary changed size during iteration
Correct
2:apple,orange.banana
3:None
'''

# the fifth problem
#It’s common to only use the values to iterate through a dictionary in Python.
# One way to do that is to use .values(). What are correct ways to use the function given the following dictionary called a_dict?
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

#Select all that apply:
for value in a_dict.values:
    print(value)

for value in a_dict.values():
    print(value)

#Correct
a_dict.values()
#Incorrect
#One of the few ways to implement .values() are the following:

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
the_values = a_dict.values()
the_values
#dict_values(['blue', 'apple', 'dog'])

# In the previous code, the_values holds a reference to a view object containing
# the values of a_dict.
# As any view object, the object returned by .values() can also be iterated over.
# In this case, .values() yields the values of a_dict:

for value in a_dict.values():
   print(value)
# blue apple dog
# Review: Iterating Over Keys


#The sixth problem
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = 0.00
for value in incomes.values():
    total_income += value

#Correct
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    new_dict[value] = key

#Correct
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for key, value in a_dict:
    if value <= 2:
        new_dict = value

a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    if value <= 2:
        new_dict[key] = value

#Correct

#You’d get the following error since dict has too many values with respect to the number of target variables.
#ValueError    Traceback (most recent call last)
#<ipython-input-21-7de594743862> in <module>

a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for key, value in a_dict:
     if value <= 2:
         new_dict = value

#ValueError: too many values to unpack (expected 2)
#The other issue with the code is that it would assign a variable value
# to new_dict, based on the if condition, instead of performing an action
# on the dictionary values.


#Which of the following are correct dictionary comprehensions
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {value: key for key, value in a_dict.items()}

#Correct
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {k: v for k, v in a_dict.items if v <= 2}

a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {k: v for k, v in a_dict.items() if v <= 2}

#Correct
objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']
a_dict = {key: value for key, value in zip(categories, objects)}


b_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {k: v for k, v in b_dict.items if v <= 2}