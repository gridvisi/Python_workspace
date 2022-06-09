'''
https://www.codewars.com/kata/59c32c609f0cbce0ea000073/train/python

Examples
One such triple is 3, 4, 5. For this challenge, you would be given the value 60 as the argument to your function, and then it would return the Pythagorean triplet in an array [3, 4, 5] which is returned in increasing order. 3^2 + 4^2 = 5^2 since 9 + 16 = 25 and then their product (3 * 4 * 5) is 60.

More examples:

argument	returns
60	[3, 4, 5]
780	[5, 12, 13]
2040	[8, 15, 17]
ALGORITHMSMATHEMATICSNUMBERS

Test.assert_equals(pythagorean_triplet(60), [3, 4, 5])
Test.assert_equals(pythagorean_triplet(780), [5, 12, 13])
Test.assert_equals(pythagorean_triplet(2040), [8, 15, 17])

def pythagorean_triplet(n):
    for x in range(1,n):
        for y in range(1,n):
            for z in range(1,n):
                if x^2 + y^2 == z^2 and x*y*z == n:
                    return x,y,z
'''
import math
print([math.sqrt(x) for x in [60,780,2040]])
def pythagorean_triplet_4(n):
    for x in range(1,n):
        for y in range(1,n):
            if x**2 + y**2 == int((n/(x*y))**2):
                return [x,y,int(n/(x*y))]
#solution *
def pythagorean_triplet_3(n):
    for x in range(1,n):
        for y in range(1,n):
            if x*x + y*y == int((n/(x*y))*(n/(x*y))):
                return [x,y,int(n/(x*y))]


def pythagorean_triplet_2(n):
    for x in range(1,n):
        for y in range(1,n):
            if math.sqrt(x*x + y*y) == int(n/(x*y)):
                return [x,y,int(n/(x*y))]
'''
Test Results:
Execution Timed Out
STDERR
Execution Timed Out (12000 ms)
'''
# since math.sqrt(a*b) < c: abc/math.sqrt(a*b) > abc/c,so that ab < n/math.sqrt(a*b)
# a*b < c^2: a*b*c<c^3 so that log3 n < c
import math

print(math.log(8,2))
# pow(8,float(1)/float(3))
# 8的开三次方


def pythagorean_triplet(n):
    bench = int(pow(n,float(1)/float(3)))
    for c in range(bench,n):
        for y in range(int(math.sqrt(n/bench)),n):
            if n%(y*c) == 0 and y*y + (n/(y*c))**2 == c*c:
                return [n//(y*c),y,c]
'''
Execution Timed Out
STDERR
Execution Timed Out (12000 ms)
'''
n = 2040

import time
st = time.time()
print(pythagorean_triplet(n))
end = time.time()
print(end - st)

st = time.time()
print(pythagorean_triplet_2(n))
end = time.time()
print(end - st)


st = time.time()
print(pythagorean_triplet_3(n))
end = time.time()
print(end - st)

st = time.time()
print(pythagorean_triplet_4(n))
end = time.time()
print(end - st)

def pythagorean_triplet(n):
    for a in range(3, n):
        for b in range(a+1, n):
            c = (a*a + b*b)**0.5
            if a*b*c > n:
                break
            if c == int(c) and a*b*c == n:
                return [a, b, c]
n = 60
print(pythagorean_triplet(n))





'''
勾股数的通解
勾股数a^2+b^2=c^2
的所有解都可以写为
a=2mn
b=m^2-n^2
c=m^2+n^2
的形式
其中m,n为任意正整数
'''

def pythagorean_triplet(n):
    ans = []
    for a in range(3, n):
        for b in range(a+1, n):
            c = (a*a + b*b)**0.5

            if a+b+c > n:
                break
            if c == int(c):# and a+b+c == n:
                ans.append((a,b,int(c)))
    return ans
n = 100
print('a+b+c<n:',pythagorean_triplet(n))

def judgeSquareSum(c):
    """
    :type c: int
    :rtype: bool
    """

    if c == (int(c ** 0.5) ** 2):
        return True

    lo, hi = 0, int(c ** 0.5)
    while (lo <= hi):
        s = lo ** 2 + hi ** 2
        if s == c:
            return True
        elif s > c:
            hi -= 1
        else:
            lo += 1
    return False
print(judgeSquareSum(50))


