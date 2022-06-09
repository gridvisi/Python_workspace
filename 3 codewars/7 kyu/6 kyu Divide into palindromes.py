'''
https://www.codewars.com/kata/5f8219c1ae0eb800291c50c1/train/python
Divide into palindromes 分成回文

@test.describe("Example tests")
def example_tests():
    test.assert_equals(lowest("aebecda"), 1)
    test.assert_equals(lowest("eutxutuatgextu"), 7)
    test.assert_equals(lowest("abbddc"), 3)
    test.assert_equals(lowest("abcd"), 1)
    test.assert_equals(lowest("aabbccdd"), 8)
    test.assert_equals(lowest(""), 0)
'''
from collections import Counter

def lowest(s):
    #if len(s) == 0: return 0
    temp = []
    C = Counter(str(s))
    odd = [k for k, v in C.items() if v % 2 == 1]
    if len(odd) == 0:return len(s)
    ans = dict(zip(odd,sorted(odd)))
    print(ans)
    for k,v in C.items():
        if v % (2*len(odd)) == 0:
            ans = dict([(key,value+k) for key,value in ans.items()])

        elif v <= len(odd) and v%2 == 0:
            return min([len(v) for k,v in ans.items()]) + 2
    return ans,temp

#1st solution
def lowest(s):
    if not s: return 0

    o = {i for i in s if s.count(i) % 2}
    s, o = len(s), len(o)

    return s // o - (s // o % 2 == 0) if o else s
s = "eutxutuatgextu"
#s = "aabbccdd"
#s = "aebecda"
print(lowest(s))

from collections import Counter

def lowest(s):
    no = sum(f % 2 for f in Counter(s).values())
    return len(s) if no == 0 else (len(s) - no) // no | 1

print('0 | 1:',0 | 1)
print('1 | 1:',1 | 1)
print('2 | 1:',2 | 1)
print('6 | 1:',6 | 1)


# not very good
from collections import Counter

def lowest(s):
    if len(s) == 0: return 0
    C = Counter(str(s))
    ans = [v % 2 == 0 for k, v in C.items()]

    if ans.count(1) < ans.count(0):
        return 1

    elif ans.count(0) > 0 and ans.count(1) % ans.count(0) == 0:
        return len(s) / ans.count(0)

    elif 2 * ans.count(1) == len(s):
        return len(s)
