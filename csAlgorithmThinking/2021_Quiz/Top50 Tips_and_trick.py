

'''
Python 3: Top 50 Tips & Tricks
Here is a list of python tips and tricks to help you write an elegant Python 3 code! This article is divided into different kinds of tricks:
Python iterable tricks.
Python comprehension tricks.
Python unpacking tricks.
Python itertools tricks.
Python collections tricks.
Python other tricks.
Python easter eggs.
Python tricks to understand the context.

'''

#1. Python Iterables tricks
#Creating a sequence of numbers (zero to ten with skips).
range(0 ,10 ,2)
#[0, 2, 4, 6, 8]

#Summing a sequence of numbers (calculating the sum of zero to ten with skips).
l = range(0 ,10 ,2)
sum(l)
#20
#Checking whether any element in the sequence is Truthful (checking whether any elements between zero and ten with skips are even).
any(a % 2== 0 for a in range(0, 10, 2))
#True
#Checking whether all elements in the sequence are Truthful(checking whether)
#all elements between zero and ten with skips are even).

all(a % 2 == 0 for a in range(0, 10, 2))
#True
#Cumulative summing a sequence of numbers(calculating the
#cumulative sum of zero to ten with skips).

import numpy as np
res = list(np.cumsum(range(0, 10, 2)))
print(res)
#[0, 2, 6, 12, 20]

#Given each iterable we construct a tuple by adding an index.
a = ['Hello', 'world', '!']
list(enumerate(a))
#[(0, 'Hello'), (1, 'world'), (2, '!')]

#Concatenating iterable to a single string.
a = ["python", "really", "rocks"]
" ".join(a)
'python really rocks'

#Combining two iterable of tuples or pivot nested iterables.
# Combining two iterables
a = [1, 2, 3]
b = ['a', 'b', 'c']
z = zip(a, b)
print(z)
#[(1, 'a'), (2, 'b'), (3, 'c')]

# Pivoting list of tuples
zip(*z)
#[(1, 2, 3), ('a', 'b', 'c')]

#Getting min / max
# from iterable (with/ without specific function).
# Getting maximum from iterable
a = [1, 2, -3]
max(a)
#2

# Getting maximum from iterable
min(a)
#1

# Bot min/max has key value to allow to get maximum by appliing function
max(a, key=abs)
#3

#Getting sorted iterable(can sort by compare function).
a = [1, 2, -3]
sorted(a)
#[-3, 1, 2]

sorted(a, key=abs)
#[1, 2, -3]

#Splitting a single string to list.
s = "a,b,c"
s.split(",")
#["a", "b", "c"]

#Initializing a list filled with some repetitive number.
print([1] * 10)
#[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

#Merging / Upserting two dictionaries.
a = {"a": 1, "b": 1}
b = {"b": 2, "c": 1}
a.update(b)
print(a)
#{"a": 1, "b": 2, "c": 1}

#Naming and saving slices of iterables.
# Naming slices (slice(start, end, step))
a = [0, 1, 2, 3, 4, 5]
LASTTHREE = slice(-3, None)
print(LASTTHREE)

slice(-3, None, None)
print(a[LASTTHREE])
#[3, 4, 5]

#Finding the index of an item in a list.
a = ["foo", "bar", "baz"]
a.index("bar")
#1

#Finding the index of the min / max item in an iterable.
a = [2, 3, 1]
min(enumerate(a), key=lambda x: x[1])[0]
#2

#Rotating iterable by k elements.
a = [1, 2, 3, 4]
k = 2
print(a[-2:] + a[:-2])
#[3, 4, 1, 2]

#Removing useless characters on the end/start/ both of your string.
name = "//George//"
name.strip("/")
'George'
name.rstrip("/")
'//George'
name.lstrip("/")
'George//'

#Reversing an iterable wit order(string, list etc).
# Reversing string
s = "abc"
print(s[::-1])
"cba"

# Reversing list
l = ["a", "b", "c"]
l[::-1]
#["c", "b", "a"]

#2.Python branching tricks Multiple predicates short - cut.
n = 10
print(1 < n < 20)
#True

#For - else construct useful when searched
# for something and find it.
# For example assume that I need to search through a list and process each item until a flag item is found and
# then stop processing. If the flag item is missing then an exception needs to be raised.
mylist = ['red','blue','yellow']
'''
for i in mylist:
    if i == theflag:
        break
    process(i)
else:
    raise ValueError("List argument missing terminal flag.")
'''

# operator.
# "Python ROCK" if True else " I AM GRUMPY"
"Python ROCK"

def foo(a,b):
    return a/b
#Try - catch - else construct.
try:
    foo(a,b)
except Exception:
    print("Exception occured")
else:
    print("Exception didnt occur")
finally:
    print("Always gets here")

#While - else construct.
i = 5
while i > 1:
    print("Whil-ing away!")
    i -= 1
    if i == 3:
        break
else:
    print("Finished up!")

#3. Python comprehensions tricks comprehension.
m = [x ** 2 for x in range(5)]
print(m)
#[0, 1, 4, 9, 16]

#Set comprehension.
m = {x ** 2 for x in range(5)}
print(m)
#{0, 1, 4, 9, 16}

#Dict comprehension.
m = {x: x ** 2 for x in range(5)}
print(m)
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#Generator comprehension.
# A generator comprehension is the lazy version of a list comprehension.
m = (x ** 2 for x in range(5))
print(m)
#< generator object < genexpr > at 0x108efe408 >
list(m)
#[0, 1, 4, 9, 16]

m = (x ** 2 for x in range(5))
next(m)
#0
list(m)
#[1, 4, 9, 16]

#List comprehension with the current and previous value.
a = [1, 2, 4, 2]
print([y - x for x, y in zip(a, a[1:])])
#[1, 2, -2]

#Note: all comprehension can use predicates with if statement.

#4. Python unpacking tricks Unpack variables from iterable.
# One can unpack all iterables (tuples, list etc)
a, b, c = 1, 2, 3
print(a, b, c)
#(1, 2, 3)

a, b, c = [1, 2, 3]
print(a, b, c)
#(1, 2, 3)

#Swap variables values.
a, b = 1, 2
a, b = b, a
print(a, b)
#(2, 1)

#Unpack variables from iterable without
#indicating all elements.
a, *b, c = [1, 2, 3, 4, 5]
print(a,b,c)
#[2, 3, 4]

#Unpack variables using the splat operator.

def test(x, y, z):
    print(x, y, z)

res = test(*[10, 20, 30])

res = test(**{'x': 1, 'y': 2, 'z': 3})


#5. Python Itertools tricks Flatten iterables.
from collections import Counter
import itertools
a = [[1, 2], [3, 4], [5, 6]]
list(itertools.chain.from_iterable(a))
#[1, 2, 3, 4, 5, 6]

#Creating cartesian products from iterables.

for p in itertools.product([1, 2, 3], [4, 5]):
    print(''.join(str(x) for x in p))
'''
(1, 4)
(1, 5)
(2, 4)
(2, 5)
(3, 4)
(3, 5)
'''
#Creating permutation from iterable.

for p in itertools.permutations([1, 2, 3, 4]):
    print(''.join(str(x) for x in p))
'''
123
132
213
231
312
321
'''
#Creating ngram from iterable.
from itertools import islice
def n_grams(a, n):
    ...
    z = (islice(a, i, None) for i in range(n))
    ...
    return zip(*z)

a = [1, 2, 3, 4, 5, 6]
print(n_grams(a, 3))
#[(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]

print(n_grams(a, 2))
#[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]

print(n_grams(a, 4))
#[(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]

#Combining two iterables of tuples with padding or pivot nested iterable with padding.
import itertools as it
x = [1, 2, 3, 4, 5]
y = ['a', 'b', 'c']
list(zip(x, y))
#[(1, 'a'), (2, 'b'), (3, 'c')]

list(it.zip_longest(x, y))
[(1, 'a'), (2, 'b'), (3, 'c'), (4, None), (5, None)]

#Creating a combination of k things from an iterable of n
import itertools

bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
list(itertools.combinations(bills, 3))
#[(20, 20, 20), (20, 20, 10), (20, 20, 10), ...]

#Creating accumulated results of iterable given a function
import itertools

list(itertools.accumulate([9, 21, 17, 5, 11, 12, 2, 6], min))
#[9, 9, 9, 5, 5, 5, 2, 2]

#Creating an iterator that returns elements from the iterable as long as the predicate is true
import itertools

itertools.takewhile(lambda x: x < 3, [0, 1, 2, 3, 4])
#[0, 1, 2]

it.dropwhile(lambda x: x < 3, [0, 1, 2, 3, 4])
#[3, 4]

#Creating an iterator that filters elements from iterable returning only those
#for which the predicate is_False_
import itertools

# keeping only false values
list(itertools.filterfalse(bool, [None, False, 1, 0, 10]))
#[None, False, 0]

#Creating an iterator that computes the function using arguments obtained from the iterable of iterables
import itertools
import operator

a = [(2, 6), (8, 4), (7, 3)]
list(itertools.starmap(operator.mul, a))
#[12, 32, 21]

#6. Python collections tricks Set basic operations.
A = {1, 2, 3, 3}
print(set(A))
#set([1, 2, 3])

B = {3, 4, 5, 6, 7}
print(set(B))
#set([3, 4, 5, 6, 7])

print(A | B)
#set([1, 2, 3, 4, 5, 6, 7])

print(A & B)
#set([3])
print(A - B)
#set([1, 2])

print(B - A)
#set([4, 5, 6, 7])

print(A ^ B)
#set([1, 2, 4, 5, 6, 7])

print((A ^ B) == ((A - B) | (B - A)))
#True


#Counter data structure(an unordered collection where elements are stored as dictionary
# keys and their counts are stored as dictionary values).
import collections
A = collections.Counter([1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7])
print(A)
Counter({3: 4, 1: 2, 2: 2, 4: 1, 5: 1, 6: 1, 7: 1})
print(A.most_common(1))
#[(3, 4)]

print(A.most_common(3))
#[(3, 4), (1, 2), (2, 2)]

#Default dictionary structure(a subclass of dictionary that retrieves default value
#when non - existing key getting accessed).
import collections
m = collections.defaultdict(int)
print(m['a'])
#0

m = collections.defaultdict(str)
print(m['a'])

m['b'] += 'a'
print(m['b'])
'a'

m = collections.defaultdict(lambda: '[default value]')
print(m['a']) #'[default value]'
print(m['b']) #'[default value]'

m = collections.defaultdict(list)
print(m['a'])
#[]

#Ordered dict structure(a subclass of dictionary that keeps order).
from collections import OrderedDict

d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
''.join(d.keys())
'acdeb'

d.move_to_end('b', last=False)
''.join(d.keys())
'bacde'

#Deques structure(_Deques are a generalization of stacks and queues)._
#import collection

Q = collections.deque()
Q.append(1)
Q.appendleft(2)
Q.extend([3, 4])
Q.extendleft([5, 6])
print(Q)
#deque([6, 5, 2, 1, 3, 4])

print(Q.pop())
#4

print(Q.popleft())
#6

print(Q)
#deque([5, 2, 1, 3])

Q.rotate(3)
print(Q)
#deque([2, 1, 3, 5])

Q.rotate(-3)
print(Q)
#deque([5, 2, 1, 3])

last_three = collections.deque(maxlen=3)
for i in range(4):
    ...
    last_three.append(i)
...
print(', '.join(str(x) for x in last_three))
'''
...
0
0, 1
0, 1, 2
1, 2, 3
2, 3, 4
'''

#Named tuples structure(create tuple - like objects that have fields accessible
#by attribute lookup as well as being indexable and iterable).
import collections
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(x=1.0, y=2.0)
print(p)
Point(x=1.0, y=2.0)
'''
p.x
1.0
p.y
2.0
'''
'''
?????????????????????SyntaxError: invalid character in identifier??????
??????????????????????????????????????????????????????????????????????????????????????????tab????????????????????????
?????????for x in range(10):???#???????????????
   ???print(x)????????????????????????
????????????????????????????????????????????????????????? # ??????????????????????????????????????????print??????????????????????????????
'''
#Use A Dictionary To Store A Switch.

func_dict = {'sum': lambda x, y: x + y,
             'subtract': lambda x, y: x - y}
func_dict['sum'](9, 3)
#12
func_dict['subtract'](9, 3)
#6

#Data classes structure
from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str

queen_of_hearts = DataClassCard('Q', 'Hearts')
print(queen_of_hearts.rank)
#'Q'
#queen_of_hearts

DataClassCard(rank='Q', suit='Hearts')
print(queen_of_hearts == DataClassCard('Q', 'Hearts'))
#True

#7. Other Python tricks Generating uuid.
# This creates a randomized 128-bit number that will almost certainly be unique.
# In fact, there are over 2?????? possible UUIDs that can be generated. That???s over five undecillion (or 5,000,000,000,000,000,000,000,000,000,000,000,000).

import uuid

user_id = uuid.uuid4()
print(user_id)
#UUID('7c2faedd-805a-478e-bd6a-7b26210425c7')

#Memoization using LRU cache.
import functools
@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Suppression of expressions
from contextlib import suppress
with contextlib.suppress(ZeroDivisionError):
 "10 / 0"
# No exception raised

#An elegant way to deal
#with a file path (3.4???)
from pathlib import Path

data_folder = Path("source_data/text_files/")

# Path calculation and metadata
file_to_open = data_folder / "raw_data.txt"
print(file_to_open.name)
"raw_data.txt"
print(file_to_open.suffix)
"txt"
print(file_to_open.stem)
"raw_data"

# Files functions
f = open(file_to_open)
f.read()
# content of the file
file_to_open.exists()
#True

#Creating decorator to separate concerns
from functools import wraps
def add_sandwich(wrapped):
    @wraps(wrapped)
    def wrapper(*args, **kwargs):
        return wrapped(*args, **kwargs) + ' sandwich'

    return wrapper


@add_sandwich
def ham():
    return 'ham'

ham()
'ham sandwich'

#Using yield to create a simple iterator

def foo(lst):
    for x in lst:
        yield x
        yield x * 2


a = [1, 3]
list(foo(a))
#[1, 2, 3, 6]

#8.Python easter eggs Anti - gravity
import antigravity
antigravity.fly()


#The Zen of Python
import this
