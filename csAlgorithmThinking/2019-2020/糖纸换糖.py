'''
Today we learn python from scratch
"Don't set out to learn Python. Choose a problem you're interested in and learn to solve it with Python." -
so we choose a math problem,buy candy and exchange candy with package
Firstly,we pay 1 rmb for a candy, then we can be award a candy with 3 package
the function solve
input the money you pay
ouput the candy you get

code
'''
import math
print(math.sqrt(10))

alex = {"candy":0, "paper":0,'rmb':100}
#每买3块糖，人民币少3块，糖纸就多3块，然后就换1块糖
# candy -3
# paper +3
# rmb -3
eat = 0
while alex['rmb'] >= 0:   # while循环终止条件
    print(alex, eat)  #

    alex['rmb'] -= 3      # 每减少1元钱
    alex['candy'] += 1    # 糖就多一块
    eat += 1              # 吃掉一块糖
    alex['candy'] -= 1    # 糖就少一块
    alex['paper'] += 1    # 增加一张糖纸

    if alex['paper'] == 3:  # 糖纸累计到3张时
        alex['paper'] = 0   # 3张糖纸换成一块糖
        alex['candy'] += 1  # 糖增加一块
        eat += 1            # 吃掉这块糖
        alex['candy'] -= 1  # 糖减少一块
        alex['paper'] += 1  # 糖纸增加一块

    elif alex['rmb'] == 0:  # 直到人民币花完
        print('final:',alex,eat)  # 循环终止



# 不用字典，思路相同也能实现

rmb = 100 #人民币
wrappers = 0  # 糖纸
eaten = 0    # 肚子里的糖
while rmb > 0:  # while 当什么时候 人民币大于零
    rmb -= 1
    eaten += 1
    wrappers += 1  #注意在最后判断rmb==0时
    if wrappers == 3:
        wrappers -= 3
        eaten += 1 #吃一个
        wrappers += 1 #糖纸加一个,请问同学为什么加糖纸 1？

print("Great！有优惠活动：")
print("剩多少钱:",rmb,"余下多少糖纸:",wrappers,"总共吃了:",eaten+rmb)






# recursion
money,price,rate = 100,1,3
def bonus(money,price,rate,eaten=0,wrappers=0):
    if money == 0:
        return "买和换共计："+f"{eaten}", "还剩糖纸："+f"{wrappers}"
    elif money > 0:
        money -= price
        eaten += 1
        wrappers += 1
        if wrappers == rate:
            wrappers -= rate
            eaten += 1
            wrappers += 1
        return bonus(money,price,rate,eaten,wrappers)

money,price,rate = 1000,4,7
money,price,rate = 100,3,3
#print(bonus(money,price,rate,eaten=0,wrappers=0))

