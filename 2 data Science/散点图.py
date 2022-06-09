import matplotlib.pyplot as plt
i1 = [7,8,3,7]
i2 = [10,3,9,6,1]
plt.ion()  # 打开交互模式
# 同时打开两个窗口显示图片
plt.figure()
plt.imshow(i1)
plt.figure()
plt.imshow(i2)
# 显示前关掉交互模式
plt.ioff()
plt.show()


import matplotlib.pyplot as plt
import random
print(random.randint(0, 1000))

try:
    ax = []
    ay = []
    plt.ion()
    while True:
        ax.append(random.randint(0, 1000))
        ay.append(random.randint(0, 1000))
        plt.clf()
        plt.axis([0, 1000, 0, 1000])
        plt.scatter(ax, ay)
        plt.pause(0.1)
        plt.ioff()
except:
    print("EXIT")

'''
cla()   # Clear axis即清除当前图形中的当前活动轴。其他轴不受影响。
clf()   # Clear figure清除所有轴，但是窗口打开，这样它可以被重复使用。
close() # Close a figure window

https://blog.csdn.net/SZuoDao/article/details/52973621?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.opensearch_close&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.opensearch_close
'''

