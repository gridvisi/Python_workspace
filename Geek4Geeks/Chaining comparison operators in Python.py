'''
Checking more than two conditions is very common in Programming Languages. Let say we want to check below condition:

a < b < c
Most common syntax to do it is as follows:

if a < b and b < c :
   {...}
In Python, there is a better way to write this using Comparison operator
Chaining. The chaining of operators can be written as follows:

if a < b < c :
    {.....}
According to associativity and precedence in Python, all comparison
operations in Python have the same priority, which is lower than that
of any arithmetic, shifting or bitwise operation.
Also unlike C, expressions like a < b < c have the interpretation that
is conventional in mathematics.

List of comparison operators in Python:

">" | "<" | "==" | ">=" | "<=" | "!=" | "is" ["not"] | ["not"] "in"
Chaining in Comparison Operators:

Comparisons yield boolean values: True or False.
Comparisons can be chained arbitrarily. For example:
x < y <= z is equivalent to x < y and y <= z,
except that y is evaluated only once.
(but in both cases z is not evaluated at all when x < y is found to be false).

Formally, if a, b, c, …, y, z are expressions and op1, op2, …, opN are comparison operators, then a op1 b op2 c … y opN z is equivalent to a op1 b and b op2 c and … y opN z, except that each expression is evaluated at most once.
Also,
a op1 b op2 c
doesn’t imply any kind of comparison between a and c, so

 a < b > c
is perfectly legal.

'''

# Python code to illustrate
# chaining comparison operators
x = 5
print(1 < x < 10)
print(10 < x < 20 )
print(x < 10 < x*10 < 100)
print(10 > x <= 9)
print(5 == x > 4)


# Python code to illustrate
# chaining comparison operators
a, b, c, d, e, f = 0, 5, 12, 0, 15, 15
exp1 = a <= b < c > d is not e is f
exp2 = a is d > f is not c
print(exp1)
print(exp2)