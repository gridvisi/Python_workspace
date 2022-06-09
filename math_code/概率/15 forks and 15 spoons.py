__author__ = 'Administrator'
#https://blog.csdn.net/u013628152/article/details/43198605

import random
from collections import Counter
while True:
    group = [random.randint(0, 1) for i in range(30)]   #叉子为1，勺子为0，随机数量生成数组group
#print(group)
    num_fork = str(group).count("1")
    num_spoon = str(group).count("0")
    if num_fork == 15 and num_spoon ==15:
        print(group)
        print(Counter(group))
        break
j = 0
while True:
    #print('随机顺序摆放的叉子和勺子:',group[j:j+10])
    fork = str((group[j:j+10])).count("1")
    spoon = str(group[j:j+10]).count("0")
    if fork == 5 and spoon == 5:
        print ('j =',j)
        print (group[j:j+10])
        break
    j += 1
'''
#for i in range(30):
#while len(group) == 30:
while counter < 31:

    x = random.randint(0, 1)
    group.append(x)
    counter+=1

    #print(num_fork)

'''
