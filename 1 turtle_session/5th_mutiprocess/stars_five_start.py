import turtle
import math
import time

colorList = ["red", "darkgreen", "purple", "violet", "gold"]
turtleList = []
for i in range(5):
    turtleList.append(turtle.Turtle(shape='turtle'))

for i in range(5):
    turtleList[i].color(colorList[i])
    turtleList[i].pensize(3)

# 设置5个海龟到五角星顶点的位置
turtleList[0].setposition(100 * math.cos(math.pi / 10), 100 * math.sin(math.pi / 10))
turtleList[0].lt(180)
turtleList[1].setposition(0, 100)
turtleList[1].rt(108)
turtleList[2].setposition(-100 * math.cos(math.pi / 10), 100 * math.sin(math.pi / 10))
turtleList[2].rt(36)
turtleList[3].setposition(-100 * math.cos(3 * math.pi / 10), -100 * math.sin(3 * math.pi / 10))
turtleList[3].lt(36)
turtleList[4].setposition(100 * math.cos(3 * math.pi / 10), -100 * math.sin(3 * math.pi / 10))
turtleList[4].lt(108)

# 各海龟轮流前进一小步，造成同步的效果
for i in range(int(200 * math.cos(math.pi / 10))):
    for j in range(5):
        turtleList[j].fd(1)
        time.sleep(0.1)


turtle.done()


#原文链接：https: // blog.csdn.net / kanesunny / article / details / 102647970