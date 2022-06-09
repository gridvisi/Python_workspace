

#1 What is the output of this code snippet?
print(bool([[]]))
print(bool([]))

#a False

#b True

#2 👇 Comment the answer, like and retweet! #python
# What is the output of the code snippet below?
print("python"[-4:0:-2])
'''
o

tho

oht

th

t
'''

#3 👇 Comment the answer, like and retweet!
# #pythont because stride is -2, but syntax is ending #-1,
# so t alone is the output.
#Which one is a subclass of tuple with field names and a class name?
'''

collections.enhancedtuple

collections.v2tuple

collections.supertuple

collections.namedtuple

collections.withfieldstuple
'''

#4 👇 Comment the answer, like and retweet! #python
#What it the output of the code snippet below?
#print(float(""))
'''

0.0

0

None

It will throw a ValueError error.
#ValueError: could not convert string to float: ''

False
'''

#5 👇 Comment the answer, like and retweet! #python
#Which one is not a valid Python encoding codec?
'''

enc4

ascii

utf_32

cp037

utf_8_sig

'''

#6 👇 Comment the answer, like and retweet! #python

#What is the output of the code snippet below?
print(~100)
'''

101

0

100

-100

-101

'''

#7 👇 Comment the answer, like and retweet! #python
#What is the output of the code snippet below?
print('[%c]' % 65)
'''

65

A

It will throw a SyntaxError error.

[65]

[A]

'''

#8 👇 Comment the answer, like and retweet! #python
# What is the output of this code?
a = -3
if a > -10:
    print('yes!')
else:
    print('no!')

"no!"

"yes!"

#9 👇 Comment the answer, like and retweet! #python
#What is the output of the code snippet below?
import copy
a = [1, 2]
b = copy.deepcopy(a)
print(a[0] is b[0])
c = [3,4]
d = c
print(c[0] is d[0])
'''

False

True

'''

#10 👇 Comment the answer, like and retweet! #python
# What is the output of the code snippet below?
a, b, *c = range(5)
print(*c)
'''

0 1 2 3 4

2 3 4

It will throw a ValueError error.

0 1 2

'''

#11 👇 Comment the answer, like and retweet! #python
#What is the type of the returned object in the code snippet below?
def foo(**kwargs):
    return kwargs

print(foo(a=1, b=2, c=3))
print(foo)
'''

A dictionary

A list

A tuple

'''

#12 👇 Comment the answer, like and retweet! #python
#What it the output of the code snippet below?
#print(int("540.689"))
print(int(540.689))
'''

540.0

541

540

It will throw a ValueError error.
'''


#13 👇 Comment the answer, like and retweet! #python
#All iterables store all elements in memory.
'''

True

False
'''

#14 👇 Comment the answer, like and retweet! #python
#Which statement is wrong?
'''

Python files should have spaces in their names.

The name of a Python file should give an indication of what the file contains.

Python files end with .py.

👇 Comment the answer, like and retweet! #python

Which one is not a type of inheritance?

Multiple inheritance

Indirect inheritance

Multilevel inheritance

👇 Comment the answer, like and retweet! #python

'''

#15 What is the output of the following code snippet?
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))

'''

[(1, 'a', 2, 'b', 3, 'c')]

[(1, 'a'), (2, 'b'), (3, 'c')]

[(1, 1), (2, 2), (3, 3), ( 'a',  'a'), ( 'b',  'b'), ('c', 'c')]
'''

#16 👇 Comment the answer, like and retweet! #python

#What is the output of the code snippet below?
print("Py"*2*True)
'''

PyPy

"Py"*2*True

It will throw a SyntaxError error.

Py*2

Py*2*True

'''