num = [i for i in range(1,26)]
alpha = ['a....z']

import string
alpha = string.ascii_lowercase
print(dict(zip(alpha,num)))

print('---------------------------')


print('dog'[:0:-1]) #default 缺省

#cooking(thing,salt,sugar)


def count_sheep(n):
    return "1 sheep..."
n = 20
print('No.1st:',count_sheep(n))

n = 2
print(count_sheep(n))

def count_sheep(n):
    ans = ''
    for i in range(1,n+1):
        ans += f"{i} sheep..."
    return ans
n = 10
print(count_sheep(n))

print('range1-1',list(range(1,1)))

# 丁丁猫的编程第一课先找到一个有趣的任务，不同方法解决任务，过程中掌握
# 数组  字典  循环

# 简化任务，小卖部没有糖纸换糖3抵1活动了，小明拿到9元钱能吃到多少块糖？
# 每块糖是3元

for i in range(10):
    print(i)


rmb = 250
price = 50  #person 50rmb/per
wrappers = 0
eaten = 0
meal_miss = 10

while rmb > 0 and '人体体征正常': #电话通知999，120来抬
    rmb -= 50  #rmb = rmb - 1
    eaten += 1
    wrappers += 1
print("sorry！没有钱了，老板")
print("sorry! 原谅我，站不起来，帮我叫车")

print("吃掉的糖总计total candy:", eaten,"糖纸共计:",wrappers)
print("剩下多少钱：",rmb)

# 任务升级，小卖部恢复回馈活动了3换1

rmb = 10 #人民币
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

# 在大喵老师遇到了一个典型奥数班同学的问题，向老板借用一块糖，还给老板3张糖纸，哈哈
if wrappers == 2:
    eaten += 1
    wrappers -= 2
print("奥数同学的借糖方案：")
print("吃掉的糖总计 total candy:", eaten,"糖纸共计:",wrappers,"剩下多少钱：",rmb)

# 初始状态的alex，10元钱，其他都为0
alex = {"candy": 0, "paper": 0, "rmb":10}
# 每买3块糖，人民币少3块，糖纸就多3块，然后换1块糖
# candy -3
# paper +3
# rmb -3
# eat = 0

eat = 0
while alex['rmb'] >= 0:
    alex['rmb'] -= 1
    alex['candy'] += 1
    eat += 1
    alex['candy'] -= 1
    alex['paper'] += 1
    if alex['paper'] == 3:
        alex['paper'] = 0
        alex['candy'] += 1
        eat += 1
        alex['candy'] -= 1

    print(alex, eat)

# Recuit 递归

money,price,rate = 101,1,3
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

print(bonus(money,price,rate,eaten=0,wrappers=0))