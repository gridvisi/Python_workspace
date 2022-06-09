# 作者hanhhh
# 创建日期：2019-12-26
# 功能：用传感器读到的数据data_light画动态变化图

from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation


data_light = [
    "eecc010201011b0000000000000000ff",
    "eecc010201011a0000000000000000ff",
    "eecc01020101280000000000000000ff",
    "eecc01020100fc0000000000000000ff",
    "eecc01020101150000000000000000ff",
    "eecc010201010f0000000000000000ff",
    "eecc010201005a0000000000000000ff",
    "eecc010201005b0000000000000000ff",
    "eecc010201009c0000000000000000ff",
    "eecc01020101100000000000000000ff",
    "eecc010201011c0000000000000000ff",
    "eecc01020101150000000000000000ff",
    "eecc01020101110000000000000000ff"]
result_data = []


# 将16进制含义的字符串转化成10进制
def hex_dec(str2):
    str2 = "0x" + str2
    b = eval(str2)
    return b


for ins in data_light:
    #     print(ins)
    result_data.append(hex_dec(ins[10:14]))
print(result_data)

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(10, 4))
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 40), ylim=(0, 300))
ax.set_aspect('auto')  # 控制长宽比
# ax.grid() # 是否要格子背景
ax.axhline(20, linestyle='--', color='black')
# 设置图片标题
ax.set_title('湿度随时间的变化')
# 设置横坐标名称
ax.set_xlabel('时间')
line, = ax.plot([], [], 'o-', lw=2)

# 由于animation必须先有指定的数据或者指定的数据大小，但是我们的数据是一个一个显示的，初期是么有数据的
# 我们又必须提前填充指定个数的数据，这里我们填充x、y刻度以外的数据，然后想办法不显示
# 我们如何不显示呢？由于这些数据本质上还是要输出的，只是不让我们看见，数据既然要输出我们就要正确的设置这些数据对应的刻度
# 既然刻度不能做出改变，我们只能在刻度标签做手脚，我们让数据中x轴标签对应的刻度小于0时，标签显示空字符串
thisx = [i for i in range(-40, 0)]
thisy = (np.zeros(40, dtype=int) - 1).tolist()


def init():
    line.set_data([], [])
    return line


global kkk
kkk = 0


def animate(lent):
    # 这种操作之前一定要确保len(thisy) = len(thisx)
    global result_data
    global kkk
    i = kkk
    kkk += 1
    del thisx[0]
    del thisy[0]
    thisx.append(max(thisx) + 1)
    thisy.append(result_data[i])
    # 设置x轴的范围
    ax.set_xlim(min(thisx), max(thisx))

    # 更新刻度，刻度只要早x轴的范围内就可以
    ax.set_xticks([i for i in range(min(thisx), max(thisx) + 1, 1)])
    # 设置刻度标签
    ax.set_xticklabels(
        [i if i >= 0 else '' for i in range(min(thisx),
                                            max(thisx) + 1, 1)],
        rotation=320)
    # 重新渲染子图
    ax.figure.canvas.draw()
    line.set_data(thisx, thisy)
    return line


# blit选择更新所有点，还是仅更新产生变化的点。应选择True
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=len(result_data),
                              interval=2000,
                              blit=False,
                              init_func=init)
# ani.save('jieky_animation.gif',writer='imagemagick')
plt.show()

# 创建：2019-12-27
# 用意：读取数据库db中light_equipment表中的数据，并实现实时画动态图

import serial
import easygui
import time
import threading
import pymysql

from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

global result_data
result_data = []

global i
i = 1


def hex_dec(str2):
    str2 = "0x" + str2
    b = eval(str2)
    return b


# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(10, 4))
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 40), ylim=(0, 600))  # 设置横轴范围和纵轴范围
ax.set_aspect('auto')  # 控制长宽比
# ax.grid() # 是否要格子背景
ax.axhline(20, linestyle='--', color='black')
# 设置图片标题
ax.set_title('湿度随时间的变化')
# 设置横坐标名称
ax.set_xlabel('时间')
line, = ax.plot([], [], 'o-', lw=2)

# 初始化
thisx = [i for i in range(-40, 0)]
thisy = (np.zeros(40, dtype=int) - 1).tolist()


def init():
    line.set_data([], [])
    return line


global kkk
kkk = 0


def animate(lent):
    # 这种操作之前一定要确保len(thisy) = len(thisx)
    #    global result_data
    global kkk
    del thisx[0]
    del thisy[0]
    # 连接数据库
    coon = pymysql.connect(
        host='127.0.0.1', user='root', passwd='a123a123',
        port=3306, db='user-msg', charset='utf8'
        #    port必须写int类型
        #    charset必须写utf8，不能写utf-8
    )
    cur = coon.cursor()  # 建立游标
    cur.execute("select num from light_equipment where id=%d" % kkk)  # 查询数据
    res = cur.fetchone()  # 获取结果
    coon.close()
    num = res[0]
    kkk += 1
    thisx.append(max(thisx) + 1)
    thisy.append(num)
    # 设置x轴的范围
    ax.set_xlim(min(thisx), max(thisx))

    # 更新刻度，刻度只要早x轴的范围内就可以
    ax.set_xticks([i for i in range(min(thisx), max(thisx) + 1, 1)])
    # 设置刻度标签
    ax.set_xticklabels(
        [i if i >= 0 else '' for i in range(min(thisx),
                                            max(thisx) + 1, 1)],
        rotation=320)
    # 重新渲染子图
    ax.figure.canvas.draw()
    line.set_data(thisx, thisy)
    return line


# blit选择更新所有点，还是仅更新产生变化的点。应选择True
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=111,
                              # fargs
                              interval=2000,
                              blit=False,
                              init_func=init)
# ani.save('jieky_animation.gif',writer='imagemagick')
plt.show()



# kkk=0
# while(kkk<10):
#    cur.execute("select num from light_equipment where id=%d"%kkk)  #查询数据
#    kkk+=1
#    res = cur.fetchone()    #获取结果

#    num=res[0]

#    print(num)

