# https://blog.csdn.net/sunchengquan/article/details/84494101?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.add_param_isCf&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.add_param_isCf

#list，dict，str虽然是Iterable，却不是Iterator
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#from collections import Iterator
from collections.abc import Iterable
#print(isinstance(a,Iterator))
print(isinstance(a,Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
'''
 DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 
 'collections.abc' is deprecated since Python 3.3, and in 3.9 it will stop working
 翻译：弃用警告：从collections中导入ABCs已被弃用，并在python3.8中将停止工作，
 可使用collections.abc代替它进行使用
'''

a = map(lambda x:x*x, a)
print(list(a))

sq = [i*i for i in a]
sq = [i*i for i in range(10)]
sq = (i*i for i in range(10))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(list(sq))

sq = (i*i for i in range(10))
for i in sq:
    print(i,end=';')

print('lambda sort')
ls = [('a',1),('b',5),('e',4),('f',2)]
print(sorted(ls))
print(sorted(ls,key=lambda ls :ls[1]))

dict1={'a':1, 'b':4, 'c':2, 'd':3}
print(sorted(dict1.items(), key=lambda item:item[1]))


"""
第一是直接作为脚本执行，
第二是import到其他的python脚本中被调用（模块重用）执行。
因此if __name__ == '__main__': 的作用就是控制这两种情况执行代码的过程，
在if __name__ == '__main__':下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，而import到其他脚本中是不会被执行的。
"""

def myYield(n):
    while n>0:
        print('开始生成。。。')
        yield n
        print('完成一次。。。')
        n -= 1
if __name__ == '__main__':
    a = myYield(3)
    print('已经实例化生成器对象')
#     a.__next__()
#     print('第二次调用__next__()方法：')
#     a.__next__()

'''
yield 语句是生成器中的关键语句，生成器在实例化时并不会被执行，而是等待调用其__next__()方法才开始运行。
并且当程序运行完yield语句后就会“吼（hold）住”，即保持当前状态且停止运行，等待下一次遍历时才恢复运行。

程序运行的结果中的空行后的输出“已经实例化生成器对象”之前，已经实例化了生成器对象，但生成器并没有运行
（没有输出‘开始生成’）。当第一次手工调用__next__()方法之后，才输出‘开始生成’，标志着生成器已经运行，
而在输出‘’第二次调用__next__()方法‘’之前并没有输出‘完成一次’，说明yield语句运行之后就立即停止了。
而第二次调用__next__()方法之后，才输出‘完成一次’，说明生成器的回复运行是从yield语句之后开始运行的
'''

'''
生成器在Python中是一个非常强大的编程结构，可以用更少地中间变量写流式代码，此外，相比其它容器对象它更能节
省内存和CPU，当然它可以用更少的代码来实现相似的功能。现在就可以动手重构你的代码了，
但凡看到类似
def something():
    result= []
    for ... in ...：
        result.append(x)
        return result
        
def iter_something():
    result = []
    for ... in ...：
        yield x
'''
def triangles():
    result = [1]
    while True:
        yield result
        result = [1] + [result[i] + result[i+1] for i in range(len(result)-1)] + [1]
print(triangles())

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

#生成器并行

def gen():
    a = yield 1
    print('yield a % s' % a)
    b = yield 2
    print('yield b % s' % b)
    c = yield 3
    print('yield c % s' % c)
    return "happy ending"


r = gen()
x = next(r)
print('next x %s' % x)
y = r.send(10)
print('next y %s' %y)
z = next(r)
print('next z %s' % z)
try:
    a = next(r)
except StopIteration as e:
    print(e)

'''
运行过程说明：

第一步：r = gen()，实例化一个生成器对象
第二步：调用next() ，遇到yield 暂停，返回值1，赋值给x
第三步：打印x的值
第四步：传值10，在暂停处接受值10，赋值给a，继续运行，打印a的值，遇到第二个yield，暂停，返回值2，赋值给y
第五步：打印y的值
第六步：调用next() ，打印b值，遇到第三个yield暂停，返回值3，赋值给z
第七步：打印z值
第八步：调用next()，打印c的值，报StopIteration错误，用try。。。except捕获错误
'''
import time
import random

food = ["韭菜鸡蛋", "猪肉白菜", "猪肉荠菜", "羊肉白菜", "猪肉大葱", "虾仁海鲜"]


def consumer(name):
    print("%s 准备吃包子啦!" % name)
    while True:
        baozi = yield 'n'
        print("[%s]馅包子来了,被[%s]吃了!" % (baozi, name))


def producer(name):
    c1 = consumer('大儿子')
    c2 = consumer('小儿子')
    c1.__next__()
    c2.__next__()
    print("%s开始准备做包子啦" % name)
    for i in range(6):
        print("第%d次做了%s个包子" % (i + 1, len(food)))
        time.sleep(random.randint(1, 3))
        f1 = food[i]
        c1.send(f1)
        food.append(f1)
        random.shuffle(food)
        c2.send(food[i])

producer('老子')

'''
迭代器
迭代器概述
可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型,如list,tuple,dict,set,str等
一类是generator ，包括生成器和带yeild的generator function
这些可以 直接作用于for循环的对象统称为可迭代对象：Iterable
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

iter()函数 创建迭代器
iter（iterable）#一个参数，要求参数为可迭代的类型

把list、dict、str等Iterable变成Iterator可以使用iter()函数
'''
from collections import Iterator
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter('abc'),Iterator))
'''
False
False
True
True
'''
'''
你可能会问，为什么list、dict、str等数据类型不是Iterator？
这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它
才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的，例如：
'''
for x in [1, 2, 3, 4, 5]:
    print(x,end=',')


# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x,end=',')
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

'''
创建一个迭代器(类)
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 
它会在对象初始化的时候执行

__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 
异常标识迭代的完成。

'''
from itertools import islice
class Fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.prev,self.curr = self.curr,self.prev+self.curr
        return self.curr
f = Fib()
print(list(islice(f ,0,10)))

'''
Fib既是一个可迭代对象（因为它实现了 __iter__方法），又是一个迭代器（因为实现了 __next__方法)
StopIteration
StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 next() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
在 20 次迭代后停止执行：
'''


class MyNumbers:
    def __init__(self):
        self.a = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = MyNumbers()
# myiter = iter(myclass)

for x in myiter:
    print(x, end=",")

'''
内置迭代器工具
比如 itertools 函数返回的都是迭代器对象
count无限迭代器
'''
from itertools import count
counter = count(start=10)
print(next(counter))
print(next(counter)) #python内建函数next()对itertools创建的迭代器进行循环

#cycle 无限迭代器，从一个有限序列中生成无限序列：
from itertools import cycle
colors = cycle(['red','black','blue'])
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))

from itertools import count
counter = count(start=10)
i=4
print(next(counter))
while i > 0:
    print(next(counter))
    i -= 1


