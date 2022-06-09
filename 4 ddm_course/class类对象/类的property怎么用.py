class People:

    def __init__(self, name, age):
        self.__name = name  # 使用双下划线__可以定义私有属性
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


# class instance 类的实例化

someone = People(name='Jack', age=20)  # 类的实例化
print(someone.get_name())  # Jack
someone.set_age(100)  # 修改name为100
print(someone.get_age())  # 100


# 可以通过更好的方式访问或者修改私有属性的值


class People:

    def __init__(self, name, age):
        self.__name = name  # 使用双下划线__可以定义私有属性
        self.__age = age

    @property  # 装饰器,通过装饰器可以直接访问__name
    def name(self):
        return self.__name

    @name.setter  # 通过这种方式之后,可以直接修改__name的值
    def name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


# class instance 类的实例化

someone = People(name='Jack', age=20)  # 类的实例化
print(someone.name)  # Jack 通过装饰器可以直接访问__name
someone.name = 'xiaohua'  # 通过@name.setter可以修改name的值
print(someone.name)  # xiaohua

