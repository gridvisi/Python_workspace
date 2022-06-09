# https://python-course.eu/oop/metaclasses.php

# https://www.tutorialspoint.com/python/python_lists.htm
'''
A metaclass is a class whose instances are classes. Like an "ordinary" class defines the behavior of the instances of the class, a metaclass defines the behavior of classes and their instances.

Metaclasses are not supported by every object oriented programming language. Those programming language, which support metaclasses, considerably vary in way they implement them. Python is supporting them.

Some programmers see metaclasses in Python as "solutions waiting or looking for a problem".

There are numerous use cases for metaclasses. Just to name a few:

logging and profiling
interface checking
registering classes at creation time
automatically adding new methods
automatic property creation
proxies
automatic resource locking/synchronization.


一个元类是一个类，其实例是类。就像一个 "普通 "的类定义了该类实例的行为，一个元类定义了类和它们的实例的行为。

元类并不被每个面向对象的编程语言所支持。那些支持元类的编程语言，在实现它们的方式上有很大的不同。Python 正在支持它们。

一些程序员认为Python中的元类是 "等待或寻找问题的解决方案"。

元类的使用情况很多。仅举几个例子。

记录和分析
接口检查
在创建时注册类
自动添加新方法
自动创建属性
代理人
自动锁定/同步资源。

定义元类
基本上，元类的定义就像其他的 Python 类一样，但是它们是继承于 "类型" 的类。
另一个区别是，当使用元类的类声明结束时，元类会被自动调用。换句话说。
如果在类头的基类之后没有传递 "metaclass "关键字（也可能没有基类），type()
（即type的__call__）将被调用。另一方面，如果使用了一个元类关键字，
分配给它的类将被调用，而不是type。

现在我们创建一个非常简单的元类。除了它将在 __new__ 方法中打印它的参数内容，
并返回 type.__new__ 调用的结果之外，它一无是处。
'''

class LittleMeta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)

class S:
    pass

class A(S, metaclass=LittleMeta):
    pass
a = A()

x = input("Do you need the answer? (y/n): ")
if x.lower() == "y":
    required = True
else:
    required = False


def the_answer(self, *args):
    return 42


class EssentialAnswers(type):

    def __init__(cls, clsname, superclasses, attributedict):
        if required:
            cls.the_answer = the_answer


class Philosopher1(metaclass=EssentialAnswers):
    pass

class Philosopher2(metaclass=EssentialAnswers):
    pass

class Philosopher3(metaclass=EssentialAnswers):
    pass


plato = Philosopher1()
print(plato.the_answer())

kant = Philosopher2()
# let's see what Kant has to say :-)
print(kant.the_answer())

'''
我们可以看到LittleMeta.__new__已经被调用，而不是type.__new__。

恢复我们在上一章的思路。我们定义了一个元类EssentialAnswers，它能够自动
包括我们的augment_answer方法。

我们在 "类型和类的关系 "一章中已经知道，在处理完类的定义后，Python 会调用

type(classname, superclasses, attributes_dict)
如果在头中声明了元类，情况就不是这样了。这就是我们在前面的例子中所做的。我们的类Philosopher1、Philosopher2和Philosopher3已经与元类EssentialAnswers挂钩了。这就是为什么EssentialAnswer将被调用而不是type。

EssentialAnswer(classname, superclasses, attributes_dict)
准确地说，调用的参数将被设置为以下值。

EssentialAnswer('Philopsopher1', 
                (), 
                {'__module__': '__main__', '__qualname__': ' Philosopher1'})
其他的哲学家类被以一种类似的方式处理。

单身模式是一种设计模式，它将一个类的实例化限制为一个对象。它被用于只需要一个对象的情况。
这个概念可以被概括为限制实例化为一定数量或固定数量的对象。

这个术语源于数学，在数学中，单子（也被称为单元集）被用于具有精确一个元素的集合。
'''


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):
    pass


class RegularClass():
    pass


x = SingletonClass()
y = SingletonClass()
print(x == y)

x = RegularClass()
y = RegularClass()
print(x == y)


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance



'''
使用Singleton类创建Singletons
另外，我们可以通过继承Singleton类来创建Singleton类，可以像这样定义。
'''
class SingletonClass(Singleton):
    pass


class RegularClass():
    pass


x = SingletonClass()
y = SingletonClass()
print(x == y)

x = RegularClass()
y = RegularClass()
print(x == y)