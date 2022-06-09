
'''
Find the greatest common divisor of two positive integers. The integers can be large, so you need to find a clever solution.
The inputs x and y are always greater or equal to 1, so the the greatest common divisor will always be an integer that is
also greater or equal to 1.  gcd(a,b) = gcd(b,a mod b)
'''

#Try to make your own gcd method without importing stuff

x,y = 44,100
def mygcd(x,y):
    x,y =min(x,y),max(x,y)
    z = y % x
    if z == 0:
        return x
    return mygcd(x,z)
print(mygcd(x,y))
