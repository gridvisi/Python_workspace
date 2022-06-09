'''
https://www.codewars.com/kata/primes-in-numbers/solutions/python
'''
n = 999
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

print(primeFactors(n))



import math
def isprime(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
for i in range(10000000,10001000):
    if isprime(i)== True:
        print('prime:',i)
print(10000993*10000891)
def primelist(n):
    pls = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if isprime(i) == True:
            pls.append(i)
    return pls


def primeFactors(n):
    p, s, pw = {}, '', 1
    if isprime(n) == True:
        return '(' + str(n) + ')'
    for i in primelist(n):
        while not n % i:
            if str(i) not in p.keys():
                p.update({str(i): 1})
                if isprime(n // i) == True:
                    p.update({str(n // i): 1})
                    for k, v in p.items():
                        s += '(' + str(k) + '**' + str(v) + ')' if v != 1 else '(' + str(k) + ')'
                    return s
            elif str(i) in p.keys():

                p[str(i)] += 1
            n = n // i
    for k, v in p.items():
        s += '(' + str(k) + '**' + str(v) + ')' if v != 1 else '(' + str(k) + ')'
    return s