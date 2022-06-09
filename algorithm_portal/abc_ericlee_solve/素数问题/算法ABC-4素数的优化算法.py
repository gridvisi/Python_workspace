
def isPrime(x):
    if x == 1:return False
    elif x == 2:return True
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

import math
def isPrime(x):
    if x == 1:return False
    elif x == 2:return True
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i == 0:
            return False
    return True