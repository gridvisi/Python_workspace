'''
https://brilliant.org/daily-problems/pay-to-play/
'''

import random
def dice(total=0): #模拟随机1次掷色子的积分
    num = random.choice(list(range(1,7)))
    if num < 6:
        total += num
        return total
    elif num == 6:
        total += 6
        return dice(total) #递归调用

print(dice(total=0))

s = 0
n = 100000 #模拟100000次结果累积求平均值
for _ in range(n):
    s += dice(total=0)
print(s/n)
# ouput ： 4.19276