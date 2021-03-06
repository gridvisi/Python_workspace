'''
https://www.codewars.com/kata/57cc40b2f8392dbf2a0003ce/train/python

*** No Loops Allowed ***

You will be given an array (a) and a value (x). All you need to do is check whether the provided array contains the value, without using a loop.

Array can contain numbers or strings. X can be either. Return true if the array contains the value, false if not. With strings you will need to account for case.

Looking for more, loop-restrained fun? Check out the other
kata in the series:

https://www.codewars.com/kata/no-loops-1-small-enough

https://www.codewars.com/kata/no-loops-3-copy-within
'''


def check(a, x):
    return x in a

a,x = [1,3,4,6,7],0
a,x = 'hello,world','word'

#2nd
check = list.__contains__

#3rd
from operator import contains as check

#4th
from typing import List, Union

def check(array: List[Union[int, str]], value: Union[int, str]) -> bool:
    """ Check whether the provided array contains the value, without using a loop. """
    return value in array