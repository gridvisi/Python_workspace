# https://www.codewars.com/kata/59ccf051dcc4050f7800008f/train/python
# 关键结论，for loop 取代 while

import time
start, limit = 57345, 90061
def factor(n):
    re = [n//i for i in range(2,n) if n%i == 0]
    return sum(re)

def factor(x):
    n,d,re = x,2,[]
    #for i in range(1,n//2+1):
    while x > 2:
        if x%d == 0:
            re.append(d)
            re.append(x//d)
            x //= d
            #d = d + 1
        elif x%d != 0:
            #x = n
            d += 1
    return sum(set(re)),sorted(re)
x = 1071625
x = 2020
st = time.time()
print('factor '+f"{x}",factor(x))
nd = time.time()
print("time used:",nd - st)

n = x
n = 2020
def primeFactors(n):
    res = ''
    #res = []
    for i in range(2, n + 1):
        num = 0
        while n % i == 0:
            num += 1
            n /= i
            if num > 0:
                res += '({}{})'.format(i, '**%d' % num if num > 1 else '')
                #res.append((i,num))
            if n == 1:
                return res
st = time.time()
print(primeFactors(n))
nd = time.time()
print("time used:",nd - st)


'''
def buddy(start, limit):
    res = []
    for i in range(start,limit+1):
        print(i,factor(i),factor(factor(i)))
        if factor(factor(i)) == i+1:
            res.append((i,factor(i)))
    return res

start, limit = 10,50
#start, limit = 1071625, 1103735
print(buddy(start, limit))
'''

# 1st solution

def div_sum(n):
    divs = set()
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            divs.add(x)
            divs.add(n // x)
    return sum(divs)


def buddy(start, limit):
    for n in range(start, limit + 1):
        buddy = div_sum(n)
        if buddy > n and div_sum(buddy) == n:
            return [n, buddy]

    return "Nothing"
print(buddy(start, limit))

# 2nd solution

def buddy(start, limit):
    for n in range(start, limit + 1):
        m = s(n)
        if m > n and n == s(m):
            return [n, m]

    return "Nothing"

n = 2020
def s(n):
    s = 0
    for i in range(2, round(n ** 0.5)):
        if n % i == 0:
            s += i
            s += n // i
    return s
print(s(n))

n = 2020
def s(n):
    s,re = 0,[]
    for i in range(2, round(n ** 0.5)):
        if n % i == 0:
            re.append(i)
            re.append(n // i)
    return sorted(re)
print(s(n))