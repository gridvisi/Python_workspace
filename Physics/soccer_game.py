'''
一、素材
因为是个模拟实验，重在功能的实现，所以素材方面就没搞得太复杂，只有一个小球图片和
一个撞击音效，下面的链接里有我打包好的素材。

在公众号回复足球可以获得下载链接。

二、程序部分
2.1 pygame最小系统

'''
import pygame, sys

# 初始化
pygame.init()

# 创建游戏窗口
WIN_SIZE = WIN_W, WIN_H = 800, 600
window = pygame.display.set_mode(WIN_SIZE)
# 设置标题
pygame.display.set_caption("弹力球")
# 设置背景颜色
window.fill((255, 255, 255))  # 白色

#主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 屏幕刷新
    pygame.display.update()


#2.2 加入小球
#将以下代码添加到主循环的上方（注：图片文件和后面的音频文件要放在与.py文件同一目录下）

#小球
ball_x = 0          #初始x坐标
ball_y = 0          #初始y坐标
ball = pygame.image.load("ball.jpg")
ball_w, ball_h = ball.get_size()
window.blit(ball, (ball_x, ball_y))

#2.3 让小球动起来
#小球
ball_x = 0          #初始x坐标
ball_y = 0          #初始y坐标
v = 3               #小球速度
ball = pygame.image.load("ball.jpg")
ball_w, ball_h = ball.get_size()
window.blit(ball, (ball_x, ball_y))

#主循环
t = 0                #时间
while True:
    t += 0.1
    s_down = v * t
    ball_y = s_down
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    window.fill((255, 255, 255))
    window.blit(ball, (ball_x, ball_y))

    # 屏幕刷新
    pygame.display.update()

'''
在加入此段代码后可以发现小球会向下做匀速直线运动了，接下来让小球在到达边界时反弹回来。

2.4 边界检测
为了便于后续扩展，先将小球的运动分为向下和向上两部分，并给小球添加一个运动方向的标志。
'''

#下面是主循环部分的代码调整，其中加入了边界检测功能。

while True:
    t += 0.1
    #向下运动
    if to_down:
        s_down = v * t
        ball_y = s_down
        #边界检测
        if ball_y >= WIN_H - ball_h:
            t = 0
            to_down = False
    #向上运动
    else:
        s_up = v * t
        ball_y = (WIN_H - ball_h) - s_up
        #边界检测
        if ball_y <= 0:
            t = 0
            to_down = True

#好了，到此为止小球就可以做往返匀速直线运动了，接下来进入到关键部分。
#2.5 加入重力
#下面让小球受到重力影响下落（忽略空气阻力）。小球在重力影响下不再做匀速运动，
# 固在小球的初始设置部分删除代码v = 3，并添加重力加速度：g = 10。
# 先回顾一下匀加速运动的速度和位移公式：

#下面是主循环部分的代码调整。

#主循环
t = 0
while True:
    t += 0.01
    #向下运动
    if to_down:
        v_down = g * t
        s_down = 1/2 * g * t * t
        ball_y = s_down
        #边界检测
        if ball_y >= WIN_H - ball_h:
            t = 0
            to_down = False
    #向上运动
    else:
        v_up = v_down - g * t
        s_up = v_down * t - 1/2 * g * t * t
        ball_y = (WIN_H - ball_h) - s_up
        #边界检测
        if ball_y <= 0:
            t = 0
            to_down = True

#2.7 给水平方向加点初速度
#自由落体模拟实验已经完成了，接下来进行平抛模拟实验。给小球一个水平方向的初速度，
# 由于小球在水平方向上不受力，所以会在水平方向上做匀速直线运动。先为小球的初始设置加入一行代码：v0_x = 0.2，表示水平方向初始速度。再将ball_x += v0_x分别添加到向下运动部分的ball_y = highest + s_down和向上运动部分的ball_y = (WIN_H - ball_h) - s_up之前。这样，小球就会按抛物线的轨迹运动了。当然还要加入左右的边界检测：

    # 左右边界检测
    if ball_x >= WIN_W-ball_w or ball_x <=0:
        v0_x = -v0_x

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
#运行程序之后，你会发现一个明显的问题，就是小球最终会在地面上一直移动，这是因为我们还没有写让小球停止的程序。

#2.8 让小球停下来
#为了让小球停下里，我们不得不再引入一个标志变量，把stop = False加入到小
# 球的初始设置里吧。然后把主循环中事件检测之前的所有代码都放到分支结构中去。

while True:
    if not stop:
        t += 0.01
        #向下运动
        if to_down:
#在每次小球到达最高点时判断是否停止运动。

#到达最高点
if v_up <= 0:
    t = 0
    to_down = True
    highest = ball_y
    # 停止运动
        if highest >= WIN_H - ball_h:
            stop = True
#看看效果如何：