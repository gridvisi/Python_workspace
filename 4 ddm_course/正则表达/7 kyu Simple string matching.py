'''
https://www.codewars.com/kata/5bc052f93f43de7054000188/train/python

Test.it("Basic tests")
Test.assert_equals(solve("code*s","codewars"),True)
Test.assert_equals(solve("codewar*s","codewars"), True)
Test.assert_equals(solve("code*warrior","codewars"),False)
Test.assert_equals(solve("c","c"),True)
Test.assert_equals(solve("*s","codewars"),True)
Test.assert_equals(solve("*s","s"), True)
Test.assert_equals(solve("s*","s"),True)
Test.assert_equals(solve("aa","aaa"), False)
Test.assert_equals(solve("aa*","aaa"), True)
Test.assert_equals(solve("aaa","aa"), False)
Test.assert_equals(solve("aaa*","aa"), False)
Test.assert_equals(solve("*","codewars"),True)
'''
import re
def solve(a,b):
    #result = re.match(r'\d([a-zA-Z]+)123', '2hjdh123ABC')
    result = re.match(r'([a])', b)
    result = re.findall(r'\a[0]([a-zA-Z])\a[-1]', b)
    result = re.match(r'\a[0]\w+\a[-1]', b)
    result = re.match(r'\a[0]*', b)
    result = re.match(r'[c]', b)
    ans = [i in b for i in a.split('*')]
    return ans[0] * ans[1] if len(ans) > 1 else ans[0]
a,b = "codewar*s","codewars"
a,b = "code*s","codewars"
a,b = "code*warrior","codewars"
a,b = "aa","aaa"
print(solve(a,b))


'''
#findall和finditer区别在于：
#findall返回一个列表，finditer返回的是迭代器。

# 5、re.fullmatch(patter, string, flags=0)
#必须整个字符串全部匹配字串才行，匹配失败返回None，成功也返回_sre.SRE_Match对象

'''
#1st solution
import re
def solve(a,b):
    return bool(re.fullmatch(a.replace('*', '.*'), b))

#2nd solution
from fnmatch import fnmatch
def solve(a, b):
    return fnmatch(b, a)

#3rd solution
def solve(a, b):
    if a == b: return True
    if "*" not in a: return False

    sides = a.split("*")
    missing = b[len(sides[0]):len(b) - len(sides[1])]
    c = a.replace("*", missing)
    return c == b

#4th solution
def solve(a,b):
    s = a.find("*")
    if s == -1:
        return a == b
    else:
        a = list(a)
        b = list(b)
        del b[s:s+1+len(b)-len(a)]
        a.remove("*")
        return a == b

#5th solution
import re

def solve(a, b):
    return bool(re.match(f"^{a.replace('*', '.*')}$", b))


# without re
#
def solve(a, b):
    if "*" in a:
        s, e = a.split("*")
        return b.startswith(s) and b.replace(s, "").endswith(e)
    else:
        return a == b

import re
def solve(a,b):
    pattern = a.replace("*", ".*")
    return bool(re.fullmatch(pattern, b))

import re
def solve(a,b):
    pattern = f'^{a.replace("*", ".*")}$'
    return bool(re.match(pattern, b))