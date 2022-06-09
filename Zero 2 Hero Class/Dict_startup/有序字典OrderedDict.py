#Python中的字典对象可以以“键：值”的方式存取数据。OrderedDict是它的一个子类，实现了对字典对象中元素的排序。比如下面比较了两种方式的不同：

import collections

print('Regular dictionary:')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
for k, v in d.items():
    print(k, v)

print('\nOrderedDict:')
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
for k, v in d.items():
    print(k, v)

#输出结果如下：
#Regular dictionary:
#a
#A
#c
#C
#b
#B

#OrderedDict:
#a
#A
#b
#B
#c
#C

#可以看到，同样是保存了ABC三个元素，但是使用OrderedDict会根据放入元素的先后顺序进行排序。由于进行了排序，所以OrderedDict对象的字典对象，
# 如果其顺序不同那么Python也会把他们当做是两个不同的对象，比如下面的代码：
import collections
print('Regular dictionary:')
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = {}
d2['c'] = 'C'
d2['a'] = 'A'
d2['b'] = 'B'

print(d1 == d2)

print('\nOrderedDict:')
d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = collections.OrderedDict()
d2['c'] = 'C'
d2['a'] = 'A'
d2['b'] = 'B'

print(d1 == d2)

#其输出结果为：
#Regular dictionary:True

#OrderedDict:False


#1、问题：我们想创建一个字典，同时对字典做迭代或者序列化操作时，也可以该控
# 制其中元素的顺序。
#2、解决：要控制字典中的顺序，可以使用collections模块中的OrderedDict
# 类。当对字典做迭代时。它会严格照元素初始添加的顺序进行。

from collections import OrderedDict
d = OrderedDict()
d['foo']=1
d['bar']=2
d['spam']=3
d['grok']=4
for key in d:
    print(key,d[key])

#3、在进行JSON编码时精确控制各字段的顺序，那只要首先在OrderedDict中
# 构建数据就可以了

import json
json.dumps(d)
'{"foo": 1, "bar": 2, "spam": 3, "grok": 4}'

#https://blog.csdn.net/weixin_41797397/article/details/81012169