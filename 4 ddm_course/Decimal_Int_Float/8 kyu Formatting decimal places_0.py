'''
https://www.codewars.com/kata/5641a03210e973055a00000d/train/python

Each number should be formatted that it is rounded to
two decimal places.
You don't need to check whether the input is a valid
number because only valid numbers are used in the tests.

Example:
5.5589 is rounded 5.56
3.3424 is rounded 3.34
'''


def two_decimal_places(n):
    # raise NotImplementedError("TODO: two_decimal_places")
    return round(n, 2)


def two_decimal_places(n):
   return round(n* 100) / 100


from numpy import round

def two_decimal_places(n):
    return round(n, decimals=2)