
'''
python标准库之collections

一.模块 collections 中的一个类—— OrderedDict 。
(字典让你能够将信息关联起来，但它们不记录你添加键 — 值对的顺序。要创建字典并记录其
中的键 — 值对的添加顺序，可使用模块 collections 中的 OrderedDict 类。 OrderedDict 实例的行为
几乎与字典相同，区别只在于记录了键 — 值对的添加顺序。)

from collections import OrderedDict
#假设age_1 到age_5 都存在（不写了）
my_dict=OrderedDict()
my_dict[age_1]="10"
my_dict[age_2]="20"
my_dict[age_3]="30"
my_dict[age_4]="40"
my_dict[age_5]="50"
for k,v in my_dict.items():
    print("他们的顺序应该是:"+k+"对应"+v)

'''
# https://babynames.net/all/english 有很多分类，比如很酷的名字集合，独特的老名字集合等等。界面很漂亮。
age_1 ="Ada"
age_2 ="Bob"
age_3 ="Cathy"
age_4 ="david" #Daniela, daniel
age_5 ="eva" #emma

from collections import OrderedDict
my_dict=OrderedDict()
my_dict[age_1]="10"
my_dict[age_2]="20"
my_dict[age_3]="30"
my_dict[age_4]="40"
my_dict[age_5]="50"
for k,v in my_dict.items():
    print("他们的顺序应该是:"+k+"对应"+v)
i = 2
j = 3
p = {}
p = {str(i):1}
p[str(i)] += 1
p.update({str(j):1})
if '3' in p.keys():
    print(True)
print(p)

num = 2
res = '({}{})'.format(i, '**%d' % num if num > 1 else '')
print(res)

'''
字典（dictionary）是Python中一种常用的数据类型。不同于其他由数字索引的序列，字典是用"键"（key）来索引的。通常表示为dict(key: val, )，有以下特征：

键可以是任何不可变（immutable）数据类型，如数字，字符串和仅包含不可变数据类型的元组
每个键必须是唯一的
字典中每一项的顺序是任意的
1. KeyError异常
在Python中如果访问字典里不存在的键，会出现KeyError异常。有些时候，字典中每个键都存在默认值是很方便的，例如下面的例子：
'''
bag = ['apple', 'orange', 'cherry', 'apple',
        'apple', 'cherry', 'blueberry']
count = {}
#for fruit in bag:
#    count[fruit] += 1

'''
Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
KeyError: 'apple'
上例统计列表bag中单词出现次数，并记录在字典count中。单词没出现一次，count中对应的键值会增加一。但是在实习运行代码时，每当单词第一次被统计就会出现'KeyError'异常，这是因为它并不在字典count中，Python中dict对象并不存在默认值。

2. 使用判断语句检查
因此，在单词第一次被统计时，需要在count中给每个键设定一个默认值1，这可以用一个判断语句来实现：
'''

for fruit in bag:
    if fruit not in count:    #如果不存在，添加
        count[fruit] = 1
    else:
        count[fruit] += 1

#print(count)
#{'apple': 3, 'blueberry': 1, 'orange': 1, 'cherry': 2}

'''
3. 使用dict.setdefault()方法
dict.setdefault(key[,default])方法接受两个参数，第一个是键的名称，第二个参数是默认值。
在调用时如果键存在字典中，会返回它的值；如果不存在，则会自动把它添加进字典中并返回默认值，
default的默认值为None。此外，default的值还可以是列表，元组，集合和字典等。
'''

d = {'a': 1, 'b': 2}
d.setdefault('a')    #键存在并返回他的值

d.setdefault('c', 3)     #添加键-值

d.setdefault('d')    #只添加键，默认值为None
#{'a': 1, 'b': 2, 'c': 3, 'd': None}

#接下来用它来实现上一个例子：

count = {}
for fruit in bag:
    count.setdefault(fruit, 0)
    count[fruit] += 1

print(count)
#{'apple': 3, 'orange': 1, 'cherry': 2, 'blueberry': 1}
#或者更简洁一些：

for fruit in bag:
    count[fruit] = count.setdefault(fruit, 0) + 1

'''
4. 使用collections.defaultdict类
class collections.defaultdict([default_factory[, ]])
defaultdict是Python内建dict类的一个子类，第一个参数为default_factory属性提供初始值，默认为None。
它覆盖一个方法并添加一个可写实例变量。它的其他功能与dict相同，但会为一个不存在的键提供默认值，
从而避免KeyError异常。之前例子的实现如下：
'''

from collections import defaultdict
count = defaultdict(int)
for fruit in bag:
     count[fruit] += 1

print(count)
#defaultdict(<class 'int'>, {'apple': 3, 'orange': 1, 'cherry': 2, 'blueberry': 1})

'''
4.1. 类型名称作为初始化函数参数
首先它可以接受类型名称来作为初始化函数的参数，比如之前的例子中以int类名称作为参数。除了标准dict操作，
它还支持__missing__(key)方法，通过参考官方文档，它的机制如下：
如果default_factory为None，会抛出以key为参数的KeyError异常。
'''

d = defaultdict()    #default_factory为None
#print(d['eric'])
'''
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
KeyError: 'eric'
如果default_factory不为None， 此处原文为：
"It is called without arguments to provide a default value for the given key, " 
"this value is inserted in the dictionary for the key, and returned."。
大概翻译了下：它会在不接收任何参数的情况下被调用，来为给定的键提供默认值，这个值会被添加进字典并被返回。
'''

d = defaultdict(list)    #default_factory是列表名称
#d['eric']    #访问一个不存在的键
#[]            #添加并返回默认值（一个空列表）
print(d)
#defaultdict(<class 'list'>, {'eric': []})

'''
因为defaultdict是dict的一个子类，事实上访问一个不存在的键时，dict类中的__getitem__方法会
调用子类中__missing__()方法（但它不能直接被dict的实例调用），并且返回或抛出__missing__()
方法所返回的值和抛出的异常。因此，如果调用default_factory引发一个异常，
该异常传播不变（propagated unchanged）。

请注意除__getitem__()之外的任何操作都不会调用__missing __()。 这意味着像正常的字典一样，get()
将返回None作为默认值，而不是使用default_factory。

另外，还可以给字典中的键映射多个值，具体方法是把多个值储存在另一个容器里（如列表，元组，字典等）。
是否使用列表或集合的选择取决于预期用途：使用列表来保存每一项的插入顺序；如果要消除重复的项（不关心顺序），可以使用元组。
'''

from collections import defaultdict
d = defaultdict(list)
for i in [1,2,3]:
    d['eric'].append(i)

print(d)
#defaultdict(<class 'list'>, {'eric': [1, 2, 3]})

d['amy'] = {}
d['amy']['a'] = 1
print(d)

'''
defaultdict(<class 'list'>, {'eric': [1, 2, 3], 'amy': {'a': 1}})
可以看出，给定默认值的类型之后并不意味着字典中所有值都必须是此类型，也可以是其他类型。还能使用相应的方法来对行操作，
如列表的append和pop等方法。

4.2. 可调用函数作为初始化函数参数
除了接受类型名称作为初始化函数的参数之外，还可以使用任何不带参数的可调用函数，并以该函数返回值作为默认值。
例如，定义函数zero()让默认值为0：
'''
from collections import defaultdict
def zero():
     return 0

d = defaultdict(zero)
print(d['eric'])
#0
print(d)
#defaultdict(<function zero at 0x100662e18>, {'eric': 0})

#或者使用lambda函数：

d = defaultdict(lambda: 0)
print(d['amy'])
#0
print(d)

#defaultdict(<function <lambda> at 0x1019d3d90>, {'amy': 0})
#需要注意的是， defaultdict接受的参数必须是可调用的。若直接传递数字0，就会出现TyptError的异常。

#d = defaultdict(0)
'''
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: first argument must be callable or None
'''

