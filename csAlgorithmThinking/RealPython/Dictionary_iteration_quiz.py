'''
Python字典迭代测验
交互式测验 ⋅ 8个问题
作者：Aman Middha
字典是Python中最重要和最有用的数据结构之一。学习如何通过字典进行迭代可以帮助你以有效的方式解决各种编程问题。测试一下你对如何更好地使用它们的理解!
在阅读完我们的《如何通过字典进行迭代》教程后，进行这个测验。
该测验包含8个问题，没有时间限制。每一个正确的答案，你会得到1分。测验结束时，你会得到一个总分。最高分是100%。祝您好运!

'''
#以下代码片断的输出结果会是什么？
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key)

'颜色'
'水果'
'宠物'

'蓝色'
'苹果'
'狗'

'''

这是在 Python 中迭代一个字典的最简单方法。只要把它直接放到 for 循环中，就可以了!
在 Python 3.6 及以后的版本中，字典的键和值是按照它们被创建的相同顺序来迭代的。然而，这种行为在不同的 Python 版本中可能有所不同，它取决于 dictionary 的插入和删除历史。
如果你把这种方法和一个小技巧一起使用，那么你可以处理任何字典的键和值。这个技巧包括使用索引操作符 [] 和 dictionary 及其键来获得对值的访问。
>>>
>>> for key in a_dict:
... print(key, '->', a_dict[key])
...
color -> blue
水果 -> 苹果
宠物 -> 狗  
'''


#下面这段代码的输出会是什么？
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog' }
d_items = a_dict.items()
print(d_items)

#[('颜色', '蓝色'), ('水果', '苹果'), ('宠物', '狗')]
#dict_items([('color'), ('fruit'), ('pet')])
#dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])

#('颜色', '蓝色'), ('水果', '苹果'), ('宠物', '狗')

'''
不正确
当你在处理字典时，你很可能想同时处理键和值。在 Python 中遍历字典的最有用的方法之一是使用 .items()，它是一个返回字典项的新视图的方法。
视图可以被迭代以得到它们各自的数据，所以你可以通过使用 .items() 返回的视图对象在 Python 中迭代一个 dictionary。
>>>
'''
for item in a_dict.items():
    print(item)
'''
('颜色', '蓝色')
('水果', '苹果')
('宠物', '狗')

回顾一下。在项目上迭代
考虑一下下面的语句。
如果你只需要处理一个字典的键，那么你可以使用 .key()，这是一个返回一个包含字典键的新视图对象的方法。
这句话是真的还是假的？
错
正确
正确
这句话是真的。如果你只需要处理一个字典的键，那么你可以使用 .key()。
'''


a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
keys = a_dict.keys()
print(keys)
#dict_keys(['color', 'fruit', 'pet'])

'''

由.key()返回的对象在这里提供了一个关于a_dict的键的动态视图。
这个视图可以用来遍历a_dict的键。
回顾一下。遍历键值

在 Python 中，只使用值来遍历一个字典是很常见的。
一种方法是使用 .values()。在下面这个叫做 a_dict 的字典中，
使用这个函数的正确方法是什么？
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

选择所有适用的。
'''
#for value in a_dict.values:
#    print(value)
# TypeError: 'builtin_function_or_method' object is not iterable

for value in a_dict.values():
    print(value)


a_dict.values()


#实现.values()的几种方法之一是以下几种。

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
the_values = a_dict.values()
print(the_values)
#dict_values(['blue', 'apple', 'dog'])

'''

 在前面的代码中，the_values持有一个对包含a_dict的值的视图对象的引用。
作为任何视图对象，由.values()返回的对象也可以被迭代。在这种情况下，.values()得到了a_dict的值。
>>>
'''
for value in a_dict.values():
    print(value)


#回顾一下。遍历键的迭代考虑一下下面的代码片段。
# Python 3. dict.keys() 返回一个视图对象，而不是一个列表
prices = {'苹果': 0.40, 'orange': 0.35, 'banana': 0.25}
for key in prices.key(): #keys()
    if key == 'orange':
        del prices[key]
# AttributeError: 'dict' object has no attribute 'key'
#你需要检查键的删除是否成功。这个程序的控制台输出会是什么？
'''
苹果
橙色
香蕉

RuntimeError: dictionary changed size during iteration
纠正
将不会有输出。
无
对于给定的这段代码，你将面临一个 RuntimeError。
>>>
>> # Python 3. dict.keys() 返回一个视图对象，而不是一个列表
>>> 价格 = {'苹果': 0.40, 'orange': 0.35, 'banana': 0.25}。
>> for key in prices.key():
...如果键=='橘子'。
... del prices[key]
...
回溯（最近一次调用）。
  文件"<input>"，第1行，在<module>中
    for key in pric
'''
'''
回溯（最近一次调用）。
  文件"<input>"，第1行，在<module>中
    for key in prices.key():
RuntimeError: dictionary changed size during iteration

这是因为 .keys() 返回一个 dictionary-view 对象，它一次产生一个键，如果你删除了一个项目 (del prices[key])，那么 Python 会引发一个 RuntimeError，因为你在迭代期间修改了 dictionary。
回顾一下。修改键和值

'''


#到目前为止，你已经接受了在 Python 中迭代字典的基本方法的测试。现在是时候看看你是否可以在迭代过程中对 dictionary 的项进行一些操作。
#下面哪些是使用 dictionary 的正确方法？选择所有适用的。
a_dict = {'一': 1, '二': 2, '三': 3, 'four': 4}
new_dict = {}
for key, value in a_dict:
    if value <= 2:
        new_dict = value

a_dict = {'一': 1, '二': 2, '三': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    new_dict[value] = key

a_dict = {'一': 1, '二': 2, '三': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    if value <= 2:
        new_dict[key] = value

incomes = {'apple': 5600.00, '橙子': 3500.00, '香蕉': 5000.00}
total_income = 0.00
for value in incomes.values():
    total_income += value
''''''

#下面哪些是正确的字典理解？
a_dict = {'一': 1, '二': 2, '三': 3, 'four': 4}
new_dict = {k: v for k, v in a_dict.items if v <= 2}

#不正确:
a_dict = {'一': 1, '二': 2, '三': 3,'四':4}
new_dict = {k: v for k, v in a_dict.items() if v <= 2}

#不正确:
a_dict = {'一': 1, '二': 2, '三': 3, '4': 4}
new_dict = {value: key for key, value in a_dict.items()}

#不正确
category = ['蓝色', '苹果', '狗']
objects = ['颜色', '水果', '宠物']
a_dict = {key: value for key, value in zip(category, objects)}
'''

正确
你会得到以下错误，因为.items()的使用是错误的。
TypeError 回溯（最近的一次调用
  <ipython-input-22-f38d8f8e7a03>在<module>中
        1 a_dict = {'一': 1, '二': 2, '三': 3, 'four': 4}
  ----> 2 new_dict = {k: v for k, v in a_dict.items if v <= 2}

  TypeError: 'buildin_function_or_method' 对象不是可迭代的。

'''
#回顾一下。字典理解

#下面哪个方法不能用来迭代字典中的项目？
import itertools
iter()
filter()
map()
#cycle()
#chain()



# https://realpython.com/iterate-through-dictionary-python/


'''
Python 的 map() 被定义为 map(function, iterable, ...) 
并返回一个迭代器，
该迭代器将函数应用于迭代器的每一个项目，按要求产生结果。

filter() 是一个内置函数，你可以用它来遍历 Python 中的一个字典，并过滤掉其中
的一些项目。这个函数被定义为 filter(function, iterable)，并从那些函数返回 
True 的 iterable 元素中返回一个迭代器。

你可以使用 itertools.cycle(iterable)，它制作一个迭代器，从 iterable 中返
回元素并保存每个元素的副本。当iterable用完时，cycle()从保存的副本中返回元素。

itertools还提供了chain(*iterables)，它获取一些迭代器作为参数，并制作一个迭
代器，从第一个迭代器中获取元素，直到它被耗尽，然后再迭代下一个迭代器，以此类推，
直到所有迭代器被耗尽。
回顾一下。Python 内置函数和库
'''





'''


Python Dictionary Iteration Quiz
Interactive Quiz ⋅ 8 Questions
By Aman Middha
Dictionaries are one of the most important and useful data structures in Python. Learning how to iterate through a Dictionary can help you solve a wide variety of programming problems in an efficient way. Test your understanding on how you can use them better!
Take this quiz after reading our How to Iterate Through a Dictionary tutorial.
The quiz contains 8 questions and there is no time limit. You’ll get 1 point for each correct answer. At the end of the quiz, you’ll receive a total score. The maximum score is 100%. Good luck!

What would be the output of the following code snippet?
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key)

blue
apple
dog

'color'
'fruit'
'pet'

'blue'
'apple'
'dog'

color
fruit
pet

This is the simplest way to iterate through a dictionary in Python. Just put it directly into a for loop, and you’re done!
In Python 3.6 and beyond, the keys and values of a dictionary are iterated over in the same order in which they were created. However, this behavior may vary across different Python versions, and it depends on the dictionary’s history of insertions and deletions.
If you use this approach along with a small trick, then you can process the keys and values of any dictionary. The trick consists of using the indexing operator [] with the dictionary and its keys to get access to the values:
>>>
>>> for key in a_dict:
...     print(key, '->', a_dict[key])
...
color -> blue
fruit -> apple
pet -> dog



What would be the output of the following code snippet?
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
d_items = a_dict.items()
print(d_items)

[('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')]
dict_items([('color'), ('fruit'), ('pet')])
dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])
Incorrect
('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')
Incorrect
When you’re working with dictionaries, it’s likely that you’ll want to work with both the keys and the values. One of the most useful ways to iterate through a dictionary in Python is by using .items(), which is a method that returns a new view of the dictionary’s items.
Views can be iterated over to yield their respective data, so you can iterate through a dictionary in Python by using the view object returned by .items():
>>>
>>> for item in a_dict.items():
...     print(item)
...
('color', 'blue')
('fruit', 'apple')
('pet', 'dog')

Review: Iterating Over Items


Consider the following statement:
If you just need to work with the keys of a dictionary, then you can use .keys(), which is a method that returns a new view object containing the dictionary’s keys.
Is this statement True or False?
False
True
Correct
The statement is True. If you just need to work with the keys of a dictionary, then you can use .keys().
>>>
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> keys = a_dict.keys()
>>> print(keys)
dict_keys(['color', 'fruit', 'pet'])

 The object returned by .keys() here provided a dynamic view on the keys of a_dict. This view can be used to iterate through the keys of a_dict.
Review: Iterating Over Keys

It’s common to only use the values to iterate through a dictionary in Python. One way to do that is to use .values(). What are correct ways to use the function given the following dictionary called a_dict?
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

Select all that apply:
for value in a_dict.values:
    print(value)

for value in a_dict.values():
    print(value)

Correct
a_dict.values()

Correct
One of the few ways to implement .values() are the following:
>>>
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> the_values = a_dict.values()
>>> the_values
dict_values(['blue', 'apple', 'dog'])

 In the previous code, the_values holds a reference to a view object containing the values of a_dict.
As any view object, the object returned by .values() can also be iterated over. In this case, .values() yields the values of a_dict:
>>>
>>> for value in a_dict.values():
...     print(value)
...
blue
apple
dog

Review: Iterating Over Keys
Consider the following code snippet:
# Python 3. dict.keys() returns a view object, not a list
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for key in prices.keys():
    if key == 'orange':
        del prices[key]

You need to check if the key deletion is successful. What would be the console output of this program?
apple
orange
banana

RuntimeError: dictionary changed size during iteration
Correct
There will be no output.
None
You will face a RuntimeError for the given piece of code.
>>>
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

This is because .keys() returns a dictionary-view object, which yields keys on demand one at a time, and if you delete an item (del prices[key]), then Python raises a RuntimeError, because you’ve modified the dictionary during iteration.
Review: Modifying Keys and Values


So far, you’ve been tested on the more basic ways of iterating through a dictionary in Python. Now it’s time to see if you can perform some actions with the items of a dictionary during iteration.
Which of the following are correct ways to use a dictionary? Select all that apply:
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for key, value in a_dict:
    if value <= 2:
        new_dict = value

a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    new_dict[value] = key

Correct
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    if value <= 2:
        new_dict[key] = value

Correct
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = 0.00
for value in incomes.values():
    total_income += value

Correct
You’d get the following error since dict has too many values with respect to the number of target variables.
ValueError    Traceback (most recent call last)
<ipython-input-21-7de594743862> in <module>
        1 a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
        2 new_dict = {}
  ----> 3 for key, value in a_dict:
        4     if value <= 2:
        5         new_dict = value

  ValueError: too many values to unpack (expected 2)

The other issue with the code is that it would assign a variable value to new_dict, based on the if condition, instead of performing an action on the dictionary values.
Review: Real-World Examples

Which of the following are correct dictionary comprehensions?
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {k: v for k, v in a_dict.items if v <= 2}

Incorrect
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {k: v for k, v in a_dict.items() if v <= 2}

Incorrect
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {value: key for key, value in a_dict.items()}

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

Which one of the following methods can’t be used to iterate over items in a dictionary?
iter()
Correct
filter()
map()
cycle()
chain()
Python’s map() is defined as map(function, iterable, ...) and returns an iterator that applies function to every item of iterable, yielding the results on demand.
filter() is a built-in function that you can use to iterate through a dictionary in Python and filter out some of its items. This function is defined as filter(function, iterable) and returns an iterator from those elements of iterable for which function returns True.
You can use itertools.cycle(iterable), which makes an iterator returning elements from iterable and saving a copy of each. When iterable is exhausted, cycle() returns elements from the saved copy.
itertools also provides chain(*iterables), which gets some iterables as arguments and makes an iterator that yields elements from the first iterable until it’s exhausted, then iterates over the next iterable and so on, until all of them are exhausted.
Review: Python Built-In Functions and Libraries

'''