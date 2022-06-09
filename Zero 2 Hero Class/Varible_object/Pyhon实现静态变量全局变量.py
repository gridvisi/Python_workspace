__author__ = 'Administrator'

# 含有类的静态方法、静态变量, 普通类成员函数, 成员变量
class People:
    count = 0
    sum = 0
    def __init__(self, name, age, gend):
        self.name = name
        self.age = age
        self.gender = gend
        People.peopleCount()    # 人数计数
        People.ageSum(age)      # 岁数计数

    def toString(self):
        print ("name : %s, age : %d, gender : %s." % (self.name,self.age, self.gender))

    # 静态函数
    @staticmethod
    def sayHi(fname):
        print ("hi," + fname)

    # 间接实现静态成员变量
    @classmethod
    def peopleCount(cls):
        cls.count += 1
        return cls.count

    # 间接实现静态成员变量, 有参数
    @classmethod
    def ageSum(cls, age):
        cls.sum += age
        return cls.sum

ple = People("mr.simple", 22, "male")
