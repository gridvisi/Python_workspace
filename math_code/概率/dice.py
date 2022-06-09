



import math
import random
dice_1 = random.choice([1,2,3,4,5,6])
dice_2 = random.choice([1,2,3,4,5,6])
dice_3 = random.choice([1,2,3,4,5,6])

print(dice_1 > dice_2,dice_1,dice_2)

#print('dice:',random.choice([1,2,3,4,5,6]))


from random import randint

def roll_66():
    total = []
    for roll in range(6):
        total.append(randint(1,6))
    return sorted(total) == [1,2,3,4,5,6]

def roll_666():
    total = []
    for roll in range(6):
        total.append(randint(1,6))
    return [total.count(i) for i in range(1,7)] == [1,2,3,4,5,6]

def roll_6():
    total = []
    for roll in range(6):
        total.append(randint(1,6))
    return total == [1,2,3,4,5,6]

yes = 0
trials = 100000
for trial in range(trials):
    if roll_6():
        yes += 1.0
print('1个色子掷出六次roll_6：',yes/trials)

for trial in range(trials):
    if roll_66():
        yes += 1.0
print('6个色子一起掷出roll_66:',yes/trials)

for trial in range(trials):
    if roll_666():
        yes += 1.0
print('6个色子一起掷出 roll_666:',yes/trials)

'''
def roll_23():
    total = 0
    for roll in range(4):
        total += randint(1,6)
    return total == 23
yes = 0
trials = 1000000
for trial in range(trials):
    if roll_23():
        yes += 1.0
print (yes/trials)

def roll_24():
    total = 0
    for roll in range(4):
        total += randint(1,6)
    return total == 24
yes = 0
trials = 1000000
for trial in range(trials):
    if roll_24():
        yes += 1.0
print (yes/trials)
'''
