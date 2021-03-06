# re模块 正则表达式,对字符串进行模糊匹配
import re

# 元字符：. ^ $ * + ? {} [] | () \

# . 代表任意的一个符号，除了\n

# ^ 代表必须是从字符串的开头进行匹配

# $ 代表必须是从字符串的结尾进行匹配

# * 代表按*左边的字符进行匹配，包含0-无穷次 默认贪婪匹配，按最多的进行匹配

# + 代表按+左边的字符进行匹配，包含1-无穷次 默认贪婪匹配，按最多的进行匹配

# ? 代表按?左边的字符进行匹配，包含0-1次 默认贪婪匹配，按最多的进行匹配

# {} 定义匹配的范围 默认贪婪匹配，按最多的进行匹配
# {0, }  表示0到穷次 相当于*
# {1, }  表示1到无穷次，相当于+
# {0,1}  表示0到1次，相当于?

# 将贪婪匹配改为惰性匹配，只需要在上面几个元字符后加?

# [] 字符集 字符集中的字符都是或的作用，在字符集有功能的符号是 - ^ \
# - 代表左边的字符到右边的字符
# [a-z] 代表a到z
# [A-Z] 代表A到Z
# [0-9] 代表0到9
# ^ 代表非
# [^a-z] 代表非a-z的所有字符

# \ 代表转义符,后面跟元字符则去除特殊功能，后面跟某些字符实现特殊功能
# \d 匹配任何十进制数；相当于[0-9]
# \D 匹配任何非数字字符；相当于[^0-9]
# \s 匹配任何空白字符; 相当于[\t\n\r\f\v]
# \S 匹配任何非空白字符; 相当于[^\t\n\r\f\v]
# \w 匹配任何字母数字字符与下划线；相当于[a-zA-Z0-9_]
# \W 匹配任何非字母数字字符与下划线；相当于[^a-zA-Z0-9_]
# \b 匹配任何一个特殊字符边界；如空格 & # 等
# 因为的python中，\b代表转义字符退格，当引入re模块想使用\b来匹配任何一个特殊字符边界时，应当使用\\b

# 匹配句子中单词的I(非单词中的I)
print(re.findall('I\\b', 'Hello, I am LIST'))  # 代表匹配'I '
# 或者
print(re.findall(r'I\b', 'Hello, I am LIST'))  # r代表使用原生字符串，字符串中的内容不作任何转义

# 求数学表达式最里层的括号中的字符
print(re.findall('\([^()]*\)', '12+(34*6+2-5*(2-1))'))   # 以(开对，以)结尾，中间不包含()的所有字符

# | 代表匹配左边的字符或右边的字符

# () 分组，将()中的字符作为一个整体
# (?P<分组名>正则) 命名分组，将取到的结果放到相应的分组名下
# 取出人名及年龄并放到命名的分组name和age中
mygroup = re.search('(?P<name>[a-z]+)(?P<age>\d+)', 'alex36wusir34xialv33')
print(mygroup.group('name'))
print(mygroup.group('age'))
