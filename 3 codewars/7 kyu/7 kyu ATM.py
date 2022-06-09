# https://www.codewars.com/kata/5635e7cb49adc7b54500001c/train/python

'''
There is enough money available on ATM in nominal value 10, 20, 50, 100, 200 and 500 dollars.
You are given money in nominal value of n with 1<=n<=1500.
Try to find minimal number of notes that must be used to repay in dollars,
or output -1 if it is impossible.
'''

def solve(n):
    re = 0
    face_value = [10,20,50,100,200,500]
    while n >= face_value[0]:
        for i in face_value[::-1]:
            if n >= i:
                re,n = re+n // i,n % i
        if n == 0:
            return re
    return -1
n = 1033
print(solve(n))

def solve(n):
    if n%10: return -1
    c, billet = 0, iter((500,200,100,50,20,10))
    while n:
        x, r = divmod(n, next(billet))
        c, n = c+x, r
    return c

def solve(n):
    t=0
    for d in [500,200,100,50,20,10]:
        a,n=divmod(n,d)
        t+=a
    if n: return -1
    return t

def solve(n, cnt=0):
    if n%10: return -1
    for i in (500,200,100,50,20,10):
        cnt += n//i
        n = n%i
    return cnt