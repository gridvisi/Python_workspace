'''
The Zen of Python?
For those who haven’t seen it before, type and execute import this in your Python interpreter, and 19 guiding principles penned by Tim Peters will show up:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren’t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one — and preferably only one — obvious way to do it.
Although that way may not be obvious at first unless you’re Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it’s a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea — let’s do more of those!
'''
a = True
b = False
c = 1
# &&, ||
print((a == 0), (b == 1),(c==True))
if (a == 0 & b == 1) | c==True:print('yes')
else:print('No')

if a == 0 & b == 1 | c==True:print('yes')
else:print('No')

# and, or
if a == 0 and b == 1 or c==True:print('yes')
else:print('No')

# These are the same logical expression in Python
# The alternative operators can be used to construct the exact same expressions
# from a semantic perspective.

'''
Explicit Is Better Than Implicit
In Python, a good naming convention not only prevents you from getting bad grades in classes but also makes your code explicit. Fortunately, there are some guidelines you can find in PEP8, and I would like to highlight some points below.

In general, avoid using names that are
1. Too general, like my_list.
2. Too wordy, like list_of_machine_learning_data_set.
3. Too ambiguous, like “l”, “I”, “o”, “O.”
Package/Module names should be all lowercase.
One-word names are preferred.
When multiple words are needed, add underscores to separate them.
Class names should follow the UpperCaseCamelCase convention.
Variables\Methods\Functions should follow the lowercase convention (add underscores to separate words if needed).
Constant names must be fully capitalized (add underscores to separate words if needed).
Everything has to be lucid and understandable.
'''
words = ['Hannibal', 'Hanny', 'Steeve']

# Novice
index = 0
for word in words:
    print(index, word)
    index += 1

# Pro
for index, word in enumerate(words):
    print(index, word)


subjects = ['math', 'chemistry', 'biology', 'pyhsics']
grades = ['100', '83', '90', '92']

grades_dict = dict(zip(subjects, grades))
print(grades_dict)

import numpy as np

a = np.arange(5)
print(a < 3)
if all(a) < 3:
    print('smaller than 3')


import numpy as np

a = np.array([True, True, True])
b = np.array([False, True, True])
c = np.array([False, False, False])

print(a.all())
print(a.any())

print(b.all())
print(b.any())

print(c.all())
print(c.any())