'''
https://www.codewars.com/kata/59c3e819d751df54e9000098/train/python

import codewars_test as test
from solution import get_consective_items

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(get_consective_items(90000, 0), 4)
        test.assert_equals(get_consective_items('ascasdaiiiasdacasdiiiiicasdasdiiiiiiiiiiisdasdasdiii', 'i'), 11)
'''

#10th solve by ericlee
def get_consective_items(items, key):
    setelement = list(items)
    i = 1
    while len(''.join(items.split(i*f"{key}"))) != len(items):
        i += 1
    return i -1
items,key = 'ascasdaiiiasdacasdiiiiicasdasdiiiiiiiiiiisdasdasdiii', 'i'
print(''.join(items.split(f"{key}")))
print(get_consective_items(items,key))


#1st
from itertools import groupby

def get_consective_items(items, key):
    items, key = str(items), str(key)
    return max((len(list(l)) for k,l in groupby(items) if k == key), default=0)

#2nd
import re

def get_consective_items(a,b):
    return len(max(re.findall(f'{b}+',str(a)) or ['']))

#3rd
def get_consective_items(items, key):
    items, key = str(items), str(key)
    count = 0
    temp = key[:]
    while temp in items:
        temp += key
        count += 1
    return count

#4th
from itertools import groupby

def get_consective_items(items, key):
    key = str(key)
    return max(
        (sum(1 for _ in grp) for k, grp in groupby(str(items)) if k == key),
        default=0
    )

