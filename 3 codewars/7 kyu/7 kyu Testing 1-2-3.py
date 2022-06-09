'''
https://www.codewars.com/kata/testing-1-2-3/train/python
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
Write a function which takes a list of strings and returns each line prepended by the correct number.
The numbering starts at 1. The format is n: string. Notice the colon and space in between.
Examples:
number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
'''
lines = ["a", "b", "c"]
def number(lines):
    return dict(zip((range(len(lines)+1)),lines))

def number(lines):
    arr = [0]*len(lines)
    arrlt = [str(i+1)+': ' for i in (range(len(lines)+1))]
    for i in range(len(lines)):
        arr[i] = arrlt[i] + lines[i]
    return arr

def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]
print(number(lines))

def number(lines):
    return ["{0}: {1}".format(i + 1, lines[i]) for i in range(len(lines))]

def number(lines):
    return ['{}: {}'.format(n, s) for (n, s) in enumerate(lines, 1)]

import itertools
def number(lines):
    counter=itertools.count(1)
    return [str( next(counter) ) + ": " + x for x in lines]