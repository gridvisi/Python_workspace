'''
https://www.codewars.com/kata/5aca48db188ab3558e0030fa/train/python

You have to create a function calcType, which receives 3 arguments: 2 numbers, and the
result of an unknown operation performed on them (also a number).

Based on those 3 values you have to return a string, that describes which operation was
used to get the given result.

The possible return strings are: "addition", "subtraction", "multiplication", "division".

Example:
calcT_type(1, 2, 3) -->   1 ? 2 = 3   --> "addition"
Notes
In case of division you should expect that the result of the operation is obtained by
using / operator on the input values - no manual data type conversion or rounding should
be performed.
Cases with just one possible answers are generated.
Only valid arguments will be passed to the function.
Only valid arguments will be passed to the function!

Test.assert_equals(calc_type(1, 2, 3), "addition")
Test.assert_equals(calc_type(10, 5, 5), "subtraction")
Test.assert_equals(calc_type(10, 4, 40), "multiplication")
Test.assert_equals(calc_type(9, 5, 1.8), "division")

FUNDAMENTALS
'''

#7th solve by eiclee
def calc_type(a, b, res):
    op = {"addition":a + b,
          "subtraction":a - b,
          "multiplication":a * b,
          "division":a/b}
    return [k for k,v in op.items() if v == res][0]
a, b ,res = 10, 4, 40
print(calc_type(a,b,res))

#1st
def calc_type(a, b, res):
    return {a + b: "addition", a - b: "subtraction", a * b: "multiplication", a / b: "division"}[res]

#3rd
def calc_type(a, b, res):
    dict = {a+b:'addition',a-b:'subtraction',a*b:'multiplication',a/b:'division'}
    return dict[res]

#4th
def calc_type(a, b, res):
    if a + b == res: return 'addition'
    if a - b == res: return 'subtraction'
    return 'multiplication' if a * b == res else 'division'



