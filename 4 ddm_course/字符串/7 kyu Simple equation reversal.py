# https://www.codewars.com/kata/5aa3af22ba1bb5209f000037/train/python
'''
Test.it("Basic tests")
Test.assert_equals(solve("100*b/y"),"y/b*100")
Test.assert_equals(solve("a+b-c/d*30"),"30*d/c-b+a")
Test.assert_equals(solve("a*b/c+50"),"50+c/b*a")

s.isalnum()  所有字符都是数字或者字母，为真返回 Ture，否则返回 False。（重点，这是字母数字一起判断的！！）
s.isalpha()   所有字符都是字母，为真返回 Ture，否则返回 False。（只判断字母）
s.isdigit()     所有字符都是数字，为真返回 Ture，否则返回 False。（只判断数字）
s.islower()    所有字符都是小写，为真返回 Ture，否则返回 False。
s.isupper()   所有字符都是大写，为真返回 Ture，否则返回 False。
s.istitle()      所有单词都是首字母大写，为真返回 Ture，否则返回 False。
s.isspace()   所有字符都是空白字符，为真返回 Ture，否则返回 False。

'''
s = 'abcde'
sl = [1,2,3,4]
sl.reverse()
print(s)
print(reversed(s))
print('1'.isdigit())

eq = "a*b/c+50"
eq = "a+b-c/d*30"
eq = "100*b/y"
def solve(eq):
    num = [c for c in eq if c.isnumeric()]
    #it = iter(''.join(num))
    it = iter(num)
    #print('x:',num)
    sq = eq[::-1]
    return ''.join([c if not c.isdigit() else next(it) for c in sq])

# 1st solution
import re

def solve(eq):
    return ''.join(reversed(re.split(r'(\W+)', eq)))
print(solve(eq))

#2nd solution
def solve(eq):
    #
    # implemantation takes advantage of abscence of spaces
    #
    leq = (eq.replace('*', ' * ')
             .replace('/', ' / ')
             .replace('+', ' + ')
             .replace('-', ' - ')
             .split(' '))

    out = ''.join(leq[::-1])

    return out

def solve(eq):
    s = eq.replace('+',' + ').replace('-',' - ').replace('/',' / ').replace('*',' * ')
    return ''.join(s.split()[::-1])


import re
def solve(eq):
    return "".join(re.split("([*+-/])", eq)[::-1])


#Not good!
from collections import deque
def solve(eq):
    num,res = '',''
    sq = deque(eq)

    while sq:
        print(sq)
        if not sq.pop().isdigit:
            res += sq.pop()
        else:
            num += sq.pop()
    return num,res

# Not good!
def solve(eq):
    i,j = 0, 1
    ans = ['']*len(eq)
    #print(ans)
    while i < j < len(eq):
        if not eq[i:j].isdigit():
            ans[len(eq)-i-1] = eq[i]
            i += 1
            j += 1
        elif eq[i:j].isdigit():
            j += 1
            ans.insert(0, eq[i:j])
    return ans
