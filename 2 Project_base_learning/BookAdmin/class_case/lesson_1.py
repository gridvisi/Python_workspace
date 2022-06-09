class Cat:  #地球人
    """定义一个猫类"""

    def __init__(self, new_name, new_age):
        """在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""
        # self.name = "汤姆"
        # self.age = 20
        self.name = new_name
        self.age = new_age
        # 它是一个对象中的属性,在对象中存储,即只要这个对象还存在,那么这个变量就可以使用
        # num = 100  # 它是一个局部变量,当这个函数执行完之后,这个变量的空间就没有了,
        # 因此其他方法不能使用这个变量

    def __str__(self):
        """返回一个对象的描述信息"""
        # print(num)
        return "名字是:%s , 年龄是:%d" % (self.name, self.age)

    def eat(self):
        print("%s在吃鱼...." % self.name)

    def drink(self):
        print("%s在喝可乐..." % self.name)

    def introduce(self):
        # print("名字是:%s, 年龄是:%d" % (汤姆的名字, 汤姆的年龄))
        # print("名字是:%s, 年龄是:%d" % (tom.name, tom.age))
        print("名字是:%s, 年龄是:%d" % (self.name, self.age))


# 创建了一个对象
tom = Cat("汤姆", 30)
print(tom)

'''
总结:

在python中方法名如果是__xxxx__()
的，那么就有特殊的功能，因此叫做“魔法”方法
当使用print输出对象的时候，只要自己定义了__str__(self)
方法，那么就会打印从在这个方法中return的数据
__str__方法需要返回一个字符串，当做这个对象的描写
'''

class Alien(object):

    def __init__(self, name):
        self.name = name
        #self.price = price
        #self.brief = brief #简介

    def walk_able(self):
        return f"{self.name}alien can walk"

    def move_able(self):
        return "alien do move"

    def talk(self):
        return f"alien talk to person with {self.name}"

    def hand(self):
        return f"alien three fingers"

    def fly(self):
        return f"{self.name} alien can fly"

kevin = Alien("kevin")

yolanda = Alien('yolanda')
print(yolanda.fly())
print(yolanda.talk())

arr = ['liu','su','kevin']
arr.append('phil')
print(arr)
#print(superappend(arr,'phil'))
age = '11.5'
print(isinstance(age,str))

print(int(1.1))

# homework

class Book:
    def __init__(self, name, author, price, stock, brief):
        self.name = name
        self.author = author
        self.price = price
        self.stock = stock
        self.brief = brief

a = Book('an','liu',45,10,'about coding')
print(a, type(a))
print(a.brief)



class person():

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
