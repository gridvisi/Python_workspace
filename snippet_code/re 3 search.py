#3.search search(正则表达式, 字符串)
#--> 查找字符串中满足正则表达式的第一个字符串。返回值是匹配对象或者None


#作业规则：一个ip地址由4个数字组成，每个数字之间用.连接。每个数字的大小是0-255 例如：255.189.10.37 正确 256.189.89.9 错误
import re
re_str = r'((\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])'
result = re.fullmatch(re_str,'255.183.10.37')
print(result)

#能够在字符串中匹配“aab”，而不能匹配“aaab”和“aaaab”的正则表达式包括（ B C ）
'''
A. “a*?b”
B. “a{,2}b”
C. “aa??b”
D. “aaa??b
'''

res = re.fullmatch(r'aa?b','aab')
print(res,res.string)

result = re.search(r'(\d)[a-zA-Z]+', '-=+3ABC7uhsh2hdje+984nf')
print(result.group(0))
print(result.group(1))
print(result.string)
print('search:',result)

str1 = 'ahsb1sssa8-jjhd7nhs+90nsjhf3-4hhh7+8kjj-'
result = re.split(r'[-+]', str1)
print('split:',result)



str1 = 'hsj8jskfh98ssjj8hshh'
result = re.sub(r'\d+','*', str1)
print(result)

str1 = '白日依山尽'
result = re.sub(r'白|月|及时|山|智\赵', '*', str1)
print(result)
with open('./data', 'r', encoding='utf-8') as f:
    content = f.read()
    # "name": "搞笑精选汇"
    result = re.findall(r'"name":"(.+?)"', content)
    print(result)

#练习：使用search匹配出一个字符串中所有的数字字符串'abc34jshd8923jkshd9lkkk890k' --> 34，8923，9，890
re_str = r'\d+'
str1 = 'abc34jshd8923jkshd9lkkk890k'
result = re.search(re_str, str1)
while result:
    print(result)
    str1 = str1[result.end():]
    result = re.search(re_str, str1)
    #print(str1)
    #print(f'match')
#原文链接：https://blog.csdn.net/zhoulei124/article/details/88994357