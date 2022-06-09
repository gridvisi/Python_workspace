'''
https://brilliant.org/daily-problems/on-a-roll/


'''
import random
def two_six_dice(x):
    cunt = 0
    dice_n = [i for i in range(1,7)]
    n = random.choices(dice_n)
    dice_m = [i for i in range(1,7)]
    m = random.choices(dice_m)
    #print(n,m)
    return int(m[0] + n[0] == x)
x = 12
#for i in range(100):
#    print(two_six_dice(x))


def twelve_dice(x):
    cunt = 0
    dice = [i for i in range(1,13)]
    n = random.choices(dice)
    return n[0] == x

# main programm

def compare(times,x):
    six_sum,twelve_sum = 0,0
    for i in range(times+1):
        six_sum += two_six_dice(x)
        twelve_sum += twelve_dice(x)
    return f"Six_sum:{six_sum}, Twelve_sum:{twelve_sum}"
times = 10000
print(compare(times,12))

def two_dice(ls):
    ans = {}
    for x in range(1,13):
        ans[x] = compare(times,x)
    return ans
ls = [i for i in range(1,12)]
print(two_dice(ls))

'''
第三个步：
编程实现数学中概率公式推导的结果，并与以上结果对比
概率原理运用以7为例。6个面的骰子掷两次。两次点数相加等于7的可能有几种组合
1st draw      1    2    3    4    5    6
2nd draw     6    5    4    3    2    1
total dots     7    7    7    7    7    7 
Probability             1/36               
共计是1/36 * 6 = 1/6 

这时，我们既可以考虑引入排列组合函数，枚举1-6之间任意2个数相加是约定数字组合；
也可以以两重for循环找出所有组合。
'''

def six_dice_math(x):
    total,hit = 0, 0

    def twleve_dice_math(x):
        return 1 / 12
    #inner function
    for i in range(1,7):
        for j in range(1,7):
            total += 1
            hit += int(i+j==x)
    return round(hit/total/twleve_dice_math(x),2)
print([six_dice_math(x) for x in range(1,13)])


def compare(times,x):
    six_sum,twelve_sum = 0,0
    for i in range(times+1):
        six_sum += two_six_dice(x)
        twelve_sum += twelve_dice(x)
    return six_sum, twelve_sum
print([round(v[0]/v[1],2) for k,v in two_dice(ls).items()])


from itertools import combinations  #permutations
def six_dice_math2(x):
    total, hit = 0, 0
    prob = dict(zip(range(1,13),[0]*12))
    arr = [i for i in range(1,7)]
    for x,y in combinations(arr,2):
        print(x,y)
        total += 1
        prob[x+y] += 1
    return prob,total
print(six_dice_math2(x))

'''
概率问题的难点是判断每个事件的发生没有关联，保持独立性。这句话比较抽象，举个栗子：锤子剪刀布游戏

如果你一直出剪刀，对方发觉规律后，对方会改为一直出锤子。这时，就丧失了独立性。因为对手认为你上次出了剪刀，
下一次还是剪刀，前后事件有关联。

如果你和电脑玩游戏就不同了。你的对手的手势姿势换成代码随机生成，运用上述random随机函数在数组：
[锤子，剪，刀布] 三者之间随机挑选一个。

因为我们的代码并没有人类的归纳总结能力，你大可放心一直出剪刀，电脑无法察觉你一直出剪刀的事实。
'''

import random

def Rock_Paper_Scissors():

    choice_RPS = ["Rock", "Paper", "Scissors"]
    you = random.choice(choice_RPS)
    me = random.choice(choice_RPS)
    result = f"{you} vs {me}"

    #第2步游戏规则的定义
    rules = {'win':['Rock vs Scissors',
                    'Scissors vs Paper',
                    'Paper vs Rock'],

            'lose':['Scissors vs Rock',
                 'Paper vs Scissors',
                 'Rock vs Paper']
             }

    #第3步判断输赢输出结果，字典

    for k,v in rules.items():
        if result in v:
            return f"{you} vs {me} : " + f"you {k} me"
        #else:
        #    return 'draw'
    return f"{you} vs {me} : " + f"you draw me"

you,me = "Rock","Paper"
print(Rock_Paper_Scissors())

# 模拟人一直出剪刀，机器随机出锤子剪刀布
def code_vs_people(me):

    choice_RPS = ["Rock", "Paper", "Scissors"]
    code = random.choice(choice_RPS)
    result = f"{code} vs {me}"

    #第2步游戏规则的定义
    rules = {'win':['Rock vs Scissors',
                    'Scissors vs Paper',
                    'Paper vs Rock'],

            'lose':['Scissors vs Rock',
                 'Paper vs Scissors',
                 'Rock vs Paper']
             }

    #第3步判断输赢输出结果，字典

    for k,v in rules.items():
        if result in v:
            return f"{k}"
    return "a draw"

'''
 for k,v in rules.items():
        if result in v:
            return f"{code} vs {me} :\n " + f"机器 {k}! computer {k} me"
        #else:
        #    return 'draw'
    return f"{code} vs {me} : " + f"平局 you draw me"
'''

me = "Scissors"
print('人机对战：',code_vs_people(me))

from collections import Counter
result = []
for _ in range(100):
    result.append(code_vs_people(me))
print(Counter(result))
