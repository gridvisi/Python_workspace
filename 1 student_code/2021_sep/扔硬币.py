#1:"one"
#2:"two"
#0-9
#0-20
def numtostring(n):
    return ['zero','one','two','three','four'][n]

import random

def flip_coin(rmb):
    flip = [1, 0]
    draw = random.choice(flip)
    if draw == 1:
        rmb += 0.5
        return flip_coin(rmb) #递归
    else:
        return rmb
rmb = 0
print('result:',flip_coin(rmb))


result = []
for i in range(10000):
    result.append(flip_coin(rmb))
print(result.count(1),result.count(0))

total = 0
three  = []
for i in range(101):
    if str(i).count('3') != 0:
        three.append(i)
        total += 1
print('total:',total,three)

#print(13.count(3))

