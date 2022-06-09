

print('---------------Python类的定义和使用-------------------')
class Ticket():
    def __init__(self,checi,fstation,tstation,fdate,ftime,ttime):
        self.checi=checi
        self.fstation=fstation
        self.tstation=tstation
        self.fdate=fdate
        self.ftime=ftime
        self.ttime=ttime
    def printinfo(self):
        print("车次：",self.checi)
        print("出发站：", self.fstation)
        print("到达站：", self.tstation)
        print("出发时间：", self.fdate)

#创建a1对象
a1 = Ticket("G11","xian","beijing",'2019-01-20','13:00','18:00')
#创建a2对象
a2=Ticket("T11","xian","beijing",'2019-01-21','13:00','19:00')
print(a1.printinfo(),a2.printinfo())

'''
python类class中_init_函数以及参数self的简单解释:
https://blog.csdn.net/LY_ysys629/article/details/54893185?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param
'''
class person():
    def __init__(self,name,gender,birth,**kw):
        self.name=name
        self.gender=gender
        self.birth=birth
        for k,w in kw.items():
            setattr(self,k,w)
    def sayhi(self):
        print('my name is',self.name)
xiaoming = person('Xiao Ming', 'Male', '1991-1-1',job='student',tel='18089355',stdid='15010')
xiaohong = person('Xiao Hong', 'Female', '1992-2-2')
print(xiaoming.name)
print(xiaohong.birth)
print(xiaoming.job)
print(xiaoming.tel)
print(xiaoming.stdid)
print(xiaoming.sayhi())

print('-----------def __init__(self, name等多参数)---------------')
#https://blog.csdn.net/m0_37693335/article/details/82972925?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param
class Student:
    def __init__(self):#两者之间的区别
        self.name = None
        self.score = None
    def __init__(self, name, score):
        self.name = name
        self.score = score

# student = Student("sansan", 90)
student = Student("sansan", 90)
student.name = 'susan'
student.score = 90
print('实例方法一：',student.name,student.score)
#print('实例方法二：',susan.name,susan.score)

# susan = Student("sunny", 78)
susan = Student("sunny", 78)
susan.name = "sunny"
susan.score = 8
print('实例方法二：',susan.name,susan.score)

'''
即显示了两种实例化的方法， 注释的部分即是在创建的时候就直接传入参数
那么这两者的区别，在哪里？
第一种的区别，他定义了这样一种类，他可以是一个空的结构，比如学生的表，当学生还没有进行考试时，他已经有了学生的姓名和成绩，当新的数据来的时候，可以直接添加进来。这个可以很方便的进行，
而第二种，则需要必须传值，不允许为空。当然第二种对于已有数据的导入是很方便的，在语句上减少了很多
'''


class Student:
    def __init__(self):  # 两者之间的区别
        self.name = None
        self.score = None

    # def __init__(self, name, score):
    #     self.name = name
    #     self.score = score

    def print_score(self):
        print("%s score is %s" % (self.name, self.score))

    def get_grade(self):
        if self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        else:
            return "C"


# student = Student("sansan", 90)
student = Student()
student.name = "sansan"
student.score = 90

# susan = Student("sunny", 78)
susan = Student()
susan.name = "susan"
susan.score = 8

student.print_score()
susan.print_score()
print(susan.get_grade())
print(student.get_grade())


print('-----------function differ with class ---------------')
#https://blog.csdn.net/brucewong0516/article/details/79124550?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param

'''
若一个function为螺丝刀 或者 扳手 或者 锯子……那么 一个class可能是一个工程师培训方案当你使用function时
你必须要清楚各个流程与functions之间的来龙去脉，然后拼装它们当你使用class时，先用这套方案培训出一个instance，
在此可以比作工作人员，然后你只需要给工作人员下达更抽象的目标命令，工作人员就会按照方案(class)来执行。
class设计要比function困难很多，但是设计完毕，实施要比function简单很多。function对过程打包，class对过程分类

作者：郭林
链接：https://www.zhihu.com/question/53644787/answer/135886199
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


优点：可以保存状态缺点：可以保存状态解释：如果不能保存状态，那么每次调用函数时，你都不得不
把相关信息通过参数传递过来，麻烦并且在参数多时容易出错。当一个东西包含状态，意味着很多操作会带有修改
其内部状态的副作用。当项目管理不善时，某些对象的内部状态可能多且关系错综复杂，会给维护和调试带来极大的复杂度。
也就是稍微改一下，很多东西就出奇怪的问题。另一方面，将逻辑、算法与状态绑定，会使其不够灵活。比如用着用着，
你有多种状态都需要同一种处理逻辑，这时候再把逻辑和算法从类里抽出来就麻烦了。当然也有纯数据的不可变的类，
比如各种 named tuple、datetime 之类的（函数本身就是个类）。函数里也可以通过操作闭包或者全局变量来保存状态。
我只是说普通用户所遇到的大部分情况。推荐策略：举棋不定时听 pylint 的话。

作者：依云
链接：https://www.zhihu.com/question/53644787/answer/135871000
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


# startup Class
class FooBar:
    def __init__(self):
        self.somevar = 42
f = FooBar()
print(f.somevar)

class FooBar:
    def __init__(self,value=42):
        self.somevar = value
f = FooBar("this is a constructor argument")
print(f.somevar)

print('-----------两种实例化的方法---------------')
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

#case_2

class Calculator:
#名字和价格是属性
    name="jisuanqi"
    price=28
    #定义的四个函数是功能
    def add(self,x,y):
        print(self.name)#这里指的是函数的属性-名字
        result=x+y
        print(result)
    def subtract(self,x,y):
        print(x-y)
    def multiply(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)

calc=Calculator()
print(calc.name)#jisuanqi
print(calc.price)#28
print(calc.add(1,2))#3
print(calc.subtract(10,2))#8