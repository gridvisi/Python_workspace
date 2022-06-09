# https://zhuanlan.zhihu.com/p/30239694
#如下定义一个动物类Animal为基类，它基本两个实例属性name和age、一个方法call。

class Animal(object):  #  python3中所有类都可以继承于object基类
   def __init__(self, name, age):
       self.name = name
       self.age = age

   def call(self):
       print(self.name, '会叫')

######
# 现在我们需要定义一个Cat 猫类继承于Animal，猫类比动物类多一个sex属性。
######
class Cat(Animal):
   def __init__(self,name,age,sex):
       super(Cat, self).__init__(name,age)  # 不要忘记从Animal类引入属性
       self.sex=sex

if __name__ == '__main__':  # 单模块被引用时下面代码不会受影响，用于调试
   c = Cat('喵喵', 2, '男')  #  Cat继承了父类Animal的属性
   c.call()  # 输出 喵喵 会叫 ，Cat继承了父类Animal的方法

