'''
学习Python的类，一直不太理解为什么一定要定义init()方法，现在简要谈一下自己的理解吧。

1、不用init()方法定义类
定义一个矩形的类，目的是求周长和面积。
'''
class Rectangle():
    def getPeri(self,a,b):
        return (a + b)*2
    def getArea(self,a,b):
        return a*b

rect = Rectangle()
print(rect.getPeri(3,4))
print(rect.getArea(3,4))
print(rect.__dict__)

'''
从上例中可以看到，我们在类中并没有定义init()方法，但是也能够得到类似的要求，结果返回了矩形实例rect的周长及面积。
但是，我们通过print(rect.dict)来看这个实例的属性，竟然是空的，我定义了一个矩形，按理来说它的属性应该是它的长、宽。但是它竟然没有。这就是没有定义init()的原因了。
并且，在实例化对象的时候，rect = Rectangle()参数为空，没有指定a、b的值，只有在调用函数的时候才指定了。且类中定义的每个方法的参数都有a、b，这显然浪费感情，在类中直接指定方法就可以了。、

因此吧，需要在类中定义init()方法，方便创建实例的时候，需要给实例绑定上属性，也方便类中的方法（函数）的定义。

2、用init()方法定义类
上述同样的例子，采用init()方法定义类，如下：
'''

class Rectangle():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def getPeri(self):
        return (self.a + self.b)*2
    def getArea(self):
        return self.a * self.b

rect = Rectangle(3,4)
print(rect.getPeri())
print(rect.getArea())
print(rect.__dict__)


class Box:
    def setDimension(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def getVolume(self):
        return self.width * self.height * self.depth

b = Box()
b.setDimension(10, 20, 30)
print(b.getVolume())


class Box:
    # def setDimension(self, width, height, depth):
    #   self.width = width
    #   self.height = height
    #   self.depth = depth
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def getVolume(self):
        return self.width * self.height * self.depth

b = Box(10, 20, 30)
print(b.getVolume())

'''
_init__方法：
使用方式：
def 类名:
        #初始化函数，用来完成一些默认的设定
        def __init__():
            pass


     总结：
__init__()方法，在创建一个对象时默认被调用，不需要手动调用
__init__(self)中，默认有1个参数名字为self，如果在创建对象时传递了2个实参，那么__init__(self)中出了self作为第一个形参外还需要2个形 参，例如__init__(self,x,y)
__init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递进去
'''
print('------------"""定义了一个Cat类"""--------------------')
class Cat:
    """定义了一个Cat类"""

    #初始化对象
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age

    #方法
    def eat(self):
        print("猫在吃鱼....")

    def drink(self):
        print("猫正在喝kele.....")

    def introduce(self):
        print("%s的年龄是:%d"%(self.name, self.age))

#创建一个对象
tom = Cat("汤姆", 40)
tom.eat()
tom.drink()
#tom.name = "汤姆"
#tom.age = 40
tom.introduce()

lanmao = Cat("蓝猫", 10)
#lanmao.name = "蓝猫"
#lanmao.age = 10
lanmao.introduce()