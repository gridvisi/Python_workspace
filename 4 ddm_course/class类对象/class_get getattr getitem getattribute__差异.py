
class Employee(object):

    def __init__(self, username, age):
        self.username = username
        self.age = age

    def __getattribute__(self, attr):
        return super(Employee, self).__getattribute__(attr)

    def __getitem__(self, attr):
        return super(Employee, self).__getattribute__(attr)

em = Employee('yiifaa', 32)

print(em.username)
#   现在支持“[]”运算符
print(em['username'])

'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'length'
'''


'''
那“_ getattribute_”与“_ getattr_”的最大差异在于：
1. 无论调用对象的什么属性，包括不存在的属性，都会首先调用“_ getattribute_”方法；
2. 只有找不到对象的属性时，才会调用“_ getattr_”方法；
'''

#4. 获取对象属性数据的三种方法
#对象的所有属性都存储在“_ dict_”中（启用了“_ slots_”除外），所以访问对象的属性数据有如下三种方法：

print(yiifaa.name)
print(yiifaa.__dict__['name'])
print(getattr(yiifaa, 'name'))

#结论每个以“__ get”为前缀的方法都是获取对象内部数据的钩子，但名称不一样，用途也存在较大的差异，只有在实践中理解它们，才能真正掌握它们的用法。