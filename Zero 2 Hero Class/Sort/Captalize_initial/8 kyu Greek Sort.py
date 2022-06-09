# https://www.codewars.com/kata/56bc1acf66a2abc891000561/train/python

greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')

def greek_comparator(lhs, rhs):
    return greek_alphabet[lhs] - greek_alphabet[rhs]