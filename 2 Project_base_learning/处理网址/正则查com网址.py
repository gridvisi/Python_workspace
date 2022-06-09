
'''
Python 使用正则表达式匹配URL网址
使用正则表达式匹配以 .com 或 .cn 为域名后缀的URL地址
'''


import re
str = "http://www.baidu.com/"
input_list = [
    "http://www.google.en/?x=jsdfkj",
    "http://www.google.de/?x=jsdfkj",
    "http://www.google.com/?x=jsdfkj",
    "http://www.google.org/?x=jsdfkj",
    "http://www.google.gov/?x=jsdfkj",
]
#regular = re.compile(r'[a-zA-Z]+://[^\s]*[.com|.cn]')
regular = re.compile(r'[a-zA-Z]+://[^\s]*[.com]')
print([f"{re.findall(regular, str)}" for str in input_list])
#['http://www.baidu.com']