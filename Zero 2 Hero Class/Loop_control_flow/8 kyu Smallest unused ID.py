'''
https://www.codewars.com/kata/55eea63119278d571d00006a/train/python

Hey awesome programmer!
You've got much data to manage and of course you use zero-based
and non-negative ID's to make each data item unique!

Therefore you need a method, which returns the smallest unused
ID for your next new data item...

Note: The given array of used IDs may be unsorted.
For test reasons there may be duplicate IDs, but you don't
have to find or remove them!

Go on and code some pure awesomeness!

import codewars_test as test
from solution import next_id

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(next_id([0,1,2,3,4,5,6,7,8,9,10]), 11)
        test.assert_equals(next_id([5,4,3,2,1]), 0)
        test.assert_equals(next_id([0,1,2,3,5]), 4)
        test.assert_equals(next_id([0,0,0,0,0,0]), 1)
        test.assert_equals(next_id([]), 0)
        test.assert_equals(next_id([0,0,1,1,2,2]), 3)
        test.assert_equals(next_id([0,1,1,1,3,2]), 4)
        test.assert_equals(next_id([0,1,0,2,0,3]), 4)
        test.assert_equals(next_id([9,8,0,1,7,6]), 2)
        test.assert_equals(next_id([9,8,7,6,5,4]), 0)
'''

def next_id(arr):
    if not arr:return 0
    return [i for i in list(range(max(arr)+2)) if i not in arr][0]

def next_id(arr):
    t = 0
    while t in arr:
        t +=1
    return t

def next_id(arr):
    for i in range(len(arr)+1):
        if i not in arr:
            return i