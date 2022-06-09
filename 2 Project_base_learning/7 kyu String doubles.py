'''
https://www.codewars.com/kata/5a145ab08ba9148dd6000094/train/python

Test.it("Basic tests")
Test.assert_equals(doubles('abbbzz'),'ab')
Test.assert_equals(doubles('zzzzykkkd'),'ykd')
Test.assert_equals(doubles('abbcccdddda'),'aca')
Test.assert_equals(doubles('vvvvvoiiiiin'),'voin')
Test.assert_equals(doubles('rrrmooomqqqqj'),'rmomj')
Test.assert_equals(doubles('xxbnnnnnyaaaaam'),'bnyam')
'''
s = 'xxbnnnnnyaaaaam'
s = 'rrrmooomqqqqj'  #'rmomj'

#1st solution
def doubles(s):
    cs = []
    for c in s:
        if cs and cs[-1] == c:
            cs.pop()
        else:
            cs.append(c)
    return ''.join(cs)

s = 'abbbzz'
s = 'xxbnnnnnyaaaaam'
print('while:',doubles(s))


from collections import deque
def doubles(s):
    i = 0
    ans = []
    ss = s + ' '
    flag = True
    for c in ss[1:]:
        print(c,s[i],flag)
        if c != s[i]:
            if flag:
                ans.append(s[i])
                flag = not flag
        flag = not flag
        i += 1  #s.index(x)
    return ans


# Not good solution!!
from collections import deque
def doubles(s):
    i, ans = 0, ''
    sq = deque(s)
    while len(deque(sq)) > 0:

        if sq[1] == s[-1]:
            return ans

        elif sq[0] == sq[1]:
            sq.popleft()
            sq.popleft()
            i += 2
            print(sq)
        elif sq[0] != sq[1]:
            ans += sq.popleft()
            ans += sq.popleft()
'''
Time: 600ms Passed: 1 Failed: 0 Exit Code: 1
Test Results:
 Basic tests
 STDERR
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    Test.assert_equals(doubles('zzzzykkkd'),'ykd')
  File "/home/codewarrior/solution.py", line 7, in doubles
    if sq[1] == s[-1]:
IndexError: deque index out of range
'''

from collections import Counter
def doubles(s):
    #sdict = Counter(s)
    ans = [(k*(v%2)) for k,v in Counter(s).items() if v%2 == 1]

    return ans

def doubles(s):
    #sq = deque()
    sq = []
    st = 0
    ans = []
    for i,e in enumerate(s):
        print(sq,st)
        if e == s[st] and st%2 == 0:
            sq.append(i)
            #st += 1
        elif e == s[st] and st%2 == 1:
            sq.pop(i)
        st += 1
    return sq

def doubles(s):
    i,j = 0,1
    ans = []
    flag = True
    while j < len(s):
        if s[i] == s[j]:
            j += 1
            #flag = not flag
        if (j-i) % 2 == 1:
            ans.append(s[i])

        if j == len(s) - 1 and s[i]!= s[j]:
            ans.append(s[j])
        i = j
        j += 1

    return ans

from collections import Counter
def doubles(s):
    ans = []
    i = 0
    while i < len(s)-1:
        flag = 0

        if s[i] == s[i+1]:
            i += 1
            flag += 1
            #flag = not flag
        if flag % 2 == 0:
            ans.append(s[i])
        i += 1
    if s[-1] != s[-2]: ans.append(s[-1])
    return ''.join(ans)

