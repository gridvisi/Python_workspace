'''
https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
Test.assert_equals(solution("helloWorld"), "hello World")
Test.assert_equals(solution("camelCase"), "camel Case")
Test.assert_equals(solution("breakCamelCase"), "break Camel Case")
Python提供了isupper()，islower()，istitle()方法用来判断字符串的大小写。
'''
s = "breakCamelCase" # "break Camel Case"
def solution(s):
    re = []
    for i in s:
        if i.isupper():
            re.append(' '+i)
        else:re.append(i)
    return ''.join(re)
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)
print(solution(s))

'''
 sl = list(s)
    re = " ".join(i) for i in sl if i.isupper()
'''