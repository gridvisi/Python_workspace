'''
https://www.codewars.com/kata/5a9078e24a6b340b340000b8/train/python
'''
import math
def isNextPrime(x):
    #lx = iter([i for i in range(int(math.sqrt(x)))])
    lx = [i for i in range(int(math.sqrt(x)))]
    if x == 2:return 2

    for i in range(3,int(math.sqrt(x))):
        if x % i != 0:
            lx = [j for j in lx if j%i != 0]
    return lx
x = 200
print(isNextPrime(x))


def isPrime(x):
    if x == 2:return True
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True
x = 27

print(isPrime(x))

def solve(n):
    if isPrime(n):return n
    s = 1
    while True:
        if isPrime(n-s):return n-s
        if isPrime(n+s):return n+s
        s += 1
print(solve(4))


#1st solution
def solve(n):
    print('starting with {0}'.format(n), flush=True)

    def is_prime(p):
        if p % 2 == 0 :
            return False
        for x in range(3,int(p**.5)):
            if p % x == 0:
                return False
        return True
        #return not any([p%x==0 for x in range(3,int(p**.5))])

    if is_prime(n):
        return n
    step = (n%2) + 1
    while 1:
        if is_prime(n-step):
            return n-step
        elif is_prime(n+step):
            return n+step
        else:
            step += 2
    return None

#2nd solution
from gmpy2 import is_prime as p

def solve(n,i=0):
    return p(n-i) and n-i or p(n+i) and n+i or solve(n,i+1)

#3rd solution
from gmpy2 import is_prime
from itertools import count

def solve(n):
    for i in count():
        if n > i and is_prime(n-i): return n-i
        if i > 0 and is_prime(n+i): return n+i