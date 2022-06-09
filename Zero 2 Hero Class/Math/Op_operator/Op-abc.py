# 配合slide python编程和中小学数学融合
# 预热逻辑任务

#There are 4 coders code in Python.
# Which is right?

print('1:',"Hi") #P

#print('2:',Hi) #

print('3:',"Hi")

print('4:',"Hi")

Hi = 17

x = 1
print(x)
print(x+1)


total = 0
for i in range(1,10):
    total = total + i
print('sum 1-10:',i,total)

'''
# CA-K56-22nd Question

Ala喜欢偶数，Beata喜欢3的倍数，Celina喜欢5的倍数。一
每个女孩都走到一个篮子里，篮子里有8个写着数字的球，然后拿着。
所有的球与数字，她喜欢。阿拉收集了数字32和52的球。贝塔
收集了24，33和45号球。Celina收集了20、25和35号球。
女孩们是按照什么顺序接近篮筐取球的？

(A) Ala, Celina, Beata
(B) Celina, Beata, Ala
(C) Beata, Ala, Celina
(D) Beata, Celina, Ala
(E) Celina, Ala, Beata

如何梳理逻辑关系？

'''
# define  return exit
def add(a, b):  #jiafa
    return 'old_brother age:',a + b
a =  7 #young_brother'age  young_brother =
#b = old brother 5 than young brother
b = 5
print(add(a,b))
#Q1:已知出生在x年，计算n岁时是哪一年？

# Ada is 1st female programmer
# alex
# henry
# zhou
# xes
# aurora  beibei

def jiafa(x,y):
    return x+y
x = 10
y = 17
print(jiafa(x,y))


def subtract(a, b):  #minus  jianfa
    pass
    return a - b

#Q2: 已知出生在x年，计算2021年是几岁？


def multiply(a, b):
    pass
    return a * b
#Q3：已知操场每圈是400米，你跑了3圈半，问跑了有多少米？


def divide(a, b):
    pass
    return a / b

# henry is 11，3 years before

def years(a,b):
    a = 11
    b = 3
    return a - b
print('market:',years(a,b))
print('mark:',a-b)

def books(x,y):
    x = 12
    y = 3
    return x/y
print("superhero",books(x,y))

def pens(y,x):
    y = 100
    x = 1
    return y+x
print('iF:',pens(y,x))




#Q4: 父母给了100元零花钱，每天花15元，够用几天？

# Q5: 妈妈改为每天给你10元，连续10天，第10天时你从收到的10元取出一半借给同桌
# 同桌第11天多还你2元，问你总共有多少钱？

# 10 * 10  -  10/2  +  (10/2+2) = ?
# x,y,z 变量赋值
x = 10 * 10
y = 10/2
z = 7
print(x - y + z)

#Q6: 妈妈每天给你n元，连续d天，你分给同桌一半，同桌还你多了两元
#请编写函数输出你总共有多少钱？

#Input:
n = 10
d = 10

x = multiply(n,d)  #n，d 是参数 argument
y = divide(n,2)
z = y + 2
result = add(subtract(x,y),z)

#Output:
print('结果一:',result)

# 可以这些写吗？
result = add(subtract(multiply(n,d),divide(n,2)),divide(n,2)+2)
print('结果二:',result)


#Q：找出三条边可以组成直角三角形Right Angle Triangle的数组
# triangle = [3,4,5]

print('勾股定理：',3**2 + 4**2 == 5**2)

def right_angle(arr):
    sq = 0
    arr = sorted(arr)
    xiebian = arr[-1]
    for i in arr[:-1]:
        sq += i**2
    return sq == xiebian**2
arr = [3,4,5]
arr = [3,5,4]
print(right_angle(arr))

#Q8:num_plate = ['渝A9919','渝C5072','渝A2966','渝D8371','渝A3417','渝A5255','渝AD9919']
# 今天是单号，限行双号，请判断哪些车号不能上路？
car_plate = ['渝A9919','渝C5072','渝A2966','渝D8371','渝A3417','渝A5255','渝AD9919']

no_way = []
for num in car_plate:
    if int(num[-1]) % 2 == 0:
        no_way.append(num)
print(no_way)

# Q9:枚举
'''
# CA-K56-22nd Question

Ala喜欢偶数，Beata喜欢3的倍数，Celina喜欢5的倍数。一
每个女孩都走到一个篮子里，篮子里有8个写着数字的球，然后拿着。
所有的球与数字，她喜欢。阿拉收集了数字32和52的球。贝塔
收集了24，33和45号球。Celina收集了20、25和35号球。
女孩们是按照什么顺序接近篮筐取球的？

(A) Ala, Celina, Beata
(B) Celina, Beata, Ala
(C) Beata, Ala, Celina
(D) Beata, Celina, Ala
(E) Celina, Ala, Beata

如何梳理逻辑关系？
如何编程解决之？
'''

names = ['Ala', 'Beata','Celina']
div = [2,3,5]
arr = [20,24,25,32,33,35,45,52]
def div_zero(name,arr):
    names = ['Ala', 'Beata', 'Celina']
    div = [2, 3, 5]
    div_dict = dict(zip(names,div))
    return [i for i in arr if not i % div_dict[name]]

print(div_zero('Beata',arr))
print(div_zero('Ala',arr))
print(div_zero('Celina',arr))

#step 2nd:
result = []

from itertools import product
from itertools import combinations
from itertools import permutations
for name in permutations(names,3):
    #print(name)
    bench = {'Ala':[32,52],
             'Beata':[24,33,45],
             'Celina':[20,25,35]
             }
    arrs = arr
    for n in name:
        temp = div_zero(n,arrs)

        if bench[n] == temp:
            result.append(n)
        arrs = [i for i in arrs if i not in temp]

print(result)



# itertoos usage
'''
from itertools import product

for bools in product((True, False), repeat=6):
    for i in range(len(bools)):
        statement = not any(bools[i + 1:]) if i < 3 else not any(bools[:i])
        if statement != bools[i]:
            break
    else:
        print(bools)
'''
