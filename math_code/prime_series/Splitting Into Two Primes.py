'''
https://brilliant.org/problems/pals-forever/
将两个大质数相乘很容易。结果是一个巨大的非质数。然而，对这个数进行因式分解是不容易的。
这也是很多加密算法的基础。

999415083136585001是两个质数的乘积。这两个质数是回文。找出这两个质数的和。

Multiplying two large primes is easy. The result is a huge non-prime
number. Factoring this number however, is
non-trivial. This is the basis behind a lot of Cryptographic algorithms.

999415083136585001 is a product of two primes. These two primes
are palindromes. Find the sum of these two palindromes.
'''

import math
def fermat(n):
    a = int(math.ceil(n**0.5))
    bn = a*a - n
    b = int(bn**0.5)
    print(a, bn,b,n)
    while b*b != bn:
        a = a + 1
        bn = a*a - n
        b = int(bn**0.5)
    p = a+b
    q = a-b
    print(p,q)

#p+q = The answer is 1999414998.
n = 999415083136585001
fermat(n)