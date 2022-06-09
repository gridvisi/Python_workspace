
import turtle

"""
R:red, G:green, B:blue
RGB颜色表示法:
    red: (255,0,0)
    green: (0,255,0) 
    blue: (0,0,255)
"""
# 1. 生成渐变色的列表
# 从红色到黄色
colors1 = [(255, g, 0) for g in range(0, 256)]
# 从黄色到绿色
colors2 = [(r, 255, 0) for r in range(255, -1, -1)]
# 从绿色到青色
colors3 = [(0, 255, b) for b in range(0, 256)]
# 从青到蓝
colors4 = [(0, g, 255) for g in range(255, -1, -1)]
# 从蓝到紫
colors5 = [(r, 0, 255) for r in range(0, 256)]
# 从紫到红
colors6 = [(255, 0, g) for g in range(255, -1, -1)]
# colors = colors1 + colors2 + colors3 + colors4 + colors5 + colors6
colors = colors1 + colors2 + colors3 + colors4 + colors5 + colors6
n = len(colors)
print('colors',n,colors)
# 2. 基于turtle生成彩虹糖(可根据自己的喜好调整彩虹棒棒糖的颜色)
# 画笔的大小: 20px
turtle.pensize(25)
# 画图的速度，0代表最快速度
turtle.speed(0)
# 设置turtle指定颜色的模式, 255代表rgb模式
turtle.colormode(255)
# 循环1000次不断画圆，画圆的同时不断调整圆的半径
for i in range(1000):
    # 如果颜色超出给定的范围，和总颜色个数取余，从头开始获取颜色。
    #color = (250-i//4, 255, 100)

    turtle.color(colors[i])
    turtle.circle(i // 3, 5)
# 彩虹色棒棒糖绘制完成
turtle.done()
