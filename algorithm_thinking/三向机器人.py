

import turtle as t

# 增加 4 步 1点钟方向走3步，5点钟方向走1步，
steps = [60,60,60,-60]  # 追加的4步

angles = [-60,-60,180,60,180,180,-60,180,
          60,180,60,180,180,-60,-60,-60,60,
          180,60,60,180,-60,-60]

mid = len(angles)
angles.extend(steps)
print(angles)

t.dot(10,'red')
for i,e in enumerate(angles):
    if i == mid:
        t.dot(17,'purple') #机器人在紫色位置停留

    t.speed(2)
    t.left(e)
    t.forward(80)
    t.left(-e) #
t.dot(10,'blue')
t.done()
