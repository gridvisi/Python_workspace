'''
https://www.codewars.com/kata/52b5247074ea613a09000164/train/python

you can put at most 8 eggs into the pot at once
it takes 5 minutes to boil an egg
we assume, that the water is boiling all the time (no time to heat up)
for simplicity we also don't consider the time it takes to put eggs into the pot or get them out of it
Example (Input --> Output)
0 --> 0
5 --> 5
10 --> 10
'''


#17 minuters
import random

print(list(range(0,17,8)))



#for i,e in enumerate()
# 煮鸡蛋 一次 8
# 5分钟
# 输入鸡蛋个数，输出煮鸡蛋的时间

import math
def cooking_time(eggs):
    return math.ceil(eggs/8) * 5


def cooking_time(eggs):
    t = 0
    while (eggs > 0):
        t += 5
        eggs -= 8
    return t


#3# no magic numbers!
POT_CAPACITY = 8
COOKING_TIME = 5

def cooking_time(eggs):
    return COOKING_TIME * ((eggs + POT_CAPACITY - 1) // POT_CAPACITY)


# For loop

def cooking_time(eggs):
    pot = 0
    for i in range(0,eggs,8):
        pot += 1
    return pot*5
eggs = 17
print(cooking_time(eggs))


def cooking_time(eggs,cap,t): #鸡蛋数，煮蛋器8容量，t=5分钟
    pot = 0
    for i in range(0,eggs,cap):
        pot += 1
        print(pot)
        # 鸡蛋数量凑不够一锅，
        # for循环还是执行了一次pot+1，
    return pot*t
eggs = 7
cap, t = 8, 5
print(f'boil {eggs} egges need',cooking_time(eggs,cap,t))

# 每锅最多放cap个鸡蛋，每锅煮熟需要5分钟

print(list(range(0,eggs,cap)))
print(list(range(0,4,8)))


# feed dog
bowl = None or "empty"
bowl = 3
if bowl == 0: #"empty"
    bowl += 5

else:
    #new = 5 - bowl
    #bowl += new
    bowl = 5

print('bowl',bowl)

import random
c = random.choices(['green','red','red','red','red'])
print(c)
if c == ['red']:
    print('sui say:','green')
print(c)

#slice

name = '张瀚文'
name = "诸葛孔明"
print(name[:2],name[2:])

print(name[:2] + name[2:])

# 0-100,之间所有个位数是0的全部列出来
ans = []
for i in range(101):
    if str(i)[-1] == '0': #数据类型 字符串，整数型
        ans.append(str(i))
print('ans:',ans)

#2nd solve
print(list(range(0,101,5)))

#3
for day in range(101):
    if day % 3 == 0 and day % 5 == 0 and day % 7 == 0:
        print(day)

#4
day = 1

while True:
    if day % 3 == 0 and day % 5 == 0 and day % 7 == 0:
        print(day)
        break
    day += 1
print(day)

a,b = 10,15

def gcd(a,b):
    while a != 0:
        a,b = b%a,a
        print(a,b)
    return a,b
#a,b =
print(gcd(a,b))