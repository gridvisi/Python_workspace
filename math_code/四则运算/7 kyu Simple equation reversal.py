'''
https://www.codewars.com/kata/5aa3af22ba1bb5209f000037/train/python

Given a mathematical equation that has *,+,-,/, reverse it as follows:

solve("100*b/y") = "y/b*100"
solve("a+b-c/d*30") = "30*d/c-b+a"
More examples in test cases.

Good luck!
Please also try:

Simple time difference
Simple remove duplicates
'''

import re
def solve(eq):
    return ''.join(reversed(re.split(r'(\W+)', eq)))
eq = 'y/g/75+k/31-45+31/25+68-79-n-19+36*c+b*65*42-59+290'
out = '290+59-42*65*b+c*36+19-n-79-68+25/31+45-31/k+75/g/y'
print(solve(eq))

def solve(eq):
    #
    # implemantation takes advantage of abscence of spaces
    #
    leq = (eq.replace('*', ' * ')
             .replace('/', ' / ')
             .replace('+', ' + ')
             .replace('-', ' - ')
             .split(' '))

    out = ''.join(leq[::-1])

    return out

# not good solution by ericlee
def solve(eq):
    num = [c for c in eq if c.isnumeric()]
    it = iter(num)
    sq = eq[::-1]
    return ''.join([c if not c.isnumeric() else next(it) for c in sq])