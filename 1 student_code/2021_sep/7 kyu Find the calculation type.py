'''
https://www.codewars.com/kata/5aca48db188ab3558e0030fa/train/python

You have to create a function calcType, which receives 3 arguments: 2 numbers, and the result of an unknown operation performed on them (also a number).

Based on those 3 values you have to return a string, that describes which operation was used to get the given result.

The possible return strings are: "addition", "subtraction", "multiplication", "division".

Example:
calcT_type(1, 2, 3) -->   1 ? 2 = 3   --> "addition"
Notes
In case of division you should expect that the result of the
operation is obtained by using / operator on the input values -
no manual data type conversion or rounding should be performed.
Cases with just one possible answers are generated.
Only valid arguments will be passed to the function.
Only valid arguments will be passed to the function!

FUNDAMENTALS

test.assert_equals(calc_type(1, 2, 3), "addition")
test.assert_equals(calc_type(10, 5, 5), "subtraction")
test.assert_equals(calc_type(10, 4, 40), "multiplication")
test.assert_equals(calc_type(9, 5, 1.8), "division")
'''

def calc_type(a, b, res):
    ops = {
            '+':"addition",
            '-':"subtraction",
            '*':"multiplication",
            '/':"division"
            }
    for op,v in ops.items():
        if eval(str(a)+op+str(b)) == res:
            return v
a,b,res = 9, 5, 1.8
print(calc_type(a,b,res))

#1st
def calc_type(a, b, res):
    return {a + b: "addition", a - b: "subtraction", a * b: "multiplication", a / b: "division"}[res]

#2nd
def calc_type(a, b, res):
    if a + b == res:
        return "addition"
    elif a - b == res:
        return "subtraction"
    elif a * b == res:
        return "multiplication"
    else:
        return "division"

#3rd
from operator import add, sub, mul, truediv

OPS = (("addition", add),
       ("subtraction", sub),
       ("multiplication", mul),
       ("division", truediv))

def calc_type(a, b, res):
    return next(kind for kind,f in OPS if f(a,b)==res)