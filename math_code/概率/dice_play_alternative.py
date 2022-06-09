# https://brilliant.org/problems/who-wins-the-dice-game/

# a，b两人轮流掷骰子，a先扔出6点，谁赢
# 经典题：99%的同学掉坑，对称思想的干扰，都选择了1/2
'''
第一轮中a扔出6点获胜的概率是1/6,如果a，b都没有扔出6点，概率是5/6 × 5/6，才进入第二轮；
第二轮a获胜的概率是 5/6 × 5/6 × 1/6，a没有获胜的概率是 5/6 × 5/6×5/6，表示没有得到6。
同理，a在第三局中获胜的概率为（5/6）×（5/6）×（5/6）×（5/6）×（1/6）

我们发现a获胜的概率序列变成：
(1 / 6), (25 / 216), (625 / 7776)...

然后我们认识到这是一个几何级数，有一个共同的比率 R = 25/36
应用无限几何级数之和的公式：
(1 / 6) x (1 / (1 - R))  = 6 / 11

结论： a是先手，赢率是6/11，比b的赢率大
'''
from random import randint
def roll_a():
    return randint(1,6)

def roll_b():
    return randint(1,6)

def roll_win(trials):
    a, b, draw = 0, 0, 0
    for trial in range(trials):
        if roll_a() > roll_b():
            return True
        if roll_a() <= roll_b():
            return False
#每1组随机测试不超过100次，共测试round=100001组
trials = 1000
round = 100001
re = 0.0
for r in range(round):
    re += roll_win(trials)
print(re/(round-1),6/11)

print(1/6)
win,lose,draw = 0,0,0
trials = 10001
for trial in range(trials):
    if roll_a() > roll_b():
        win += 1.0
    if roll_a() < roll_b():
        lose += 1.0
    if roll_a() == roll_b():
        draw+= 1.0

print('分别掷出'+f"{trial}"+"次 play A的赢率：",win/trials)
print('分别掷出'+f"{trial}"+"次 play A的pei率：",lose/trials)
print('分别掷出'+f"{trial}"+"次 play A的平局的：",draw/trials)