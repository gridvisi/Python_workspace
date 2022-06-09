
import re
text = "阅读量 9999, 点赞量 7788"
ret_sub = re.sub(r'\d+', '8800', text)
print(ret_sub)

str = 'abcaaa'
print(re.sub(r'(.)\1+','x',str))

pattern = 'aaa'
print('result =', re.match(pattern, str))

pattern = 'ab'
result = re.match(pattern, str)
print(result.group())

inputStr = "hello crifan, nihao crifan"
replacedStr = re.sub(r"hello (\w+), nihao \1", "\g<1>", inputStr)
print("replacedStr=",replacedStr) #crifan

# 首先清楚手机号的规则
# 1.都是数字 2.长度为11 3.第一位是1 4.第二位是35678中的一位


'''
正则表达式

    1️⃣单字符匹配规则

字符    功能
.       匹配任意1个字符(除了\n)
[]      匹配[]中列举的字符
\d      匹配数字,也就是0-9
\D      匹配非数字,也就是匹配不是数字的字符
\s      匹配空白符,也就是 空格\tab
\S      匹配非空白符,\s取反
\w      陪陪单词字符, a-z, A-Z, 0-9, _
\W      匹配非单词字符, \w取反
   2️⃣表示数量的规则

字符    功能
*       匹配前一个字符出现0次多次或者无限次,可有可无,可多可少
+       匹配前一个字符出现1次多次或则无限次,直到出现一次
?       匹配前一个字符出现1次或者0次,要么有1次,要么没有
{m}     匹配前一个字符出现m次
{m,}    匹配前一个字符至少出现m次
{m,n}   匹配前一个字符出现m到n次
    例一: 验证手机号码是否符合规则(不考虑边界问题)
————————————————
版权声明：本文为CSDN博主「itw_wang」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_40136018/article/details/81183504
'''
pattern = "1[35678]\d{9}"
phoneStr = "18230092223"

result = re.match(pattern, phoneStr)
result.group()

'''
5. 表示边界

字符    功能
^       匹配字符串开头
$       匹配字符串结尾
\b      匹配一个单词的边界
\B      匹配非单词边界
例三: 边界(制定规则来匹配str="ho ve r")
'''

import re

# 定义规则匹配str="ho ve r"
# 1. 以字母开始
# 2. 中间有空字符
# 3. ve两边分别限定匹配单词边界

pattern = r"^\w+\s\bve\b\sr"
str = "ho ve r"
result = re.match(pattern, str)
print(result)

s = "I have a dog , I have a cat,I have a mouse,"

print(re.findall(r'I have a (?:dog|cat)', s))
print(re.findall( r'I have a (?:dog|cat|mouse)', s))
#['I have a dog', 'I have a cat']                #正如我们所要的
#下面再看看不用无捕获组会是什么后果：
print(re.findall( r'I have a (dog|cat)', s))
print(re.findall( r'I have a (dog|cat|mouse)', s))

s="123??<><>\n456 \n789"
print(re.findall(r'.+',s))

s="123??<><>\n456 \n789"
s="123333 kkk\n456 \n789"
print(re.sub(r'(.)\1+',lambda n:n.group().swapcase(),s))

s = 'apple'
it = iter(s)
x = s.find('p')
y = s.find('f')
p = s.index('p')
z1 = s.find(next(it))
z2 = s.find(next(it))
print(x,y,z1,z2,p)