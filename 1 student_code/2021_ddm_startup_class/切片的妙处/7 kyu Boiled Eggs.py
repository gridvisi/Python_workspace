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


