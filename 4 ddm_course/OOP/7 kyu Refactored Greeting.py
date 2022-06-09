'''
https://www.codewars.com/kata/5121303128ef4b495f000001/train/python

下面的代码可以使用一点面向对象的艺术性。虽然这是一个简单的方法，而且它的工作原理很好，
但在一个更大的系统中，最好将方法组织成类/对象。(或者，至少，类似的东西取决于你的语言)

重构下面的代码，使其属于一个Person类/对象。每个Person实例将有一个greet方法。
Person实例应该被实例化为一个名称，这样就不必再将其传递到每个greet方法调用中。

下面是最终重构后的代码的使用方法。
'''
#1st solution
# TODO: This method needs to be called multiple times for the same person (my_name).
# It would be nice if we didnt have to always pass in my_name every time we needed to great someone.

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, your_name):
        return "Hello {you}, my name is {me}".format(you=your_name, me=self.name)

#2nd solution
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, other):
        return f"Hello {other}, my name is {self.name}"




class Person():
    def __init__(self,my_name):
        self.name = my_name
        #self.your_name = your_name

    def __str__(self):
        return self.name

    def greet(my_name, your_name):
        return "Hello %s, my name is %s" % (your_name, my_name)

joe = Person('Joe')
print(joe)
print(joe.greet('kate'))

#https://zhuanlan.zhihu.com/p/141873874
class Person(object):
    """一个简单的类."""
    species = "Homo Sapiens" # 类属性

    def __init__(self, name):  # 特殊方法--构造方法

        """一旦基于类实例化一个对象，即会自动调用此方法
         """
        self.name = name  #  实例属性赋值，即将实例化对象的参数值赋给对象


    def __str__(self):  # 特殊方法
        """  当Python试图将对象转换为字符串时，将运行此方法。在使用print()等函数时返回该字符串
         """
        return self.name

    def rename(self, renamed):  # 普通方法
        """ 重新分配并打印name属性"""
        self.name = renamed
        print("现在我的名字是： {}".format(self.name))