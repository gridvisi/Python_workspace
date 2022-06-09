# https://blog.csdn.net/xrinosvip/article/details/89647884

'''
https://www.codewars.com/kata/55ddb0ea5a133623b6000043/train/python

class MyClass:
    pass

myObject = MyClass();
test.assert_equals(MyClass.__name__, "MyClass")

class_name_changer(MyClass, "UsefulClass");
test.assert_equals(MyClass.__name__, "UsefulClass")

class_name_changer(MyClass, "SecondUsefulClass");
test.assert_equals(MyClass.__name__, "SecondUsefulClass")
'''
class Myclass:
    def __init__(self, name):
        self.name = "Myclass"
user = Myclass('your name')
print(user.name)

class cls:
    def __init__(self, name,age):
        self.name = name
        self.age = age

peer = cls
peer.name = 'eric'
print(peer.name)


#1st solution
def class_name_changer(cls, new_name):
    assert new_name[0].isupper() and new_name.isalnum()
    cls.__name__ = new_name
    peer = cls
    return peer
#cls = Myclass
#print(cls.name)
new_name = "SecondUsefulClass"
print('cls:',class_name_changer(cls, new_name))

SecondUsefulClass = cls
SecondUsefulClass.age = '17'
print('SecondUsefulClass_name:',SecondUsefulClass.name)  #继承了name的值
print('SecondUsefulClass_age:',SecondUsefulClass.age)
'''
在Python类中规定，函数的第一个参数是实例对象本身，并且约定俗成，把其名字写为self。
其作用相当于java中的this，表示当前类的对象，可以调用当前类中的属性和方法。

class是面向对象的设计思想，instance（也即是 object，对象）是根据 class 创建的
一个类（class）应该包含 数据 和 操作数据的方法，通俗来讲就是 属性 和 函数（即调用方法）

类 class 中为啥用使用 self ？
在类的代码（函数）中，需要访问当前的实例中的变量和函数，即，访问Instance中的：
对应的变量（property)：Instance.ProperyNam，去读取之前的值和写入新的值
调用对应函数（function）：Instance.function()，即执行对应的动作
-> 而需要访问实例的变量和调用实例的函数，当然需要对应的实例Instance对象本身
-> 而Python中就规定好了，函数的第一个参数，就必须是实例对象本身，并且建议，约定俗成，把其名字写为self
-> 所以，我们需要self（需要用到self）
首先，在Python中类的定义：

在python中，类是通过关键字 class 定义的：
class 后面紧跟 类名，即 Person，类名通常大写字母开头，紧接着是(object),表示该类是从哪个类继承下来的，
通常，如果没有合适的 继承类，就使用 object 类，这是所有类最终都会 继承的类
'''


class Person(object):
    pass

#将 Person类实例化，创建实例化是通过 类名+() 实现的

class Person(object):
    pass
student = Person()    # 创建类的实例化
print(student)

'''
可以看到，变量 student指向的就是一个 Person的 object，后面的  0x0000026EE434D8D0 
是内存地址，每个 object 的地址都不一样，而 Person 本身则是一个 类
也可以给实例变量绑定属性，比如：为 student 绑定  name 和 score 属性
'''


class Person(object):
    pass
student = Person()
# print(student)
# print(Person)
student.name = "Gavin"     # 为实例变量 student 绑定 name 属性   类似于 赋值 操作
student.score = 100        # 为 其绑定  score 属性
print(student.name)
print(student.score)


class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
# 传入空参数的情况，会报错：
student = Person('mcree',100)  # 此处应该有参数传入，却没有传
print(student.name)
print(student.score)

'''
注意：

1、__init__ 方法的第一个参数永远是 self ，表示创建的实例本身，因此，在 __init__ 方法的内部，就可以把
各种属性绑定到 self，因为 self 就指向创建的 实例本身

2、使用了 __init__ 方法，在创建实例的时候就不能传入 空的参数了，必须传入与 __init__ 方法匹配的参数，
但是 self 不需要传，python解释器会自己把实例变量传进去

在类中定义多个函数相互调用
'''


class Person(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        sum = self.x + self.y
        return sum

    def square(self):
        squr = pow(self.x, 2) + pow(self.y, 2)
        return squr

    def add_square(self):
        c = self.add() + self.square()
        return c


student = Person(3, 4)
print(student.add())
print(student.square())
print('--------- 我是可爱的分割线-----------')
print(student.add_square())

'''
通过上述的例子可以看出，与普通的函数相比，在类中定义的函数只有两点点不同：

1、第一个参数永远是 self ，并且调用时不用传递该参数

2、在类中函数相互调用要加 self ，如上例中： c = self.add()+self.square(), 
不加 self ，会报错： 函数未定义，看下图
除此之外，类的方法和普通函数没甚区别，当然也可以使用 默认参数、可变参数和关键字参数，例子如下
'''


class Person(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, z=16):  # 设置 默认变量 z =16,这只是个普通的局部变量，非实例变量，实例变量需要 self.z = z,这样定义
        sum = self.x + self.y + z
        return sum

    def square(self):
        squr = pow(self.x, 2) + pow(self.y, 2)
        return squr

    def add_square(self, z):  # 调用时传入变量，这也是个普通的局部变量，非实例变量
        c = self.add() + self.square() + z
        return c


student = Person(3, 4)
print(student.add())
print(student.square())
print('--------- 我是可爱的分割线-----------')
print(student.add_square(16))

'''
看了上述的例子可能还是不明白 self 到底是个什么鬼，为啥要使用self这鬼东西 ？，没关系，往下看

其实 self 这家伙简单的说就是把 class 中 定义的 变量和函数 变成 实例变量和实例函数，作为类 class 的成员，
使得成员间能互相调用，而不需要从外部调用 数据（即变量）和 方法（即 函数），以实现数据的封装，
以上面的 Person 类为例：

创建实例的时候需要给出实例变量 x,y, 调用函数时给出 z ，调用很容易，却不知道内部实现的细节 

总之，类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都相互独立、互不影响；
方法是与实例绑定的函数，和普通的函数不同，方法可以直接访问实例的数据

其实 self 中存储的是 实例变量 和 实例函数 的属性，可以理解为一个字典（ dict ），
如：{'name':'zhang','age':'18'}就是这些。

注意只有数据属性，并没有创建新的类的方法。  类----->通过实例化生成----对象---->（对象只是一串类似于字典的数据，
没有把类的里的方法复制给你，python没有new这个方法！）

通过这个例子可以看出， z 本来是 add() 函数的默认形参，通过将其实例化，就可以在其他函数体内调用 实例变量 z 
被实例化以后，就可以利用实例化的方法访问它
那么 self 到底是什么？

'''


class Box(object):
    def __init__(self, boxname, size, color):
        self.boxname = boxname
        self.size = size
        self.color = color  # self就是用于存储对象属性的集合，就算没有属性self也是必备的

    def open(self, myself):
        print('-->用自己的myself，打开那个%s,%s的%s' % (myself.color, myself.size, myself.boxname))
        print('-->用类自己的self，打开那个%s,%s的%s' % (self.color, self.size, self.boxname))

    def close(self):
        print('-->关闭%s，谢谢' % self.boxname)


b = Box('魔盒', '14m', '红色')
b.close()
b.open(b)  # 本来就会自动传一个self，现在传入b，就会让open多得到一个实例对象本身，print看看是什么。
print(b.__dict__)  # 这里返回的就是self本身，self存储属性，没有动作。

'''
self代表类的实例，而非类；self 就是 对象/实例 属性集合

Box 是个类-----》self 实例化------》 b对象/ 实例

class 抽象体------》实例化------》对象/实例，
含有属性：{'boxname':'魔盒', ‘size’：‘14m’, 'color':'red'}，即 self

self 看似是整个对象，实际上清楚地描述了类就是产生对象的过程，描述了 self 就是得到了 对象，
所以 self 内的键值可以直接使用

正如自然界中一个有效的对象，必须包括：
1、描述对象的属性；2、对象的方法

所以 self是必须的，也是对象中重要的特性
'''


class Box(object):
    def myInit(mySelf, boxname, size, color):
        mySelf.boxname = boxname
        mySelf.size = size
        mySelf.color = color  # 自己写一个初始化函数，一样奏效,甚至不用self命名。其它函数当中用标准self
        return mySelf  # 返回给实例化过程一个对象！神奇！并且含有对象属性/字典

    # def __init__(self, boxname, size, color):
    #     self.boxname = boxname
    #     self.size = size
    #     self.color = color  #注释掉原来标准的初始化

    def open(self, myself):
        print(self)
        print('-->用自己的myself，打开那个%s,%s的%s' % (myself.color, myself.size, myself.boxname))
        print('-->用类自己的self，打开那个%s,%s的%s' % (myself.color, myself.size, myself.boxname))

    def close(self):
        print('-->关闭%s，谢谢' % self.boxname)


# 经过改造，运行结果和标准初始化没区别

b = Box().myInit('魔盒', '14m', '红色')
# b = Box('魔盒', '14m', '红色')#注释掉原来标准的初始化方法
b.close()
b.open(b)  # 本来就会自动传一个self，现在传入b，就会让open多得到一个实例对象本身，print看看是什么。
print(b.__dict__)  # 这里返回的就是self本身，self存储属性，没有动作。

'''
换个角度来讲，对类的操作有：

1、定义属性 ； 2、调用方法

对类的反馈有：

1、得到属性 ； 2、执行方法

在 class 类的函数中，为什么 self是必要的，因为 self 是对象的载体，可以理解成一个字典，看下面代码：

注意此处的： mySelf.__dict__['aa'] = 'w'  #甚至可以像字典一样操作； 在 b.__dict__ 的结果中显示为：'aa':'w'

故可以把 self 理解成存储 实例化对象属性的字典(dict), self 存储属性，而没有动作执行

self总是指调用时的类的实例。

python 中一些特殊的实例变量：

1、私有变量(private),只有内部可以访问，外部不能访问，私有变量是在名称前以两个下划线开头，如：__name，
其实私有变量也不是完全不能被外部访问，不能直接访问是因为python解释器对外把 __name 变量改成了 _类名__name,
所仍然可以通过 _类名__name 来访问 __name .

2、在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

3、以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当
你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
'''