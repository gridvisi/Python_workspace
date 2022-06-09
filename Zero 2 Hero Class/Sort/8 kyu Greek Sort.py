'''
https://www.codewars.com/kata/56bc1acf66a2abc891000561/train/python

Examples
greek_comparator('alpha', 'beta')   <  0
greek_comparator('psi', 'psi')      == 0
greek_comparator('upsilon', 'rho')  >  0
'''

text = ['alpha', 'beta']
text = ['upsilon', 'rho']
print(sorted(text))

def greek_comparator(lhs, rhs):
    # the tuple greek_alphabet is defined in the global namespace
    text = [lhs, rhs]
    text_sort = sorted(text)
    return text,text_sort

lhs, rhs = 'up', 'down'
lhs, rhs = 'down','up'
print(greek_comparator(lhs, rhs))