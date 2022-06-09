'''
https://www.codewars.com/kata/5539fecef69c483c5a000015/train/python

a = [9923, 9931, 9941, 9967]
test.assert_equals(backwardsPrime(9900, 10000), a)
'''
start, stop = 9900, 10000
import math
def is_prime(n):
    if n == 1:return False
    if n == 2:return True
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            return False
    else:return True
print(is_prime(70207))
print(is_prime(1095403))
print(is_prime(3045901))

def backwardsPrime(start, stop):
    res = []
    x = [i for i in range(start,stop) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0]# your code
    for i in x:
        if is_prime(i):
            if is_prime(int(str(i)[::-1])):
                res.append(i)
    return res


def backwardsPrime(start, nd):
    return [i for i in range(start, nd + 1) if i != int(str(i)[::-1]) and isPrime(i) and isPrime(int(str(i)[::-1]))]

def isPrime(n):
    return all([n % i != 0 for i in range(2, int(n ** .5) + 1)])

start, stop = 1,2020
print(backwardsPrime(start, stop))