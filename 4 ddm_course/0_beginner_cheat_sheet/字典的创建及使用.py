'''

1 创建字典
字典以类似于下面的方式表示：
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
字典由键及其相应的值组成，这种键值对称为项（item）。在前面的示例中，键为名字，而值为电话号码。每个键与其值之间都用冒号（:）分隔，项之间用逗号分隔，而整个字典放在花括号内。空字典（没有任何项）用两个花括号表示，类似于下面这样： {}。

1.1 dict函数
可使用函数dict从其他映射（如其他字典）或键-值对序列创建字典。
'''



items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
d
{'age': 42, 'name': 'Gumby'}
d['name']
'Gumby'
#还可使用关键字实参来调用这个函数，如下所示：

d = dict(name='Gumby', age=42)
print(d)
#{'age': 42, 'name': 'Gumby'}

'''
尽管这可能是函数dict最常见的用法，但也可使用一个映射实参来调用它，这将创建一个字典，
其中包含指定映射中的所有项。像函数list、 tuple和str一样，如果调用这个函数时没有提
供任何实参，将返回一个空字典。从映射创建字典时，如果该映射也是字典（毕竟字典是Python
中唯一的内置映射类型），可不使用函数dict，而是使用字典方法copy，这将在本章后面介绍。

1.2 字典的基本操作
字典的基本行为在很多方面都类似于序列。

len(d)返回字典d包含的项（键值对）数。
d[k]返回与键k相关联的值。
d[k] = v将值v关联到键k。
del d[k]删除键为k的项。
k in d检查字典d是否包含键为k的项。
虽然字典和列表有多个相同之处，但也有一些重要的不同之处。
键的类型：字典中的键可以是整数，但并非必须是整数。字典中的键可以是任何不可变的类型，如浮点数（实数）、字符串或元组。
自动添加：即便是字典中原本没有的键，也可以给它赋值，这将在字典中创建一个新项。然而，如果不使用append或其他类似的方法，就不能给列表中没有的元素赋值。
成员资格：表达式k in d（其中d是一个字典）查找的是键而不是值，而表达式v in l（其中l是一个列表）查找的是值而不是索引。这看似不太一致，但你习惯后就会觉得相当自然。毕竟如果字典包含指定的键，检查相应的值就很容易。
示例：
henry@ubuntu:~/python$ cat database.py 
'''
#!/usr/bin/env python3
# 一个简单的数据库
# 一个将人名用作键的字典。每个人都用一个字典表示，
# 字典包含键'phone'和'addr'，它们分别与电话号码和地址相关联
people = {
'Alice': {
'phone': '2341',
'addr': 'Foo drive 23'
},
'Beth': {
'phone': '9102',
'addr': 'Bar street 42'
},
'Cecil': {
'phone': '3158',
'addr': 'Baz avenue 90'
}
}
# 电话号码和地址的描述性标签，供打印输出时使用
labels = {
'phone': 'phone number',
'addr': 'address'
}
name = input('Name: ')
# 要查找电话号码还是地址？
request = input('Phone number (p) or address (a)? ')
# 使用正确的键：
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'
# 仅当名字是字典包含的键时才打印信息：
if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))

'''
henry@ubuntu:~/python$ ./database.py 
Name: Alice
Phone number (p) or address (a)? p
Alice's phone number is 2341.
henry@ubuntu:~/python$ ./database.py 
Name: Alice
Phone number (p) or address (a)? a
Alice's address is Foo drive 23.
'''

'''

1.3 通过字典键名为格式化字符串提供变量
当格式化字符串"{name}".format_map(字典)中的name在字典中存在对应的键名时，
可以直接使用format_map(字典）来对格式化字符串进行填充。

'''
phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'}
print("Cecil's phone number is {Cecil}.".format_map(phonebook))
#"Cecil's phone number is 3258.

'''

2 常见字典操作函数
2.1 clear
方法clear删除所有的字典项，这种操作是就地执行的（就像list.sort一样），因此什么都不返回（或者说返回None）。

'''
d = {}
d['name'] = 'Gumby'
d['age'] = 42
d
{'age': 42, 'name': 'Gumby'}
returned_value = d.clear()
d
{}
print(returned_value)
None

#这为何很有用呢？我们来看两个场景。下面是第一个场景：

x = {}
y = x
x['key'] = 'value'
y
#{'key': 'value'}
x = {}
y
#{'key': 'value'}

#下面是第二个场景：

x = {}
y = x
x['key'] = 'value'
y
#{'key': 'value'}
x.clear()
y
#{}

'''
在这两个场景中， x和y最初都指向同一个字典。在第一个场景中，我通过将一个空字典
赋给x来“清空”它。这对y没有任何影响，它依然指向原来的字典。这种行为可能正是你想
要的，但要删除原来字典的所有元素，必须使用clear。如果这样做， y也将是空的，
如第二个场景所示。

2.2 copy及deepcopy
方法copy返回一个新字典，其包含的键-值对与原来的字典相同（这个方法执行的是浅复制，
因为值本身是原件，而非副本）。

'''
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'    #原值不变
y['machines'].remove('bar')  #原值一起变化
y
#{'username': 'mlh', 'machines': ['foo', 'baz']}
x
#{'username': 'admin', 'machines': ['foo', 'baz']}
y['machines'][0]='aaa'   #原值一起变化
x
#{'username': 'henry', 'machines': ['aaa', 'baz']}
y
#{'username': 'mlh', 'machines': ['aaa', 'baz']}

#为避免上述问题可以使用copy模块中的deepcopy函数来执行深复制，即同时复制值及其包含的所有值。

from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
c
#{'names': ['Alfred', 'Bertrand', 'Clive']}
dc
{'names': ['Alfred', 'Bertrand']}

'''
2.3 fromkeys
方法fromkeys创建一个新字典，其中包含指定的键，且每个键对应的值都是None。
'''

{}.fromkeys(['name', 'age'])
#{'age': None, 'name': None}

#这个示例首先创建了一个空字典，再对其调用方法fromkeys来创建另一个字典，
#这显得有点多余。你可以不这样做，而是直接对dict（前面说过， dict是所有字典所属的类型）
# 调用方法fromkeys。

dict.fromkeys(['name', 'age'])
#{'age': None, 'name': None}
#如果你不想使用默认值None，可提供特定的值。

dict.fromkeys(['name', 'age'], '(unknown)')
#{'age': '(unknown)', 'name': '(unknown)'}

#2.4 get
#通常，如果你试图访问字典中没有的项，将引发错误。而使用get在访问字典中不存在的项
# 时默认返回None，并且不会引发上述错误。

d = {}
#print(d['name'])
'''
Traceback (most recent call last):
File "<stdin>", line 1, in ?
KeyError: 'name'
而使用get不会这样：
'''

print(d.get('name'))
'''
None
如你所见，使用get来访问不存在的键时，没有引发异常，而是返回None。你可指定“默认值”，
这样将返回你指定的值而不是None。
'''

d.get('name', 'N/A')
'N/A'
#如果字典包含指定的键， get的作用将与普通字典查找相同。

d['name'] = 'Eric'
d.get('name')
'Eric'

'''
2.5 items
方法items返回一个包含所有字典项的列表，其中每个元素都为(key, value)的形式。
字典项在列表中的排列顺序不确定。
'''

d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
d.items()

#dict_items([('url', 'http://www.python.org'), ('spam', 0), ('title', 'Python Web Site')])

#返回值属于一种名为字典视图的特殊类型，字典视图可用于迭代；另外，你还可确定其长度
# 以及对其执行成员资格检查。

it = d.items()
len(it)
#3
print(('spam', 0) in it)
#True

#视图的一个优点是不复制，它们始终是底层字典的反映。当底层字典的内容被修
# 改时，视图呈现出来的是修改后的值。

d['spam'] = 1
print(('spam', 0) in it)
#False

d['spam'] = 0
print(('spam', 0) in it)
#True
#然而，如果你要将字典项复制到列表中（在较旧的Python版本中，方法items就是这样做的），
# 可自己动手做。

list(d.items())
#[('spam', 0), ('title', 'Python Web Site'), ('url', 'http://www.python.org')]

'''
2.6 keys
方法keys返回一个字典视图，其中包含指定字典中的键。

'''
d.keys()
#dict_keys(['title', 'url', 'spam'])


'''

2.7 pop
方法pop可用于获取与指定键相关联的值，并将该键-值对从字典中删除。

'''
d = {'x': 1, 'y': 2}
d.pop('x')
1
print(d) #{'y': 2}

'''

2.8 popitem
方法popitem类似于list.pop，但list.pop弹出列表中的最后一个元素，而popitem随机地弹出一个字典
项，因为字典项的顺序是不确定的，没有“最后一个元素”的概念。如果你要以高效地方式逐个删除并处理所
有字典项，这可能很有用，因为这样无需先获取键列表。
'''

d = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'}
d.popitem()
#('url', 'http://www.python.org')
d
#{'spam': 0, 'title': 'Python Web Site'}

'''
2.9 setDefalult
当指定的键不存在时， setdefault使用参数中提供的值来更新字典，并返回对应的键值；
当指定的键存在时，直接返回其值，并保持字典不变。
'''

d = {}
d.setdefault('name', 'N/A')
'N/A'
d
#{'name': 'N/A'}

d['name'] = 'Gumby'
d.setdefault('name', 'N/A')
'Gumby'
d
#{'name': 'Gumby'}
#与get一样，值是可选的；如果没有指定，默认为None。

d = {}
print(d.setdefault('name'))
#None
d
#{'name': None}

'''

2.10 update
方法update使用一个字典中的项来更新另一个字典。

'''
d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
    }
x = {'title': 'Python Language Website'}
d.update(x)
d
#{'url': 'http://www.python.org', 'changed':
#'Mar 14 22:09:15 MET 2016', 'title': 'Python Language Website'}

#对于通过参数提供的字典，将其项添加到当前字典中。如果当前字典包含键相同的项，就替换它。
# 可像调用本章前面讨论的函数dict（类型构造函数）那样调用方法update。这意味着调用update时，
# 可向它提供一个映射、一个由键值对组成的序列（或其他可迭代对象）或关键字参数。


'''

2.11 values
方法values返回一个由字典中的值组成的字典视图。不同于方法keys，方法values返回的视
图可能包含重复的值。

'''
d = {}
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 1
d.values()
#dict_values([1, 2, 3, 1])


