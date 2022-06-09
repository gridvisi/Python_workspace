'''
https://www.codewars.com/kata/59aa6567485a4d03ff0000ca/train/python

Test.assert_equals(solve(1,25),4)
Test.assert_equals(solve(100,1000),28)
Test.assert_equals(solve(100,2000),47)
Test.assert_equals(solve(100,3000),65)
Test.assert_equals(solve(100,4000),95)
'''
import math
def square(x):
    sq = sum([int(i)**2 for i in str(x)])
    while sq:
        #print('sq:',sq)
        if sq == 10:
            return 1
        elif sq <= 10 or sq >= 10:
            sq = sum([int(i)**2 for i in str(sq)])
print(square(7))

def isPrime(x):
    if x!= 1 and (x == 2 or x == 3):
        return x

    elif x > 3:
        for i in range(2,int(math.sqrt(x))+1):
            if x % i == 0:
                return
        return x

print(len([isPrime(i) for i in range(1,1000) if isPrime(i)]))
print([isPrime(i) for i in range(1,1000) if isPrime(i)])


def solve(a,b):
    ans = [isPrime(i) for i in range(a,b+1) if isPrime(i)]
    return len([square(i) for i in ans if square(i)])

a,b = 100,4000
#print(solve(a,b))


#2nd solution
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqrtn = int(n ** 0.5) + 1
    for i in range(5, sqrtn, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def end_one(n):
    while n > 6:
        n = sum(map(lambda x: int(x) * int(x), f"{n}"))
        if n == 1:
            return True

def solve(a, b):
    return sum(1 for n in range(a, b) if is_prime(n) and end_one(n))

'''
import gmpy2
gmpy2.mpz(n)#初始化一个大整数
gmpy2.mpfr(x)# 初始化一个高精度浮点数x
d = gmpy2.invert(e,n) # 求逆元，de = 1 mod n
C = gmpy2.powmod(M,e,n)# 幂取模，结果是 C = (M^e) mod n
gmpy2.is_prime(n) #素性检测
gmpy2.gcd(a,b)  #欧几里得算法，最大公约数
gmpy2.gcdext(a,b)  #扩展欧几里得算法
gmpy2.iroot(x,n) #2x开n次根
'''

#1st solution
from gmpy2 import is_prime
from itertools import accumulate


def create_solver(n):
    cache = {1: 1}
    c2s = {str(a): a * a for a in range(10)}

    def f(n):
        seen = set()
        while n not in cache:
            seen.add(n)
            cache[n] = -1
            n = sum(map(c2s.get, str(n)))
        r = int(cache[n] == 1)
        for k in seen:
            cache[k] = r
        return r

    arr = list(accumulate(f(a) and is_prime(a) for a in range(n)))
    return lambda a, b: arr[b - 1] - arr[a - 1]


solve = create_solver(50_000)




a = [isPrime(i) for i in range(1,1000) if isPrime(i)]
p = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

for i in a:
    if i not in p:
        print('prime:',i,len(p))