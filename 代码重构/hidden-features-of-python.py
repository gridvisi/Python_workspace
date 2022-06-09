'''
https://stackoverflow.com/questions/101268/hidden-features-of-python


Quick links to answers:
Argument Unpacking
Braces
Chaining Comparison Operators
Decorators
Default Argument Gotchas / Dangers of Mutable Default arguments
Descriptors
Dictionary default .get value
Docstring Tests
Ellipsis Slicing Syntax
Enumeration
For/else
Function as iter() argument
Generator expressions
import this
In Place Value Swapping
List stepping
__missing__ items
Multi-line Regex
Named string formatting
Nested list/generator comprehensions
New types at runtime
.pth files
ROT13 Encoding
Regex Debugging
Sending to Generators
Tab Completion in Interactive Interpreter
Ternary Expression
try/except/else
Unpacking+print() function
with statement

'''



# Function argument unpacking
#You can unpack a list or a dictionary as function arguments using * and **.
#For example:
def draw_point(x, y):
    return x**2 + y**2

point_foo = (3, 4)
point_bar = {'y': 3, 'x': 2}

draw_point(*point_foo)
print(draw_point(**point_bar))

'''
描述符
它们是一大堆 Python 核心功能背后的魔法。

当你使用点状访问来查找一个成员 (例如，x.y)，Python 首先在实例字典中查找这个成员。
如果没有找到，它就在类的字典中寻找它。如果在类的字典中找到它，并且对象实现了描述符协议，
Python 将执行它，而不是仅仅返回它。一个描述符是任何实现了 
__get__, __set__, 或 __delete__ 方法的类。

下面是你如何使用描述符来实现你自己的 (只读) 属性版本。

class Property(object):
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, obj, type):
        if obj is None:
            return self
        return self.fget(obj)
and you'd use it just like the built-in property():

class MyClass(object):
    @Property
    def foo(self):
        return "Foo!"
你可以像使用内置的property()一样使用它。


描述符在 Python 中被用来实现属性、绑定方法、静态方法、类方法和槽，以及其他一些东西。
对它们的理解使我们很容易看到为什么很多以前看起来像Python的 "怪癖 "的东西会变成这样。

Raymond Hettinger 有一个很好的教程，对它们的描述比我要好得多。
'''


class Property(object):
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, obj, type):
        if obj is None:
            return self
        return self.fget(obj)

#and you'd use it just like the built-in property():

class MyClass(object):
    @Property
    def foo(self):
        return "Foo!"