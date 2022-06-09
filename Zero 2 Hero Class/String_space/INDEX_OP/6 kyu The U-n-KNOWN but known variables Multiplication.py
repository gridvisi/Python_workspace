'''
https://www.codewars.com/kata/571a8920b29485b065000582/train/python
'''
import string
def the_var(the_variables):
    alpha = string.ascii_lowercase
    return alpha.index(the_variables)
the_variables = 'j'
the_variables = 'p'
print([the_var(i) for i in 'jpol'])
print([ord(i.upper()) for i in 'jpol'])
print([ord(i.title()) for i in 'jpol'])

def score(c):
    return abs(ord(c) - ord('n'))

def the_var(s):
    a, b = s.split("*")
    return score(a) * score(b)