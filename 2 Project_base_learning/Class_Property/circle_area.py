
import math

class Circle:

    def __init__(self, radius):  # 圆的半径radius
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2  # 计算面积

    @property
    def perimeter(self):
        return 2*math.pi*self.radius  # 计算周长

c = Circle(10)
print(c.radius)
print(c.area)  # 可以像访问数据属性一样去访问area, 会触发一个函数的执行, 动态计算出一个值
print(c.perimeter)  # 同上


#solution 2nd


class Circle:

    def __init__(self, radius):  # 圆的半径radius
        self.radius = radius

    #@property
    def area(self):
        return math.pi * self.radius**2  # 计算面积

    #@property
    def perimeter(self):
        return 2*math.pi*self.radius  # 计算周长

c = Circle(10)
print(c.radius)
print(c.area)  # 可以像访问数据属性一样去访问area, 会触发一个函数的执行, 动态计算出一个值
print(c.perimeter)  # 同上


#3rd statemothed
class Foo:

    @staticmethod
    def spam(x, y, z):
        print(x, y, z)

    # spam = staticmethod(spam)


print(type(Foo.spam))
Foo.spam(1, 2, 3)

f = Foo()
f.spam(4, 5, 6)

