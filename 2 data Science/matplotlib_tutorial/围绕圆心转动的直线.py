#https://zhuanlan.zhihu.com/p/147943960
# 引用所需要的库
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 定义画布
fig, ax = plt.subplots()
line, = ax.plot([], [])  # 返回的第一个值是update函数需要改变的


# 获取直线的数组
def line_space(B):
    x = np.linspace(0, 10, 100)
    return x, x + B


# 这里B就是frame
def update(B):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 20)
    x, y = line_space(B)
    line.set_data(x, y)
    return line

# 使用函数并保存保存会在下一篇文章讲
# 可以用plt.show()来代替一下
# matplotlib.animation.HTMLWriter
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), interval=50)
ani.save('move1.html', writer='imagemagick', fps=10)
ani.matplotlib.animation.HTMLWriter



# 引用所需要的库
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#
# # 定义画布
fig, ax = plt.subplots()
line, = ax.plot([], [])  # 返回的第一个值是update函数需要改变的
# 定义初始函数
def ini():
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    return line


def update(theta):
    x, y = round(theta)
    line.set_data(x, y)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    return line


theta_ = np.linspace(0, np.pi * 2, 100)
x_round = np.cos(theta_)
y_round = np.sin(theta_)
ax.plot(x_round, y_round)
ax.grid()
ax.axis('scaled')
ani = FuncAnimation(fig, update, init_func=ini, frames=np.linspace(0, 2 * np.pi, 100), interval=10)
# 保存会在下一篇文章讲
ani.save('move.html', writer='ddm', fps=10)