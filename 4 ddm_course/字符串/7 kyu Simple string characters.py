'''
https://www.codewars.com/kata/5a29a0898f27f2d9c9000058/train/python

In this Kata, you will be given a string and your task will be to return a list of
ints detailing the count of uppercase letters, lowercase, numbers and special
characters, as follows.

Solve("*'&ABCDabcde12345") = [4,5,5,3].
--the order is: uppercase letters, lowercase, numbers and special characters.
'''
s = "*'&ABCDabcde12345"
def solve(s):
    up,low,num,spec = 0, 0 ,0, 0
    for c in s:
        if c.isupper():
            up += 1
        elif c.islower:
            low += 1
        elif c.isnumber()
            num += 1
        elif isinstance(c,anu)