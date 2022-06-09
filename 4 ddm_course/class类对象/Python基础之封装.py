'''
　一、什么是封装
　　在程序设计中，封装（Encapsulation）是对具体对象的一种抽象，即将某些部分隐藏起来，在程序外部看不到，其

含义是其他程序无法调用。

　　要了解封装，离不开“私有化”，就是将类或者是函数中的某些属性限制在某个区域之内，外部无法调用。

　　二、为什么要封装
　　封装数据的主要原因是：保护隐私（把不想别人知道的东西封装起来）

　　封装方法的主要原因是：隔离复杂度（比如：电视机，我们看见的就是一个黑匣子，其实里面有很多电器元件，对于

用户来说，我们不需要清楚里面都有些元件，电视机把那些电器元件封装在黑匣子里，提供给用户的只是几个按钮接口，

通过按钮就能实现对电视机的操作。）

　　提示：在编程语言里，对外提供的接口（接口可理解为了一个入口），就是函数，称为接口函数，这与接口的概念还

不一样，接口代表一组接口函数的集合体。

　　三、封装分为两个层面
　　封装其实分为两个层面，但无论哪种层面的封装，都要对外界提供好访问你内部隐藏内容的接口（接口可以理解为入

口，有了这个入口，使用者无需且不能够直接访问到内部隐藏的细节，只能走接口，并且我们可以在接口的实现上附加更

多的处理逻辑，从而严格控制使用者的访问）

　　第一个层面的封装（什么都不用做）：创建类和对象会分别创建二者的名称空间，我们只能用类名.或者obj.的方式去

访问里面的名字，这本身就是一种封装。
'''


'''
注意：对于这一层面的封装（隐藏），类名.和实例名.就是访问隐藏属性的接口
第二个层面的封装：类中把某些属性和方法隐藏起来(或者说定义成私有的)，只在类的内部使用、外部无法访问，或
者留下少量接口（函数）供外部访问。
Python中私有化的方法也比较简单，即在准备私有化的属性（包括方法、数据）名字前面加两个下划线即可。
类中所有双下划线开头的名称如__x都会自动变形成：_类名__x的形式：
'''
class A:
    __N=0
    #类的数据属性就应该是共享的,但是语法上是可以把类的数据属性设置成私有的如__N,会变形为_A__N

    def __init__(self):
        self.__X=10 #变形为self._A__X
    def __foo(self): #变形为_A__foo
        print('from A')
    def bar(self):
        self.__foo() #只有在类内部才可以通过__foo的形式访问到.　

'''
　这种自动变形的特点：

　　　　1、类中定义的__x只能在内部使用，如self.__x，引用的就是变形的结果。

　　　　2、这种变形其实正是针对外部的变形，在外部是无法通过__x这个名字访问到的。

　　　　3、在子类定义的__x不会覆盖在父类定义的__x，因为子类中变形成了：_子类名__x,而父类中变形成了：_父

类名__x，即双下滑线开头的属性在继承给子类时，子类是无法覆盖的。

　　注意：对于这一层面的封装（隐藏），我们需要在类中定义一个函数（接口函数）在它内部访问被隐藏的属性，然后

外部就可以使用了

　　这种变形需要注意的问题是：

　　1、这种机制也并没有真正意义上限制我们从外部直接访问属性，知道了类名和属性名就可以拼出名字：_类名__属

性，然后就可以访问了，如a._A__N
'''

a = A()
print("2 ---------输出结果----------")
print(a._A__N)
print(a._A__X)
print(A._A__N)

# 2、变形的过程只在类的定义是发生一次,在定义后的赋值操作，不会变形
a = A() #实例化对象a
print(a.__dict__) #打印变形的内容
a.__Y = 20 #新增Y的值，此时加__不会变形
print(a.__dict__) #打印变形的内容
print("2 ---------输出结果----------")

# 3、在继承中，父类如果不想让子类覆盖自己的方法，可以将方法定义为私有的
class A:  # 这是正常情况
    def fa(self):
        print("from A")

    def test(self):
        self.fa()

class B(A):
    def fa(self):
        print("from B")

b = B()
b.test()

#fa被定义成私有的情况：

class A:  # 把fa定义成私有的，即__fa
    def __fa(self):  # 在定义时就变形为_A__fa
        print("from A")

    def test(self):
        self.__fa()  # 只会与自己所在的类为准,即调用_A__fa


class B(A):
    def __fa(self):  # b调用的是test，跟这个没关系
        print("from B")

print("3 -------输出结果 - --------")
#from A
b = B()
b.test()


'''

　四、特性（property）
　　1、什么是特性property

　　property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值（就是一个装饰器）
　　注意：被property装饰的属性会优先于对象的属性被使用，而被propery装饰的属性,分成三种：
property、被装饰的函数名.setter、被装饰的函数名.deleter（都是以装饰器的形式）。

'''
print("property: -------输出结果 - --------")
class room:  # 定义一个房间的类
    def __init__(self, length, width, high):
        self.length = length  # 房间的长
        self.width = width  # 房间的宽
        self.high = high  # 房间的高

    @property
    def area(self):  # 求房间的平方的功能
        return self.length * self.width  # 房间的面积就是：长x宽

    @property
    def perimeter(self):  # 求房间的周长的功能
        return 2 * (self.length + self.width)  # 公式为：（长 + 宽）x 2

    @property
    def volume(self):  # 求房间的体积的功能
        return self.length * self.width * self.high  # 公式为：长 x 宽 x 高


r1 = room(2, 3, 4)  # 实例化一个对象r1
print("r1.area：", r1.area)  # 可以像访问数据属性一样去访问area,会触发一个函数的执行,动态计算出一个值
print("r1.perimeter：", r1.perimeter)  # 同上，就不用像调用绑定方法一样，还得加括号，才能运行
print("r1.volume：", r1.volume)  # 同上，就像是把运算过程封装到一个函数内部，我们不管过程，只要有结果就行
#------------输出结果 - --------------
'''
print(r1.area)  #： 6
print(r1.perimeter) #： 10
print(r1.volume)  #： 24
'''

'''
2、为什么要用property
将一个类的函数定义成特性以后，对象再去使用的时候obj.name,根本无法察觉自己的name是执行了一个函数然后
计算出来的，这种特性的使用方式遵循了统一访问的原则。
'''

class people:  # 定义一个人的类
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex  # p1.sex = "male",遇到property，优先用property

    @property  # 查看sex的值
    def sex(self):
        return self.__sex  # 返回正真存值的地方

    @sex.setter  # 修改sex的值
    def sex(self, value):
        if not isinstance(value, str):  # 在设定值之前进行类型检查
            raise TypeError("性别必须是字符串类型")  # 不是str类型时，主动抛出异常
        self.__sex = value  # 类型正确的时候，直接修改__sex的值，这是值正真存放的地方
        # 这里sex前加"__",对sex变形，隐藏。

    @sex.deleter  # 删除sex
    def sex(self):
        del self.__sex


p1 = people("egon", "male")  # 实例化对象p1
print('# 查看p1的sex，此时要注意self.sex的优先级:',p1.sex)
# 查看p1的sex，此时要注意self.sex的优先级

p1.sex = "female"  # 修改sex的值
print('查看修改后p1的sex:',p1.sex)  # 查看修改后p1的sex

print('查看p1的名称空间，此时里面有sex:',p1.__dict__)  # 查看p1的名称空间，此时里面有sex
#{'name': 'egon', '_people__sex': 'female'}

del p1.sex  # 删除p1的sex
print(p1.__dict__)  # 查看p1的名称空间，此时发现里面已经没有sex了
#{'name': 'egon'}
#-------输出结果 - ----------
#male
#female
#{'name': 'egon', '_people__sex': 'female'}
#{'name': 'egon'}


'''
python并没有在语法上把它们三个内建到自己的class机制中，在C++里一般会将所有的所有的
数据都设置为私有的，然后提供set和get方法（接口）去设置和获取，在python中通过property
方法可以实现。

五、封装与扩展性
封装在于明确区分内外，使得类实现者可以修改封装内的东西而不影响外部调用者的代码；而外部使
用用者只知道一个接口(函数)，只要接口（函数）名、参数不变，使用者的代码永远无需改变。这就
提供一个良好的合作基础——或者说，只要接口这个基础约定不变，则代码改变不足为虑。 

'''
#类的设计者
class room: #定义一个房间的类
    def __init__(self,name,owner,length,width,high):
        self.name = name
        self.owner = owner
        self.__length = length #房间的长
        self.__width = width #房间的宽
        self.__high = high #房间的高
    @property
    def area(self): #求房间的平方的功能
        return self.__length * self.__width #对外提供的接口，隐藏了内部的实现细节，\
                                            # 此时我们想求的是房间的面积就是：长x宽

#实例化对象通过接口，调用相关属性得到想要的值：


#类的使用者
r1 = room("客厅","michael",20,30,9) #实例化一个对象r1
print("area : ---------输出结果-----------")
print(r1.area) #通过接口使用（area），使用者得到了客厅的面积
print("area + volumn: ---------输出结果-----------")
#600 #得到了客厅的面积

#　　扩展原有的代码，使功能增加：

#类的设计者，轻松的扩展了功能，而类的使用者完全不需要改变自己的代码
class room: #定义一个房间的类
    def __init__(self,name,owner,length,width,high):
        self.name = name #房间名
        self.owner = owner #房子的主人
        self.__length = length #房间的长
        self.__width = width #房间的宽
        self.__high = high #房间的高
    @property
    def area(self): #对外提供的接口，隐藏内部实现
        return self.__length * self.__width,\
               self.__length * self.__width * self.__high
        # 此时我们增加了求体积,
        # 内部逻辑变了,只需增加这行代码就能简单实现,而且外部调用感知不到,仍然使
        # 用该方法，但是功能已经增加了

#对于类的使用者，仍然在调用area接口的人来说，根本无需改动自己的代码，就可以用上新功能：

#类的使用者
r1 = room("客厅","michael",20,30,9) #实例化一个对象r1
print(r1.area)

#通过接口使用（area），使用者得到了客厅的面积
#--------------输出结果---------------
#(600, 5400) #得到了新增的功能的值