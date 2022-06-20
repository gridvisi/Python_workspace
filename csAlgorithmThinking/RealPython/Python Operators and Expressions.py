'''
Python Operators and Expressions
9%
That's correct!
In the Python statement x = a + 5 - b:
a and b are ________
a + 5 - b is ________
terms, a group
operands, an equation
operators, a statement
operands, an expression
Correct
The objects that operators act on are called operands.
An expression involving operators and operands is called an
expression.

Python Operators and Expressions
18%
That's correct!
What is the value of the expression 100 / 25?
Correct
If you answered 4, you might have forgotten that the result of
standard division is always float.
The value of 100 // 25 (integer division) is 4.

Python Operators and Expressions
27%
That's correct!
Is it safe to directly use the == operator to determine whether
objects of type float are equal?
Sure! Go for it.
Nope, not a good idea.
Correct
Internal representation of float objects is not precise, so they
can’t be relied on to equal exactly what you think they will:
>>>
>>> 1.1 + 2.2 == 3.3
False

You should instead compute whether the numbers are close enough
to one another to satisfy a specified tolerance:
>>>
>>> tolerance = 0.00001
>>> abs((1.1 + 2.2) - 3.3) < tolerance
True

Consider the following code snippet:
x = 10.0
y = (x < 100.0) and isinstance(x, float)

After these are executed, what is the value of y?
True
Correct
None
0
False
1
This is a case where the terms of the expression, (x < 100.0)
and isinstance(x, float), are both not only truthy, but actually
equal to the Python value True.
The expression is therefore also True.

Python Operators and Expressions
45%
That's correct!
Which of the following are truthy:
[]
0.000001
Correct
True
Correct
False
0
'None'
Correct
The Python object None is falsy, but the non-empty string
'None' is truthy.
0.000001, a non-zero numeric value, is also truthy. But barely
Python Operators and Expressions
54%
That's incorrect!

Suppose the following statements are executed:
a = 100
b = 200

What is the value of the expression a and b?
100
200
Incorrect
False
True
Incorrect
0
When two non-Boolean values are joined by and or or, the value
of the expression is one of the operands, not True or False.
For two non-Boolean values a and b:
If a is a or b ,  b is a and b:
truthy a b
falsy b a


63%
That's incorrect!
The function sqrt() from the math module computes the square root of a number.
Will the highlighted line of code raise an exception?
x = -100
from math import sqrt
x > 0 and sqrt(x)

No
Incorrect
Yes
Incorrect
In the highlighted line, x > 0 is False.
The expression is already known to be falsy at that point.
Due to short-circuit evaluation, sqrt(x)
(which would raise an exception) is not evaluated.

For two objects x and y:
x is y is True
if and only if
id(x) == id(y)
False
True

Which of the following operators has the lowest precedence?
and
Incorrect
**
%
+
not
Incorrect
and has the lowest precedence of all the operators covered in
this tutorial except or.
The question doesn’t state whether the + operator listed is
binary addition or unary positive.
But it doesn’t matter—it wouldn’t have a lower precedence than
and either way.

What is the value of the expression 1 + 2 ** 3 * 4?
36
4097
33
Correct
108
The ** operator has the highest precedence, followed by *, and + the lowest.
Thus, the calculations are performed as follows:
1 + (2 ** 3) * 4
1 +    (8    * 4)
1 +        32
      33

To spare the reader from recalling the order of precedence,
it wouldn’t be a bad idea to write this as 1 + ((2 ** 3) * 4),
even though the parentheses don’t change the way the expression
is evaluated

Write Python code to:
Create a variable x with the value 100
Increase the value of x fivefold using an augmented assignment
operator
Correct
For reference, here’s our solution:
x = 100
x *= 5


'''