'''
https://www.codewars.com/kata/545c4f7682e55d3c6e0011a1/train/python

有n个球，编号从0到n-1（0,1,2,3,等等）。其中大部分球的重量相同，但有一个球比较重。你的任务是找到它。

你的函数将收到两个参数--一个天平对象，和一个球的数量。天平对象只有一个方法。

    get_weight(left, right)
其中左和右是分别放在左盘和右盘的球的数量数组。

如果该方法返回-1，则左盘较重。

如果该方法返回1，则右盘更重。

如果该方法返回0，则两个锅的重量相同。

那么，是什么让这个卡塔的 "全能大师 "版本？首先，它不像以前的版本那样只限于8个球--
你的解决方案必须适用于8-500个球。

第二，你不能使用超过数学上必要的尺度。这里有一个图表。


小球数量  | 次数
ball count | uses
-----------------
           0-9 |    2
       10-27 |    3
      28-81  |    4
     82-243 |    5
   244-500 |    6
'''

#Top 1st
def find_ball(scales, n):
    select = list(range(n))
    while len(select) > 1:
        left, right, unused = select[::3], select[1::3], select[2::3]
        if len(select) % 3 == 1: unused.append(left.pop())
        select = [left, unused, right][scales.get_weight(left, right) + 1]
    return select.pop()

#Ref lower level
def find_ball(scales):
    part = [[None, 0, 1], [2, 3, 4], [5, 6, 7]]
    res1 = scales.get_weight(part[-1], part[1])
    res2 = scales.get_weight([part[res1][-1]], [part[res1][1]])
    return part[res1][res2]


def find_ball(scales, ball):
    if len(ball) == 3:
        flag = scales.get_weight(ball[1],ball[2])
        return ball[flag]

    l,m,r = list(range(0,ball//3)),list(range(ball//3,2*ball//3)),list(range(2*ball//3,ball))
    w1 = scales.get_weight(l,m)
    if w1 == 0:
        return find_ball(r)
    elif w1 == -1:return find_ball(scales,m)
    elif w1 == 1: return find_ball(scales,l)
