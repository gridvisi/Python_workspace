'''
https://brilliant.org/daily-problems/losing-intuition/

Today's Challenge
Suppose you play a game where you win 25% of the time.



Which is more likely to happen?

A. You lose the first eight games.

B. You lose the first four games, then win the fifth.


'''

win_lose = ['w','l','l','l'] #0.25,0.75

import random
def odd(n):
    win_lose = ['w', 'l', 'l', 'l']

    s = ''
    for _ in range(10000):
        s += random.choice(win_lose)

        '''
        if s == 'w':
            win.append(s)        
        else:
            lose.append(s)
        '''
    win, lose = ''.join(s).count("llllw"), ''.join(s).count("llllllll")
    win, lose = ''.join(s).count("llllw"), ''.join(s).count("llllllll")
    return win,lose
n = 8
print(odd(n))

#compare s[0:4]=="llll" and s[4] == "w"
#vs. s[0:8] == "llllllll"
def odd():
    win_lose = ['w', 'l', 'l', 'l']
    eight,fifth = 0,0
    s = ''
    for _ in range(1000000):
        s += random.choice(win_lose)
        #print(s)

    for i in range(len(s)-8):
        if s[i:i+5] == 'llllw':
            fifth += 1

        elif s[i:i+8] == "llllllll":
            eight += 1

    return eight,fifth,round(eight/fifth,5)
print(round(0.75**4 / 0.25,5))


print(odd())



# 夏令营预测连续下雨问题转换


sun_rain = ['r','s','s','s'] #0.25,0.75

import random
def randomSR():
    sun_rain = ['r','s','s','s']

    s = ''
    for _ in range(100000):
        s += random.choice(sun_rain)
    prob_A = ''.join(s).count("rrrrs")
    prob_B = ''.join(s).count("ssssssss")
    return prob_A,prob_B

print('the 1st:',randomSR())

#compare s[0:4]=="llll" and s[4] == "w"
#vs. s[0:8] == "llllllll"
def randomSR_2nd():
    sun_rain = ['r', 's', 's', 's']
    eight,fifth = 0,0
    s = ''
    for _ in range(100000):
        s += random.choice(sun_rain)
        #print(s)

    for i in range(len(s)-8):
        if s[i:i+5] == 'ssssr':
            fifth += 1

        elif s[i:i+8] == "ssssssss":
            eight += 1

    return fifth,eight,round(eight/fifth,5)
print(round(0.75**4 / 0.25,5))
print('the 2nd:',randomSR_2nd())

'''
1.26562
(100353, 79205, 1.267)
'''

'''
结果是不是违反直觉！连续8天都是晴天的概率竟然远远大于连续4天晴天且第5天下雨的概率！
Ada疑惑地将结果告诉大喵老师后，大喵老师并没有直接告诉Ada，她的算法是正确还是错误

但是，大喵老师请同学们一起讨论Ada的算法！
同学们都陷入长时间的思考 ... ... 有同学感到哪里不对劲，但指不出究竟问题在哪儿？

大喵老师给同学给出一个字符串：
'''

ls = "ssssrsssssssssrrssr"
ls = ''
sun_rain = ['r', 's', 's', 's']
for d in range(60):
    ls += random.choice(sun_rain)
print('ls:',ls)
print('five_day:',ls.count("ssssr"))
print('eight_day:',ls.count("ssssssss"))


# 从相同位置开始，分别切片5和8试试看
# 比较的方法变化后，结果也不同！！

five_day, eight_day = 0 , 0
for i in range(len(ls) - 8):
    if ls[i:i + 5] == 'ssssr':
        five_day += 1

    elif ls[i:i + 8] == "ssssssss":
        eight_day += 1
print("five_day:",five_day,"eight_day:",eight_day)