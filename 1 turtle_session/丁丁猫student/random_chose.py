import random
names = ['henry','liuzhimo','xing']
names = ['feifei','xiaozhe','xueer']
print('机选之人回答问题：',random.choice(names))

#print(random())

classIsOver = ['yes','no']
print('20210911:',random.choice(classIsOver))

cai = ['Rock', 'Paper', 'Scissors'] #列表，
# 数组
ages = [12,11,10]
print(sorted(ages,reverse=False)) #逆转

#鸡，蛋
print(sorted(['鸡','蛋'],reverse=True))
print(sorted(['chicken','Egg']))

print(sorted(['Abb','Aab','abc','bcd','aaa','aab','AAA','ABA','Aaa','AAa','AAb']))
#高级函数
#alphabet
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)

#decode
#encode
#password,id

# 3 :-1,0 1
#google

print(random.choice(cai))

names = ['lzy','lzj','phil']
color = ['red','yellow','blue']

result = random.choice(names)
print(result)
print(random.choice(color))

def muti(x,y):
    return x*y

miss_kata = ['Enumerable Magic#17-sort that list by value',
             'Enumerable Magic#16-Sort that List']

#1、试着1，3，5，7 加到99？
print('odd sum:',[i for i in range(100) if i%2==1])
print('slice:',list(range(101))[1::2])
print('chongqing'[::2])
print('chongqing'[0:5:2])# start:end:step
print(['chongqing'[i] for i in [1,4,8]])

#100 台阶，step=1，2，3，到第100台阶，总共有多少种走法？

import math
print(5%3,5/3,5//3) #
print(int(5/3),math.ceil(5/3),math.floor(5/3))
print(round(5/3,5))


#2、如果你有1000块钱，总共能换到多少块糖？

#3、运用3种代码写法实现1千万以内所有整除3的数并且比较时间效率

# 1000rmb，5%，1050
# 每个月 + 下个月

import math
print(math.pi,math.e)

