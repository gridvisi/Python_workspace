'''
https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/train/python

Given a month as an integer from 1 to 12, return to which quarter of the year it
belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June),
is part of the second quarter; and month 11 (November), is part of the fourth quarter.

FUNDAMENTALS
'''

def quarter_of(month):
    return (month-1)//3 + 1

#1st
def quarter_of(month):
    # your code here
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4

#2nd
from math import ceil
def quarter_of(month):
    return ceil(month / 3)

#3rd
def quarter_of(n):
    return (n + 2) // 3