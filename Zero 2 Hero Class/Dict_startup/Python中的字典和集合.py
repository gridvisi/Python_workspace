
def fillable(stock, merch, n):
    stock = {
        'football': 4,
        'boardgame': 10,
        'leggos': 1,
        'doll': 5}
    return stock[merch] > n if stock.get(merch,False) else False

stock = 4
merch = 'football'
n = 3
print(fillable(stock, merch, n))





#Dictionaries
#dict
mike_id = {'mike',123}
mike_id = {'mike':123}
print('output:',mike_id['mike']) #key,value
name = {'phil':'李泓霏'}

#今天的作业是用字典生成一个紧急电话号码本
# 示范：
Emergency_call = {'114':"查号台",'119':'火警'}  #emergence
#生成号码本后，查询两个紧急电话：急救和火灾
# lift1 =7  lift2 = 10 call = 8



d1={"one":1,"two":2,"three":3}#字面量句法
d2=dict(one=1,two=2,three=3)
d3=dict([("one",1),("two",2),("three",3)])
d4=dict({"one":1,"two":2,"three":3})
d5=dict(zip(["one","two","three"],[1,2,3]))#zip并行解包
print(d1==d2==d3==d4==d5)#True


'''
以上五种方法创建的字典是相等的。

2、isintance
映射类型（Mapping Types）是一种关联式的容器类型，它存储了对象与对象之间的映射关系。
字典是Python中唯一的映射类型，它是存储了若干键值对（由键映射到值）的关联容器。

collections.abc模块中有两个抽象基类，分别是Mapping和MutableMapping，它们为dict和其他类似的类型定义形式接口。

isinstance：判定object的类型
语法：isinstance(object, classinfo)

其中，object 是变量，classinfo 是类型即 (tuple,dict,int,float,list,bool等) 和 class类
若参数object是classinfo类的实例，或者object是classinfo类的子类的一个实例， 返回 True；若 object 不是一个给定类型的的对象，则返回结果总是False。
若classinfo不是一种数据类型或者由数据类型构成的元组，将引发一个TypeError 异常。
eg:
'''

from _collections_abc import Mapping
my_dict={}
print(isinstance(my_dict,Mapping))

'''
isinstance和type的区别：
若对象是classinfo中一个类的子类，isinstance可以判断出来返回True，
而type是不能的。

3、字典推导
字典推导:在{}中使用命令语句加for甚至if实现迭代推导出新列表的操作。
'''
Country_Codes = [(86,"China"),
                 (91,"India"),
               (1,"United States"),
               (62,"Indonesia"),
               (55,"Brazil"),
               (92,"Pakistan"),
               (81,"Japan"),
                (81,"Australia"),
                 (89,"Auckland")
               ]

dict1={country:code for code,country in Country_Codes}
#推导过程
print(dict1)

dict2={code:country.upper() for code,country in Country_Codes if code>80}#由限制要求创建字典
print(dict2)
#输出：
#{'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62, 'Brazil': 55, 'Pakistan': 92, 'Japan': 81}
#{86: 'CHINA', 91: 'INDIA', 92: 'PAKISTAN', 81: 'JAPAN'}


'''
4、setdefault：处理找不到的键
d.setdefault VS d.get
d.setdefault(k,[default])和d.get(k,[default])两种方法都可以处理找不到的键的情况，区别在于setdefault在返回默认值的同时能够在原字典创建新的k-default键值对。
所以更新某个键值对但键不一定存在时，用d.setdefault更好一些.

eg1:处理找不到的键
'''
names=["Ailee","Bob","Cindy"]
ages=["19","17","15"]
dict3={x:y for x,y in zip(names,ages)}#用zip可以并行拆包.
print(dict3)
print(dict3.get("David","20"))
print(dict3)#get处理查不到的键时返回默认值，但不会在原字典创建这个键.
dict3.setdefault("David","20")
print(dict3)#setdefault处理查不到的键时返回默认值，并且会在原字典创建这个键.

'''
二、多样化的字典
1、defaultdict：处理找不到的键的另一选择
格式：class collections.defaultdict([default_factory[, ...]])
defaultdict是內建dict的子类，它能够在查询找不到的键时为其创造默认值，
由此避免抛出keyerror。其他功能与dict相同。

eg:defaultdict推导
'''
from _collections import defaultdict
dict3=defaultdict(list,[(x,y) for x,y in zip([1,2,3,4,5],list("apple"))])
print(dict3)
#输出：
#defaultdict(<class 'list'>, {1: 'a', 2: 'p', 3: 'p', 4: 'l', 5: 'e'})

from _collections import defaultdict

namelist = ['Ailee', 'Bob', 'Cindy', 'Ailee', 'Bob', 'Cindy', 'Cindy', 'Cindy', 'Bob', 'Cindy', 'Ailee', 'Bob', 'Bob']
count = defaultdict(int)  # 使用记录值数据结构整型作为默认的工厂函数

for x in namelist:
    count[x] += 1

print(count)
# defaultdict(<class 'int'>, {'Ailee': 3, 'Bob': 5, 'Cindy': 5})

'''
原理解释：defaultdict在查询找不到的键时会通过__getitem__调用__missing__，然后__missing__根据default_factory选择返回默认值。当不输入default_factory时，会抛出keyerror。
我们可以通过print (defaultdict.__missing__.__doc__)来看__missing__的内部实现：

__missing__(key) # Called by __getitem__ for missing key; pseudo-code:
  if self.default_factory is None: raise KeyError((key,))
  self[key] = value = self.default_factory()#为找不到的键创建默认值
  return value
'''

'''
default_factory的选择

类型名称作为初始化函数参数
此类设置根据创建字典的值的需求而定；
若值以整型记录可用int；若用列表记录多个数据可用list。
可调用函数作为初始化函数参数
使用任何不带参数的可调用函数，并以该函数返回值作为默认值。
仍以点名code为例，有两种方法：
1）自定义函数：

def zero():
    return 0
count=defaultdict(zero)
2）使用lambda创建匿名函数

count=defaultdict(lambda :0)
'''
'''
2、子类化UserDict
UserDict继承自抽象基类（abstract based class）中的MutableMapping。
图片描述

UserDict是让用户继承写子类的。之所以倾向于从UserDict而不是dict继承的
原因是，这是因为在覆盖重写dict类的 get(k, default)、__setitem__( )、
__contain__( )、__missing__( ) 等方法时，常常又会使用到 mapObj[k]、
 k in mapObj、mapObj[k] 等语法形式，这样一不小心就会造成这些内部方法的
 无穷递归调用。但是UserDict就不会有此类问题。

UserDict有一个data的属性，是dict的实例。用户定义UserDict的子类时如果
重写方法，并不会递归调用UserDict的其他方法，而是对UserDict.data进行操
作，这样就减少了用户自定义dict时防范死循环递归的难度。

eg:
'''
import collections
class Modified_Dict(collections.UserDict):#继承自UserDict
    def __missing__(self,key):
        if isinstance(key, str):#防止递归循环，及时抛出keyerror
            raise KeyError(key)
        return self[str(key)]
    def __contains__(self,key):
        return str(key) in self.data
    def __setitem__(self, key, item):
        self.data[str(key)]=item
dict4=Modified_Dict({'Ailee': 3, 'Bob': 5, 'Cindy': 5})#使用新dict类构造字典
print(dict4["Ailee"])#输出：3
dict4.update({"one":1,"two":2})
print(dict4)#输出：{'Ailee': 3, 'Bob': 5, 'Cindy': 5, 'one': 1, 'two': 2}

#错误示范：这里应该加圆括号建立自定义dict的空字典，否则之后的数据无法被更新

dict5=Modified_Dict
dict5.update({"one":1,"two":2})
print(dict5)#<class '__main__.Modified_Dict'>发现update失败 -_-!

'''
UserDict继承自Mapping基类，诸如MutableMapping.update和Mapping.get也很实用。（截止2017.12.15 未掌握Mapping.get）

3、不可变映射类型
从Python3.3开始，type模块引入了一个封装类名叫做MappingProxyType。MappingProxyType提供一个可读的动态映射视图，即用户无法从这个视图对原映射进行改动，但是原映射有改动时可以通过这个视图观察到。
此类型特点在于防止用户错误的修改映射。
'''

from types import MappingProxyType
Prize_number={'Ailee': 3, 'Bob': 5, 'Cindy': 5}
dict6=MappingProxyType(Prize_number)
dict6["Ailee"]=6#不支持改动。TypeError: 'mappingproxy' object does not support item assignment
print(dict6)

Prize_number["Ailee"]=6
print(dict6)#{'Ailee': 6, 'Bob': 5, 'Cindy': 5}原映射改动可视。

'''
4、其它映射类型
collections.OrderedDict
OrderedDict能够记住key的插入先后顺序。
eg:
'''
from _collections import OrderedDict
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
print(OrderedDict(sorted(d.items())))
print(OrderedDict(sorted(d.items(),key=lambda t :t[1])))

'''
输出：

OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
在之前第二章namedtuple中也提到过。namedtuple的实例方法_asdict()把具名元组以collections.OrderedDict的形式返回。

collections.ChainMap
ChainMap可以容纳数个不同的映射对象，然后在进行键查找操作的时候，这些对象会被当成一个整体被逐个查找，直到键被找到为止。
查询规则片段：
'''
import builtins
#pylookup = ChainMap(locals(), globals(), vars(builtins))

'''
想了解更多：
https://docs.python.org/3/lib...
collections.Counter
counter用来统计目标集合中不同的元素及其频数，利用most_common([n])返回前n个频数最高的值以及相应的计数。

eg:
'''
from collections import Counter
ct=Counter('wasdddsasd')
print(ct)#Counter({'d': 4, 's': 3, 'a': 2, 'w': 1})
ct.update("dassddd")
print(ct.most_common(2))#[('d', 8), ('s', 5)]

'''
三、集合
1、集合的定义与字面量
定义：Python标准文库给出的定义：A set object is an unordered collection of distinct hashable objects.
翻译过来就是：set是一个包含不同可散列对象的无序集合
种类：集合这种数据结构包含set和frozenset，两者的区别在于后者不可变而前者可变，类似于元组之于列表。因此frozenset相比set不具备修改一类的方法。
本质：集合是许多唯一对象的聚集，所以可以用来去重。
新建set：

在大括号中直接填写元素，类似字典
set1={"apple","banana","pear"}
利用构造方法set()，类似list()
set4=set("apple")
空集的构造
注意空集的构造只能用set()而不能用{}，{}是空字典而非空集
set3=set()
新建frozenset：

只能使用构造方法frozenset()
frozenset1=frozenset(range(5))
print(frozenset1)#frozenset({0, 1, 2, 3, 4})
只能使用此方法的原因是Python中没有针对frozenset的特殊字面量句法（对于列表的字面量句法就是[]这样子 ）。
集合推导：
集合推导在大括号中进行，思路与列表推导，字典推导类似。
eg:
'''

