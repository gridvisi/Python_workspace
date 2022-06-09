'''
https://www.codewars.com/kata/5716955a794d3013d00013f9/train/python
'''

import string
def the_var(the_variables):
    alpha = string.ascii_lowercase
    print(alpha)
    return alpha.index(the_variables[0]) + alpha.index(the_variables[2])

def the_var(vars):
    return sum(ord(c) - 96 for c in vars.split("+"))
the_variables = 'd+g'
print(the_var(the_variables))