from pprint import pprint
#              ID    First Name     Last Name
line_record = "2        John         Smith"
pprint(line_record)
# '2        John         Smith'
print(line_record)
# 2        John         Smith

ID = slice(0, 8)
FIRST_NAME = slice(9, 21)
LAST_NAME = slice(22, 27)
print(ID,FIRST_NAME,LAST_NAME)

name = f"{line_record[FIRST_NAME].strip()} {line_record[LAST_NAME].strip()}"
print(name)
print(line_record[0:8])

# name == "John Smith"

import sys
print(sys.argv)

print(str(("Python".encode())))

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1+p2)

import difflib
x = difflib.get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'], n=2)
print(x)
# returns ['apple', 'ape']

from collections import Counter

cheese = ["gouda", "brie", "feta", "cream cheese", "feta", "cheddar",
          "parmesan", "parmesan", "cheddar", "mozzarella", "cheddar", "gouda",
          "parmesan", "camembert", "emmental", "camembert", "parmesan"]

cheese_count = Counter(cheese)
print(cheese_count.most_common(3))
# Prints: [('parmesan', 4), ('cheddar', 3), ('gouda', 2)]
print(cheese_count["mozzarella"])
# Prints: 1
cheese_count["mozzarella"] += 1

print(cheese_count["mozzarella"])
# Prints: 2




'''

#import how_to_time
import time

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = how_to_time.how_to_time.now()
        return cls(t.year, t.month, t.day)
'''