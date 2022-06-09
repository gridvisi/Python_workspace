'''
https://www.codewars.com/kata/534ea96ebb17181947000ada/train/python

The sequence starts with subtraction rather than addition, and even if you start "from the back" it alternates
Prime numbers:

'''

def breakChocolate(n, m,cut = 0):
    if n == m == 0:
        return cut
    if m == 1:
        cut += n-1
        return cut
    else:
        cut += 2+n-1+m-1-1
        return breakChocolate(n-1, m-1,cut)
n,m = 0,0
print(breakChocolate(n, m))

def breakChocolate(n, m):
    return max(n*m-1,0)
'''
def breakChocolate(n, m,cut=0):
    n,m = max(n,m),min(n,m)
    cut = 0
    if m == 1:
        cut += n-1
        return cut
    else:
        cut += 2+n-1+m-1-1
        return breakChocolate(n-1, m-1) + breakChocolate(n-1, 1)+breakChocolate(1, m-1)
'''