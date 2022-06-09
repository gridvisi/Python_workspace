'''
https://www.codewars.com/kata/58069e4cf3c13ef3a6000168/train/python
'''
n = 1020
def reverse(n):
    return int(''.join([i for i in str(n)[::-1]][1:]) if str(n)[0] == 0 else str(n)[::-1])
print(reverse(n))

#1st solution
def reverse(n):
    m = 0
    while n > 0:
        n, m = n // 10, m * 10 + n % 10
    return m

#2nd solution
def reverse(n):
    return int(str(n)[::-1])

#rd solution
def reverse(n):
    r = 0
    while n:
        r = r*10 + n%10
        n //= 10
    return r