#https://stackoverflow.com/questions/68645/are-static-class-variables-possible-in-python

class MyClass:
  i = 3

print(MyClass.i)
#3

m = MyClass()
m.i = 4
print(MyClass.i, m.i)
#(3, 4)

#3
class Test():
    i = 3
t = Test.i
print('Test t:',Test.i)

j = Test()
for i in range(10):
    j.i += i
print(j.i)

print(Test.__dict__)
print(j.__dict__)

'''
注意到当属性i被直接设置在t上时，实例变量t.i是如何与 "静态 "类变量不同步的。
这是因为i被重新绑定在t命名空间中，而这个命名空间与Test命名空间不同。如果你
想改变一个 "静态 "变量的值，你必须在它最初定义的范围（或对象）内改变它。
我给 "静态 "加了引号，因为 Python 并没有像 C++ 和 Java 那样真正有静态变量。

尽管它没有说任何关于静态变量或方法的具体内容，但 Python 教程中有一些关于类和
类对象的相关信息。

@Steve Johnson也回答了关于静态方法的问题，在Python库参考中的 "内置函数 "下
也有记载。
'''
class Test(object):
    i = 3 # class (or static) variable
    @classmethod
    def g(cls, arg):
        # here we can use 'cls' instead of the class name (Test)
        if arg > cls.i:
            cls.i = arg # would be the same as Test.i = arg1


class Test(object):

    # regular instance method:
    def MyMethod(self):
        pass

    # class method:
    @classmethod
    def MyClassMethod(klass):
        pass

    # static method:
    @staticmethod
    def MyStaticMethod():
        pass

'''
静态和类方法
正如其他答案所指出的，静态方法和类方法可以通过内置的装饰器轻松实现。

class Test(object):

    # 常规的实例方法。
    def MyMethod(self):
        传递

    # 类方法。
    @classmethod
    def MyClassMethod(klass):
        通过

    # 静态方法。
    @staticmethod
    def MyStaticMethod():
        通过
像往常一样，MyMethod()的第一个参数被绑定到类的实例对象。
相反，MyClassMethod()的第一个参数与类对象本身绑定
（例如，在本例中，Test）。对于MyStaticMethod()，
没有一个参数是被绑定的，而且拥有参数是可选的。

"静态变量"
然而，实现 "静态变量"（好吧，反正是可变的静态变量，如果
这不是自相矛盾的话......）并不是那么简单的。正如 millerdev 
在他的回答中指出的，问题在于 Python 的类属性不是真正的 
"静态变量"。考虑一下。
'''

class Test(object):
    i = 3  # This is a class attribute

x = Test()
x.i = 12   # Attempt to change the value of the class attribute using x instance
print('x.i,Test.i:',x.i,Test.i)
#assert x.i == Test.i  # ERROR
assert Test.i == 3    # Test.i was not affected
assert x.i == 12      # x.i is a different object than Test.i

# how to correct above:
class Test(object):

    _i = 3

    @property
    def i(self):
        return type(self)._i

    @i.setter
    def i(self,val):
        type(self)._i = val

## ALTERNATIVE IMPLEMENTATION - FUNCTIONALLY EQUIVALENT TO ABOVE ##
## (except with separate methods for getting and setting i) ##

class Test(object):

    _i = 3

    def get_i(self):
        return type(self)._i

    def set_i(self,val):
        type(self)._i = val

    i = property(get_i, set_i)

x1 = Test()
x2 = Test()
x1.i = 50
assert x2.i == x1.i  # no error
assert x2.i == 50    # the property is synced


#Immutable "Static Variables"
class Test(object):

    _i = 3

    @property
    def i(self):
        return type(self)._i

## ALTERNATIVE IMPLEMENTATION - FUNCTIONALLY EQUIVALENT TO ABOVE ##
## (except with separate methods for getting i) ##

class Test(object):

    _i = 3
    @property  #TypeError: 'property' object is not callable
    def get_i(self):
        return type(self)._i

    i = property(get_i)
#Now attempting to set the instance i attribute will return an AttributeError:

x = Test()
assert x.i == 3  # success
x.i = 12         # ERROR

x = Test()
assert x.i == Test.i  # ERROR

# x.i and Test.i are two different objects:
type(Test.i)  # class 'property'
type(x.i)     # class 'int'
'''
assert Test.i == x.i这一行产生了一个错误，因为Test和x的i属性是两个不同的对象。

很多人都会觉得这很奇怪。然而，它不应该是这样的。如果我们回去检查我们的Test类定义（第二个版本），我们会注意到这一行。

    i = property(get_i) 
显然，Test的成员i必须是一个属性对象，这是从属性函数返回的对象类型。

如果你觉得上述内容令人困惑，你很可能还在从其他语言（如Java或C++）的角度考虑问题。你应该去研究属性对象，关于Python属性的返回顺序，描述符协议，以及方法解析顺序（MRO）。

我在下面提出了一个解决上述 "问题 "的方法；但是我强烈建议--至少在你彻底理解为什么 assert Test.i = x.i 会导致错误之前，你不要尝试做类似下面的事情。
'''