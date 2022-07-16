'''
https://www.codewars.com/kata/56968ce7753513604b000055/train/python

描述任务

你的任务是计算一个底部是正方形的金字塔的最大可能高度（完整的层数），给定n个立方体的参数，
我们可以建立的顶层总是只有1个立方体，并且永远存在。没有空洞的区域，这意味着每一层都必须
完全由立方体填充。

因此，这些层是这样构建的：角的立方体总是覆盖它下面的角的立方体的内部25%，因此每行比下面
的立方体多一个立方体。

如果你只得到5个立方体，下层将有4个立方体，而最上面的1个立方体将位于它们的正中间，即下层
4个立方体的交界处。

如果给你14个立方体，你可以建一个3层的金字塔，但13个是不够的，因为你会缺少一个立方体，所
以只有2层是完整的，还有一些立方体是剩余的。

在给定的立方体数量下，我们可以建造的最高的金字塔是什么？只需返回完整的层数即可。



示意图

测试用例子

 4 --> 1

 5 --> 2

13 --> 2

14 --> 3

***难度稍高于加农炮的任务，因为任务是给出总数，推算层数，而且不计入不完整的层——
不能凑出m*m的正方形。有兴趣的先了解加农炮任务链接

Python数值计算 编程助力数学和物理趣味任务

开始今天的任务解析。
首先找出相邻的上下层的数字规律，即可以由上一层的数字推导出下一层的数字​。非常便于
用代码表达：上一层正方形边长是n，下一层边长就是n+1
考虑while循环，每一次循环减去n**2，n-> 1,2,3,...
'''

def pyramid_height(n):
    h = 0
    while n > 0:
        h += 1
        n -= h ** 2
    return h-1 if n < 0 else h
n = 14
print(pyramid_height(n))


# Rank 1st

from itertools import count
print(count())
print(next(count()))

f = lambda a:a ** 2
print('next:',next(x for x in count() if f(x) == 100))


f = lambda n: n * (n + 1) * (2 * n + 1) // 6
print(f)
def pyramid_height(n):
    return next(x for x in count() if f(x + 1) > n)

n = 100
print("pyramid_height =",pyramid_height(n))

#Tips itertools.count(）
from itertools import count
import itertools
for number in itertools.count():
    if number > 20:
        break
    print(number)


for number in itertools.count(start=10, step=4):
    print(number)
    if number > 20:
        break

from itertools import chain
a = (x for x in ['1', '2', '3', '4'])
b = (x for x in ['x', 'y', 'z'])
print(' '.join(chain(a, b)))