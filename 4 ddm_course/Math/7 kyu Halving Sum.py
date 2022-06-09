'''
https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d/train/python

Task
Given a positive integer n, calculate the following sum:

n + n/2 + n/4 + n/8 + ...
All elements of the sum are the results of integer division.

Example
25  =>  25 + 12 + 6 + 3 + 1 = 47
ALGORITHMS
'''

def halving_sum(n):

    ans = n
    while n >= 1:
        print(n)
        n = n//2
        ans += n
    return ans
n = 25
print(halving_sum(n))

#1st solution
def halving_sum(n):
    s=0
    while n:
        s+=n ; n>>=1
    return s

#2nd solution
def halving_sum(n):
    if n == 1:
        return 1
    else:
        return n + halving_sum(n//2)