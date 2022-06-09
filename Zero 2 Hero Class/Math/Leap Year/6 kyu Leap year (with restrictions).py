'''
https://www.codewars.com/kata/5848947d59fdc010fe00023e/train/python

Task
You're given a year n (1583 <= n < 10000). You need to create a function which return True if n is a leap year and False otherwise.

Restrictions
Your code mustn't contain:

def
if
eval or exec
return
import
Note
Feel free to rate the kata when you finish it :)

P.S.: Sofisticated cheats are welcome.

PUZZLESGAMESDECLARATIVE PROGRAMMING
'''

lambda n:n%100 != 0 and n%4 == 0 or n%400 == 0
is_leap = lambda y: y%4==0 and y%100!=0 or y%400==0
def is_leap(n):
    return n%100 != 0 and n%4 == 0 or n%400 == 0