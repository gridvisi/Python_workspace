
import re
#在python中，使用正则表达式，需要先导入re模块。
#使用
print(re.__all__)

#查看模块的全部属性和函数
print(re.__all__)

# 打印结果
'''
['match', 'fullmatch', 'search', 'sub', 
    'subn', 'split', 'findall', 'finditer', 
    'compile', 'purge', 'template', 'escape', 
    'error', 'Pattern', 'Match',
     'A', 'I', 'L', 'M', 'S', 'X', 'U', 'ASCII', 
    'IGNORECASE', 'LOCALE', 'MULTILINE', 'DOTALL', 
    'VERBOSE', 'UNICODE']
'''

#常用方法：
#1、re.match(patter, string, flags=0)
#必须从字符串起始位开始匹配，匹配失败返回None，成功返回_sre.SRE_Match对象，该对象包含两个方法：
#（1）  span() ：该方法返回匹配位起始到终止位的索引组成的元组。（符合左闭右开原则）
#（2）  group() ：该方法返回所匹配的子串。

import re
a = re.match('www', 'www.baidu.com')
print(a.span())  # (0, 3)
print(a.group())  # 'www'

#2、re.search(patter, string, flags=0)
#扫描整个字符串，匹配失败返回None，成功也返回第一次匹配子串的_sre.SRE_Match对象，该对象包含两个方法：
#（1）  span() ：该方法返回匹配位从起始到终止位的索引组成的元组。（符合左闭右开原则）
#（2）  group() ：该方法返回所匹配的子串。

import re
a = re.search('www', 'bwwwn.www')
print(a.span())  # (1, 4)
print(a.group())  # 'www'

#match和search区别：
#match必须从字符串开始出就匹配；search则可以搜索整个字符串。。。


#3、re.findall(patter, string, flags=0)
#扫描整个字符串，返回字符串中所有匹配到子串组成的列表：

import re

a = re.findall('www', 'bwwwn.www')
print(a)  # ['www', 'www']
#上边代码意思是从' bwwwn.www '搜索www，返回所有匹配到的字串组成的列表。

#4、re.finditer(patter, string, flags=0)
#扫描整个字符串，返回字符串中所有匹配到子串组成的迭代器，迭代器元素是_sre.SRE_Match对象，

#findall和finditer区别在于：
#findall返回一个列表，finditer返回的是迭代器。


# 5、re.fullmatch(patter, string, flags=0)
#必须整个字符串全部匹配字串才行，匹配失败返回None，成功也返回_sre.SRE_Match对象，

#该对象包含两个方法：（1）span() ：该方法返回匹配位从起始到终止位的索引组成的元组。（符合左闭右开原则）
# （2）group() ：该方法返回所匹配的子串。

import re
a = re.fullmatch('www', 'www')
print(a.span())  # (0,3)
print(a.group())  # 'www'

#6、re.sub(patter, repl, string, count=0, flags=0)
#匹配成功替换该函数用于将string字符串中所有匹配的patter（子串）的内容替换成repl，repl可以是字符串，也可以是函数，count参数控制最多替换多少次；如果count为0，则全部替换。

import re

a = re.sub('xxx', '鸡西', '鸡小西就读于xxx小学', count=0)
print(a)  # '鸡小西就读于鸡西小学'
import re

a = re.sub('-', '/', '2019-02-22', count=0)
print(a)  # '2019/02/22'

#要替换的是函数情况：经常会用到

s = 'javac#'
def fn(param):
    print(param)  # <re.Match object; span=(4, 6), match='c#'>
    result = param.group()
    return ',' + result

r = re.sub('c#', fn, s)
print(r)  # java,c#

#上边代码，替换的是一个函数，匹配到的字符，将会传给param参数，函数参数param它是一个_sre.SRE_Match对象，所以使用group方法，可以获取到匹配到的字符，然后动态操作这个字符即可。。。
# 在看一个小demo：需求是 把字符串中大于等于 5 的数字替换成1，小于 5 的替换成 0

s = 'a82b3b6c2d5'

def fn(param):
    res = param.group()
    if int(res) >= 5:
        return ',1'
    else:
        return ',0'


r = re.sub('\d', fn, s)
print(r)  # a,1,0b,0b,1c,0d,1

#7、string.replace
#也是将字符串替换成xxx
s = 'javac#'
r = s.replace('c#', ',python')
print(r)  # java,python
#上边代码，由于字符串不可变特性，所以replace方法会生成一个新字符串。
#方法第三个参数flags,flags是匹配模式意思，下边代码，加上re.I，忽略大小写，大写字母A也会匹配到

s = 'aAbB'
r = re.findall('a', s, re.I)
print(r)  # ['a', 'A']
#多个模式之间用 | 隔开如：re.I | re.S re.I 忽略大小写，大小写字母都可匹配到
#re.S 让.忽略换行符 \n ，也就是匹配所有
#常用的概括字符集：
#\d - ---------  表示0 - 9阿拉伯数字 相当于[0 - 9]

import re

s = 'abc123'
print(re.findall('\d', s))  # ['1', '2', '3']
#\D - --------- 表示匹配非数，除数字之外的所有相当于[ ^ 0 - 9]
s = 'a1b2c3, \r $%&*.'

print(re.findall('\D', s))  # ['a', 'b', 'c', ',', ' ', '\r', ' ', '$', '%', '&', '*', '.']
#\w - ------ 表示匹配数字、字母、下划线  \w相当于[a - zA - Z0 - 9_]

s = 'a1b2c3, \r $%&*.'
print(re.findall('\w', s))  # ['a', '1', 'b', '2', 'c', '3']
#\W - --------- 表示匹配非数字、字母、下划线 （与\w相反）

s = 'a1b2c3, \r $%&*.'
print(re.findall('\W', s))  # [',', ' ', '\r', ' ', '$', '%', '&', '*', '.']
#\s - --------- 表示匹配空白字符如：制表符、回车、换行、空格

s = 'a1b2c3, \r \n$%&*.'
print(re.findall('\s', s))  # [' ', '\r', ' ', '\n']
#\S - --------- 表示匹配非空白字符
s = 'a1\r \n$*.'

print(re.findall('\S', s))  # ['a', '1', '$', '*', '.']
#.---------- 表示匹配除换行符 \n 外其他所有
s = 'aAbB'
r = re.findall('.', s)
print(r)  # ['a', 'A', 'b', 'B']

#数量词：{},意思是要匹配的数量

s = '333abc12'
r = re.findall('3{3}', s)  # 前边3是匹配条件，后边3是匹配规则，必须要3个3才能匹配到，{}要匹配的数量
print(r)  # ['333']

# 需求：把字符串中 abcd 和bcd匹配出来
s = 'abcd23i,o3bcd-03desdc'
print(re.findall('[a-d]{3,4}', s))  # ['abcd', 'bcd']
#上边代码，[a - d],{3, 4},意思是在字符串s中匹配a到d个字母匹配到一个字串的数量是3到4个。
# （2）需求：把字符串中的java和JavaScript匹配出来

s = 'JavaScriptabc2332java1ABC'
r = re.findall('[a-zA-Z]{4,10}', s)
print(r)  # ['JavaScript', 'java']
#上边代码，要求匹配一个单词的长度是4 - 10这一区间内。

'''
我们思考个问题，上边代码，为什么会把JavaScript全部匹配出来，按道理来说，当匹配到长度为4的单词的时候
（s前边的a），就已经符合条件了，为什么还会继续往后匹配呢？

原因在于：正则表达式的数量词分贪婪和非贪婪之分,
数量词的贪婪匹配和非贪婪匹配
默认情况下，python是一个贪婪匹配模式，也就是说尽可能的按照区间中最大值取匹配，
上边代码， 当匹配到s前边a的时候，python还会向后去匹配，直到不符合条件或者超出最大值范围，才会停止匹配。

非贪婪匹配：
'''
s = 'JavaScriptabc2332java1ABC'
r = re.findall('[a-zA-Z]{4,10}?', s)
print(r)  # ['Java', 'Scri', 'ptab', 'java']

#上边代码，在花括号最后加上一个问号，匹配模式是编程非贪婪匹配，也就是以区间中最小值为匹配的数量，
# 所以输出结果都是以4个单词为一组的单词。。。

#常用的数量词
#{}上边已经讲过
#*表示匹配星号前边的字符匹配0次或者无限次

s = 'pytho11python22pythonnnn333pythonnnn'
r = re.findall('python*', s)
print(r)  # ['pytho', 'python', 'pythonnnn', 'pythonnnn']

#+   表示匹配
#加号#前边的字符匹配1次或者无限次

s = 'pytho11python22pythonnnn333pythonnnn'
r = re.findall('python+', s)
print(r)  # ['python', 'pythonnnn', 'pythonnnn']

#?   表示匹配问号前边的字符匹配0次或者1次(如果是重复了，如果问号前边的n出现的次数大于1次，它会把重复的n去掉

s = 'pytho11python22pythonnnn333pythonnnn'
r = re.findall('python？', s)
print(r)  # ['pytho', 'python', 'python', 'python']

#注意普通字符后边的问号和花括号后边的问号作用是不一样的。。。

#边界匹配
# ^ 从字符串的开始位置 匹配
#$  从字符串的末尾开始匹配

# 需求  qq号要求4-8位数之间
s = '12345678'
r = re.findall('^[0-9]{4,8}$', s)  # 必须以4位数开始，以8位数结束，4位数-8位数区间的都可以匹配到
print(r)  # ['12345678']
if r:
    print('正确')  # 正确
else:
    print('错误')

#group组()在括号里边都算是一组，在租后边加上数量词，相当于，把组重复多少次

s = '333ab333c12333'
r = re.findall('(333){1}', s)  # 意思是：前边333重复一次还是333，所以能匹配三个333
print(r)  # ['333', '333', '333']

#()和[]区别,()里边元素是且关系，里边字符必须都出现才行，如：（abc） abc必须都存在才行
#[]里边的元素关系是或关系，如：[abc]或a,或b,或c

#看几个小demo需求：输出字符串中 < span > 和 < / span > 中间的内容，在爬虫爬取数据中非常常用。。。

s = '<span>8月19日，甘肃考察调研</span>'
r = re.findall('<span>(.*)</span>', s)
print(r)  # ['8月19日，甘肃考察调研']
s = '<span>甘肃考察调研</span><span>甘肃考察调研</span>'
r = re.findall('<span>(.*)</span><span>(.*)</span>', s)
print(r)  # [('甘肃考察调研', '甘肃考察调研')]

#如果匹配多个，在列表中会以元祖的形式输出。。。

#一、校验数字的表达式
#数字： ^ [0 - 9] *$
#n位的数字： ^ \d
#{n}$

#至少n位的数字： ^ \d
#{n, }$

#m - n位的数字： ^ \d
#{m, n}$

#零和非零开头的数字： ^ (0 | [1 - 9][0 - 9] *)$
#非零开头的最多带两位小数的数字： ^ ([1 - 9][0 - 9] *) + (.[0-9]{1, 2})?$

#带1 - 2位小数的正数或负数： ^ (\-)?\d + (\.\d{1, 2})?$
#正数、负数、和小数： ^ (\- | \+)?\d + (\.\d+)?$
#有两位小数的正实数： ^ [0 - 9] + (.[0-9]{2})?$

#有1~3位小数的正实数： ^ [0 - 9] + (.[0-9]{1, 3})?$

#非零的正整数： ^ [1 - 9]\d *$ 或 ^ ([1 - 9][0 - 9] *)
#{1, 3}$ 或 ^\+?[1 - 9][0 - 9] *$

#非零的负整数： ^ \-[1 - 9][]
#0 - 9″ * $ 或 ^ -[1 - 9]\d *$

#非负整数： ^ \d +$ 或 ^ [1 - 9]\d * | 0$
#非正整数： ^ -[1 - 9]\d * | 0$ 或 ^ ((-\d+) | (0 +))$

#非负浮点数： ^ \d + (\.\d+)?$ 或 ^ [1 - 9]\d *\.\d * | 0\.\d * [1 - 9]\d * | 0?\.0 + | 0$
#非正浮点数： ^ ((-\d+(\.\d+)?) | (0 + (\.0+)?))$ 或 ^ (-([1 - 9]\d * \.\d * | 0\.\d *[1-9]\d *)) | 0?\.0 + | 0$

#正浮点数： ^ [1 - 9]\d *\.\d * | 0\.\d * [1 - 9]\d *$ 或 ^ (
#            ([0 - 9] +\.[0-9] *[1-9][0-9] *) | ([0 - 9] * [1 - 9][0 - 9] *\.[0-9]+) | ([0 - 9] * [1 - 9][0 - 9] *))$

#负浮点数： ^ -([1 - 9]\d * \.\d * | 0\.\d *[1-9]\d *)$ 或 ^ (
#    -(([0 - 9] +\.[0-9] *[1-9][0-9] *) | ([0 - 9] * [1 - 9][0 - 9] *\.[0-9]+) | ([0 - 9] * [1 - 9][0 - 9] *)))$

#浮点数： ^ (-?\d+)(\.\d +)?$ 或 ^ -?([1 - 9]\d * \.\d * | 0\.\d *[1-9]\d * | 0?\.0+ | 0)$


#二、校验字符的表达式
#汉字： ^ [\u4e00 -\u9fa5]{0, }$

#英文和数字： ^ [A - Za - z0 - 9] +$ 或 ^ [A - Za - z0 - 9]
#{4, 40}$

#长度为3 - 20
#的所有字符： ^.{3, 20}$

#由26个英文字母组成的字符串： ^ [A - Za - z] +$
#由26个大写英文字母组成的字符串： ^ [A - Z] +$
#由26个小写英文字母组成的字符串： ^ [a - z] +$
#由数字和26个英文字母组成的字符串： ^ [A - Za - z0 - 9] +$

#由数字、26个英文字母或者下划线组成的字符串： ^ \w +$ 或 ^\w
#{3, 20}$
#中文、英文、数字包括下划线： ^ [\u4E00 -\u9FA5A - Za - z0 - 9_]+$
#中文、英文、数字但不包括下划线等符号： ^ [\u4E00 -\u9FA5A - Za - z0 - 9]+$ 或 ^ [\u4E00 -\u9FA5A - Za - z0 - 9]{2, 20}$

#可以输入含有 ^ % & ’, ;=?$\”等字符：[ ^ % & ',;=?$\x22]+

#禁止输入含有~的字符：[ ^ ~\x22]+


#三、特殊需求表达式
#Email地址： ^ \w + ([-+.]\w+) * @\w + ([-.]\w+) *\.\w + ([-.]\w+) *$
#域名：[a - zA - Z0 - 9][-a - zA - Z0 - 9]
#{0, 62}( /.[a - zA - Z0 - 9][-a - zA - Z0 - 9]
#{0, 62})+ /.?

#InternetURL：[a - zA - z] +: // [ ^\s]*或 ^ http: // ([\w-]+\.) + [\w -]+(/[\w-./ ? % &=] *)?$

#手机号码：
# ^ (13[0 - 9] | 14[5 | 7] | 15[0 | 1 | 2 | 3 | 5 | 6 | 7 | 8 | 9] | 18[0 | 1 | 2 | 3 | 5 | 6 | 7 | 8 | 9])\d{8}$

#电话号码(“XXX - XXXXXXX”、”XXXX - XXXXXXXX”、”XXX - XXXXXXX”、”XXX - XXXXXXXX”、”XXXXXXX”和”XXXXXXXX)：
# ^ ($$\d{3, 4}-) |\d{3.4} -)?\d{7, 8}$

#国内电话号码(0511 - 4405222、021 - 87888822)：
# \d{3} -\d{8} |\d{4} -\d{7}

#身份证号(15位、18位数字)：
# ^ \d{15} |\d{18}$

#短身份证号码(数字、字母x结尾)：
# ^ ([0 - 9]){7, 18}(x | X)?$ 或 ^\d{8, 18} | [0 - 9x]{8, 18} | [0 - 9X]{8, 18}?$

#帐号是否合法(字母开头，允许5 - 16字节，允许字母数字下划线)：
# ^ [a - zA - Z][a - zA - Z0 - 9_]{4, 15}$

#密码(以字母开头，长度在6~18之间，只能包含字母、数字和下划线)：
# ^ [a - zA - Z]\w{5, 17}$

#强密码(必须包含大小写字母和数字的组合，不能使用特殊字符，长度在8 - 10之间)：
# ^ (?=.* \d)(?=.*[a - z])(?=.*[A-Z]).{8, 10}$

#日期格式：
# ^ \d{4} -\d{1, 2} -\d{1, 2}

#一年的12个月(01～09和1～12)：
# ^ (0?[1-9] | 1[0-2])$

#一个月的31天(01～09和1～31)：
# ^ ((0?[1-9]) | ((1 | 2)[0 - 9]) | 30 | 31)$

#钱的输入格式：有四种钱的表示形式我们可以接受:”10000.00″ 和 “10, 000.00″, 和没有 “分” 的 “10000″ 和 “10, 000″：
# ^ [1 - 9][0 - 9] *$

#这表示任意一个不以0开头的数字，但是，这也意味着一个字符”0″不通过，所以我们采用下面的形式：
# ^ (0 | [1 - 9][0 - 9] *)$

#一个0或者一个不以0开头的数字.我们还可以允许开头有一个负号：
# ^ (0 | -?[1-9][0-9] *)$

#这表示一个0或者一个可能为负的开头不为0的数字.让用户以0开头好了.把负号的也去掉，因为钱总不能是负的吧.下面我们要加的是说明可能的小数部分：
# ^ [0 - 9] + (.[0-9]+)?$

#必须说明的是，小数点后面至少应该有1位数，所以”10.”是不通过的，但是 “10″ 和 “10.2″ 是通过的：
# ^ [0 - 9] + (.[0-9]{2})?$

#这样我们规定小数点后面必须有两位，如果你认为太苛刻了，可以这样：
# ^ [0 - 9] + (.[0-9]{1, 2})?$

#这样就允许用户只写一位小数。下面我们该考虑数字中的逗号了，我们可以这样：
# ^ [0 - 9]{1, 3}(, [0 - 9]{3})*(.[0-9]{1, 2})?$

#1到3个数字，后面跟着任意个逗号 + 3个数字，逗号成为可选，而不是必须：
# ^ ([0 - 9] + | [0 - 9]{1, 3}(, [0-9]{3}) *)(.[0-9]{1, 2})?$

#备注：这就是最终结果了，别忘了”+”可以用” * ”替代。如果你觉得空字符串也可以接受的话(奇怪，为什么?)
# 最后，别忘了在用函数时去掉去掉那个反斜杠，一般的错误都在这里
#xml文件：
# ^ ([a - zA - Z] + -?) + [a - zA - Z0 - 9] +\\.[x | X][m | M][l | L]$

#中文字符的正则表达式：[\u4e00 -\u9fa5]
#双字节字符：[ ^\x00 -\xff] (包括汉字在内，可以用来计算字符串的长度(一个双字节字符长度计2，ASCII字符计1))

#空白行的正则表达式：\n\s *\r(可以用来删除空白行)

#HTML标记的正则表达式： < (\S * ?)[ ^ >] * >.* ? < / \1 > | <.* ? / > (网上流传的版本太糟糕，上面这个也仅仅能部分，对于复杂的嵌套标记依旧无能为力)

#首尾空白字符的正则表达式： ^ \s * |\s *$或( ^\s *) | (\s * $)(可以用来删除行首行尾的空白字符(包括空格、制表符、换页符等等)，非常有用的表达式)

#QQ号,(QQ号从10000开始
# [1 - 9][0 - 9]#{4, }

#中国邮政编码：
# [1 - 9]\d{5}(?!\d) (中国邮政编码为6位数字)

#IP地址(提取IP地址时有用)
# \d +\.\d +\.\d +\.\d +

#IP地址：
#((?:(?:25[0-5] | 2[0-4]\\d |[01]?\\d?\\d)\\.){3}(?:25[0 - 5] | 2[0 - 4]\\d | [01]?\\d?\\d))