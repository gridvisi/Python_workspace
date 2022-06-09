'''
https://www.codewars.com/kata/557e8a141ca1f4caa70000a6/train/python

Description:
A triangle number is a number where n objects form an equilateral triangle (it's a bit hard to explain). For example, 6 is a triangle number because you can arrange 6 objects into an equilateral triangle:

  1
 2 3
4 5 6
8 is not a triangle number because 8 objects do not form an equilateral triangle:

   1
  2 3
 4 5 6
7 8
In other words, the nth triangle number is equal to the sum of the n natural numbers from 1 to n.

Your task:
Check if a given input is a valid triangle number. Return true if it is, false if it is not (note that any non-integers, including non-number types, are not triangle numbers).

You are encouraged to develop an effective algorithm: test cases include really big numbers.

Assumptions:
test.assert_equals(is_triangle_number(3), True)
test.assert_equals(is_triangle_number(5), False)
test.assert_equals(is_triangle_number("hello!"), False)
test.assert_equals(is_triangle_number(6.15), False)
'''

# solution based on the fact that triangle numbers are defined by forumla n(n+1)/2
# so if we have integer n which can fit into formula for our number, then number is triangle
# We simply need to solve equation like ax^2+bx+c = 0 and check if answer is integer
# 25 ms for 34 tests

from math import sqrt
def is_triangle_number(number):
    if type(number) is not int:
        return False

    n = (-1 + sqrt(1 + 8 * number)) / 2.0
    if n.is_integer():
        return True
    return False

import re
def is_triangle_number(number):
    if str(type(number)) == "<class 'float'>" or isinstance(number,int) or number == 1:
        if int(number) == number:
            number = int(number)
        else:
            return False
    elif str(type(number)) == "<class 'list'>":
        number = number[0]
    elif str(type(number)) == "<class 'str'>":

        if not number.isdigit():
            return False
        number = int(number)
    else:
        return False
    right = 0
    for i in range(number):
        right += i
        if number == right:
            return True
    return False
number = 'hello'
#number = 10
number = "[6.0]"

print('alnum:',number.isalnum())
#number = [6.0]
print('eval:',eval(number))
print(is_triangle_number(number))


#re
import re
string="-1.5"
print(re.findall(r"\d+\.?\d*",string)[0])