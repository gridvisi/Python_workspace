'''
https://www.codewars.com/kata/52840d2b27e9c932ff0016ae/train/python

Write a function that gets a sequence and value and returns true/false depending
on whether the variable exists in a multidimentional sequence.

Example:

locate(['a','b',['c','d',['e']]],'e'); // should return true
locate(['a','b',['c','d',['e']]],'a'); // should return true
locate(['a','b',['c','d',['e']]],'f'); // should return false

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(locate(['a','b',['c','d',['e']]],'a'), True)
    Test.assert_equals(locate(['a','b',['c','d',['e']]],'d'), True)
    test.assert_equals(locate(['a','b',['c','d',['e']]],'e'), True)
    test.assert_equals(locate(['a','b',['c','d',['e']]],'f'), False)
    Test.assert_equals(locate(['a','b',['c','d',['e',['a','b',['c','d',['e4']]]]]],'e4'), True)
    Test.assert_equals(locate(['a','b',['c','d',['e',['a','b',['c','d',['e',['a','b',['c','d',['e4',['a','b',['c','d',['e',['a','b',['c','d',['e',['a','b',['c','d',['e14']]]]]],]]]]]]]]],]]],'e'), True)
'''

#Recurtion
#15th solution by ericlee
def flatarrs(arrs):
    ans = []
    for arr in arrs:
        if type(arr) == str:
            ans.append(arr)
            yield arr
        else:
            yield from flatarrs(arr)
arrs = ['a','b',['c','d',['e']]]
arrs = ['a','b',['c','d',['e',['a','b',['c','d',['e',['a','b',['c','d',['e4',['a','b',['c','d',['e',['a','b',['c','d',['e',['a','b',['c','d',['e14']]]]]],]]]]]]]]],]]]
print(list(flatarrs(arrs)))

def locate(seq, value):
    #ans = flat(seq)
    return value in list(flatarrs(seq))
seq, value = ['a','b',['c','d',['e',['a','b',['c','d',['e4']]]]]],'e4'
print(locate(seq, value))


#1st solution
def locate(seq, value):
    for s in seq:
        if s == value or (isinstance(s,list) and locate(s, value)):
            return True
    return False

#3rd solution
def flatten(seq):
    for e in seq:
        if isinstance(e, list):
            yield from flatten(e)
        yield e

def locate(seq, value):
    return any(e == value for e in flatten(seq))

#
def locate(seq, value):
    if isinstance(seq, (tuple, list)):
        return any(locate(x, value) for x in seq)
    return seq == value

#
def locate(seq, value):
    for x in seq:
        if x == value:
            return True
        if isinstance(x, list):
            if locate(x, value) == True:
                return True
    return False

#jason
def locate(seq, value):
    return f'"{value}"' in __import__('json').dumps(seq)




from numpy import *
a = [
    [ 0 , 1 , 2 , 3],
    [ 4 , 5 , 6 , 7],
    [ 8 , 9 ,10, 11]
     ]

a = arange(12).reshape(3,4)
print(a.flatten())

import collections
def flat(seq):
    iterator, sentinel, stack = iter(seq), object(), []
    while True:
        value = next(iterator, sentinel)
        if value is sentinel:
            if not stack:
                break
            iterator = stack.pop()

        elif isinstance(value, str):
            yield value

        else:
            try:
                new_iterator = iter(value)

            except TypeError:
                yield value
            else:
                stack.append(iterator)
                iterator = new_iterator

def locate(seq, value):
    #ans = flat(seq)
    return value in list(flat(seq))
seq, value = ['a','b',['c','d',['e',['a','b',['c','d',['e4']]]]]],'e4'
print(locate(seq, value))