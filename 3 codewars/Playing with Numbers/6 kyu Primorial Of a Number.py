

'''
https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124/train/python

Input >> Output Examples:
1- numPrimorial (3) ==> return (30)
Explanation:
Since the passed number is (3) ,Then the primorial should obtained
by multiplying 2 * 3 * 5 = 30 .

Mathematically written as , P3# = 30 .
2- numPrimorial (5) ==> return (2310)
Explanation:
Since the passed number is (5) ,Then the primorial should obtained
by multiplying 2 * 3 * 5 * 7 * 11 = 2310 .

Mathematically written as , P5# = 2310 .
3- numPrimorial (6) ==> return (30030)
Explanation:
Since the passed number is (6) ,Then the primorial should obtained
by multiplying 2 * 3 * 5 * 7 * 11 * 13 = 30030 .

Mathematically written as , P6# = 30030 .
'''


#1st
def num_primorial(n):
    primorial, x, n = 2, 3, n-1
    while n:
        if all(x % d for d in range(3, int(x ** .5) + 1, 2)):
            primorial *= x
            n -= 1
        x += 2
    return primorial



#3rd
def num_primorial(n):
    p = []
    val = 2
    while len(p) < n:
        for div in p:
            print('div:',div,p)
            if val%div==0:
                val += 1
                break
        else:
            p.append(val)
    val = 1
    for x in p:
        val *= x
    return val
n = 6
print(num_primorial(n))

p = []
for i in p:
    print('test for []:',2%i)
else:print("not excuse loop")
'''

#2nd
#from gmpy2 import next_prime


def num_primorial(n: int) -> int:
    p = prev = 1
    for _ in range(n):
        prev = next_prime(prev)
        p *= prev
    return p

'''


# Python Program to find prime numbers in a range

import time
def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n + 1)]

    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is
        # a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    c = 0

    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            c += 1
    return c,len(prime),[i for i,e in enumerate(prime) if e]

    # Driver function


import time
t0 = time.time()
c = SieveOfEratosthenes(100)
print("Total prime numbers in range:", c)

t1 = time.time()
print("Time required:", t1 - t0)




def num_primorial(m):
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    n = int(m**1.5)
    prime = [True for i in range(n + 1)]

    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is
        # a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    c = 0

    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            c += 1
    ans = [i for i,e in enumerate(prime) if e]
    res = 1
    '''
    for i in ans:
        if str(i) == str(i)[::-1]:
            res.append(i)
    '''
    for i in ans[2:m+3]:
        res *= i
    return res ,ans[2:m+3]#c,len(ans),res,len(res) #,ans[2:m+1]

m = 6
print(num_primorial(m))




import math
value = math.factorial(6)
print(value)