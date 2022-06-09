from os import name

__author__ = 'Administrator''''
class A(object):
    def _init_(self,name):
        self.name = name

    def _getName(self):
        return 'A'+ self.name


class B(A):
    def _init_(self, name):
        super(B, self)._init_(name)
        print("hi")
        self.name = name
    def getName(self):
        return 'B '+self.name

if __name__=='__main__':
    b = B('hello')
    print (b.getName())


class A(object):
    def __init__(self):
        self.m = False

    def aa(self):
        self.m = True

class B(A):
    def __init__(self):
        super(B, self).__init__()
    def bb(self):
        print(self.m)


class aa:
    def _init_(self):
        self.x = 10
        self.y = 12
    def hello(self, x):
        return x + 1
print(aa.x)

class bb(aa):
    def _init_(self):
        aa._init_(self) #如果注销此行，下边打印b.x和b.y将报错，未定义
                                        #通过类名字调用父类的构造方法函数
        self.z = 14

a = aa()
print (a.x, a.y)
b = bb()
print (b.x, b.y)
'''


class shop():
    def __init__(self,name,cuisine,number_served):
        self.cuisine=cuisine
        self.name=name
        self.number_served=number_served

    def describe_shop(self):
        pop = 'welcome to ' + self.name + ' ' + self.cuisine
        return pop

    def open_shop(self):
        notice = self.name + ' ' + 'is opening'
        return notice

    def set_number_served(self):
        number = 'today total ' + str(self.number_served) + ' people be served'
        return number

my_shop = shop('lala','hotpot',17)
your_shop = shop('breadtalk','chinesetyle',99)

# describe_shop(my_shop.name)
# open_shop(your_shop.name)
print (my_shop.name)
print (my_shop.describe_shop())
print (my_shop.open_shop())
print (my_shop.set_number_served())
print('  ')
print (your_shop.describe_shop())
print (your_shop.open_shop())
print (your_shop.set_number_served())


class hotel(shop):
    def __init__(self,name,cuisine,number_served):
        super().__init__(name,cuisine,number_served)
        self.number_capacity = 100

    def hotel_occupy_status(self):
        if self.number_served > self.number_capacity:
            occupy_status = 'sorry sir!' + self.name + 's all room be reserved'
        else:
            occupy_status = 'thank you sir!' + self.name + 'your room is to be reserved'
        return occupy_status

guest_booking = hotel(' 7 days inn','biz',66)
print(guest_booking.hotel_occupy_status())

guest_booking = hotel(' 7 days inn','biz',122)
print(guest_booking.hotel_occupy_status())
