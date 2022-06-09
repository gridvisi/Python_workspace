'''
https://realpython.com/instance-class-and-static-methods-demystified/
Table of Contents

Instance, Class, and Static Methods — An Overview
Instance Methods
Class Methods
Static Methods
Let’s See Them In Action!
Delicious Pizza Factories With @classmethod
When To Use Static Methods
Key Takeaways
'''
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

'''
注意: 对于 Python 2 用户。从 Python 2.4 开始，@staticmethod 和 @classmethod 装饰器就可以使用了，这个例子可以正常使用。你可以选择用 class MyClass(object):语法来声明一个继承自 object 的新式类，而不是使用一个普通的类 MyClass:声明。除此之外，你就可以开始了。

实例方法
MyClass上的第一个方法，叫做method，是一个普通的实例方法。这是基本的，不加修饰的方法类型，你大多数时候都会用到。你可以看到这个方法只接受一个参数self，当方法被调用时，这个参数指向MyClass的一个实例（当然实例方法可以接受的参数不止一个）。

通过self参数，实例方法可以自由访问同一对象上的属性和其他方法。这使得它们在修改对象的状态时有很大的权力。

它们不仅可以修改对象状态，实例方法还可以通过self.__class__属性访问类本身。这意味着实例方法也可以修改类的状态。

类方法
我们来对比一下第二个方法，MyClass.classmethod。我用 @classmethod 装饰器标记了这个方法，以标志它是一个类方法。

类方法不接受self参数，而是接受一个cls参数，当方法被调用时，这个参数指向类而不是对象实例。

因为类方法只能访问这个 cls 参数，所以它不能修改对象实例的状态。那就需要访问self。然而，类方法仍然可以修改适用于类的所有实例的类状态。

静态方法
第三个方法，MyClass.staticmethod用@staticmethod装饰符标记为静态方法。

这种类型的方法既不接受self参数，也不接受cls参数（当然也可以自由接受任意数量的其他参数）。

因此静态方法既不能修改对象状态，也不能修改类状态。静态方法在访问数据方面受到限制--它们主要是一种命名空间方法的方式。

让我们来看看它们的实际应用吧
我知道到目前为止，我们的讨论都是相当理论化的。我相信你对这些方法类型在实践中的不同有一个直观的理解是很重要的。
我们现在就来看看一些具体的例子。

让我们来看看当我们调用这些方法时，这些方法在操作中是如何表现的。我们先创建一个类的实例，然后对其调用三种不同的方法。

MyClass的设置方式是，每个方法的实现都会返回一个包含信息的元组，以便我们跟踪正在发生的事情--以及该方法可以访问类或
对象的哪些部分。

下面是我们调用一个实例方法时发生的情况。

通过www.DeepL.com/Translator（免费版）翻译

NOTE: For Python 2 users: The @staticmethod and @classmethod decorators are available as of Python 2.4 and this example will work as is. Instead of using a plain class MyClass: declaration you might choose to declare a new-style class inheriting from object with the class MyClass(object): syntax. Other than that you’re good to go.

Instance Methods
The first method on MyClass, called method, is a regular instance method. That’s the basic, no-frills method type you’ll use most of the time. You can see the method takes one parameter, self, which points to an instance of MyClass when the method is called (but of course instance methods can accept more than just one parameter).

Through the self parameter, instance methods can freely access attributes and other methods on the same object. This gives them a lot of power when it comes to modifying an object’s state.

Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute. This means instance methods can also modify class state.

Class Methods
Let’s compare that to the second method, MyClass.classmethod. I marked this method with a @classmethod decorator to flag it as a class method.

Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.

Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.

Static Methods
The third method, MyClass.staticmethod was marked with a @staticmethod decorator to flag it as a static method.

This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).

Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.

Let’s See Them In Action!
I know this discussion has been fairly theoretical up to this point. And I believe it’s important that you develop an intuitive understanding for how these method types differ in practice. We’ll go over some concrete examples now.

Let’s take a look at how these methods behave in action when we call them. We’ll start by creating an instance of the class and then calling the three different methods on it.

MyClass was set up in such a way that each method’s implementation returns a tuple containing information for us to trace what’s going on — and which parts of the class or object the method can access.

Here’s what happens when we call an instance method:
'''
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

Pizza(['mozzarella', 'tomatoes'])
Pizza(['mozzarella', 'tomatoes', 'ham', 'mushrooms'])
Pizza(['mozzarella'] * 4)


def __init__(self, ingredients):
    self.ingredients = ingredients


def __repr__(self):
    return f'Pizza({self.ingredients!r})'

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

Pizza.margherita()
Pizza.prosciutto()

import math
class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

