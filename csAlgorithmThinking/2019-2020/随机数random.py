
import random
import numpy as np
import itertools

random.random()
from random import randint
chinese = [randint(60, 100) for _ in range(40)]
english = [randint(60, 100) for _ in range(40)]
math = [randint(60, 100) for _ in range(40)]

totals = []

for c, e, m in zip(chinese, english, math):
    totals.append(c + m + e)

for x in totals:
    print(x)

e1 = [randint(60, 100) for _ in range(40)]
e2 = [randint(60, 100) for _ in range(42)]
e3 = [randint(60, 100) for _ in range(42)]
e4 = [randint(60, 100) for _ in range(46)]
count = 0
for s in chain(e1, e2, e3, e4):
    if s >= 90:
        count += 1
print (count)

s1 = [1, 2, 3]
s2 = [4, 5, 6]
s3 = [7, 8, 9]
for (a, b, c) in zip(s1, s2, s3):
    print(a, b, c)
