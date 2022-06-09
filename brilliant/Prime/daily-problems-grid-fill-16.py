'''
https://brilliant.org/daily-problems/grid-fill-16
'''

def isPrime(x):
    if x==1 or x==2:return False
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
    else:
        return True

p = [i for i in range(3,30) if isPrime(i)]
print(p)

from itertools import combinations
from itertools import permutations
def test(p):
    a, b, c, d, e, f, g = p
    target = a + b + c
    # target must be prime...
    if target in (2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 37, 39, 41, 43, 47, 53, 59):
        if a + d + g == target and e + d + c == target and e + f + g == target:
            print(p)
            print("answer is ", b + d + f)
            return True
    return False
nums = (5, 7, 11, 13, 17, 19, 23)
for p in permutations(nums):
    if test(p):
        break

import itertools
for t in itertools.permutations((5,7,11,13,17,19,23)):
    if sum(t[:3])==sum(t[4:])==sum(t[0:7:3])==sum(t[2:5]):
        print(t,f" mid column sum={sum(t[1:6:2])}")


import itertools
board = [5, 7, 11, 13, 17, 19, 23]
number = list(itertools.permutations(board))
for row in number:
    a = row[0] + row[1] + row[2]
    b = row[2] + row[3] + row[4]
    c = row[4] + row[5] + row[6]
    if a == b and b == c:
        d = row[2] + row[4] + row[6]
        if d == 37 or d == 39 or d == 41 or d== 43:
            print(d)
'''
Output:
        39
        39 
'''