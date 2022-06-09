'''
https://brilliant.org/problems/pals-forever/
Multiplying two large primes is easy. The result is a huge non-prime number.
Factoring this number however, is non-trivial.
This is the basis behind a lot of Cryptographic algorithms.

999415083136585001 is a product of two primes. These two primes are palindromes.
Find the sum of these two palindromes.
两个大质数相乘很容易。结果是一个巨大的非质数。
然而，对这个数进行因式分解是不容易的。
这也是很多加密算法的基础。

999415083136585001是两个质数的乘积。这两个质数是回文。
找出这两个质数的和。
'''
import math
x = 999415083136585001
print(int(math.sqrt(x)))

def isPrime(n):
    if n == 2 or n==3:
        return n
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return n
x = 3
print(int(math.sqrt(x)))

print([i for i in range(100) if isPrime(i)])

def proPrime(x):
    bench = int(math.sqrt(x))
    print(bench)
    for i in range(2,bench+1):
        if isPrime(i):
            if x % i == 0:
                if isPrime(x//i):
                    return i,x//i
x = 77
x = 999415083136585001
print(proPrime(x))