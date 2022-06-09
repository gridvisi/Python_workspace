
'''
属性的访问限制
python中定义的普通变量，可以被外部访问。但是有时候，定义的变量不希望被外部访问。
python对属性权限的控制是通过属性名来实现的。如果一个属性由双下划线(__)开头，
该属性就无法被外部访问。如果外部需要访问这种变量，可以通过实例方法来访问，
在下文将会介绍如何访问。
'''

class Person(object):
    def __init__(self, name):
        self.name = name
        self._title = 'Mr'
        self.__job = 'Student'
p = Person('Bob')
print(p.name)    # => Bob
print(p._title)  # => Mr
#print(p.__job)
# => Error
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'Person' object has no attribute '__job'

'''
属性以"__xxx__"的形式定义的，是可以被外部访问的。它在python中称之为特殊属性。一般都是python内置的属性或者方法，一般我们定义属性和方法时不建议使用这种形式。
类属性
直接在类中创建的属性就叫类属性。
实例属性每个实例各自拥有，相互独立；而类属性有且只有1份，创建的实例都会继承自唯一的类属性。
意思就是绑定在一个实例上的属性不会影响到其它的实例。如果在类上绑定一个属性，那么所有的实例
都可以访问类属性，且访问的类属性是同一个，一旦类属性改变就会影响到所有的实例。
'''


class Person(object):
    address = 'Earth'  # 类属性address
    def __init__(self, name):
        self.name = name

print(Person.address)
  # => Earth  类属性直接绑定在类上的，可以不实例化直接通过类名调用类属性

p1 = Person('Bob')
p2 = Person('Alice')
print(p1.address  )
# => Earth   # 通过实例来调用类属性
print(p2.address )
# => Earth

'''
例：请给 Person 类添加一个类属性 count，每创建一个实例，count 属性就加 1，
这样就可以统计出一共创建了多少个 Person 的实例
'''


class Person(object):
    count = 0
    count += 1

    def __init__(self, name):
        self.name = name


p1 = Person('Bob')
print(Person.count)  # 1

p2 = Person('Alice')
print(Person.count)  # 1

p3 = Person('Tim')
print(Person.count)  # 1
#上述代码没有达到想要的效果。

class Person(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1


p1 = Person('Bob')
print(Person.count)  # 1

p2 = Person('Alice')
print(Person.count)  # 1

p3 = Person('Tim')
print(Person.count)  # 1
#上述代码达到想要的效果!!!

'''
__init__理解成是一个构造函数，构造函数外围的count=0理解成是一个默认参数，而在实例化对象的实现
最先调用的是构造函数，然后在第一次调用构造函数里面的count因为没有值就是使用默认参数，因此第一次
调用的count是0的默认值，然后第二次调用的时候是有参调用以此用的是有参的count。
count=0，是对最初的第一次赋值，只作用一次，往后每个对象都会使用改变后的count。
实例属性和类属性重名
当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问
'''


class Person(object):
    address = 'zhejiang'

    def __init__(self, name):
        self.name = name


p1 = Person('Bob')
p2 = Person('Alice')

print('Person.address = ' + Person.address)  # zhejiang

p1.address = 'shanxi'
print('p1.address = ' + p1.address)  # shanxi
print('Person.address = ' + Person.address)  # zhejiang
print('p2.address = ' + p2.address)  # zhejiang
'''
可见，千万不要在实例上修改类属性，它实际上并没有修改类属性，而是给实例绑定了一个实例属性。

定义实例方法
使用场景：一个实例的私有属性通过“__属性名”来定义，无法被外部所访问。但是可以从类的内部进行间
接访问，即通过实例方法来访问。
实例方法：在类中定义的函数，第一个参数是self，指向调用该方法的实例本身。
'''

class Person(object):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

#get_name就是一个实例方法。调用实例方法必须在实例上调用

p1 = Person('xiaoming')
p1.get_name()  # xiaoming
#在实例方法内部，可以访问所有实例属性，如果外部需要访问私有属性，可以通过方法调用获得。
#类方法在class中定义的全部是实例方法，实例方法第一个参数self是实例本身。

class Person(object):
    count = 0

    @classmethod
    def how_many(cls):
        return cls.count

    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1


print('Person.how_many:',Person.how_many())
p1 = Person('Bob')
print('Person.how_many Bob:',Person.how_many())


@classmethod
def how_many(cls):
    return cls.count

def __init__(self, name):
    self.name = name
    Person.count = Person.count + 1

print(Person.how_many())
p1 = Person('Bob')
print(Person.how_many())

#通过标记一个 @ classmethod，该方法将绑定到Person类上，而非类的实例。类方法的第一个参数传入的是类本身，
# 上面的cls.count相当于Person.count。因为在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，
# 只能获得类的引用。类方法是通过类来直接调用的，或者通过实例直接来调用。

class Person(object):
    count = 0

    @classmethod
    def how_many(cls):
        return cls.count

    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1

mcree = Person
mcree.count = 0
student = Person('larry')
print(student.how_many())

student = Person('lucy')
print(student.how_many())

student = Person('lucy')
print(student.how_many())
print('mcree:',mcree.count,mcree.how_many())


#12、阅读下面的程序，判断其是否可以正常运行，如果可以运行则写出执行结果，如果不能运行则写出理由。
class Test:
    def init(self, value):
        self.__value__ = value

    @property
    def value(self):
        return self.__value


t = Test
t.value = 5
print(t.value)
#t = Test(3)
#t.value = 5