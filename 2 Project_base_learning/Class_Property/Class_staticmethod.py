import time

class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():  # 用Date.now()的形式去产生实例,该实例用的是当前时间
        t = time.localtime()  # 获取结构化的时间格式
        return Date(t.tm_year, t.tm_mon, t.tm_mday)  # 新建实例并且返回

    @staticmethod
    def tomorrow():  # 用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


a = Date('1987', 11, 27)  # 自己定义时间
b = Date.now()  # 采用当前时间
c = Date.tomorrow()  # 采用明天的时间

print(a.year, a.month, a.day)
print(b.year, b.month, b.day)
print(c.year, c.month, c.day)

'''
@staticmethod
通常情况下，在类中定义的所有函数（注意了，这里说的就是所有，跟self啥的没关系，
self也只是一个再普通不过的参数而已）都是对象的绑定方法，对象在调用绑定方法时
会自动将自己作为参数传递给方法的第一个参数。除此之外还有两种常见的方法：
静态方法和类方法，二者是为类量身定制的，但是实例非要使用，也不会报错。
是一种普通函数，位于类定义的命名空间中，不会对任何实例类型进行操作，
python为我们内置了函数staticmethod来把类中的函数定义成静态方法

@classmethod
类方法是给类用的，类在使用时会将类本身当做参数传给类方法的第一个参数，
python为我们内置了函数classmethod来把类中的函数定义成类方法
'''

class A:

    x=1

    @classmethod
    def test(cls):
        print(cls, cls.x)

class B(A):
    x=2

B.test()

# 以上应用场景
import time

class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


class EuroDate(Date):
    def __str__(self):
        return 'year:%s month:%s day:%s' % (self.year, self.month, self.day)

e = EuroDate.now()
print(e)  # 我们的意图是想触发EuroDate.__str__,但是结果为

#以上修改为

class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # @staticmethod
    # def now():
    #     t=time.localtime()
    #     return Date(t.tm_year,t.tm_mon,t.tm_mday)

    @classmethod  # 改成类方法
    def now(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)  # 哪个类来调用,即用哪个类cls来实例化


class EuroDate(Date):

    def __str__(self):
        return 'year:%s month:%s day:%s' % (self.year, self.month, self.day)


e = EuroDate.now()
print(e)  # 我们的意图是想触发EuroDate.__str__,此时e就是由EuroDate产生的,所以会如我们所愿

# time
t = time.localtime()
print(t.tm_year, t.tm_mon, t.tm_mday)

#
#__str__定义在类内部，必须返回一个字符串类型，
#什么时候会出发它的执行呢？打印由这个类产生的对象时，会触发执行

class People:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return '<name:%s,age:%s>' %(self.name,self.age)

p1=People('egon',18)
print(p1)
print(str(p1))
