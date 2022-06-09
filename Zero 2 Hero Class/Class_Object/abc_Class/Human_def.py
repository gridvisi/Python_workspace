
class Human():

    def __init__(self ,name ,gender):

        self.name = name
        self.gender = gender

    def speak_name(self): #// the sel f -going to speak the name
        print("MY Name is Will:", self.name)

will = Human("William" ,"Male")

print(will.name)
print(will.gender)

will.speak_name()


#case 2nd
class Color:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def hex_code(self):
        return f"#{format(self.r, '02x')}" \
               f"{format(self.g, '02x')}" \
               f"{format(self.b, '02x')}"

cat = Color('red','green','blue')
print('FORMAT:',format('red','02x'))
cat.hex_code()

'''
这是一个颜色的表示，可以输出颜色的十六进制代码。仍然有些简单，对于大多数人来说，
他们所需要的只是一个看起来像这样的类。

一个类，实际上，只是一个名字空间，它可以被调用来创建基于名字空间的对象。

__init__是最常见的 "魔法 "方法。提供了一个类的实例（通过self参数），
你可以初始化该实例的数据。它有一定的规则 (特别是它得到一个实例并返回 None)，
但最终它就像任何方法一样。

hex_code展示了函数操作的基本原理。每个方法调用（color.hex_code()）
都隐含地将对象作为调用的第一个参数。作为一个社区，我们使用self来确保我们知道
我们在谈论的是当前的对象。如果有任何参数被传递，这些参数的传递方式与函数参数
的传递方式相同，只是从第二个位置参数开始。在函数内部，我们可以使用self来访问实例属性。

现在你知道了足够的知识来制作简单的类。

现在，在这之后，它可以变得更加复杂，但让我们做一些简单的东西。

'''


class Vehicle:
    height = 1
    default_wheels = 4
    default_length = 10

    def __init__(self, wheels, length=10):
        self.wheels = wheels
        self.length = length

    def drive(self):
        """Do stuff here."""

    @classmethod
    def make(cls):
        return cls(cls.default_wheels, cls.default_length)

    def __eq__(self, other):
        return self.wheels == other.wheels and self.length == other.length and self.height == self.height


'''
        
        
在类的标题下，我们定义了类的属性。height, default_wheels, 和
default_length
是类本身可用的属性。你可以只用Vehicle.default_wheels这样的类型来访问它们。很简单，但是在
__eq__
中你看到了一个怪癖：实例也可以访问类的变量。

这允许你做一些事情，比如在类中设置默认值，这些值可以在子类中被重写。

接下来你会看到 @ classmethod。

@classmethod将函数从一个实例方法

（我在上面讨论过）变为一个类方法。一个类方法得到的是作为第一个参数的类型，或者说是类，而不是一个实例。
在Python中，我们用cls表示这一点。在makE中，我们使用
cls来制造一个类的实例，并返回它。

最后要介绍的是魔法方法。这些是编写类的实际困难部分。有几十个这样的方法，了解每个方法的来龙去脉本身就
可以写一两篇文章了。在这个例子中，__eq__是平等运算符的覆盖。当你做my_object == another_object时，
你调用了这些对象中的一个（或两个）__eq__方法。

另一个话题（我在这里不涉及，因为它会使这个答案的长度再次增加一倍）是继承，根据你的用法，它可以很简单也可
以很复杂。

13.6Kviews查看51upvotes

 '''
