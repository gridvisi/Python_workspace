'''
前序：format是python2.6新增的一个格式化字符串的方法，相对于老版的%格式方法，它有很多优点。
不需要理会数据类型的问题，在%方法中%s只能替代字符串类型
单个参数可以多次输出，参数顺序可以不相同
填充方式十分灵活，对齐方式十分强大
官方推荐用的方式，%方式将会在后面的版本被淘汰
'''

#1、位置参数
print('{} , {}'.format(1,2))
print('{0} , {1}'.format(1,2))
print('{0} , {1}, {1}, {1}'.format(1,2))

#2、关键字参数
print('{a} {b}'.format(a=2,b=3))
print('{a} {b} {a} {a} {a}'.format(a=2,b=3))

#3、通过对象的属性
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
print('name is {p.name}, age is {p.age}'.format(p=Person('lili', 12)))

#4、使用对象下标
print('{0[0]},{0[1]}'.format([1,2,3]))

#5、填充与对齐
#冒号做为命令的开始，后面跟不同的指令，具体顺序如下：
#填充符号、对齐方式(> 右对齐，< 左对齐，^ 居中对齐)、宽度、进制

print('{:*>5}'.format(100))
print('{:0>5}'.format(100))

#进制输出    b、d、o、x分别是二进制、十进制、八进制、十六进制。
print('{:0<8b}'.format(10))

#3、浮点型的精度
print('{:.2f}'.format(3.1415))

#1、千位分隔符，参数必须为数字
print('{:,}'.format(10000000))

#time
from datetime import datetime
now=datetime.now()
print('{:%Y-%m-%d %X}'.format(now))

