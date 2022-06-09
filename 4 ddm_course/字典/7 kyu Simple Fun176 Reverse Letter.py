'''
https://www.codewars.com/kata/58b8c94b7df3f116eb00005b/train/python

Test.describe("Basic test")

Test.assert_equals(reverse_letter("krishan"),"nahsirk")

Test.assert_equals(reverse_letter("ultr53o?n"),"nortlu")

Test.assert_equals(reverse_letter("ab23c"),"cba")

Test.assert_equals(reverse_letter("krish21an"),"nahsirk")
'''

def reverse_letter(string):
    return ''.join([i for i in string if i.isalpha()])[::-1]
string = "ultr53o?n"
print(reverse_letter(string))

#1st solution
def reverse_letter(s):
  return ''.join([i for i in s if i.isalpha()])[::-1]

#2nd solution
def reverse_letter(string):
    return ''.join(filter(str.isalpha, reversed(string)))


#3rd solution
import re
def reverse_letter(string):
    return re.sub("[^a-zA-Z]","",string)[::-1]


#4th solution
def reverse_letter(s):
    return ''.join(filter(str.isalpha, s))[::-1]

# case study extend
info = "gfhajsh136ju879kdi"
'''
上述例子展示遍历info，若为英文，则使用空格代替，最后打印截取后的长度
isalpha:可用于判断字符串是否存在英文字母
isalnum:可用于判断字符串是否都是字母数字
'''
for i in info:
    if i.isalpha():
        info = info.replace(i," ")#若为字母，使用空格代替
l = info.split()
print(len(l))

'''
 正则判断是否含有英文和数字

 import re
 print(re.findall('.*r(.*)b.*', 'www.runoob.com'))
 
 判断有数字：re.match(r'[+-]?\d+$', s) s 为数字， 返回数字位置 ，
 not re.match(r'[+-]?\d+$', s) 返回为True说明不含有数字
 判断有英文字符： re.match(r'[a-z]+',s) 返回小写字母位置
 re.match(r'[a-z]+',s,re.I) 对大小写敏感。返回字母位置
 not re.match(r'[a-z]+',s,re.I) 返回为True说明没有英文字符
'''

import re
print(re.findall('.*r(.*)b.*', 'www.runoob.com'))
