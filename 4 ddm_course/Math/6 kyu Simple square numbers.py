'''
https://www.codewars.com/kata/5edc8c53d7cede0032eb6029/train/python

solve(13) = 36
# because 36 is the smallest perfect square that can be added to 13 to form a perfect
square => 13 + 36 = 49

solve(3) = 1 # 3 + 1 = 4, a perfect square
solve(12) = 4 # 12 + 4 = 16, a perfect square
solve(9) = 16
solve(4) = -1
'''
# since that:(x + x - i) * i == n
# so that: x = (n/i + i)/2
import math
def solve(n):
    i = 1
    while n % i == 0:
        if (n//i + i) % 2 == 0:
            sqr = (n//i + i)//2
            print(sqr)
            if (sqr+sqr-i) * i == n:
                return (sqr-i)**2
        i += 1
    return -1
n = 17
print(solve(n))

#1st solution
def solve(n):
    for i in range(int(n**0.5), 0, -1):
        x = n - i**2
        if x > 0 and x % (2*i) == 0:
            return ((n - i ** 2) // (2 * i)) ** 2
    return -1