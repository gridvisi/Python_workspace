#  python3中所有类都可以继承于object基类
class Animal(object):
   def __init__(self, name, age):
       self.name = name
       self.age = age

   def call(self):
       print(self.name, '会叫')

cat = Animal('kitty',5)
print('cat.name:',cat.name)
# 同时output-> kitty 会叫

print('cat.call:',cat.call)
print('cat.call():',cat.call())  #None
# TypeError: call() missing 1 required positional argument: 'self'

######
# 现在我们需要定义一个Cat 猫类继承于Animal，猫类比动物类多一个sex属性。
######
class Cat(Animal):
   def __init__(self,name,age,sex):
       super(Cat, self).__init__(name,age)  # 不要忘记从Animal类引入属性
       self.sex=sex

if __name__ == '__main__':  # 单模块被引用时下面代码不会受影响，用于调试
   c = Cat('ketty', 2, '男')  #  Cat继承了父类Animal的属性
   c.call()  # 输出 喵喵 会叫 ，Cat继承了父类Animal的方法

'''
注意：一定要用 super(Cat, self).__init__(name,age) 去初始化父类，
否则，继承自 Animal的 Cat子类将没有 name和age两个属性。
函数super(Cat, self)将返回当前类继承的父类，即 Animal，然后调用__init__()方法，
注意self参数已在super()中传入，在__init__()中将隐式传递，不能再写出self。

Python 对子类方法的重构
上面例子中 Animal 的子类 Cat 继承了父类的属性和方法，但是我们猫类 Cat 有自己的
叫声 '喵喵' ，这时我们可以对父类的 Call() 方法进行重构。如下：
'''

class Cat(Animal):
   def __init__(self, name, age, sex):
       super(Cat, self).__init__(name,age)
       self.sex = sex

   def call(self):
       return print(self.name,'会喵喵叫')

   def genderJudge(self):
        if self.sex == '男':
            return print(f"{self.name}不是母猫！")

if __name__ == '__main__':
   c = Cat('丁大猫', 2, '男')
   c.call()  # 输出-> 丁大猫 会“喵喵”叫
   c.genderJudge()


# 继承类的属性
'''
共同的部分：
如何修改上面的动物的类？
猫和蜗牛共同的属性：eat,walk
猫和蜗牛不同的属性: call

'''
#  python3中所有类都可以继承于object基类

class Animal(object):
   def __init__(self,name, eat, walk):
       self.name = name
       self.eat = eat
       self.walk = walk

   def call(self):
       print(self.name, '会叫')

Cat = Animal
c = Cat('kitty','鱼', '猫步') #,喵喵'
print(Cat.call)
print(c.name,c.call()) #kitty None
print('c.call-1:',c.call)
print('c.call-2:',c.call())

#不要忘记从Animal类引入属性

class Cat(Animal):
   def __init__(self,name,eat,walk,call):
       super(Cat, self).__init__(name,eat,walk)
       self.call = call

cat1 = Cat('kitty','鱼', '猫步','喵喵') #
print('cat-1.walk:',cat1.walk)
print('cat-1.call:',cat1.call)

# 单模块被引用时下面代码不会受影响，用于调试
if __name__ == '__main__':
     cat2 = Cat('ada','鱼', '猫步','miao')
     # Cat继承了父类Animal的吃和走的属性
     print('cat2.eat',cat2.eat)
     print('cat2.call:',cat2.call)
     cat2.call
     # 输出 喵喵 会叫 ，Cat继承了父类Animal的方法


#
class Cat(Animal):
   def __init__(self,name,eat,walk,gender):
       super(Cat, self).__init__(name,eat,walk)
       self.gender = gender

if __name__ == '__main__':
     cat3 = Cat('brown','鱼', '猫步','male cat')
     # Cat继承了父类Animal的吃和走的属性
     print('cat2.eat',cat3.eat)
     print('cat2.call:',cat3.call)
     cat3.call()
     # 输出 brown会叫 ，Cat继承了父类Animal的方法




