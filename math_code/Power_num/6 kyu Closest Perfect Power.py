'''
https://www.codewars.com/kata/57c7930dfa9fc5f0e30009eb/train/python

Your task is to write a function that returns the perfect power nearest any number.

Notes
When the input itself is a perfect power, return this number
Since 4 is the smallest perfect power, for inputs < 4 (including 0, 1, and negatives) return 4
The input can be either a floating-point number or an integer
If there are two perfect powers equidistant from the input, return the smaller one
Examples
For instance,

 0  -->   4
11  -->   9    #  9 = 3^2
34  -->  32    # 32 = 2^5 and 36 = 6^2 --> same distance, pick the sm
'''

import math
def closest_power(n):
    close = 10000 #float("info")
    ans = []
    for e in range(2, math.ceil(n ** 0.5) + 1):
        gap = abs(math.log(n,e)- round(math.log(n,e)))
        if gap < close:
            ans.append([gap,e,round(math.log(n,e))])
    seq = sorted(ans)[:2]
    a,b = seq[0][1]**seq[0][2],seq[1][1]**seq[0][2]
    if abs(a - n) < abs(b - n):
        return a
    elif abs(a - n) > abs(b - n):
        return b

    return a
n = 34
print(closest_power(n))


from math import ceil, floor, log2

def closest_power(n):
    return (4 if n <= 4 else min(
        (f(n ** (1 / i)) ** i
            for i in range(2, ceil(log2(n)) + 1)
            for f in (floor, ceil)),
        key = lambda x: (abs(x - n), x)))