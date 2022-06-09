'''
https://brilliant.org/daily-problems/safe-cities/
'''

#一个骰子的模拟
import random
number_of_rolls = 200
regress_count = 0

no_regress_count = 0
roll = 0
for i in range(number_of_rolls):
    oldroll = roll
    roll = random.randint(1, 6)
    print(roll, end = " ");
    if (oldroll >= 5):
        if (roll < 5):
            regress_count += 1
        else:
            no_regress_count +=1
print("")

print("Total number of rolls:", number_of_rolls)

print("Number of times top performance went to average or worse:", regress_count)

print("Number of times top performance stayed high:", no_regress_count)


# 三个dice一起模拟

#Python 3 Show original code

import random
number_of_rolls = 200
regress_count = 0
no_regress_count = 0
roll = 0

for i in range(number_of_rolls):
    oldroll = roll
    roll = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    print(roll, end = " ")

    if (oldroll >= 16):
        if (roll < 16):
            regress_count += 1

        else:
            no_regress_count +=1
print("")

print("Total number of rolls:", number_of_rolls)
print("Number of times top performance went to average or worse:", regress_count)
print("Number of times top performance stayed high:", no_regress_count)
