import sys
re = [i for i in range(100000) if i%2 == 0]
print(sys.getsizeof(re))
re_range = (range(0,100000,2))
print(sys.getsizeof(re_range))

res = []
for i in range(100000):
    if i%2 == 0:
        res.append(i)
print(sys.getsizeof(res))

people = [
{ 'name': 'John', "age": 64 },
{ 'name': 'Janet', "age": 34 },
{ 'name': 'Ed', "age": 24 },
{ 'name': 'Sara', "age": 64 },
{ 'name': 'John', "age": 32 },
{ 'name': 'Jane', "age": 34 },
{ 'name': 'John', "age": 99 },
]

import operator
print(people.sort(key=operator.itemgetter('age')))
print(people.sort(key=operator.itemgetter('name')))
print(people)

mylist = [i for i in range(10)]
print(mylist)  # [0, 1, 2, 3,4, 5, 6, 7, 8, 9]

'''
自3.7版之后，Python开始能提供数据类别。比起常规类或其他替代方法(如返回多个值或字典)，它有着更多优点：

数据类需要很少的代码
可以比较数据类，因为 eq 可以实现此功能
数据类需要类型提示，减少了发生错误的可能性
可以轻松打印数据类以进行调试，因为__repr__可以实现此功能
这是一个工作中的数据类示例：
'''

from dataclasses import dataclass
@dataclass
class DataClassCard:
    rank: str
    suit: str

queen_of_hearts = DataClassCard('Q', 'Hearts')
print(queen_of_hearts.rank)
#'Q'
print(queen_of_hearts)
DataClassCard(rank='Q', suit='Hearts')
print(queen_of_hearts == DataClassCard('Q', 'Hearts'))
#True

'''
5.查找最频繁出现的值
要查找列表或字符串中最频繁出现的值：

max()将返回列表中的最大值。key参数采用单个参数函数自定义排序顺序，在本例中为test.count，该函数适用于迭代器上的每个项目。
test.count是list的内置功能。它接受一个参数，并计算该参数的出现次数。因此test.count(1)将返回2，而test.count(4)将返回4。
set(test)返回test中的所有唯一值，所以{1、2、3、4}
那么在这一行代码将接受test的所有唯一值，即{1、2、3、4}。接下来，max将对其应用list.count 函数并返回最大值。

还有一种更有效的方法：

'''
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key = test.count))
# 4

from collections import Counter
Counter(test).most_common(1)
# [4: 4]

'''
6. 合并字典 (Python 3.5+)
自 Python 3.5 以来，合并字典更容易了。
如果有重叠的键，第一个字典的键将被覆盖。在 Python 3.9 中合并字典变得更加干净。上述Python 3.9中的合并可以重写为。
合并 = dict1 | dict2

durian 榴莲
damson plum西洋李bai子
dangshan pear砀山梨
date枣 ；椰du枣
date pit枣核
downy pitch毛桃zhi
duke公爵dao樱桃
dry fruit干果

mango 芒果、mandarin 柑橘、mangosteen 山竹 grapefruit 葡萄柚（西柚）、kiwi fruit 猕猴桃（奇异果）、
pitaya/dragon fruit 火龙果  pomegranate 石榴、pomelo 柚子、文旦 blueberry 蓝莓、strawberry草莓、
cranberry 蔓越莓、mulberry 桑葚、bayberry 杨梅  lemon 柠檬、persimmon 柿子 hazelnut 榛子、peanut 
花生、walnut 核桃、coconut 椰子、chestnut 栗子（板栗）、betel nut 槟榔
damson 大马士革李
date枣
date pit枣核
decayed fruit烂果
downy pitch毛桃
dry fruit干果
duke公爵樱桃
peach 桃子、flat peach 蟠桃、juicy peach 水蜜桃、honey peach 蜜桃，外加nectarine 油桃（虽然没有peach）
melon 瓜、watermelon 西瓜、rock melon 哈密瓜（澳洲说法）、muskmelon 香瓜、甜瓜
'''
name = ['apple','banana','carrot','date']
cname = ['苹果','香蕉','胡萝卜','枣']
dict1 = dict(zip(name,cname))
print(dict1)

name2 = ['apple pie','banana','carrot','date','blueberry']
cname2 = ['苹果派','香蕉','胡萝卜','枣子','蓝莓']
dict2 = dict(zip(name2,cname2))
print(dict2)

dict1.update(dict2)
print(dict1)