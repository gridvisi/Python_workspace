
'''

Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。

语法：

re.sub(pattern, repl, string, count=0, flags=0)
参数：

pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

'''

import re
"""
-1234, A193, B123, C124
You must change it to the following:
A1234,- B193, B123, B124
"""
def normalize_orders(matchobj):
    print(matchobj)
    if matchobj.group(1) == '-':
        return "A"
    else:
        return "B"
re.sub('([-|A-Z])', normalize_orders, '-1234, A193, B123, C124')

import re


# 将匹配的数字乘以 2
def double(matched):
    print('matched: ', matched)
    print("matched.group('value'): ", matched.group('value'))
    value = int(matched.group('value'))
    return str(value * 2)

string = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, string))