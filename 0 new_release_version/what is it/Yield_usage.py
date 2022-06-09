#https://blog.csdn.net/u011318077/article/details/93749143

fruit = ('apple','banana','carrot','grapes')
num_stock = ('20','17','10','10')
num = (int(i) for i in num_stock)
print(num)
print(list(num))

num = [int(i) for i in num_stock]
print(num)

fruit_stock = dict(zip(fruit,num))
print(fruit_stock)

sell_out = ('10','10','5','8')
sell_out = [-int(i) for i in sell_out]
fruit_sell = dict(zip(fruit,sell_out))
balance = fruit_stock.update(fruit_sell)
print(balance,fruit_stock)

fruit_stock = dict(zip(fruit,num))
print('**',dict(fruit_sell,**fruit_sell))

fruit_stock = dict(zip(fruit,num))
print((fruit_stock.items(),fruit_sell.items()))

balance = [(x+y) for x,y in zip(fruit_stock.values(),fruit_sell.values())]
print(dict(zip(fruit_stock.keys(),balance)))
print(dict(zip(fruit_stock.items(),balance)))

id = ['13701183019','sim','Lijing','VIP']
sort_pattern = lambda c:(c,c[1].islower(),c.isdigit(),c[0].isupper())
print(sorted(id,key=sort_pattern))

id = ['china','14b','Panda','DRAGON']
sort_pattern = lambda c:(c[0].isdigit(),c[1].islower(),c[0].isupper())
print(sorted(id))
print(sorted(id,key=sort_pattern))

id = ['china','14b','Panda','DRAGON','Rmb']
sort_pattern = lambda c:(c[0].isdigit(),c[0:1].islower(),c.isupper())
print(sorted(id,key=sort_pattern))


# dict
'''
Updating Dictionary in Python 3.9
Python 3.9 is under active development and scheduled to be released in October this year. On Feb 26, the development team released its alpha 4 version. One of the new features, relevant to almost all Python programmers, is the introducing of new merge (|) and update (|=) operators.
Let’s take a quick peek what this is in this article.
Dictionaries
Dictionaries, commonly known as dict, are one of the most important built-in data types in Python . This data type is a flexibly-sized collection of key-value pairs, and it’s best known for having a constant time for data lookup because of its hashing implementation.
Here are some common usages:
# Declare a dict
'''

student = {'name': 'John', 'age': 14}

# Get a value
age = student['age']
# age is 14

# Update a value
student['age'] = 15
# student becomes {'name': 'John', 'age': 15}

# Insert a key-value pair
student['score'] = 'A'
# student becomes {'name': 'John', 'age': 15, 'score': 'A'}

'''
Merging Dictionaries — Old Ways
Sometimes, we need to merge two dictionaries for further processing. Prior to the official release of 3.9, there are several ways we can do this. Suppose we have two dicts: d1and d2. We want to create a new dict called d3, a union of d1 and d2. To illustrate what we shall do if there are some overlapping keys between the merging dicts, we have another dict d2a, which has an overlapping key with d1.
# two dicts to start with
'''

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d2a = {'a': 10, 'c': 3, 'd': 4}

# target dict
d3 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

'''
Using the update() method
The first way is to use the dict’s method update(). The following code snippet shows you how to do it. Note that we’ll have to create a copy of d1 first, as the update()function will modify the original dict.
# create a copy of d1, as update() modifies the dict in-place
'''
# d3 is {'a': 1, 'b': 2}

# update the d3 with d2
d3.update(d2)
# d3 now is {'a': 1, 'b': 2, 'c': 3, 'd': 4}
'''
When there are overlapping keys, we have to be more cautious regarding which 
values are to be kept. As you can see below, the dict that is passed as the 
argument in the update() method will “win” the game by having the value (i.e., 10) 
for the overlapping key (i.e., ‘a’).
'''
d3 = d1.copy()
d3.update(d2a)
# d3 now is {'a': 10, 'b': 2, 'c': 3, 'd': 4}
# This is not the way that we want

d3 = d2a.copy()
d3.update(d1)
# d3 now is {'a': 1, 'c': 3, 'd': 4, 'b': 2}
# This is the way that we want

d3 = {**d1, **d2}
# d3 is {'a': 10, 'b': 2, 'c': 3, 'd': 4}
# Not right

d3 = {**d2a, **d1}
# d3 is {'a': 1, 'c': 3, 'd': 4, 'b': 2}
# Good

'''
Using dict(iterable, **kwarg)
One way to create a dict in Python is using the dict(iterable, **kwarg) method. 
Specifically relevant to the current topic is that when the iterable is a dict, 
a new dict will be created with the same key-value pairs. For the keyword arguments,
 we can pass another dict such that it will add the key-value pairs to the dict that 
 is going to create. Note that this keyword argument dict will replace the value with 
 the same key — something like “last seen wins.” Please see below for an example.
'''
d3 = dict(d1, **d2)
# d3 is {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Good, it's what we want

d3 = dict(d1, **d2a)
# d3 is {'a': 10, 'b': 2, 'c': 3, 'd': 4}
# Not right, 'a' value got replaced

'''
One thing to note is that this method only works when the keyword argument dict has 
strings as their keys. Like below, a dict using an intas its key won’t work.
'''
dict({'a': 1}, **{2: 3})
#Traceback (most recent call last):  File "<stdin>", line 1, in <module>
#TypeError: keywords must be strings
dict({'a': 1}, **{'2': 3})
#{'a': 1, '2': 3}

#Merging Dictionaries — New Feature In the latest release of Python 3.9.0a4, we can use the merging operator | to merge two dicts very conveniently. An example is given below. You may have noticed that when there are overlapping keys between these two dicts, the last seen wins, and this behavior is consistent with what we’ve seen above, such as the update()method.
# use the merging operator |
d3 = d1 | d2
# d3 is now {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# good

d3 = d1 | d2a
# d3 is now {'a': 10, 'b': 2, 'c': 3, 'd': 4}
# not good

'''
Related to this merge operator is the augmented assignment version, 
which operates in-place (i.e., update the left side dict). Essentially, 
it functions the same way as the update() method. The following code snippet 
shows you its usage:
# Create a copy for d1
'''
d3 = d1.copy()

# Use the augmented assignment of the merge operator
d3 |= d2
# d3 now is {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# good

d3 |= d2a
# d3 now is {'a': 10, 'b': 2, 'c': 3, 'd': 4}
# not good

'''
Closing Thoughts
This article reviewed the new feature of merging and updating dictionaries in Python 3.9. There are several other new updates/improvements in several modules, such as asyncio, math, and os modules. See the official website for more information. I can’t wait to check them out in its official release in October!
Are you ready for Python 3.9? Stay tuned for a review of its new features when it is officially released!
Thank you for reading!
'''