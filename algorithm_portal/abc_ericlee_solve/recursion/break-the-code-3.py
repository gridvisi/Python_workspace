# https://brilliant.org/problems/break-the-code-3/

def rec(n):
    if n <= 0:
        return 0
    return 3 + rec(rec(n - x))
n,x = 5,2
print(rec(n))
'''
the return value is 3 + something. so i checked what happened if n=3.
_ = 4 will result in return 0 -> no problem
_ = 3 will result in return 0 -> no problem
_ = 2 will again result in return 3+something -> might cause a problem

but big values for n will cause a problem for 3 and 4 too.
'''