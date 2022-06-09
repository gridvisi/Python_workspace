'''
https://www.codewars.com/kata/sort-arrays-ignoring-case/train/python
Sort the given strings in alphabetical order, case insensitive. For example:
["Hello", "there", "I'm", "fine"]  -->  ["fine", "Hello", "I'm", "there"]
["C", "d", "a", "B"])              -->  ["a", "B", "C", "d"]
Test.assert_equals(sortme(["Hello", "there", "I'm", "fine"]), ["fine", "Hello", "I'm", "there"])
Test.assert_equals(sortme(["C", "d", "a", "B"]), ["a", "B", "C", "d"])
Test.assert_equals(sortme(["CodeWars"]), ["CodeWars"])

print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写
'''
words = ["Hello", "there", "I'm", "fine"] #["fine", "Hello", "I'm", "there"]
#words = ["CodeWars"]
def sortme(words):
    res = []
    if len(words) == 1:return words
    for w in words:
        res.append(w.capitalize())
    re = sorted(res)
    for i,e in enumerate(re):
        if e not in words:
            re[i] = re[i].lower()
    return re

def sortme(words):
    return sorted(words, key=str.lower)
print(sortme(words))

#6 kyu Convert string to camel case
'''
Complete the method/function so that it converts dash/underscore delimited words 
into camel casing. The first word within the output should be capitalized only 
if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case).

[w.lower() for w in sorted(res) if w[1:] in [u[1:] for u in words] and w not in words]
完成方法/函数，以便将以短划线/下划线分隔的单词转换为驼色大小写。
只有当原始单词大写时，输出中的第一个单词才应该大写
（称为上Camel Case，也称为Pascal Case）。
Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
Python中单引号，双引号，3个单引号及3个双引号的区别
https://blog.csdn.net/woainishifu/article/details/76105667
'''
def to_camel_case(text):
    if text.find('-') != -1:
        re = [w.capitalize() for w in text.split('-')[1:]]
        return text.split('-')[0]+''.join(re)
    elif text.find('_') != -1:
        re = [w.capitalize() for w in text.split('_')[1:]]
        return text.split('_')[0]+''.join(re)
    elif text.find('-') == -1:
        return ''

def to_camel_case(text):
    re = list(text)
    for i,e in enumerate(re):
        if e == '-' or e == '_':
            re[i] = ''
            re[i+1] = re[i+1].capitalize()
    return ''.join(re)

s = "the_Super-man"
def to_camel_case(s):
    return s[0] + s.title().translate(None,"-_")[1:] if s else s
#print('chongqing78'.translate(None,"gq"))
print(to_camel_case(s))
import re
def to_camel_case(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)

def to_camel_case(text):
    words = text.replace('_', '-').split('-')
    return words[0] + ''.join([x.title() for x in words[1:]])
'''
#translate() #方法语法
str.translate(table)
bytes.translate(table[, delete])
bytearray.translate(table[, delete])
text = 'love'
'''

text = "The-stealth-warrior"
text = 'the-stealth_warrior'
text = "the_stealth-warrior"
text = "the_stealth_warrior"
text = ''

text = "The-super-Man"
text = 'the-super_man'
text = "the_Super-man"
text = "the_super_man"
#text = ''
print(text.find('-'),text.find('_'))
#print("the_stealth_warrior".split('-'))
print(to_camel_case(text))

str1 = "List of name:\neric Li\ncharls Deng"
print(str1)