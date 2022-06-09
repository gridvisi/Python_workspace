
#brilliant
#
'''

但是，当你把一叠球落下时，这一叠球中最上面的球与它下面的球相撞，反过来又与它正下方的球相撞，
以此类推。在这一连串的碰撞中，一个球可以从其他球中窃取能量，使其走得更快。这就是上边的球为
什么能走得这么高的原因。

我们先简单的从一个高尔夫球堆叠在保龄球上开始。我们来算一算，当堆叠的高尔夫球落下时，高尔夫
球能获得多少能量。与其用高度来处理，我们只看碰撞前后的速度。

在保龄球与地面相撞的那一刻，两个球都是以v的速度向下运动，假设保龄球保持了所有的动能，那么
它将以同样的速度v向上反弹，但它马上又与高尔夫球相撞，而高尔夫球仍然以v的速度向下运动。

brilliant交互做的非常细致，动态演示了大球静止和运动两种情况下，大小两球相撞后前后的运动
状态示意：
'''

"""

Solution of the Brilliant problem 2020-05-10 "

Supersonic Bouncy Ball"

"""



def number_of_balls(v_0, v_max):

    """

    Calculates the numbers of balls required to achieve v_max

    """

    res_v = 2*v_0+v_0

    num_balls = 2

    while res_v < v_max:

        res_v = 2*res_v+v_0

        num_balls += 1

    return num_balls


V_MAX = 343
FIRTS_BALL_SPEED = 1



print("The minimum number of balls required to exceed the speed"

      "最少需要的小球数量为多少时，速度超过声速"

      " {}km/h is {}. ".

     format(V_MAX, number_of_balls(FIRTS_BALL_SPEED, V_MAX)))



#最少需要的小球数量为多少时，速度超过声速
#输出 The minimum number of balls required to exceed the speed 343km/h is 9.