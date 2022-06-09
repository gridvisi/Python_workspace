import re

string = '(a(b))e(ac)a(d)'
p1 = re.compile(r'[(](.*?)[)]', re.S)  # 最小匹配
p2 = re.compile(r'[(](.*)[)]', re.S)  # 贪婪匹配
print(re.findall(p1, string))
print(re.findall(p2, string))
'''
解释一下：

1.正则匹配串前加了r就是为了使得里面的特殊符号不用写反斜杠了。

2.[ ]具有去特殊符号的作用,也就是说[(]里的(只是平凡的括号

3.正则匹配串里的()是为了提取整个正则串中符合括号里的正则的内容

4. .是为了表示除了换行符的任一字符。*克林闭包，出现0次或无限次。

5. 加了？是最小匹配，不加是贪婪匹配。

6. re.S是为了让.表示除了换行符的任一字符。

'''

s = "我是一个人(中国人)aaa[真的]bbbb{确定}"

s = "hello example (words(more words) here) something"
a = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", s)

print(a)

import string
#String_
st1 = "123(234)345"

#String_
#st2 = st1.substring(st1.indexOf("(" ) +1 ,st1.indexOf(")"))
