'''
https://brilliant.org/daily-problems/same-or-different/

answer by brilliant
here are 88 possible outcomes. If YY represents a yellow ball and BB a blue one, then the possible sequences of three draws are as follows:
BBB \\ YBB \\ BYB \\ BBY \\ BYY \\ YBY \\ YYB \\ YYY.
BBB
YBB
BYB
BBY
BYY
YBY
YYB
YYY.
In 44 of these cases, Ese wins:
BBB,\ BYB,\ YBY,\ YYY.
BBB, BYB, YBY, YYY.
In the other 44 cases, Oke wins:
YBB,\ BBY,\ BYY,\ YYB.
YBB, BBY, BYY, YYB.
So, they each have the same chance of winning.
'''


# total 8 combination
# there is 4 option which first and third is same color
# [blue,yellow,blue],[blue,blue,blue],[yellow,blue,yellow],[yellow,yellow,yellow]
# there is option which 1st and 3rd is differ color
# [blue,yellow,yellow],[blue,blue,yellow],[yellow,blue,blue],[yellow,yellow,blue]



import random
balls = ['blue','yellow']
def draw_ball(balls):
    res = []
    for i in range(3):
        op = random.choices(balls)
        res.append(op)
    return res[0] == res[2]
#print(draw_ball(balls))
times = 1000000
same = 0
for i in range(times):
    same += draw_ball(balls)
print(same/times)