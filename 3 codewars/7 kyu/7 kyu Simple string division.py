'''
https://www.codewars.com/kata/5b83c1c44a6acac33400009a/train/python

For example:
solve('1234',1) = 234 because ('1','234') or ('12','34') or ('123','4').
solve('1234',2) = 34 because ('1','2','34') or ('1','23','4') or ('12','3','4').
solve('1234',3) = 4
solve('2020',1) = 202
'''

def solve(st, k):
    length = len(st) - k
    return max(int(st[i:i + length]) for i in range(k + 1))

st,k = '1234',2
print(solve(st,k))
