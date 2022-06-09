#https://gridvisi.github.io/ddm.github.io/post/20200707-coding-camp-lecture-1/
'''
+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
0    1   2    3   4   5
-6 - 5 - 4  - 3  -2  -1

'''

name1,name2 = '胡迪童','胡越'
surname = name1[0]
print(surname,name1[0] == name2[0])

result = []
if name1[0] == '胡' or name2[1] == '胡':
    result = "至少有一人姓胡"
    print('有幸福的吗？',result)

result = []
if name1[0] == '胡' and name2[1] == '胡':
    result = "都姓胡"
    print('全部都幸福吗？',result)
else:
    result = "都不姓胡"
    print('全部都幸福吗？', result)



print(all([True,False,True])) # bool and or

person = ["lyc","诸葛亮", "李张梓霖","张李梓沐","邓爱希香","lyc" ,"李张总领", "张涵奇", "周宏宇", "唐诚心", "刘一芝",
          "汪刚", "郑嘉", "龙心", "谭心", "邢小台", "宋雨","张吴含","张吴","李懿轩","lyc"]

for name in person:
    if name[0:2] == '诸葛':
        print(name)


print(person.index( "李张梓霖"),person.index( "龙心"))
for i,e in enumerate(person):
    print(i,e)




print(person.index("lyc"))
person = set(person)
print(person)
lyc = "李昱辰"

res_li = [name for name in person if name[0] == "李" or name[0] == "l"]
print('li:',res_li)

print([i+"同学" for i in person])

#print("lyc",person.count("lyc"))
'''
for i in range(len(person)):
    person[i]= [person[i]+"同学"]
print("lyc:",person)
'''



# 索引
huamince = person
person = []
person.append("杰罗姆")
#print("周宏宇的位置：",person.index("周宏宇"))
print(person,huamince)

person.append("杰罗姆")
print("杰罗姆的位置：",person.index("杰罗姆"))
print("杰罗姆的位置：",person.index("杰罗姆"))
print(person,huamince)

person.append("李懿轩")
print("李懿轩的位置：",person.index("李懿轩"))
print(person,huamince)

# 查询名单有没有某人？
for name in person:
    if name == "李懿轩":
        print("I found you,liyixuan")
    else:
        pass
print("not found",name)


# 添加某同学buddy

math = ['alan','betty','carol','david','eric','fanny']
cs = ['alan','carol','david','eric','gigi','jerry','lily']

destmate = dict(zip(math,cs))
print(destmate)
print(zip(math,cs))


print(person[1][0:2])
dual_sur = ['张吴']

for name in person:
    #print(name)
    if '张' in name[0] and len(name) <= 3 and name[0:2] not in dual_sur:
        print('alan lee',name)

name = "蔡徐坤"
genders = "男"
name = input("input your name:")


print(name,'我只看这一行结果：',genders == "男")
print(name == genders)


class Tool(object):
    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0
    def __init__(self, name):
        self.name = name
        # 针对类属性做一个计数+1
        Tool.count += 1

# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

# 知道使用 Tool 类到底创建了多少个对象?
print("现在创建了 %d 个工具" % Tool.count)

# buddy search class


from dataclasses import dataclass, field
@dataclass(order=True)
class Buddy:
    name: str
    course: str
    gender: str
    grade: int
    membership: str
    def profile(self):
        res = {}
        res[name] = (self.name,self.course,self.gender,self.grade,self.membership)
        return res

    def paycheck(self,pay_status,amount):
        name = self.name
        course = self.course
        #discount = 0.8
        pay_status = pay_status # 0:unpaid,1=paid
        amount = amount
        return {self.name:(pay_status,amount)}

    def rate(self,membership):
        name = self.name
        course = self.course
        if self.membership == "primer":
            discount = 0.85
        elif self.membership == "advance":
            discount = 0.75
        return discount

zhou = Buddy("周宏宇","vex python","male",2,"primer")
#zhou.paycheck("paid",2000)
#print(zhou.paycheck())
print(zhou.paycheck("paid",2000))
print(zhou.paycheck("paid", 2000*zhou.rate(zhou.membership)))

Jerome = Buddy("杰罗姆","python","male",1,"advance")
print(zhou)
name = "zhouhy"
print(zhou.profile())

name = "Jerome"
print(Jerome.profile())

names = ["zhouhy","Jerome"]


class Buddy(object):
    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0
    def __init__(self, name,course,gender,grade):
        self.name = name
        self.course = course
        self.gender = gender
        self.grade = grade
zhou = ("周宏宇","vex","male","junior")
name = zhou[0]
zhou_class = Buddy( "周宏宇","vex","male","junior")
print(zhou_class)
print(zhou_class.name)
print(zhou_class.course)# = zhou[1]
print(zhou_class.gender) # = zhou[2]
print(zhou_class.grade) # = zhou[3]




'''
school = person
for person in school:
      if person[4] == 'math' and person[] == 'gemini':
       my_buddy.append(person)
'''



ls = ['liu','cheng']
ls.append('xin')
print(ls)

print(3.0 == 3)

print('李懿轩'[0],'李懿轩'[::],'李懿轩'[::-1])
print("张李严谨"[::-1][:2][::-1] == "张李严谨"[-2:])
print("张李严谨"[::-1][:2][::-1], "张李严谨"[:-2],"张李严谨"[-2:])

lucas = 'male'
tobby = 'male'
cxuk = 'female'

print(0 and 0)
print(0 or 2)
print('mcree' and 'lucas')

'''

import math
x,i = 6,0
print(x % 2 == 0)
print(int(math.sqrt(x - i)) == math.sqrt(x - i))

def close(x,i):
    i = 0
    if int(math.sqrt(x - i)) == math.sqrt(x - i):
        return x-i

    elif int(math.sqrt(x + i)) == math.sqrt(x + i):
        return x+i
    close(x,i+1)
    close(x, i - 1)

print(close(10,0))



b = '111'
b_10 = 2**(3-1) + 2**(3-2) + 2*(3-3)


student = ["lzl","zhy","lzh","zhq","lxch","lyn"]
print(len(student))
print(student.index("lxch"))

for i,e in enumerate(student):
    print(i,e)


#name = input("input your name:")
#print(name)

ls = [2,3,3,4,5,6] #去重 set

re = []
for i in ls:
    if i not in re:
        re.append(i)
print(re)

print(set(ls))

a = b = c = d = 1

'''