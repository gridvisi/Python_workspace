'''
https://www.codewars.com/kata/52210226578afb73bd0000f1/train/python

你听说过 "电子绕核 "这个游戏吗？我不允许给你完整的游戏规则，就这么多。
游戏是用4到6个骰子来玩的 所以你会得到4到6个数字，每个1到6的阵列
名正言顺.你必须连续五次返回正确的数字，你的解决方案被认为是正确的。
如果你按 "提交 "键，你会得到一个数组和预期值!
[ 1, 2, 3, 4, 5 ] -> 6
[ 2, 2, 3, 3 ] -> 4
[ 6, 6, 4, 4, 1, 3 ] -> 2
[ 3, 5, 3, 5, 4, 2 ] -> 12
以下是一些输入/输出对，供你参考。
'''
# point awarded for each dot that is around a central dot
# ie. 5 has 4 dots surrounding | 3 has 2 dots surrounding

def electrons_around_the_cores(dice):
    # Just so you can try some numbers
    return sum([i-1 if i%2 == 1 else 0 for i in dice])

dice = [ 6, 6, 4, 4, 1, 3 ]
dice = [ 3, 5, 3, 5, 4, 2 ]
print(electrons_around_the_cores(dice))

#1st solution
electrons = {3:2, 5:4}

def electrons_around_the_cores(dice):
  return sum(electrons.get(d, 0) for d in dice)

def electrons_around_the_cores(dice):
    return sum([0,0,0,2,0,4,0][d]for d in dice)


def electrons_around_the_cores(dice):
    # Just so you can try some numbers

    electrons = 0
    for i in range(0, len(dice)):
        if dice[i] == 3:
            electrons += 2

        if dice[i] == 5:
            electrons += 4
    return electrons

from collections import Counter
def electrons_around_the_cores(dice):
    return sum( (x-1)*n for x,n in Counter(dice).items() if x>1 and x&1 )

def electrons_around_the_cores(dice):
    return sum(2 if i==3 else 4 if i==5 else 0 for i in dice)


def electrons_around_the_cores(rolls):
    # point awarded for each dot that is around a central dot
    # ie. 5 has 4 dots surrounding | 3 has 2 dots surrounding
    return sum(({3: 2, 5: 4}.get(roll, 0) for roll in rolls))