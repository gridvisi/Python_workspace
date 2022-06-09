'''
https://www.codewars.com/kata/5b162ed4c8c47ea2f5000023/train/python
'''

print(int('001'),'100'[:1],['100'] + ['099'] + ['99'])
def solve(n):
    x = str(n)
    res = [x] + [str(int(x[:i]) - 1) + '9' * (len(x) - i) for i in range(1,len(x))]
    #print(res)
    #print(lambda x : (sum(map(int,x)), int(x)))
    return int(max(res, key = lambda x : (sum(map(int,x)), int(x))))

n = 99
print(solve(n))

def dig_sum(n):
    return sum(map(int, str(n)))

def solve(n):
    candidates = [n] + [ n // 10**i * 10**i - 1 for i in range(1, len(str(n))) ]
    return max(candidates, key=dig_sum)

def solve(n):
    s = str(n)
    l = len(s)
    if l == 1 or (l == 2 and s[1] in {"8", "9"}):
        return n
    for i in range(l-1):
        if s[i+1] != "9":
           return int(f"{s[:i]}{int(s[i]) - 1}{'9' * (l - i - 1)}")

def solve(n): return max([n]+[n-n%10**i-1 for i in range(len(str(n)))],key=lambda n:(sum(map(int,str(n))),n))

def solve(n):
    s, i = [int(i) for i in str(n)], 1
    while i<len(s) and s[i]==9:i+=1
    s[i-1] -= 1
    s[i:] = [9]*len(s[i:])
    return max([n,int(''.join(map(str,s)))],key=lambda x:sum(int(i) for i in str(x)))

import numpy as np
def solve(n):
    x = str(n)
    max1 = sum([int(i) for i in x])
    ans = n
    for i in range(len(x)-1, 0, -1):
        a = str(int(x[:i])-1) + '9'*(len(x)-i)
        b = np.array(list(a)).astype(int)
        if b.sum() > max1:
            max1 = b.sum()
            ans = int(a)
    return ans


from itertools import product


def solve(n):
    result, last_ds = 0, str(n)[1:]
    for c in product('89', repeat=len(last_ds)):
        for i in range(0, 10):
            if int(str(i) + "".join(c)) <= n and int(str(i) + "".join(c)) > result:
                result = int(str(i) + "".join(c))

    return result

def solve(n):
    ln = list(map(int, str(n)))
    max_sum = ln[:]
    nine_index = len(ln) - 1
    while nine_index > 0:
        ln[nine_index] = 9
        ln[nine_index -1] -= 1
        if sum(ln) > sum(max_sum):
            max_sum = ln[:]
        nine_index -=1
    return int(''.join(map(str, max_sum)))