'''
4+3x=8
6a-5+1=2-2a
-5+12Y=0
'''
import string
print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置
#'world hello world'

'''
print(string.ascii_letters)     # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.ascii_lowercase)   # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase)   # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.digits)            # '0123456789'
print(string.hexdigits)         # '0123456789abcdefABCDEF'
print(string.octdigits)         # '01234567'
print(string.printable)         # '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
print(string.punctuation)       # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.whitespace)        # ' \t\n\r\x0b\x0c'
print('————————————————')
s = 'ahelloaworld'
print(string.capwords(s, 'a'))
https://blog.csdn.net/c20081052/article/details/80920073
'''
import re
alpha = string.ascii_lowercase
operator = '+-='
#equation = input('')
equation = '3x+4-x=20'

res = re.findall(r'\d+[a-z]',equation)
resletter = re.findall(r'\[a-z]',equation)
print('refindall',res,resletter)
#res = [i for i in equation if i not in operator]
#res = re.split('[+=-]', equation)
re_left,re_right = re.split('[=]', equation)

print(re_left,re_right)
re_left,re_right = re_left.split('+-'),re_right.split('[+-]')
print(re_left,re_right)

'''
'.'

默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括\n

'^'

匹配字符开头

'$'

匹配字符结尾

'*'

匹配*号前的字符0次或多次

'+'

匹配前一个字符1次或多次

'?'

匹配前一个字符1次或0次

'{m}'

匹配前一个字符m次

'{n,m}

匹配前一个字符n到m次

'|'

匹配符号两边的任意一个，相当于或

'(...)'

分组匹配

'\A'

只从字符开头匹配，比如re.search("\Aabc","gggggabc") 是匹配不到的

'\Z'

匹配字符结尾，和$一样

'\d'

匹配数字0-9

'\D'

匹配非数字

'\w'

匹配[A-Za-z0-9]

'\W'

匹配非[A-Za-z0-9]

'\s'

匹配空白字符、\t、\n、\r 
————————————————
版权声明：本文为CSDN博主「昆昆欧粑粑」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/likunkun__/article/details/81707883
a = 'likunhong23student'
b = re.search("(?P<name>[a-zA-Z]+)(?P<age>[0-9]+)(?P<job>\w+)",a).groupdict()
print(b)

split()分割
res = re.split('[0-9]+', 'ab23bas23basd9989ad')
print(res)  #结果为['ab', 'bas', 'basd', 'ad']

'''
