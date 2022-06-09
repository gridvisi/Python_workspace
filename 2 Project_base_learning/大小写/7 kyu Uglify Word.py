'''
https://www.codewars.com/kata/5ce6cf94cb83dc0020da1929/train/python

在这个卡塔中，你必须制作一个名为uglify_word的函数（在Java和Javascript中为uglifyWord）。
它接受一个字符串参数。

uglify_word是做什么的？
它从前面检查给定字符串中的字符，并进行迭代，在迭代中，它做了以下步骤。

有一个标志，它将从1开始。
在迭代索引中检查当前的char。
如果是一个字母字符[a-zA-Z]，并且标志值等于1，那么将这个字符改为大写。
如果是一个字母字符[a-zA-Z]，并且标志值等于0，那么将这个字符改为小写。
否则，如果它不是一个字母字符，那么将标志值设置为1。
如果当前的char是字母字符，则对flag做一个布尔不操作。
迭代完成后，返回在这种迭代中可能被改变的固定字符串。

Test.assert_equals(uglify_word("AAA"), "AaA")
Test.assert_equals(uglify_word("AaA"), "AaA")
Test.assert_equals(uglify_word("BbB"), "BbB")
Test.assert_equals(uglify_word("aaa-bbb-ccc"), "AaA-BbB-CcC")
Test.assert_equals(uglify_word("AaA-BbB-CcC"), "AaA-BbB-CcC")
Test.assert_equals(uglify_word("eeee-ffff-gggg"), "EeEe-FfFf-GgGg")
Test.assert_equals(uglify_word("EeEe-FfFf-GgGg"), "EeEe-FfFf-GgGg")
Test.assert_equals(uglify_word("qwe123asdf456zxc"), "QwE123AsDf456ZxC")
Test.assert_equals(uglify_word("Hello World"), "HeLlO WoRlD")
'''

#6th solution by ericlee
import string
s = "qwe123asdf456zxc"
def uglify_word(s):
    ans = []
    flag = 1
    for e in s:
        if e in string.ascii_letters: #e.isalpha():
            #放在if循环outside会造成后果？
            if flag == 1:
                ans.append(e.capitalize())
                #flag = not flag
            else:
                ans.append(e.lower())
            flag = not flag
        else:
            flag = 1
            ans.append(e)
    return ''.join(ans)

s = "Hello World"
print(uglify_word(s))

#1st solution
import re

def uglify_word(s): return re.sub(r'[a-z]+',repl,s.lower())
def repl(m):        return ''.join( (str.upper,str.lower)[i&1](c) for i,c in enumerate(m[0]) )

#2nd solution
def uglify_word(s):
    flag = 1
    ugly = []
    for c in s:
        ugly.append(c.upper() if flag else c.lower())
        flag = not flag or not c.isalpha()
    return ''.join(ugly)

#rd solution
def uglify_word(s):
    r, f = [], 1
    for c in s:
        if not c.isalpha():
            f = 1
            r.append(c)
            continue
        r.append(getattr(c, ["lower", "upper"][f])())
        f = not f
    return "".join(r)