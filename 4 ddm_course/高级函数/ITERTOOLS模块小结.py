'''
一、组成
itertools主要来分为三类函数，分别为无限迭代器、输入序列迭代器、组合生成器，我们下面开始具体讲解。

二、无限迭代器
1、Itertools.count(start=0, step=1)
创建一个迭代对象，生成从start开始的连续整数，步长为step。
如果省略了start则默认从0开始，步长默认为1
如果超过了sys.maxint，则会移除并且从-sys.maxint-1开始计数。

作者：kivinsae
链接：https://www.jianshu.com/p/73b17486ef8c
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

from itertools import *
for i in zip(count(2,6), ['a', 'b', 'c']):
    print(i)
#输出为：
#    (2, 'a')    (8, 'b')    (14, 'c')


'''
2、Itertools.cycle(iterable)
创建一个迭代对象，对于输入的iterable的元素反复执行循环操作，内部生成iterable中的元素的一个副本，
这个副本用来返回循环中的重复项。
'''

from itertools import *
i = 0
for item in cycle(['a', 'b', 'c']):
    i += 1
    if i == 10:
        break
    print(i, item)

'''
3、Itertools.repeat(object[, times])
创建一个迭代器，重复生成object，如果没有设置times，则会无线生成对象。
'''
from itertools import *
for i in repeat('kivinsae', 5):
    print(i)