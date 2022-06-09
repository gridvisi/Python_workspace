'''
https://blog.csdn.net/linxinfa/article/details/93617615

1 概述
当我们在Python中使用正则表达式时，re模块内部会干两件事情：
编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
用编译后的正则表达式去匹配字符串。

那么如果一个正则表达式要重复使用几千次，出于效率的考虑，我们是不是应该先把这个正则先预编译好，
接下来重复使用时就不再需要编译这个步骤了，直接匹配，提高我们的效率

2 compile()
预编译十分的简单,re.compile()即可；演示如下：
'''

import re
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')  # 编译
A = re_telephone.match('010-12345').groups()  # 使用
print(A)  # 结果 ('010', '12345')
B = re_telephone.match('010-8086').groups()  # 使用
print(B)  # 结果 ('010', '8086')

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
C = re_telephone.match('010-80860101').groups()  # 使用'-'后的号码长度是3-8之间，否则报错：
# 长度不在(\d{3,8}，AttributeError: 'NoneType' object has no attribute 'groups'
print(C)  # 结果 ('010', '8086')

re_telephone = re.compile(r'^(\d{3})-(\d{4})-(\d{4})$')
d = re_telephone.match('137-0118-3019').groups()
print(d)

# 01：“.”匹配任意1个字符
result = re.match(".....", "baaop")
a = result.group()
print(a)
#结果：baaop

# 02:“[]”匹配[]中列举的字符
# 字符串第一个字符只要存在于[]中就能成功匹配，
# [a-zA-Z0-9_]表示可以匹配"a-z","A-Z","0-9"和"_"区间内的所有元素
result = re.match("[Aa]", "Aaaaaaabbba")
a = result.group()
print(a)
#结果：A

# 03:"\d"匹配数字，即0-9
result = re.match("嫦娥\d号", "嫦娥9号")
a = result.group()
print(a)
#结果：嫦娥9号

# 04：“\D”匹配非数字，即不是数字
result = re.match("嫦娥\D号", "嫦娥a号")
a = result.group()
print(a)
#结果：嫦娥a号

# 05：“\s”匹配空白，即 空格，tab键
result = re.match("嫦娥\s号", "嫦娥 号")
a = result.group()
print(a)
#结果：嫦娥 号

# 06：“\S”匹配非空白
result = re.match("嫦娥\S号", "嫦娥1号")
a = result.group()
print(a)
#结果：嫦娥1号

# 07："\w"匹配单词字符，即a-z，A-Z，0-9、_
result = re.match("嫦娥\w号", "嫦娥_号")
a = result.group()
print(a)
#结果：嫦娥_号

# 08："\W"匹配单词字符，即匹配非单词字符
result = re.match("嫦娥\W号", "嫦娥￥号")
a = result.group()
print(a)
#结果：嫦娥￥号

'''
一、re.sub(pattern, repl, string, count=0, flags=0)
re是正则的表达式，sub是substitute，表示替换
re.sub共有五个参数。

re.sub(pattern, repl, string, count=0, flags=0)
1
其中三个必选参数：pattern, repl, string

两个可选参数：count, flags

二、参数讲解
1、pattern参数
pattern，表示正则中的模式字符串，这个没太多要解释的。

需要知道的是：
反斜杠加数字："N，则对应着匹配的组matched group 比如\6""，表示匹配前面pattern中的第6个group
意味着，pattern中，前面肯定是存在对应的组，后面也才能去引用
举个例子

'''

import re

inputStr = "hello world, nihao world"
replacedStr = re.sub(r"hello (\w+), nihao \1", "dingdingmao", inputStr)
print("replacedStr = ", replacedStr)
#输出结果为: replacedStr =  "dingdingmao"

inputStr = "hello world, nihao world"
replacedStr = re.sub(r"world", "dingdingmao", inputStr)
print("replacedStr = ", replacedStr)
#输出结果为: replacedStr =  "dingdingmao"

'''
注意，上面的(\w+)，括号括起来表示一个组；
里面的\w表示匹配字母、数字、下划线，等价于[A-Za-z0-9_]；
然后+表示匹配前面的子表达式一次或多次。
所以(\w+)就是匹配多个字母、数字、下划线的意思。表达式中的\1表示匹配第一个组，第一个组就是(\w+)。
'''

