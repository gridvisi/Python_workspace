'''
https://www.codewars.com/kata/primes-in-numbers/train/python
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.
p = [i for i in range(2,int(math.sqrt(n)+1)) if not n%i]
Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

Test Results:
Test Passed
'' should equal '(7919)'
Test Passed
'(7537)' should equal '(7537)(123863)' =
Test Passed
'(7)' should equal '(7)(5113051)'
Test Passed
Test Passed
'''

print(7537*123863,7*5113051,(2**4*3*11*43*15073))
n = 86240
print(2**5 *5*7**2*11)
import math
def primeFactors(n,p = []):
    for i in range(2,n):
        if not n%i:
            p.append(i)
            print(n//i,p)
            last = n // i
            return primeFactors(n//i,p)
    return p

def isprime(n):
    if n == 1:return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

def primelist(n):
    pls = []
    for i in range(2,int(math.sqrt(n)) + 1):
        if isprime(i) == True:
            pls.append(i)
    return pls

print(isprime(1))
print(primelist(7919))

def primeFactors(n):
    p, s, pw = {}, '', 1
    if isprime(n) == True:
        return n
    for i in primelist(n):
        while not n % i:
            if str(i) not in p.keys():
                p.update({str(i): 1})
                if isprime(n//i) == True:
                    p.update({str(n // i): 1})
                    for k, v in p.items():
                        s += '(' + str(k) + '**' + str(v) + ')' if v != 1 else '(' + str(k) + ')'
                    return s
            elif str(i) in p.keys():
                print(i,p)
                p[str(i)] += 1
            n = n // i
    for k, v in p.items():
        s += '('+str(k)+'**'+ str(v)+')' if v != 1 else '('+str(k)+')'
    return s,p


n =7775460

n = 342217392   #return ('(2**4)(3)(11)(43)(15073**2)', {'2': 4, '3': 1, '11': 1, '43': 1, '15073': 2})
#n = 7919
#n = 933555431
#n = 35791357
#n = 86240


'''        

def primeFactors(n):
    p, s, pw = [], '', 1
    for i in range(2, n):
        while not n % i:
            p.append(i)
            n = n // i
    for i in sorted(set(p)):
        print(sorted(set(p)))
        s += '('+str(i) + '**' + str(p.count(i))+')' if p.count(i) !=1 else '('+ str(i)+')'
    return s
n =7775460
print(primeFactors(n))
'''

#TOP 1
def primeFactors(n):
    ret = ''
    for i in range(2, n + 1):
        num = 0
        while(n % i == 0):
            num += 1
            n /= i
        if num > 0:
            ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
        if n == 1:
            return ret
n = 342217392
n = 2019
n = 1000
n = 13701183019
n = 18611372500
n = 86729 * 17
n = 86240
print(n)
print(primeFactors(n))

def primeFactors(n):
    i, j, p = 2, 0, []
    while n > 1:
        while n % i == 0: n, j = n / i, j + 1
        if j > 0: p.append([i,j])
        i, j = i + 1, 0
    return ''.join('(%d' %q[0] + ('**%d' %q[1]) * (q[1] > 1) + ')' for q in p)

def primeFactors(n):
  result = ''
  fac = 2
  while fac <= n:
    count = 0
    while n % fac == 0:
      n /= fac
      count += 1
    if count:
      result += '(%d%s)' % (fac, '**%d' % count if count > 1 else '')
    fac += 1
  return result