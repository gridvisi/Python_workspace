'''
https://brilliant.org/daily-problems/broken-fan/
'''
import sympy as sp
from   sympy.abc import a, b, c, d # angles from left to right

# all equations I found...
equations = [sp.Eq(a+b, 120), # a + b = 120
             sp.Eq(b+c+d, a), # b + c + d = a
             sp.Eq(c, d)]     # c = d

result = sp.solve(equations)
# {a: d + 60, b: 60 - d, c: d}
print(result[b]+result[c])
