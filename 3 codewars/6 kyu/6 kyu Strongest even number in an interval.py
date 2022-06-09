'''
https://www.codewars.com/kata/strongest-even-number-in-an-interval/train/python
Test.assert_equals(strongest_even(1, 2), 2)
test.assert_equals(strongest_even(5, 10), 8)
test.assert_equals(strongest_even(48, 56), 48)
test.assert_equals(strongest_even(129, 193), 192)
'''
import time
print(bin(129),bin(192))
n,m = 129,193

def strongest_even(n, m):
    bin_lst = min([str(bin(i))[2:][::-1] for i in range(n,m+1)])
    return int(str(bin_lst)[::-1],2)
start = time.time()
print('solution 1',strongest_even(n,m))
end = time.time()
print(end - start)

"""Strongest even number in an interval kata

Defines strongest_even(n, m) which returns the strongest even number in the set
of integers on the interval [n, m].

Constraints:
    1. 1 <= n < m < MAX_INT

Note:
    1. The evenness of zero is need not be defined given the constraints.
    2. In Python 3, the int type is unbounded. In Python 2, MAX_INT is
    determined by the platform.

Definition:
    A number is said to be more strongly even than another number if the
    multiplicity of 2 in its prime factorization is higher than in the prime
    factorization of the other number.
"""
from math import log2
m = 193
print(bin(m),log2(m),int(log2(m)))

def strongest_even(n, m):
    """Returns the strongest even number in the set of integers on interval
       [n, m].
    """
    #It can be shown that the largest power of 2 on an interval [n, m] will
    #necessarily be the strongest even number. Check first if the interval
    #contains a power of 2, by comparing the log2 of the endpoints.
    if int(log2(m)) > int(log2(n)):
        return 2**int(log2(m))

    #Modify the endpoints exclude any odd numbers. If the two endpoints are
    #equal, the original interval contains only a single even number. Return it.
    n += n % 2
    m -= m % 2
    if n == m:
        return n

    #All optimizations and edge cases are exhausted. Recurse with the
    #modified endpoints halved, and multiply the result by 2.
    return 2*strongest_even(n // 2, m // 2)
n,m = 1,1000000000
start = time.time()
print(strongest_even(n,m))
end = time.time()
print('solution log2',end - start)

def strongest_even(n, m):
    while True:
        if m & m - 1 < n: return m
        m &= m - 1
n,m = 9,11
print('9&8:',1001&1000)
start = time.time()
print('bit：',strongest_even(n,m))
end = time.time()
print(end - start)

#十进制6-9 为例：9 二进制为 1001  9-1= 1000
#位运算​：1001&1000 = 0​

#print('8&7:',1000& bin(7))
a,b = 8,7
print(bin(a),bin(b))
print(a & b)
print(a | b)
print(a and b)
print(a or b)

print('描述小南刚学了二进制，他想知道一个数的二进制表示中有多少个1，你能帮他写一个程序来完成这个任务吗？')

