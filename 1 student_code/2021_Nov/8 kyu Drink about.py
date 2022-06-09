'''
https://www.codewars.com/kata/56170e844da7c6f647000063/train/python

Kids drink toddy.
Teens drink coke.
Young adults drink beer.
Adults drink whisky.
Make a function that receive age, and return what they drink.

Rules:

Children under 14 old.
Teens under 18 old.
Young under 21 old.
Adults have 21 or more.
Examples: (Input --> Output)

13 --> "drink toddy"
17 --> "drink coke"
18 --> "drink beer"
20 --> "drink beer"
30 --> "drink whisky"
'''


def people_with_age_drink(age):
    return ''

#递归：函数调用自己

def add(x,y):  #定义一个add函数有两个参数：
    return x + y
x,y = 1,2
print(add(x,y))

# 1 + 2 + 3
s = add(1,2)
print(add(s,3))
print(add(add(1,2),3))

s = [[2,3],[3,5]]
def square(x=2,y=3):  #定义一个面积函数有两个参数：
    return x * y

res = []
for c in s:
    x,y = c #赋值
    res.append(square(x,y))
print(res)

# function case-2

#判断能否整除400的子函数
def fourhundred(n):
    return n % 400 == 0

#判断能否整除 4 的子函数
def four(n):
    return n % 4 == 0

#判断能否整除100的子函数
def hundred(n):
    return n % 100 == 0

'''
今天的挑战：判断2020年是闰年吗？
如果不是，未来距离2020年最近的闰年是哪一年？
闰年的规则是：
1、公历年份是4的倍数的，不肯定都是闰年。
2、公历年份是整百数的，必须是400的倍数才是闰年。
运用 or 和 and 换一种方式描述闰年：
要判断某一年是不是闰年，拆解任务分为先定义三个子函数：
judge_1 = 能否整除 4
judge_2 = 能否整除 100
judge_3 = 能否整除 400
然后，三个判断之间运用 or 和 and 满足闰年定
'''

def leapYear(n):
    if fourhundred(n) or (not hundred(n) and four(n)):
        return True
    return False
n = 2400
print('leapY：',leapYear(n))

print('True or False-1:',True or False)
print('True or False-2:',False or True)

print('True AND False-1:',True and False)
print('True AND False-2:',False and True)