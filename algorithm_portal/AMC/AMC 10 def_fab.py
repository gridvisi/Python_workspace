'''
F(A * B) = F(A) + F(B)
A,B positive and rational
F(P) = P only if every prime number p
which x is F(x) < 0

17/32  11/16  7/9  7/6  25/11
'''
import math
def flog(x):
    return math.log(x,2)

def f(a,b):
    return flog(a * b)

#flog(a) + flog(b) == flog(a * b)

#f(p) = f(1) + f(p) = p
