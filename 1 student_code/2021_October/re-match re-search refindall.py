# https://blog.csdn.net/szlcw1/article/details/49557399

import re
str = 'Hello World!'
print(re.match(r'Wor',str))
print(re.match(r'Hell',str))

print(re.findall(r'Wor',str))
print(re.search(r'or',str))

print(str.find('or'))

'''
如果你想以迭代方式返回匹配，可以使用 finditer() 方法来代替。
PS:re.search()和re.match()函数返回match对象包括分组时，group(0)返回完整匹配的字符串，
group(1)及以上分别返回各分组字符串。groups()函数返回各分组组成的元组对象。
'''