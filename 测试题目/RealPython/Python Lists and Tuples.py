
'''
Which of the following are true of Python lists?


A given object may appear in a list more than once

Correct

These represent the same list:

['a', 'b', 'c']

['c', 'a', 'b']


A list may contain any type of object except another list


All elements in a list must be of the same type
There is no conceptual limit to the size of a list

Correct

A list is an ordered collection of objects. The order of
the elements is an innate characteristic of the list.

A list may contain any number of elements (constrained by
the computer’s memory, of course), of any type.
The same object may occur any number of times.

Review: Lists are Ordered, Lists Can Contain Arbitrary
Objects
'''

#2
'''
Assume the following list definition:

>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
Several short REPL sessions are shown below. Which display correct output?


>>> print(a[4::-2])
['quux', 'baz', 'foo']
Correct

>>> print(a[-6])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
Incorrect

>>> print(a[-5:-3])
['bar', 'baz']
Correct

>>> a[:] is a
True
Incorrect

>>> max(a[2:4] + ['grault'])
'qux'
Correct

Here is a diagram to remind you of the list indices:

Diagram of a Python list
Correct Answers
>>> print(a[4::-2])
['quux', 'baz', 'foo']
Slice syntax [4::-2] begins with the element at index 4 ('quux') and proceeds to the start of the list, skipping every other item. That yields the elements at indices 4, 2, and 0.
>>> print(a[-5:-3])
['bar', 'baz']
[-5:-3] starts at index -5 and goes up to but not including index -3, which designates items 'bar' and 'baz'.
>>> max(a[2:4] + ['grault'])
'qux'
a[2:4] returns the slice ['baz', 'qux']. The + operator concatenates, so the argument to max() is ['baz', 'qux', 'grault']. The maximum value (for strings, the latest in alphabetical order) is 'qux'.
Incorrect Answers
>>> print(a[-6])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
As you can see from the diagram, negative indices begin with -1, so -6 actually is a valid index, corresponding to the first item in the list ('foo'). This statement would not actually generate an error.
Positive indices, on the other hand, start with 0, so 6 would not be a valid index for this list.
>>> a[:] is a
True
Recall that for a string s, s[:] returns a reference to s. So s is s[:] is True. For a list, a[:] is a copy of a—they do not reference the same object.
Review: List Elements Can Be Accessed by Index
'''

#3
'''
Consider the following nested list definition:

x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
A schematic for this list is shown below:

Nest list example
What is the expression that returns the 'z' in 'baz'?

ach of the four indices in the answer can be specified as a positive or negative number:

Expression	Selects
x[1]
x[-2]	The second element of x:
[3.141, 20, [30, 'baz', 2.718]]
x[1][2]
x[1][-1]	The third element of that sublist:
[30, 'baz', 2.718]
x[1][2][1]
x[1][2][-2]	The second element of that sublist: 'baz'
x[1][2][1][2]
x[1][2][1][-1]	The third character of 'baz': 'z'
'''

#4
'''
Same nested list as the previous question:

x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
Nest list example
What expression returns the list ['baz', 2.718]?

x[1][2][1:]
Correct

Expression	Selects
x[1]	The second element of x:
[3.141, 20, [30, 'baz', 2.718]]
x[1][2]	The third element of that sublist:
[30, 'baz', 2.718]
x[1][2][1:3]
or
x[1][2][1:]	The slice ['baz', 2.718]
Review: Lists Can Be Nested
'''

#5
'''
List a is defined as follows:

a = [1, 2, 3, 4, 5]
Select all of the following statements that remove the middle element 3 from a so that it equals [1, 2, 4, 5]:


a[2:3] = []
Correct

a[2] = []
Incorrect

del a[2]
Incorrect

a.remove(3)
Correct

a[2:2] = []

Correct answers
>>> del a[2]
>>> a
[1, 2, 4, 5]
The del command simply removes the specified list item. This is arguably the most straightforward way to remove the middle item from a.
>>> a[2:3] = []
>>> a
[1, 2, 4, 5]
a[2:3] represents the slice of a consisting of the single element 3. The slice assignment a[2:3] = [] replaces that slice with an empty list, which effectively removes that element.
>>> a.remove(3)
>>> a
[1, 2, 4, 5]
The .remove() method removes the specified argument from the target list, if it is present. This is a nice way to remove an item from a list by specifying its value, rather than its index in the list.
Incorrect answers
>>> a[2:2] = []
>>> a
[1, 2, 3, 4, 5]
a[2:2] is an empty slice. The slice assignment a[2:2] = [] does not replace anything in a. This statement leaves a unchanged.
>>> a[2] = []
>>> a
[1, 2, [], 4, 5]
a[2] designates a single item, not a slice. Thus, a[2] = [] replaces that item with an empty list.
Review: Lists Are Mutable
'''

#6
'''
Python Lists and Tuples
54%
That's incorrect!
List a is defined as follows:

a = ['a', 'b', 'c']
Which of the following statements adds 'd' and 'e' to the end of a, so that it then equals ['a', 'b', 'c', 'd', 'e']:


a[-1:] = ['d', 'e']

a[len(a):] = ['d', 'e']
Incorrect

a.extend(['d', 'e'])
Correct

a.append(['d', 'e'])

a += ['d', 'e']
Correct

a += 'de'
Incorrect

Correct Answers
Each of the following statements appends 'd' and 'e' to a:

>>> a += ['d', 'e']
>>> a
['a', 'b', 'c', 'd', 'e']
The += augmented assignment operator expects an iterable as the second operand. It iterates over the second operand and adds the resulting items to the end of the target operand.
>>> a += 'de'
>>> a
['a', 'b', 'c', 'd', 'e']
Remember that when Python iterates over a string, the result is a list of the component characters. Thus, this statement also appends the list ['d', 'e'].
>>> a.extend(['d', 'e'])
>>> a
['a', 'b', 'c', 'd', 'e']
The .extend() method also expects an iterable as an argument, and adds the designated items to the target list.
>>> a[len(a):] = ['d', 'e']
>>> a
['a', 'b', 'c', 'd', 'e']
a[len(a):] designates an empty slice at the end of a. This assignment replaces that slice with ['d', 'e'].
Incorrect Answers
These statements do not append 'd' and 'e' to a:

>>> a.append(['d', 'e'])
>>> a
['a', 'b', 'c', ['d', 'e']]
The .append() method takes a single object as its argument, and adds that object intact to the end of the target list. So this statement actually adds the list ['d', 'e'] to the end of a.
>>> a[-1:] = ['d', 'e']
>>> a
['a', 'b', 'd', 'e']
a[-1:] designates the slice of a consisting of only the element 'c', so this statement replaces that slice with ['d', 'e']:
Review: Lists Are Mutable
'''

#7
'''


You have a list a defined as follows:

a = [1, 2, 7, 8]
Write a Python statement using slice assignment that will fill in the missing values so that a equals [1, 2, 3, 4, 5, 6, 7, 8].

You have a list a defined as follows:

a = [1, 2, 7, 8]
Write a Python statement using slice assignment that will fill in the missing values so that a equals [1, 2, 3, 4, 5, 6, 7, 8].

a[2:2] = [3,4,5,6]
Correct
For reference, here’s our solution:

a[2:2] = [3, 4, 5, 6]

a[2:2] designates the empty slice of the original a 
between values 2 and 7. The assignment statement shown 
inserts the items in [3, 4, 5, 6] into that location.
'''

#8
'''
Suppose you have the following tuple definition:

t = ('foo', 'bar', 'baz')
Which of the following statements replaces the second element ('bar') with the string 'qux':


t[1:1] = 'qux'

It’s a trick question—tuples can’t be modified.

Correct

t[1] = 'qux'

t(1) = 'qux'

That’s the main difference between tuples and list: tuples are immutable.

Tuples can be indexed, though. And remember that even though tuples are defined using parentheses, tuple indexing uses square brackets just like list indexing.

Review: Defining and Using Tuples
'''

#9
'''
Write Python code to create a tuple with a single element, the string 'foo', and assign it to a variable called t.

t = ('foo')
Incorrect
Answer does not define a tuple

This is what we expected to see:
t = ('foo',)

Specifying a single value in parentheses doesn’t define a tuple—Python interprets the value as an expression in grouping parentheses:

>>> t = ('foo')
>>> t
'foo'
>>> type(t)
<class 'str'>
To distinguish this from a singleton tuple, you need to include a trailing comma before the closing parenthesis:

>>> t = ('foo',)
>>> t
('foo',)
>>> type(t)
<class 'tuple'>
This is also one of those cases where you can leave the parentheses off. The trailing comma causes Python to assume a tuple:

>>> t = 'foo',
>>> t
('foo',)
>>> type(t)
<class 'tuple'>
Review: Defining and Using Tuples
'''

#10
'''
Consider this assignment statement:

a, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9)[1::3]
Following execution of this statement, what is the value of b:


6


2


4


5

Correct

The slice expression on the right side of the assignment produces the tuple (2, 5, 8):

>>> (1, 2, 3, 4, 5, 6, 7, 8, 9)[1::3]
(2, 5, 8)
The assignment is thus equivalent to this compound tuple packing/unpacking assignment:

>>> a, b, c = (2, 5, 8)
b is given the value 5.

Review: Tuple Assignment, Packing, and Unpacking

'''

#11
'''
Assume x and y are assigned as follows:

x = 5
y = -5
What is the effect of this statement:

x, y = (y, x)[::-1]

The values of x and y are swapped


Both x and y are -5


Both x and y are 5


The values of x and y are unchanged

Correct

The slice expression on the right side of the assignment reverses the tuple:

>>> (y, x)[::-1]
(5, -5)
The assignment is thus equivalent to this compound tuple packing/unpacking assignment:

>>> x, y = (5, -5)
x and y retain the values they had originally.

Review: Tuple Assignment, Packing, and Unpacking
'''

