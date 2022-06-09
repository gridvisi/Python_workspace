'''

目录
一、re.findall函数介绍
二、代码如下
三、re.findall中正则表达式(. *?)
四、re.findall中参数re.S的意义
一、re.findall函数介绍它在re.py中有定义：

def findall(pattern, string, flags=0):
    """Return a list of all non-overlapping matches in the string.

    If one or more capturing groups are present in the pattern, return
    a list of groups; this will be a list of tuples if the pattern
    has more than one group.
    Empty matches are included in the result."""
    return _compile(pattern, flags).findall(string)
返回string中所有与pattern匹配的全部字符串, 返回形式为数组。
findall()函数的两种表示形式
'''

import re

kk = re.compile(r'\d+')
print(kk.findall('one1two2three3four4'))
# [1,2,3,4]

# 注意此处findall()的用法，可传两个参数;
kk = re.compile(r'\d+')
print(re.findall(kk, "one123"))
# [1,2,3]

# https://www.codewars.com/kata/586d6cefbcc21eed7a001155/solutions/python
def longest_repetition(chars):
    if not chars: return ("", 0)
    longest = max(re.findall(r"((.)\2*)", chars), key=lambda x: len(x[0]))
    return (longest[1], len(longest[0]))

chars = 'abbabbbaa'
print(re.findall(r"((.)\2*)", chars))


# list = re.findall(regex,string,flag)

import re
string0 = 'abcdefgh'
list0 = re.findall('ab',string0)
print("string0:",list0)
# ['ab']


string1 = 'abcdefghab'
list1 = re.findall('ab',string1)
print("string1:",list1)
# ['ab', 'ab']


string2 = 'abcdefghab'
list2 = re.findall('(ab)cd',string2)
print("string2:",list2)
# ['ab']


string3 = 'abcdefghabcd'
list3 = re.findall('(ab)cd',string3)
print("string3:",list3)
# ['ab', 'ab'] 一个字组匹配到两处 只显示子组内容


string4 = 'abcdefghabcd'
list4 = re.findall('(ab)cd(ef)',string4)
print("string4:",list4)
# [('ab', 'ef')]

string5 = 'abcdefghabcd'
list5 = re.findall('((ab)cd(ef))',string5)
print("string5:",list5)
# [('abcdef', 'ab', 'ef')]  整体匹配到1处，有3个子组

string6 = 'abcdefghabcdef'
list6 = re.findall('(ab)cd(ef)',string6)
print("string6:",list6)
# [('ab', 'ef'), ('ab', 'ef')]


# 注意：
# 1.用findall来匹配时，如果正则表达式中没有子组，则返回的列表中的每一项都是匹配到的字符串，
# 匹配到几处就有几个
#
#
# 2.如果正则表达式中含有一个子组，
# 则返回的列表中的各项是匹配到的字符串的子组内容，整体匹配到几处就有几个子组内容
#
#
# 3.如果正则表达式中含有多个子组
# 则返回含有元组的列表
# 正则字符串整体匹配到几处就有几个元组
# 每个元组中的内容是 正则表达式每个子组匹配到的内容



import re

kk = re.compile(r'\d+')
kk.findall('one1two2three3four4')
# [1,2,3,4]

# 注意此处findall()的用法，可传两个参数;
kk = re.compile(r'\d+')
re.findall(kk, "one123")
# [1,2,3]


#二、实例代码 后面会讲解代码里的各个部分，先列出来

import re

str = 'aabbabaabbaa'
# 一个"."就是匹配除 \n (换行符)以外的任意一个字符
print(re.findall(r'a.b', str))  # ['aab', 'aab']

# *前面的字符出现0次或以上
print(re.findall(r'a*b', str))  # ['aab', 'b', 'ab', 'aab', 'b']

# 贪婪，匹配从.*前面为开始到后面为结束的所有内容
print(re.findall(r'a.*b', str))  # ['aabbabaabb']

# 非贪婪，遇到开始和结束就进行截取，因此截取多次符合的结果，中间没有字符也会被截取
print(re.findall(r'a.*?b', str))  # ['aab', 'ab', 'aab']

# 非贪婪，与上面一样，只是与上面的相比多了一个括号，只保留括号的内容
print(re.findall(r'a(.*?)b', str))  # ['a', '', 'a']

str = '''aabbab
         aabbaa
         bb'''  # 后面多加了2个b

# 没有把最后一个换行的aab算进来
print(re.findall(r'a.*?b', str))  # ['aab', 'ab', 'aab']

# re.S不会对\n进行中断
print(re.findall(r'a.*?b', str, re.S))  # ['aab', 'ab', 'aab', 'aa\n         b']

#三、re.findall中正则表达式(. *?)

str = 'aabbabaabbaa'
#1.符号.就是匹配除 \n(换行符)以外的任意一个字符

print('(r a.b',re.findall(r'a.b', str))
# ['aab', 'aab']

#2.符号 * 前面的字符出现0次或以上

print(re.findall(r'a*b', str))
# ['aab', 'b', 'ab', 'aab', 'b']

#3.符号. * 贪婪，匹配从. * 前面为开始到后面为结束的所有内容

print(re.findall(r'a.*b', str))
# ['aabbabaabb']

#4.符号. *? 非贪婪，遇到开始和结束就进行截取，因此截取多次符合的结果，中间没有字符也会被截取
print(re.findall(r'a.*?b', str))
# ['aab', 'ab', 'aab']

#5.符号(. *?) 非贪婪，与上面一样，只是与上面的相比多了一个括号，只保留括号的内容

print(re.findall(r'a(.*?)b', str))
# ['a', '', 'a']

#关于带括号与不带括号的区别

import re

string = "abcdefg  acbdgef  abcdgfe  cadbgfe"

# 不带括号
regex = re.compile("((\w+)\s+\w+)")
print(regex.findall(string))
# 输出：[('abcdefg  acbdgef', 'abcdefg'), ('abcdgfe  cadbgfe', 'abcdgfe')]

regex1 = re.compile("(\w+)\s+\w+")
print(regex1.findall(string))
# 输出：['abcdefg', 'abcdgfe']

regex2 = re.compile("\w+\s+\w+")
print(regex2.findall(string))
# 输出：['abcdefg  acbdgef', 'abcdgfe  cadbgfe']

#第一个 regex 中带有2个括号，其输出list 中包含2个 tuple
#第二个 regex 中带有1个括号，其输出内容是括号匹配到的内容，而不是整个表达式所匹配到的结果。
#第三个 regex 中不带括号, 其输出的内容就是整个表达式所匹配到的内容。
#实际上这并不是python特有的，这是正则所特有的 ， 任何一门高级语言使用正则都满足这个特点：
# 有括号时只能匹配到括号中的内容，没有括号【相当于在最外层增加了一个括号】。在正则里面
"()"
#代表的是分组的意思，一个括号代表一个分组，你只能匹配到"()"中的内容。

#四、re.findall中参数re.S的意义
#1.字符串变为（后面多加了2个b）

str = '''aabbab
         aabbaa
         bb'''

#2.参数无re.S，没有把最后一个换行的aab算进来

print(re.findall(r'a.*?b', str))
# ['aab', 'ab', 'aab']

#3.参数有re.S，不会对\n进行中断

print(re.findall(r'a.*?b', str, re.S))
# ['aab', 'ab', 'aab', 'aa\n         b']

#1.先说一下findall()函数的两种表示形式
import re

kk = re.compile(r'\d+')
kk.findall('one1two2three3four4')
# [1,2,3,4]

# 注意此处findall()的用法，可传两个参数;
kk = re.compile(r'\d+')
re.findall(kk, "one123")
# [1,2,3]

#2.正则表达式可能遇到的坑 - -- 正则表达式中有括号()
#1.正则表达式中当没有括号时，就是正常匹配，在本例中
"/w+/s+/w+"
#第一次匹配到的字符为
#"2345  3456", 由于是贪婪模式会继续匹配, 第二次从
"4567"
#开始匹配匹配到的结果为字符串
"4567 5678"

import re

string = "2345  3456  4567  5678"
regex = re.compile("\w+\s+\w+")
print(regex.findall(string))
# ['2345 3456', '4567 5678']

# !!!  首先的知道各个字符所表达的含义，这里只说一下 / s 和 / S
#\s - - 匹配任何不可见字符，包括空格、制表符、换页符等等
#\S - - 匹配任何可见字符
#通常[ / s / S] -- 可匹配任意字符
#[\s\S] * ? -- 匹配懒惰模式的任意字符

#2.正则表达式中有一个括号时, 其输出的内容就是括号匹配到的内容，而不是整个表达式所匹配到的结果, 但是整
# 个正则表达式执行了只不过只输出括号匹配到的内容, 在第一次匹配时跟上述没有括号时一样，匹配到
# "2345  3456", 只不过只输出( / w +)匹配到的结果 即 "2345", 第二次匹配同理从"4567"开始，匹配到
#"4567  5678", 但是还是只是输出 "4567"

import re

string = "2345  3456  4567  5678"
regex = re.compile("(\w+)\s+\w+")
print(regex.findall(string))
# ['2345', '4567']

#3.当正则表达式中有两个括号时，其输出是一个list中包含2个tuple, 从输出的结果可以看出，有两个元组，每一个元组中有两
#个字符串: 其中第一个字符串"2345 3456" 是最外面的括号输出的结果，第二个是里面括号( / w +)输出的结果
#"2345", 第二个元组是第二次匹配的结果 - - 详解同第一次匹配。

import re

string = "2345  3456  4567  5678"
regex = re.compile("((\w+)\s+\w+)")
print(regex.findall(string))
# [('2345  3456', '2345'), ('4567  5678', '4567')]



