# https://brilliant.org/daily-problems/polyglots/
'''
Out of 404404 students of Brilliant Language School, 192192 learn
German, 162162 Spanish, and 122122 French. Every student learns at
least one of these three languages.

Also, 3030 students learn both German and Spanish, 3030 students
both German and French, and 3030 both Spanish and French.

How many students learn all three languages?
'''

import sympy

U = 404
G = 192
S = 162
F = 122
GS = 30
GF = 30
SF = 30
X = sympy.Symbol('X')

# U = (counts) - (exactly doubly counted) - 2*(triply counted)
eq = sympy.Eq(U, F + G + S - (GF + GS + SF - (3*X)) - 2*X)

print(sympy.solve(eq))