'''
https://brilliant.org/courses/logic-deduction/introduction-68/warmup-puzzles/2/

Rae, Knuck, and Lex are robots from 3 different models.

Rae is not the newest.

Knuck is the oldest.

Lex is not the oldest.

What’s the correct order, from newest to oldest?
'''

ages = ['','',''] #newest --> oldest

robots = ['Rae', 'Knuck', 'Lex']
#1 Rae index() != 0, is not the robots[]  == newest.
#2 Knuck is index() == 2, the oldest.
#3 Lex's index() in (0,1) or is not the oldest.

from itertools import permutations #全排列

# 2 * 3 = 6

for robot in permutations(robots,len(robots)):
    print(robot)
    if robot.index('Rae') != 0:
        # 1 Rae index() != 0, is not the robots[]  == newest.
        if robot.index('Knuck') == 2:
        # 2 Knuck is index() == 2, the oldest.
            if robot.index('Lex') in (0,1):
         # 3 Lex's index() in (0,1) or is not the oldest.
                 print('000:',robot)
                 print('-----------------------------------------')



'''
https://brilliant.org/courses/logic-deduction/introduction-68/warmup-puzzles/5/

In the next race:

One robot finishes between Rae and Lex
Two robots finish between Lex and Ty
Rae didn’t finish second
In what order did they finish?

在接下来的比赛中。
一个机器人在雷伊和莱克斯之间完成比赛
两个机器人在莱克斯和泰之间完成比赛
Rae没有获得第二名
他们是按什么顺序完成的？

'''
from itertools import permutations
names = ["Marv", "Rae", "Ty","Lex"]
for name in permutations(names,len(names)):
    if abs(name.index("Rae") - name.index("Lex"))==2:
    #一个机器人在雷伊和莱克斯之间完成比赛
        if abs(name.index("Lex") - name.index("Ty")) == 3:
        #两个机器人在莱克斯和泰之间完成比赛
            if name.index("Rae") != 1:
                #Rae没有获得第二名
                print("#他们是按什么顺序完成的:",name)





'''
https://brilliant.org/courses/logic-deduction/introduction-68/harder-challenges/3/

Marv, Rae, and Ty race.

They report only that Rae finishes ahead of Ty.

In how many different orders could the racers finish?

2,3,4,5,6
'''

from itertools import permutations
names = ["Marv", "Rae", "Ty"]
#Rae finishes ahead of Ty
#Rae 领先于 Ty
#

result = []
for name in permutations(names,len(names)):
    if name.index('Rae') < name.index("Ty"):
        result.append(name)
print(result,len(result))




'''
https://brilliant.org/courses/logic-deduction/introduction-68/harder-challenges/5/
In the next race, five robots compete. They report that:

Marv finishes either second or fourth.

Rae finishes either first or fifth.

Lex finishes either third or fourth.

Ty finishes either first or second.
Mig finishes either third or fifth.
How many different orderings are possible?

在接下来的比赛中，有五个机器人参加比赛。他们报告说。
Marv获得了第二或第四名。
Rae获得第一或第五名。
Lex获得第三或第四名。
Ty获得第一或第二名。
Mig获得第三或第五名。

'''

from itertools import permutations
names = ["Marv","Rae","Lex","Ty","Mig"]
result = []
for name in permutations(names,len(names)):
    if name[1] == "Marv" or name[3] == "Marv":
        if name[0] == "Rae" or name[4] == "Rae":
            if name[2] == "Lex" or name[3] == "Lex":
                if name[0] == "Ty" or name[1] == "Ty":
                    if name[2] == "Mig" or name[4] == "Mig":
                        result.append(name)
print(result)
