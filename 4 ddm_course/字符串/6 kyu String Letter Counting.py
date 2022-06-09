'''
https://www.codewars.com/kata/59e19a747905df23cb000024/train/python
'''
s = "The quick brown fox jumps over the lazy dog." #), "1a1b1c1d3e1f1g2h1i1j1k1l1m1n4o1p1q2r1s2t2u1v1w1x1y1z"
from collections import Counter
def string_letter_count(s):
    ans = sorted([(str(v),k) for k,v in (Counter(s.lower()).items()) if k.isalpha()],key=lambda x:x[1])
    return ''.join([''.join(i) for i in ans])
print( string_letter_count(s))

#1st solution
from collections import Counter

def string_letter_count(s):
    cnt = Counter(c for c in s.lower() if c.isalpha())
    return ''.join(str(n)+c for c,n in sorted(cnt.items()))

from collections import Counter

def string_letter_count(s):
    cnt = Counter(filter(str.isalpha, s.lower()))
    return ''.join(f'{v}{k}' for k, v in sorted(cnt.items()))