

class person(object):
   address = '中国'  # 类属性，没个实例的公共属性

   def __init__(self, name, sex, age):  # 相当于java中的构造方法
       self.name = name  # 实例属性
       self.sex = sex  # 实例属性
       self.age = age  # 实例属性

   def dance(self):  # 方法
       print(self.name, '跳了一场舞')
       return self.name, '跳了一场舞'

   def surname(self):
       return self.name[0]
hong = person('小红', '女', 18)  # 实例化小红，将实例化的对象赋值给变量hong
ming = person('小明', '男', 26)
hua = person('小花', '女', 22)

print(hong.name,hong.dance(),hong.surname())

#freecodecamp
class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()


class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()

# Singleton

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    if (id(s1) == id(s2)):
        print ("Same")
    else:
        print ("Different")


# __repr__方法
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    p = point(3, 4)
    print(p)

'''
在这段代码当中我们定义了一个简单的类，它当中有x和y两个元素，但是如果我们直接运行的话，屏幕上会输出这样一个结果：

<__main__.point object at 0x10a18c210>


这个是解释器在执行的时候这个实例的一些相关信息，但是对于我们来说几
乎没有参考意义，我们想要的是这个实例当中具体的值，而不是一个内存当
中的地址。

想要实现这个功能，我们有很多方法，下面我们一一来看。

__str__方法


__str__方法大家应该都不陌生，它类似于Java当中的toString方法，
可以根据我们的需要返回实例转化成字符串之后的结果。

比如，我们可以在类当中重载这个方法，就可以根据我们的需要输出结果了：
'''
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'x: %s, y: %s' % (self.x, self.y)

#x: 3, y: 4
q = point
print(q(3,4))

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x: %s, y: %s' % (self.x, self.y)

    def __repr__(self):
        return '<point x: %s, y: %s>' % (self.x, self.y)
s = point
print('s_repr_:',s(3,4))

'''
这是为什么呢，难道__repr__和__str__是一样的吗？如果是一样的，Python
的设计者干嘛要保留两个完全相同的函数呢，为什么不去掉其中一个呢？

在分析原因之前，我们先来做一个实验，如果我们两个函数都重载，那么当我们输
出的时候，程序执行的是哪一个呢？为了做好区分，我们把repr当中的输出的格式
稍微修改一下。
'''

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x: %s, y: %s' % (self.x, self.y)

    def __repr__(self):
        return '<point x: %s, y: %s>' % (self.x, self.y)
'''
先别着急下结论，我们再把这段代码拷贝到jupyter notebook当中，我们这次
不通过打印输出，而通过jupyter自带的交互框输出交互结果，我们再来看下：

也就是说通过重载__format__方法，我们把原本固定的格式化的逻辑做成了可配置的。
这样大大增加了我们使用过程当中的灵活性，这种灵活性在一些问题场景当中可以大大简化和简洁我们的代码。对于Python这门语言来说，我个人感觉实现功能只是其中很小的一个部分，把代码写得简洁美观，才是其中的大头。这也是为什么很多人都说Python易学难精的原因。



今天的文章就是这些，如果觉得有所收获，请顺手点个关注或者转发吧，你们的举手之劳
'''
# https://zhuanlan.zhihu.com/p/130442206

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x: %s, y: %s' % (self.x, self.y)

    def __format__(self, code):
        return 'x: {x}, y: {y}'.format(x = self.x, y = self.y)


formats = {
    'normal': 'x: {p.x}, y: {p.y}',
    'point' : '({p.x}, {p.y})',
    'prot': '<{p.x}, {p.y}>'
}

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x: %s, y: %s' % (self.x, self.y)

    def __format__(self, code):
        return formats[code].format(p=self)