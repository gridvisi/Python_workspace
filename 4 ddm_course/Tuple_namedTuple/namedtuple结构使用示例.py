from collections import namedtuple

# 初始化需要两个参数，第一个是 name，第二个参数是所有 item 名字的列表。
coordinate = namedtuple('Coordinate', ['x', 'y'])

c = coordinate(10, 20)
# or
c = coordinate(x=10, y=20)

c.x == c[0]
c.y == c[1]
x, y = c

"""
比如我们用户拥有一个这样的数据结构，每一个对象是拥有三个元素的tuple。
使用namedtuple方法就可以方便的通过tuple来生成可读性更高也更好用的数据结构。
"""
from collections import namedtuple
websites = [
 ('Sohu', 'http://www.google.com/', u'张朝阳'),
 ('Sina', 'http://www.sina.com.cn/', u'王志东'),
 ('163', 'http://www.163.com/', u'丁磊')
]
Website = namedtuple('Website', ['name', 'url', 'founder'])
for website in websites:
 website = Website._make(website)
 print(website)
 print(website[0], website.url)

from collections import namedtuple

# 基本例子
Point = namedtuple('Point', ['x', 'y'])  # 类名为Point,属性有'x'和'y'

p = Point(11, y=22)  # 用位置或关键字参数实例化，因为'x'在'y'前，所以x=11,和函数参数赋值一样的
print(p[0] + p[1])  # 我们也可以使用下标来访问
# 33

x, y = p  # 也可以像一个元组那样解析
print(x, y)
# (11, 22)

print(p.x + p.y)  # 也可以通过属性名来访问
# 33

print(p)  # 通过内置的__repr__函数，显示该对象的信息
# Point(x=11, y=22)

t = [11, 22] # 列表 list
p = Point._make(t) # 从列表中直接赋值，返回对象
print(Point(x=11, y=22))
# Point(x=11, y=22)

p = Point(x=11, y=22) # 新建一个对象
d = p._asdict() # 解析并返回一个字典对象
print(d)
# {'x': 11, 'y': 22}

p = Point(x=11, y=22)  # x=11,y=22
print(p)
# Point(x=11, y=22)

d = p._replace(x=33)  # x=33,y=22 新的对象
print(p)
# Point(x=11, y=22)
print(d)
# Point(x=33, y=22)


from collections import namedtuple

# 创建一个namedtuple的学生类,第一个参数是命名元组的名称，第二个参数是命名元组的属性，多个用空格隔开(或者逗号)
Student = namedtuple('Student', 'gender age height')

# 实例化学生,赋予属性，和上面第二个参数相对应
Miles = Student('Male', 24, 1.92)
Mary = Student('Female', 18, 1.68)

# 查看属性
print(Miles)  # 查看Miles所有属性
print(Mary.height)  # 查看Mary的身高
print(Miles[1])  # 通过索引查看Miles的年龄
print('==============')

# 遍历元组
for i in Mary:
    print(i)