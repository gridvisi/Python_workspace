# while loop终止时，循环的次数是多少

floor = -1
start = 1
current = start  #current就是电梯开始停留的楼层
while current != floor:
    print('细节回放：',current, floor)
    current -= 1
print('final result exit while loop:',current,floor)


# A job need 10 person work for 18 days
# if person -= 4 ,the question is how many days we need to solve

person = 10
days = 18
work_per_day_person = 1
day = 1

# 假设6人完成的工作量累积和10人工作量累积比较
while (person-4) * day != person * days:
    day += 1
print(day)

#2rd question of math
computer = 3
hour = 6
work = 1440
target = 2800
hour_exp = 1 #
# computer add on 4 set
# 1 set per day : how many pict?
power = work / computer / hour
print(power)
while hour_exp*(computer+4)*power != target:
    hour_exp += 1  #hour_exp = hour_exp + 1
print(hour_exp)

# map(list)
family = [79,23,34,83,49]
# 3 years before,how old are all of family?
# n years ago, ?
father = family[-1]
#运用地址脚标赋值给father，mother，grandmother

print(family[-1],father)
print(father - 3)
print(family[2:4])
father,mother,grandmother = family[1:-1]
print(father,mother,grandmother)

#2 slice Right position to start or end ?

'''
1. 询问：请输入一个数字。根据输入数字判断它是单数、双数、还是其他。
2. 询问：请输入一个数字。根据输入数字判断它是5的倍数、9的倍数、同时
是5和9的倍数、其他。

3. 询问：请输入一个数字。根据输入数字判断它是否为质数。
4. 找到1万以内所有能够同时被7整除，而且十位数是0的数字，并将它们加入列表
中。删除列表中最小的那一个，将剩下的输出出来。
'''

def IsOdd_Even(n):
    return 'even 偶数' if n%2==0 else 'odd 奇数'
n = 17
print(IsOdd_Even(n))

#如何多行实现？
def IsOdd_Even(n):
    if n % 2 == 0:
        return 'even 偶数'
    else:return 'odd 奇数'
    #return 'even 偶数' if n%2==0 else 'odd 奇数'

# n 是3的整数倍吗
import random
n = random.choices(list(range(100)))
print('n:',n)
def IsThird(n):
    if n[0] % 3 == 0:
        return f"{n[0]}是3的整数倍"
    else:
        return f"{n[0]}不是3的整数倍"
print(IsThird(n))

#1st 猜拳
import random
zhang = random.choices(['石头','剪刀','布'])
li = random.choices(['石头','剪刀','布'])
print(zhang,li)
#判断谁赢？
# Tip


#2nd
# random 随机生成一个0 ，2021之间的整数
# 判断n 是17的整数部吗？
# 如果是就输出n
# 如果不是就输出比n大，离n最近的数整除17
# 写成函数名 isSvtnum(n)

# 5的倍数

def isFive(n):
    return n%5 == 0
