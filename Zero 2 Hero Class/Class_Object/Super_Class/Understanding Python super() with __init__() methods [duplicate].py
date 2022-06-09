# stackflow: Understanding Python super() with __init__() methods [duplicate]
# https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
class Base(object):
    def __init__(self):
        print ("Base created")

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()

ChildA()
ChildB()

#"What difference is there actually in this code?:"
'''
这段代码的主要区别是，在 ChildB 中，你在 __init__ 中得到了一层间接性，super 使用它所
定义的类来决定在 MRO 中查找下一个类的 __init__。

我在 "如何在 Python 中使用'super'？"这个经典问题的答案中说明了这一区别，它演示了依赖注
入和合作式多重继承。
'''
class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super().__init__()

'''
If Python didn't have super
Here's code that's actually closely equivalent to super 
(how it's implemented in C, minus some checking and fallback 
behavior, and translated to Python):
'''
class ChildB(Base):
    def __init__(self):
        mro = type(self).mro()
        check_next = mro.index(ChildB) + 1 # next after *this* class.
        while check_next < len(mro):
            next_class = mro[check_next]
            if '__init__' in next_class.__dict__:
                next_class.__init__(self)
                break
            check_next += 1

# Written a little more like native Python:
class ChildB(Base):
    def __init__(self):
        mro = type(self).mro()
        for next_class in mro[mro.index(ChildB) + 1:]: # slice to end
            if hasattr(next_class, '__init__'):
                next_class.__init__(self)
                break

'''
如果我们没有super对象，我们就不得不到处写这样的手工代码（或者重新创建！），以确保我们在方法
解析顺序中调用适当的下一个方法。

在Python 3中，super是如何做到这一点的，而不被明确告知它是从哪个类和实例中调用的方法？

它得到了调用的堆栈框架，并找到了类（隐含地存储为本地自由变量__class__，使调用的函数成为类
的闭包）和该函数的第一个参数，这应该是通知它使用哪个方法解析顺序（MRO）的实例或类。

由于它需要MRO的第一个参数，在静态方法中使用super是不可能的，因为它们不能访问它们被调用的类的MRO。

对其他答案的批评。
super()可以让你避免明确地引用基类，这很好。但主要的优势在于多重继承，在那里可以发生各种有趣的事情。
如果你还没有，请看关于super的标准文档。

这很容易让人误解，也没有告诉我们什么，但是super的意义不是为了避免写父类。
关键是要确保方法解析顺序（MRO）中的下一个方法被调用。这在多重继承中变得很重要。
'''
# Now remember, ChildB uses super, ChildA does not:
class Base(object):
    def __init__(self):
        print("Base init'ed")

class ChildA(Base):
    def __init__(self):
        print("ChildA init'ed")
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        print("ChildB init'ed")
        super().__init__()

# And let's create a dependency that we want to be called after the Child:
print("-----------UserA(),UserB()-----------------")

ChildA()
ChildB()
class UserDependency(Base):
    def __init__(self):
        print("UserDependency init'ed")
        super().__init__()

# Now remember, ChildB uses super, ChildA does not:
class UserA(ChildA, UserDependency):
    def __init__(self):
        print("UserA init'ed")
        super().__init__()

class UserB(ChildB, UserDependency):
    def __init__(self):
        print("UserB init'ed")
        super().__init__()
print("----------------------------------------")
UserA()
UserB()


class Polygon(object):
  def __init__(self, id):
      self.id = id


'''
解释一下。在super()中使用self.__class__替代类名会导致递归。
super让我们在MRO中查找子类的下一个父类（见本答案的第一部分）。
如果你告诉super我们在子实例的方法中，那么它就会查找下一个方法（可能是这个），
导致递归，可能会导致逻辑上的失败（在回答者的例子中，确实如此），
或者在超过递归深度时出现RuntimeError。
'''
class Rectangle(Polygon):
  def __init__(self, id, width, height):
     super(self.__class__, self).__init__(id)
     self.shape = (width, height)

class Square(Rectangle):
  pass

Square('a', 10, 10)