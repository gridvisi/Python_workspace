__author__ = 'Administrator'
class People:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def walk(self):
        print('%s is walking' %self.name)
    def foo(self):
        print('from father %s' %self.name)

class Teacher(People):
    school = 'oldboy'
    def __init__(self,name,age,sex,level,salary):
        People.__init__(self,name,age,sex)
        self.level = level
        self.salary = salary
    def bar(self):
        People.foo(self)
        print('from teacher')

class Student(People):
    pass

t = Teacher('egon',13,'male',10,3000)
# print(t.name,t.age)
print(t.__dict__)
t.walk()
t.bar()
t.foo()
'''
整个思路是这样：
1、描述一个称之为”shop“的类，类包含3个属性：店名和口味，人数，3家店通用的要素。
     打印输出验证代码正确。再定义营业状态，”正在营业“还是”休息打烊“
2、再追加一个新要素，空房间可以供订购的数量，只适于7天酒店。判断客人数量和房间空出的数量
'''
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
class shop():
    def __init__(self,name,cuisine):  # 店的类包含两个参数
        self.cuisine=cuisine
        self.name=name

    def describe_shop(self):         # 入店欢迎词
        pop = 'welcome to ' + self.name + 'self.cuisine '
        return pop

    def  open_shop(self):     # 正在营业中”
        notice = self.name + ' ' + 'is opening'
        return notice

my_shop = shop('lala','hotpot')  # describe_shop(名字，口味)
your_shop = shop('breadtalk','chinesetyle')   # open_shop(your_shop.name)

print (my_shop.name)
print (my_shop.name,'入店欢迎词：',my_shop.describe_shop())
print (my_shop.open_shop())
print (your_shop.name,'入店欢迎词：',your_shop.describe_shop())
print (your_shop.open_shop())

#进一步描述你和我的店有多少人光临，需要增加一个熟悉number_served，描述方法如下：

def  set_number_served(self):
    number = 'today total '
    str(self.number_served) + ' people be served'
    return number

#增加以后，就可以输出到店客人的人数，完整代码如下：

class shop():
    def __init__(self,name,cuisine,number_served):
         self.cuisine=cuisine
         self.name=name
         self.number_served=number_served

    def describe_shop(self):
         pop = 'welcome to ' + self.name + '，祝您消费愉快！ '
         return pop

    def open_shop(self):
         notice = self.name + ' ' + 'is opening'
         return notice

    def set_number_served(self):
         number = 'today total: '+ str(self.number_served) + ' people be served'
         return number

my_shop = shop('lala','hotpot',17)  # “辣辣”火锅店 今天又17人到店
your_shop = shop('breadtalk','chinesetyle',99)  # “中国口味”茶餐厅有99人到店

#print('- - - + - - -+- - - + - - -+- - - + - - -+- - - + - + - - -+- - - + - - -+- - - + - - -+- - - + - - -+')
print('  ')
print (my_shop.describe_shop(),my_shop.set_number_served())
print (your_shop.open_shop(),your_shop.set_number_served())
print (my_shop.set_number_served())
print (your_shop.set_number_served())

'''
有一家旅店需要建新的类，可以继承上面的父类，但有一个属性是酒店特有的，需要说明是否客满
number_capacity =100 说明酒店共有100个房间，如果到店的客人数量大于100，说明房间全部
订出，没有空房，否则可以预定。
'''
class hotel(shop):
    def __init__(self,name,cuisine,number_served):
     super().__init__(name,cuisine,number_served)
     self.number_capacity =100

    def hotel_occupy_status(self):
        if self.number_served >  self.number_capacity:
            occupy_status = 'sorry sir!' + self.name + 's all room be reserved'
        else:
            occupy_status = 'thank you sir!' + self.name + 'your room is to be reserved'
        return occupy_status
print('  ')
guest_booking = hotel(' 7 days inn','biz',66)
print(guest_booking.hotel_occupy_status())
guest_booking = hotel(' 7 days inn','biz',122)
print(guest_booking.hotel_occupy_status())