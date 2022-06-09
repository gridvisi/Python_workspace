# 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。
# 对象：它是类的实例化。
# 方法：类中定义的函数。

# 类(Class) 由3个部分构成:
'''
类的名称:类名
类的属性:指对象的特征（一组数据）
类的方法:允许对象进行操作的方法 (行为/功能)
'''


# Python 3.x中取消了经典类，默认都是新式类。
# 新式类的语法 -> class 类名(object): pass

# 类对象支持两种操作：属性引用 和 实例化。
# 属性引用的语法：obj.属性
# 类实例化的语法：obj = 类名()
# 类中方法的调用：obj.方法名()


# 下面分析新式类的2种常见形式：

# 例1：
# 自定义一个类student
class student(object):
    def speak(self):  ## 哪个对象调用了这个方法，self就是那个对象；可以把self理解为一个形参
        print("%s 说：我今年%s岁" % (self.name, self.age))


# 类student 实例化一个对象john
john = student()
# 给对象添加属性
john.name = "约翰"
john.age = 19
# 调用类中的 speak()方法
john.speak()


# <<<约翰 说：我今年19岁


# 例2：
class student(object):
    # 定义构造方法
    def __init__(self, n, a):  # __init__() 是类的初始化方法；它在类的实例化操作后 会自动调用，不需要手动调用；
        # 设置属性
        self.name = n
        self.age = a

    # 定义普通方法
    def speak(self):
        print("%s 说：我今年%s岁" % (self.name, self.age))


# 类student 实例化一个对象john
john = student("约翰", 19)

# 调用类中的 speak()方法
john.speak()


# >>>约翰 说：我今年19岁

# 在python中使用__开头 并以__结尾的方法，称之为魔法方法；
# __init__(self) 是类的初始化方法，也称构造方法，是一种特殊的魔法方法。
# __init__(self)在实例化后，会自动调用，而不用手动调用，所以一般把属性设置在_init__()里。
# 常用到的魔法方法还有：__str__(self) 、 __del__(self)等。

## __str__(self)
class student(object):
    # 定义构造方法
    def __init__(self, n, a):
        # 设置属性
        self.name = n
        self.age = a

    # 输出一个字符串(追踪对象属性信息变化)
    def __str__(self):  # __str__(self)不可以添加参数(形参)
        return "名字：%s 年龄：%d" % (self.name, self.age)


# 实例化一个对象john
john = student("约翰", 19)

# 当使用print输出对象时，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
print(john)
# >>>名字：约翰 年龄：19


class Date(object):
   day = 0
   month = 0
   year = 0

   def __init__(self, year=0, month=0, day=0):
       self.day = day
       self.month = month
       self.year = year

   @classmethod
   def from_string(cls, date_as_string):
       year, month, day = date_as_string.split('-')
       date = cls(year, month, day)
       return date

   @staticmethod
   def is_date_valid(date_as_string):
       """
      用来校验日期的格式是否正确
       """
       year, month, day = date_as_string.split('-')
       return int(year) <= 3999 and int(month) <= 12 and int(day) <= 31

date1 = Date.from_string('2012-05-10')
print(date1.year, date1.month, date1.day)
is_date = Date.is_date_valid('2012-09-18') # 格式正确 返回True