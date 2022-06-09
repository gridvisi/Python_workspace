'''
https://www.codewars.com/kata/5f77d62851f6bc0033616bd8/train/python
你的任务是编写一个名为valid_spacing()或validSpacing()的函数，用来检查一个字符串是否具有有效的间距。
该函数应该返回 True 或 False。

对于这个卡塔，有效间距的定义是字与字之间有一个空格，并且没有前导空格或尾部空格。下面是函数返回的一些例子。
@test.describe('Sample Tests')
def sample():
    test.assert_equals(valid_spacing('Hello world'),True)
    test.assert_equals(valid_spacing(' Hello world'),False)
    test.assert_equals(valid_spacing('Hello  world '),False)
    test.assert_equals(valid_spacing('Hello'),True)
    test.assert_equals(valid_spacing('Helloworld'),True)

'Hello world' = True
' Hello world' = False
'Hello world  ' = False
'Hello  world' = False
'Hello' = True
# Even though there are no spaces, it is still valid because none are needed
'Helloworld' = True
# True because we are not checking for the validity of words.
'Helloworld ' = False
' ' = False
'' = True
'''


def valid_spacing(s):

    return s[0] != ' ' and s[-1] != ' ' and len(''.join(s.split(' '))) - len(s) < 2
s = ' Hello world'
print(valid_spacing(s))

