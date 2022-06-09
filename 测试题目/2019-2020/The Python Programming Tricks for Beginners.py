'''
Trick #1: Nested Lists Combination
itertools is probably one of my favorite Python library.
Imagine your code had a dozen of lists and after some manipulation,
you ended up with a deeply nested list. itertools is exactly what
you need to resolve this syntactical mess.
'''
import itertools
flatten = lambda x: list(itertools.chain.from_iterable(x))
s = [['"', 'An', 'investment'], ['in'], ['knowledge'], ['pays'], ['the', 'best'], ['interest."', '--'], ['Benjamin'], ['Franklin']]
print(' '.join(flatten(s)))

res = ''
for i in s:
    res += ' '.join(i)
print(res)


#Trick #2: Powerful One-Liners
#Are you tired of reading through lines of code and getting lost in conditional statements?
# Python one-liners might just be what you are looking for. For example, the conditional statements
alpha = 8
if alpha > 7:
    beta = 999
elif alpha == 7:
    beta = 99
else:
    beta = 0
#can really be simplified to:
beta = 999 if alpha > 7 else 99 if alpha == 7 else 0

# list
lst = [1, 3, 5]
doubled = []
for num in lst:
    doubled.append(num*2)

#can be simplified to just one line:
doubled = [num * 2 for num in lst]

#Trick #5: Printing Made Easy
#The last trick is something I wish I had known earlier.
# Turns out to print an array with strings as one comma-separated string,
# we do not need to use .join() and loops.

row = ["1", "bob", "developer", "python"]
print(','.join(str(x) for x in row))
#1,bob,developer,python


#This simple one-liner will do:
print(*row, sep=',')  #1,bob,developer,python

import pprint; pprint.pprint(zip(('Byte', 'KByte', 'MByte', 'GByte', 'TByte'), (1 << 10*i for i in range(5))))