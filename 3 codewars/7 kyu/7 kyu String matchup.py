'''
https://www.codewars.com/kata/59ca8e8e1a68b7de740001f4/train/python

Test.assert_equals(solve(['abc', 'abc','xyz','abcd','cde'], ['abc', 'cde', 'uap']), [2, 1, 0])
Test.assert_equals(solve(['abc', 'xyz','abc', 'xyz','cde'], ['abc', 'cde', 'xyz']), [2, 1, 2])
Test.assert_equals(solve(['quick', 'brown', 'fox', 'is', 'quick'], ['quick', 'abc', 'fox']), [2, 0, 1])
'''
from collections import Counter
def solve(a,b):
    #dup,single = set(a,b),set(b)-set(a,b)
    res = dict([(k,v-1) for k,v in (Counter(a) + Counter(b)).items() if k in Counter(b).keys()])
    #print(sorted(res,key=lambda x:b[0]))
    return [res[k] for k in b]
#sorted([i[1] for i in res],key=lambda x:b)
a,b = ['quick', 'brown', 'fox', 'is', 'quick'], ['quick', 'abc', 'fox']

# 1st solution
def solve(a,b):
    return [a.count(e) for e in b]

# 2nd solution
from collections import Counter

def solve(a,b):
    c = Counter(a)
    return [c[s] for s in b]
print(solve(a,b))

# 3rd solution
def solve(a,b):
    return [a.count(x) for x in b]
