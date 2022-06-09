'''
https://www.codewars.com/kata/598f76a44f613e0e0b000026/train/python


'''

#16th solution by ericle
s = "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"
def sum_of_integers_in_string(s):
    sn = ''.join([' ' if not i.isnumeric() else i for i in s]).split()
    return sum([int(i) for i in sn])

s = "12.4"
print(sum_of_integers_in_string(s))

#1st solution
import re
def sum_of_integers_in_string(s):
    return sum(int(x) for x in re.findall(r"(\d+)", s))

#2
import re
def sum_of_integers_in_string(s):
    return sum(map(int, re.findall("\d+", s)))


#3
def sum_of_integers_in_string(s):
    return sum(map(int, ''.join(c if c.isdigit() else ' ' for c in s).split()))

#5
from re import findall
def sum_of_integers_in_string(string: str) -> int:
    """ Get the sum of the integers inside a string. """
    return sum(map(int, findall("\d+", string)))

def sum_of_integers_in_string(s):
    for x in s:
        if not x.isdigit(): s = s.replace(x, ' ')
    return sum(map(int, s.split()))



def sum_of_integers_in_string(s):
    return sum([int(i) for i in s if i.isnumeric()])
#print(sum_of_integers_in_string(s))