# https://stackoverflow.com/questions/21584812/python-classes-best-practices
# key point:
'''
While reading 'The Object-Oriented Thought Process' book (Matt Weisfeld : Developer's Library) ... The author states continuously throughout it:
"...Access to attributes within an object should be controlled by the object itself—no other object should directly change an attribute of another..."
"...If you control the access to the attribute, when a problem arises, you do not have to worry about tracking down every piece of code that might have changed the attribute—it can only be changed in one place (the setter)..."
I will be sticking to setters and getters then. Suggested/mentioned here Python's @property and @.setter make it even easier.

在阅读'The Object-Oriented Thought Process'一书（Matt Weisfeld : Developer's Library）时......。作者在书中不断地指出
"......对对象内部属性的访问应该由对象本身控制--其他对象不应该直接改变另一个对象的属性......"
"......如果你控制了对属性的访问，当出现问题时，你就不必担心追踪每一段可能改变属性的代码--它只能在一个地方（setter）被改变......"
那么我将坚持使用setter和getter。这里建议/提到Python的@property和@.setter让它变得更加简单。
'''
class MyClass(object):
    def __init__(self):
        super(MyClass, self).__init__()
        self.my_attr = 'My_Value'

    def doSomething(self):
        localVariable = self.my_attr
        print(localVariable)


class MyClass(object):
    def __init__(self):
        super(MyClass, self).__init__()
        self.my_attr = 'My_Value'

    def getMyAttr(self):
        return self.my_attr

    def doSomething(self):
        localVariable = self.my_attr
        print(localVariable)

