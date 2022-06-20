
#https://realpython.com/quizzes/python-dictionary-iteration/viewer/
'''
What would be the output of the following code snippet?

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key)

blue
apple
dog

'blue'
'apple'
'dog'

color
fruit
pet
Incorrect

'color'
'fruit'
'pet'
Incorrect

This is the simplest way to iterate through a dictionary in Python. Just put it directly into a for loop, and you’re done!

In Python 3.6 and beyond, the keys and values of a dictionary are iterated over in the same order in which they were created. However, this behavior may vary across different Python versions, and it depends on the dictionary’s history of insertions and deletions.

If you use this approach along with a small trick, then you can process the keys and values of any dictionary. The trick consists of using the indexing operator [] with the dictionary and its keys to get access to the values:

>>> for key in a_dict:
...     print(key, '->', a_dict[key])
...
color -> blue
fruit -> apple
pet -> dog
Review: Basics of Iterating Through a Dictionary

'''


#2
'''
What would be the output of the following code snippet?

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
d_items = a_dict.items()
print(d_items)

dict_items([('color'), ('fruit'), ('pet')])


('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')


dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])

Correct

[('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')]


When you’re working with dictionaries, it’s likely that you’ll want to work with both the keys and the values. One of the most useful ways to iterate through a dictionary in Python is by using .items(), which is a method that returns a new view of the dictionary’s items.

Views can be iterated over to yield their respective data, so you can iterate through a dictionary in Python by using the view object returned by .items():

>>> for item in a_dict.items():
...     print(item)
...
('color', 'blue')
('fruit', 'apple')
('pet', 'dog')
Review: Iterating Over Items
'''

#3
'''
Consider the following statement:

If you just need to work with the keys of a dictionary, then you can use .keys(), which is a method that returns a new view object containing the dictionary’s keys.

Is this statement True or False?


True

Correct

False


The statement is True. If you just need to work with the keys of 
a dictionary, then you can use .keys().

>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> keys = a_dict.keys()
>>> print(keys)
dict_keys(['color', 'fruit', 'pet'])
The object returned by .keys() here provided a dynamic view on the 
keys of a_dict. This view can be used to iterate through the keys of a_dict.
Review: Iterating Over Keys
'''

#4
'''
It’s common to only use the values to iterate through a dictionary in Python. 
One way to do that is to use .values(). 

What are correct ways to use the function given the following dictionary 
called a_dict?

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
Select all that apply:


a_dict.values()
Incorrect

for value in a_dict.values():
    print(value)
Correct

for value in a_dict.values:
    print(value)

One of the few ways to implement .values() are the following:

>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> the_values = a_dict.values()
>>> the_values
dict_values(['blue', 'apple', 'dog'])

In the previous code, the_values holds a reference to a view object 
containing the values of a_dict.
As any view object, the object returned by .values() can also be 
iterated over. In this case, .values() yields the values of a_dict:

>>> for value in a_dict.values():
...     print(value)
...
blue
apple
dog
Review: Iterating Over Keys
'''

#5
'''
Consider the following code snippet:

# Python 3. dict.keys() returns a view object, not a list
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for key in prices.keys():
    if key == 'orange':
        del prices[key]
You need to check if the key deletion is successful. 
What would be the console output of this program?


None


There will be no output.


RuntimeError: dictionary changed size during iteration

Correct

apple
orange
banana

You will face a RuntimeError for the given piece of code.

>>> # Python 3. dict.keys() returns a view object, not a list
>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> for key in prices.keys():
...     if key == 'orange':
...         del prices[key]
...
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    for key in prices.keys():
RuntimeError: dictionary changed size during iteration
This is because .keys() returns a dictionary-view object, 
which yields keys on demand one at a time, and if you delete an 
item (del prices[key]), then Python raises a RuntimeError, 
because you’ve modified the dictionary during iteration.

Review: Modifying Keys and Values
'''

#6
'''
So far, you’ve been tested on the more basic ways of iterating through 
a dictionary in Python. Now it’s time to see if you can perform some 
actions with the items of a dictionary during iteration.

Which of the following are correct ways to use a dictionary? 
Select all that apply:


a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {} 
for key, value in a_dict.items():
    if value <= 2:
        new_dict[key] = value
Correct

a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    new_dict[value] = key
Correct

incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = 0.00
for value in incomes.values():
    total_income += value
Correct

a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {} 
for key, value in a_dict:
    if value <= 2:
        new_dict = value

You’d get the following error since dict has too many values with respect to the number of target variables.

ValueError    Traceback (most recent call last)
<ipython-input-21-7de594743862> in <module>
        1 a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
        2 new_dict = {}
  ----> 3 for key, value in a_dict:
        4     if value <= 2:
        5         new_dict = value

  ValueError: too many values to unpack (expected 2)
The other issue with the code is that it would assign a variable value 
to new_dict, based on the if condition, instead of performing an action 
on the dictionary values.

Review: Real-World Examples
'''

#7
'''
Which of the following are correct dictionary comprehensions?


a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {value: key for key, value in a_dict.items()}
Correct

a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {k: v for k, v in a_dict.items() if v <= 2}
Correct

a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {k: v for k, v in a_dict.items if v <= 2}
Incorrect

objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']
a_dict = {key: value for key, value in zip(categories, objects)}
Correct

You’d get the following error since .items() is used incorrectly:

TypeError        Traceback (most recent call last)
  <ipython-input-22-f38d8f8e7a03> in <module>
        1 a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
  ----> 2 new_dict = {k: v for k, v in a_dict.items if v <= 2}

  TypeError: 'builtin_function_or_method' object is not iterable
Review: Dictionary Comprehensions
'''

#8
'''
Which one of the following methods can’t be used to iterate over items 
in a dictionary?


iter()

Incorrect

chain()


filter()


cycle()


map()

Incorrect

Python’s map() is defined as map(function, iterable, ...) and returns an 
iterator that applies function to every item of iterable, yielding the 
results on demand.
filter() is a built-in function that you can use to iterate through a 
dictionary in Python and filter out some of its items. 

This function is defined as filter(function, iterable) and returns an 
iterator from those elements of iterable for which function returns True.
You can use itertools.cycle(iterable), which makes an iterator returning 
elements from iterable and saving a copy of each. When iterable is exhausted, 
cycle() returns elements from the saved copy.

itertools also provides chain(*iterables), which gets some iterables as 
arguments and makes an iterator that yields elements from the first 
iterable until it’s exhausted, then iterates over the next iterable 
and so on, until all of them are exhausted.

Review: Python Built-In Functions and Libraries
'''
