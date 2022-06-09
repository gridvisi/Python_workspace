
# -*- coding:utf-8 -*-
# re 正则表达式
import re

# raw string 原生字符串
s1 = "abc\nop"
s2 = r"abc\nop"
print("s1=",s1)
print("s2=",s2)# 逗号隔开的输出会默认输出一个空格以分开
print(s2,s2) # 再次验证该空格

# -*- coding:utf-8 -*-
# re 正则表达式
import re
# patter 正则表达式
# string 待匹配的母字符串
# flags 标志位：是否区分大小写、是否多行匹配

text = 'This is a student,named MY from SJTU University.'

# re.match(pattern, string, flags=0)
# 定死了必须从开头的首元素位置（索引为0）开始匹配
res = re.match('This',text)# 默认flag为0，完全匹配模式（严格大小写、字符配对）
# <re.Match object; span=(0, 4), match='This'>
print(res)
res = re.match('this',text)
# None
print(res)
res = re.match('this',text,re.I)# 置 flags 为 re.I后忽略大小写；爬虫数据清洗通常使用多行匹配且不区分大小写的匹配模式
# <re.Match object; span=(0, 4), match='This'>
print(res)
res = re.match('is',text) # None，re.match()非开头即是匹配得到也不能够配对
print(res)
res = re.match('(.*)is',text)
# "."匹配任意字符（默认为贪婪模式、尽可能多地匹配） + "*"匹配前一个字符0次或多次 = 若存在，则往前取任意多字符直到起始位置（全部取）
# <re.Match object; span=(0, 7), match='This is'>
print(res)
res = re.match('(.*) is',text)# ' is'往前全部取、包括正则表达式子串本身（贪婪、会尽可能多匹配），上一个是'is'往前全部取，两者运行结果一样
# <re.Match object; span=(0, 7), match='This is'>
print(res)
res = re.match('(.*) is ',text)# ' is '往前全部取（包括正则表达式子串本身、贪婪模式会尽可能多匹配）
# <re.Match object; span=(0, 8), match='This is '>
print(res)
res = re.match('(.*?)is',text)# ‘？'匹配前一个元素0次或1次，默认懒惰模式、尽可能少匹配、故不含包括正则表达式子串，此例子中即不含'is'
# <re.Match object; span=(0, 4), match='This'>
print(res)
res = re.match('(.*?) is',text)
# <re.Match object; span=(0, 5), match='This '># 注意区分这句与上一句，一个空格引起差异
print(res)
res = re.match('(.*?)is ',text)
# <re.Match object; span=(0, 7), match='This is'>
print(res)
res = re.match('(.*?) is ',text) # 由上述三句可知'?'懒惰模式无法舍弃空格
# <re.Match object; span=(0, 8), match='This is '>
print(res)

'''
re.match(pattern, string, flags=0)
实例运行结果
'''
# -*- coding:utf-8 -*-
# re 正则表达式
import re

str = 'This is the last one'
res = re.match('(.*) is (.*?).*',str,re.M | re.I)
print(res)
res = re.match('(.*) is (.*?)(.*)',str,re.M | re.I)
print(res)
res = re.match('(.*) is (.*).*',str,re.M | re.I)
print(res)
res = re.match('(.*) is (.*)',str,re.M | re.I)
print(res)
# 以上四个运行结果同为 <re.Match object; span=(0, 20), match='This is the last one'>
res = re.match('(.*) is (.*?)',str,re.M | re.I)
print(res)
# <re.Match object; span=(0, 8), match='This is '>
# 由上可知，'.*'贪心匹配、元素有则取之
# 由上可知，'.*？'懒惰匹配、满足正则子串即可（注意：空格也要匹配）
# 数据清洗通常使用多行匹配 re.M 且不区分大小写 re.I 的匹配模式

#强化理解一：贪心模式与懒惰模式
text = "aAbBAABBCcCcDdDdcCdD"

print( re.match("a.*d",text,re.I))
# <re.Match object; span=(0, 20), match='aAbBAABBCcCcDdDdcCdD'>
print( re.match("a.*d",text))
# <re.Match object; span=(0, 19), match='aAbBAABBCcCcDdDdcCd'>
print( re.match("a.*?d",text))
# <re.Match object; span=(0, 14), match='aAbBAABBCcCcDd'>
print( re.match("a.*?d",text,re.I))
# <re.Match object; span=(0, 13), match='aAbBAABBCcCcD'>

print( re.match("a.*b",text,re.I))
print( re.match("a.*?b",text,re.I))
print( re.match("a.*?B",text),re.I)
print( re.match("a.*?B",text))
print( re.match("a.*?b",text))
# 上边四句的输出结果依次对应如下：
# <re.Match object; span=(0, 8), match='aAbBAABB'>
# <re.Match object; span=(0, 3), match='aAb'>
# <re.Match object; span=(0, 4), match='aAbB'> RegexFlag.IGNORECASE
# <re.Match object; span=(0, 4), match='aAbB'>
# <re.Match object; span=(0, 3), match='aAb'>

'''
强化理解二：实例补充
	贪心尽可能多、从原母字符串原长逐渐剔减，
	惰性则正则字串刚好满足条件即可
	
	由此两个强化理解的实例可知，re.match的正则表达式为字符串，需要使用单或双引号格式，但有无小括号并不影响re.match的匹配。
	剩下的诸如特殊表达式序列、字符集、以花括号指定匹配次数、顺/逆序肯/否定环视等知识点，多多敲码、多看官方文档。
视野拓展：查看官方的开发文档
'''
# -*- coding:utf-8 -*-
import re
text = 'This is a text written by MY ,' \
       'from SheHui University on 2019/11/06 at 00:39.'
res = re.search(r'(\d)',text,re.I)
# <re.Match object; span=(69, 70), match='2'>
# \d 同 [0-9] 匹配任意（单个）十进制数
print(res)
res = re.search(r'(\D)',text,re.I|re.M)
# <re.Match object; span=(0, 1), match='T'>
# \D 同 [^0-9] 匹配任意（单个）非数字字符
# 注意：符号^在方括号内
print(res)

res = re.search(r'(\d).*',text,re.I|re.M)
# <re.Match object; span=(69, 89), match='2019/11/06 at 00:39.'>
print(res)
# res = re.search(r'.*(\d)',text,re.I)
# res = re.search(r'.*(\D).*',text,re.I)
# res = re.search(r'.*(\D)',text,re.I)
res = re.search(r'(\D).*',text,re.I|re.M)
# 上边被注释掉的3句，运行结果与此句相同
# <re.Match object; span=(0, 88), match='This is a text written by a student named MY from>
print(res)

res = re.search(r'(\w)',text,re.I|re.M)
# <re.Match object; span=(0, 1), match='T'>
# \w 同 [a-zA-Z0-9]
print(res)
res = re.search(r'(\W)',text,re.I|re.M)
# <re.Match object; span=(4, 5), match=' '>
# \W 同 [^a-zA-Z0-9]
print(res)
res = re.search(r'(\W).*',text,re.I|re.M)
# <re.Match object; span=(4, 76), match=' is a text written by MY ,from SheHui University >
print(res)
res = re.search(r'(\w)(.*)',text,re.I|re.M)
# <re.Match object; span=(0, 76), match='This is a text written by MY ,from SheHui Univers>
print(res)

'''
re.search(pattern, string, flags=0)
实例运行结果
'''
# -*- coding:utf-8 -*-
# re 正则表达式
# patter 正则表达式
# 用于替换的字符串
# string 要被替换的母字符串
# count 替换次数,默认为0表示无穷多次
# flags 标志位：是否区分大小写、是否多行匹配
# re.sub(pattern, repl, string, count=0, flags=0)
import re
# 单纯替换
text = '1+1=2'
res = re.sub(r'=',r'>',text,0,re.I)
print(text)
print(res)
print('------------0------------')
# 去除注释（无用信息、这在爬虫中往往用于数据清理）
text = '1+1=2 # 这是客观真理 \n' \
       ' 1+1>2 # 这是团结的力量 \n' \
       ' 1+1<2 # 这是内斗结果 \n'
res = re.sub(r'#.*$',r'',text,0,re.M)
print(text)
print('------------1----------')
print(res)
print('------------2----------')
res = re.sub(r'#.*$',r'',text,0,re.M)
print(res)
print('------------3----------')
res = re.sub(r'#.*$',r'',text,0,re.M|re.S)
print(res)
print('----------4------------')
res = re.sub(r'#.*$',r'',text,1,re.M)
print(res)
print('----------5------------')
res = re.sub(r'#.*$',r'',text,2,re.M) # 多行模式，去掉注释（替换）次数为 2
print(res)
print('----------6------------')
res = re.sub(r'#.*$',r'',text,3,re.M)
print(res)
print('----------7------------')
res = re.sub(r'#.*$',r'',text,2)# 不出标志说明是多行模式的话，$ 仅仅匹配末尾
print(res)
print('----------8------------')
res = re.sub(r'#.*$',r'',text,2,re.X)
print(res)
# 详细模式的多行将忽略空白字符和注释，故替换失败
# re.find（）查找默认对多行模式生效
print('----------9------------')
res = re.findall('#',text)
print(res)

'''
re.sub(pattern, repl, string, count=0, flags=0)
实例运行结果（第一部分）
实例运行结果（第二部分
'''
# -*- coding:utf-8 -*-
# re.subn(pattern, repl, string, count=0, flags=0)
import re
text = '1+1=2 # 这是客观真理 \n' \
       ' 1+1>2 # 这是团结的力量 \n' \
       ' 1+1<2 # 这是内斗结果 \n'
res = re.subn(r'#.*$',r'',text,0,re.M)
print(res)
# subn 与 sub 这两个函数用法完全一样，只是前者返回元组，后者返回字符串

'''
re.subn(pattern, repl, string, count=0, flags=0)
实例运行结果，自行对比上一个
'''
# -*- coding:utf-8 -*-
# re 正则表达式
# patter 正则表达式(定义字符串如何构成）
# flags 标志位：是否区分大小写、是否多行匹配
# re.compile(pattern[, flags])
import re
words = 'wooves Tools food too cool hello zoo \n goods'
ret = re.compile(r'\w*oo\w*') # 编译生成查找含有oo字母元素的单词的正则表达模式对象 obj对象可以直接调用re的方法
print(re.findall(ret,words)) # re.findall() 默认多行查找
print((ret.findall(words))) # 这是第二种有效的等价写法
# 正则模式的对象obj可以直接调用re的任何方法

'''
re.compile(pattern[, flags])
实例运行结果
'''
import re
# re.escape(string)
# string 为需要转义的字符串（常作为正则表达字串）
str = 'www.12306.cn \n' \
      'www.baidu.com '
pat = '\w+w..*'
ret = re.escape(pat)
print( pat)
print( ret)
# findall(pattern, string, flags=0)
print( re.findall(pat,str))
print( re.findall(ret,str))
print( re.findall(r'\w+w..*',str))
print( re.findall(r'(\w+)(w.)(.*)',str))
# 输出依次为
# \w+w..*
# \\w\+w\.\.\*
# ['www.12306.cn ', 'www.baidu.com ']
# []
# ['www.12306.cn ', 'www.baidu.com ']
# [('ww', 'w.', '12306.cn '), ('ww', 'w.', 'baidu.com ')]
# escape “逃离”->“偏离原有意图”
# 不再是 raw string 原生字符串、可以可以表示转义
# 而是 硬生生的字符本身、别无组合之后的其他意思

'''
re.escape(string)
实例运行结果
'''
import re

res = re.findall(r"\d", "图书馆2019年11月的阅读次数为 99万")  # 返回的是不可修改的元组
print(res) # ['2', '0', '1', '9', '1', '1', '9', '9']
res = re.findall(r"(\d+)", "图书馆2019年11月的阅读次数为 99万，点赞数：3200")
print(res)  # ['2019', '11', '99', '3200']
res = re.findall(r"(\D+)", "图书馆2019年11月的阅读次数为 99万，点赞数：3200")
print(res)  # ['2019', '11', '99', '3200']
for i in res:
    print(i)

print('--------分割线---------')
# words = ['wooves','Tools','food','too','cool','hello','zoo']
words = 'wooves Tools food too cool hello zoo \n goods'
print("1 ",re.findall(r'Oo',words))
print('2 ',re.findall(r'Oo',words,re.I))
print('3 ',re.findall(r'(\w+)(Oo)(\w*)',words,re.I))
    # 方式3 正则表达式全部被括号分割包围时，结果为元组内部嵌套了列表
    # 方式4 将按照元祖形式输出符合匹配条件的“单词”（即含有元素“oo”、不区分大小写）
print('4 ',re.findall(r'\w+Oo\w*',words,re.I))
print('5 ',re.findall(r'\w+(Oo\w*)',words,re.I))
    # 当正则表达式只是部分还有括号时，仅输出 括号部分对应的元祖（字符串）
print('6 ',re.findall(r'(\wOo)w*',words,re.I))
print('7 ',re.findall(r'(\wOo).*',words,re.I))
print('8 ',re.findall(r'(\wOo)(.*)',words,re.I))
print('9 ',re.findall(r'\wOo.*',words,re.I))
print('10 ',re.findall(r'\w+oo\w.*',words))
print('11 ',re.findall(r'\w+oo\w.*',words,re.S))
    # re.S 模式下 '.'可以匹配任意字符，包括默认不允许的回车‘\n’换行符

'''
findall(pattern, string, flags=0)
实例运行结果
'''
ret=re.findall('www.(baidu|oldboy).com','www.oldboy.com')
print(ret) # ['oldboy']
ret=re.findall('www.(?:baidu|oldboy).com','www.oldboy.com')
print(ret) # ['www.oldboy.com']
# findall会优先把匹配结果组里内容返回,这也正是上边只输出部分括号对应的正则匹配结果的原因
# 如果想要完整的正则匹配结果,使用 ‘?:’取消优先级权限即可

#强化理解之优先级问题
# re 正则表达式
# patter 正则表达式(定义字符串如何构成）
# string 待查找的母字符串
# flags 标志位：是否区分大小写、是否多行匹配
# re.finditer(pattern, string, flags=0)
import re
words = 'wooves Tools food too cool hello zoo \n goods'
ret = re.compile(r'(\w*)(oo)(\w*)') # 编译生成查找含有oo字母元素的单词的正则表达模式对象
res = re.finditer(ret,words)
for i in res:
    print(i)
    print(i.groups())# 所有分组；正则表达模式有了括号才有分组，否则为空
    print(i.span())# 生产的区间始终是“左闭右开”格式
# 需要注意的是，re.finditer()与re.find()一样，只输出有括号的部分
# 但区别是 前者生成列表，后者生成元组

'''
re.finditer(pattern, string, flags=0)
实例运行结果
'''
# -*- coding:utf-8 -*-
# re 正则表达式
# patter 正则表达式（用于替换的字符串）
# string 作为分隔素材的母字符串
# maxsplit 用于指定最大分割次数，不指定则默认为0表示无穷大、将全部分割
# flags 标志位：是否区分大小写、是否多行匹配
# re.split(pattern, string[, maxsplit=0, flags=0])
# 返回列表

import re
words = 'wooves Tools food too cool hello zoo \n goods'
res = re.split(r'\W',words)
print(res)
res = re.split(r'\s',words)
print(res)
res = re.split(r'\s+',words) # 这才是正确去除所有空白符 [\t\n\r\f\v] 因为 *与+ 表示贪心模式(?要看情况）
print(res)
res[1]='123' # 成功修改，故返回的是列表而不是元组
print(res)

text = '?a_b!2@'
res = re.split(r'\w+',text) # 由该句可知：\w除了匹配字母和数字，还匹配下划线（标识符命名规则……）
print(res)

print(re.split('a','1A1a2A3',re.I)) # ['1A1', '2A3']
print(re.split('a','1A1a2A3',0,re.I))# ['1', '1', '2', '3']
# 请注意使用格式这个大坑，否则将会导致re.I无法忽略字母的大小写

'''
re.split(pattern, string[, maxsplit=0, flags=0])
实例运行结果

\w      匹配字母数字及下划线，即：\w = [a-zA-Z0-9] + '_'
\W      匹配f非字母数字下划线，即: \W = [^a-zA-Z0-9] + '_' 
\s      匹配任意空白字符，即: \s = [\t\n\r\f\v]
\S      匹配任意非空字符，即: \S = [^\t\n\r\f\v]
\d      匹配任意十进制数数字，即： \d = [0-9]
\D      匹配任意非数字字符，即： \D = [^0-9]
\A      只在字符串首部开始匹配
\b		匹配位于开始或结尾的空字符串
\B		匹配不位于开始或结尾的空字符串
\Z      匹配字符串结束，如果存在换行，只匹配换行前的结束字符串
\z      匹配字符串结束
\G      匹配最后匹配完成的位置
\n      匹配一个换行符
\t      匹配一个制表符
^       匹配字符串的开头
$       匹配字符串的末尾
.       匹配任意字符，除了换行符，re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
[....]  用来表示一组字符，单独列出：[amk]匹配a,m或k
[^...]  不在[]中的字符：[^abc]匹配除了a,b,c之外的字符
*       匹配0个或多个的表达式
+       匹配1个或者多个的表达式
?       匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
{n}     精确匹配n前面的表示
{m,m}   匹配n到m次由前面的正则表达式定义片段，贪婪模式
a|b     匹配a或者b 
#()      匹配括号内的表达式，也表示一个组

re模式
	前面的*,+,?等都是贪婪匹配，也就是尽可能匹配：
“从整个字符串逐减1个末尾元素直至满足条件……”
	后面加?号使其变成惰性匹配：
“从字符串的第一个元素开始，逐增1个首部元素直至满足条件……”
1
2
3
4

贪婪模式与惰性匹配
'''
res = re.search(r"\d+", "图书馆2019年11月的阅读次数为 99万").group()  # 只匹配第一组数字
print(res) # 2019
res = re.search(r"\d+", "图书馆2019年11月的阅读次数为 99万")
# print(res) # <re.Match object; span=(3, 7), match='2019'>
print(res.groups())# () 由此可知group存在的条件是正则匹配使用了小括号
res = re.search(r"(\d+)", "图书馆2019年11月的阅读次数为 99万")
# print(res) # <re.Match object; span=(3, 7), match='2019'>
print(res.groups())# ('2019',)
res = re.search(r"(\d)(\d+)", "图书馆2019年11月的阅读次数为 99万")
# print(res) # <re.Match object; span=(3, 7), match='2019'>
print(res.groups())# ('2', '019')
res = re.search(r"(\d+)(\d)", "图书馆2019年11月的阅读次数为 99万")
# print(res) # <re.Match object; span=(3, 7), match='2019'>
print(res.groups())# ('201', '9')
res = re.search(r"(\d)(\d+)(\d)(\D)", "图书馆2019年11月的阅读次数为 99万")
# print(res) # <re.Match object; span=(3, 8), match='2019年'>
print(res.groups())# ('2', '01', '9', '年')
res = re.search(r"(\d+)(.*)", "图书馆2019年11月的阅读次数为 99万，点赞数：3200")
print(res)  # <re.Match object; span=(3, 30), match='2019年11月的阅读次数为 99万，点赞数：3200'>
print(res.groups())  # ('2019', '年11月的阅读次数为 99万，点赞数：3200')
print(res.group(0))
print(res.group(1))
print(res.group(2))# 超出索引将会输出空列表，不报异常

'''
group(s)
实例运行结果
'''
import re

a = "123abc456"
res = re.search("([0-9]*)([a-z]*)([0-9]*)",a)  #123abc456,返回整体
print(res.groups())
for i in range(1+len(res.groups())):
    print(res.group(i))
# 由此可见，group(i)参数i并非像索引那般范围被限定在了[0,len)左闭右开区间
# 而是[0,len]双闭合，即能够取到参数len
# 另外，值得注意的是 group 与 groups不是拼写错误，而是规定……
# 注意融会贯通，当只需要各个列表元素时，使用以下的写法
print("----------------我是分割线----------------")
for i in res.groups():
    print(i)

#强化对res.group()的理解
'''
特别补充说明：
	一般情况下，group()和groups()方法 仅与re.match()或re.search() 共同使用，不涉及其他 re的操作。
	虽然re.findall()与re.finditer()在它们的正则表达式存在圆括号时，也可以使用，但由于返回的是列表数据类型，直接调用会更加方便、高效。
（任意长）词组：
	ret = re.compile(r'\w+',re.I)
	匹配到任意一个字母或单词（不区分大小写）、中文（单个汉字或连续的多个汉字）、或连续的阿拉伯数字，也可为此三者直接相连的组合体
	及一反三：	
	r'\w+abc\w*'表示含有字母abc（必须完全匹配abc）的单词/字符串
（任意长）数字：
	ret = re.compile(r'\d+')
	匹配到任意数字（串）
（任意长）空白字符：
	r'\s+'或r'\s*' 可用于数据清洗
	举一反三：
	re.split(r'\s+',text,0,re.S|re.X)文本按照空白字符全部分割
	re.sub(r'\s+',r'',text,0,re.S|re.X))文本所有空白字符一律删除
（多行）注释去除
	re.sub(r'#.*$',r'',text,0,re.M)
（多行）数据删除
	re.sub(r'.*?<p>',r'',text),re.S|re.X)
	<p>标签之前全部删除 可等效改为r'.*<p>'或r'.+<p>'或r'.+?<p>'
	举一反三：
	r'<p>.*'或r'<p>.+' 表示匹配<p>标签之后全部数据
	说明：<p>标签本身也在数据范围之内（贪婪模式）

'''


def fizzBuzz(n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]

n = input('input n:')
res = fizzBuzz(eval(n))  # str(n)将报错
print(res)