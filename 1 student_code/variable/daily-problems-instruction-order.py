# https://brilliant.org/daily-problems/instruction-order/
# 考察编程思想，通过拖拽图标3步实现任务目标
#  how to swap x, y  ?
'''
Initially, variables x and y contain values A and B, respectively.
You have three instructions at your disposal:

a. Set x to x minus y.
b. Set x to x plus y.
c. Set y to x minus y.

'''
x, y = 3, 4
x = x + y
y = x - y
x = x - y
print(x,y)

#name1 =（    ） 和  name2=（  ） 一起学编程！

def fat(name1,name2):
    return f"{name1} and {name2} study python"

name1 = "lzj"
name2 = "lzy"

name1 = "lz"
name2 = "ly"

def fat(name1,name2):
    return f"{name1}{name2}"
name1 = "十个"
name2 = "苹果"
print(fat(name1,name2))

def fat(num,name2): #数量，水果名称
    return f"{num}同学，分{num}{name2}"*10
num = "100个"
name2 = "苹果"
print(fat(num,name2))
#10 apple

def box_fruit(name):
    return name * 10

name = 'apple '
name = 'banana'
print(box_fruit(name))


# 加法

def add(x,y):
    return x + y
x,y = 8,9
print(add(x,y))
print(add(1,2))

# 365 * 24 + 60/15 * 10
#

# escape time
#lijunlin math problem
# 变量表达

vFuse = 8   #mm
lenFuse = 960  # mm
t1 = lenFuse / vFuse
print(t1)

vPerson = 5 # m
lenEscape = 500
t2 = lenEscape / vPerson
print(t2)

# 1 + 2*3-4
#print(less(add(1,2*3),4))

#如果t1 大于 t2，安全
#如果t1 小于 t2，不安全

print("安全" if t1 > t2 else "不安全")

#if 是如果的意思， else 是那么的意思

teacher= 9
lijunlin = 10
print("老师年龄大" if teacher > lijunlin else "学生年龄大")

#3 蜜雪冰城

milk_tea = 10
orange_tea = 11
print(f"milk_tea milk_tea贵" if milk_tea > orange_tea else f"orange_tea的价格是{orange_tea}，贵")


# 100 rmb，6元一杯，每3杯送一杯

rmb = 100
p = 10
song = 3

print(int(rmb/p + rmb/p/song))



