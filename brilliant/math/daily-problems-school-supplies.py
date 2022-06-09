'''
https://brilliant.org/daily-problems/school-supplies/
'''
import sympy as sp
from sympy.abc import f, g, h, i

eq1 = sp.Eq((f + g + h)/3, i)
eq2 = sp.Eq((f + h)/2, g)
eq3 = sp.Eq((h + g)/2, f + i)

print(*sorted([(k, v.subs(i, 1)) for k, v in sp.solve([eq1, eq2, eq3]).items()]+ [(i, 1)], key=lambda x: x[1]))

# (f, 1/3) (g, 1) (i, 1) (h, 5/3)