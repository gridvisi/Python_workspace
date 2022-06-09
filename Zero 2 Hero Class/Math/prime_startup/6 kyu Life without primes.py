'''
https://www.codewars.com/kata/59f8750ac374cba8f0000033/train/python

Consider an array that has no prime numbers, and none of its elements has any prime digit. It would start with: [1,4,6,8,9,10,14,16,18,40,44..].

12 and 15 are not in the list because 2 and 5 are primes.

You will be given an integer n and your task will be return the number at that index in the array. For example:

solve(0) = 1
solve(2) = 6

      for i in str(ans):
            if i not in prim:
                continue

'''
prim = '2357'
ans = 44
print(all([i in prim for i in str(ans)]))
print(all([i for i in str(ans) if i in prim]))
print([i for i in str(ans) if i in prim])
print(all([[[]]]))

# [1,4,6,8,9,10,14,16,18,40,44..]

#1st
n,forbid = 100000, set("2357")
sieve, notPrimes = [0]*(n+1), [1]
for i in range(2, n+1):
    if sieve[i]:
        if not (forbid & set(str(i))): notPrimes.append(i)
    else:
        for j in range(i**2, n+1, i):  sieve[j] = 1

def solve(n): return notPrimes[n]

# Optimization Solution timeout solution > 12000ms
import math
def notPrime(x):
    if x==1 or x==0:return False
    return any([not x%i for i in range(2,int(x**0.5)+1)])

print('notPrime:',notPrime(11))

def solve(n):
    cunt,ans = 0,1
    res = []
    prim = ['2','3','5','7']
    while cunt < n:
        if all([i not in prim and notPrime(ans) for i in str(ans)]):
            res.append(ans)
            cunt += 1

        ans += 1
    return ans-1
n = 10
print(solve(n))





# timeout solution > 12000ms
import math
def isPrime(x):
    if x==1 or x==0:return False
    return all([x%i for i in range(2,int(x**0.5)+1)])

print('isPrime:',isPrime(11))

def solve(n):
    cunt,ans = 0,1
    res = []
    prim = ['2','3','5','7']
    while cunt <= n:
        if all([i not in prim and not isPrime(ans) for i in str(ans)]):
            res.append(ans)
            cunt += 1

        ans += 1
    return ans-1,cunt,res
n = 10
print(solve(n))


a = {';'}
print(list(a)[0])