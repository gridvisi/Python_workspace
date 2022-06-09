# https://zhuanlan.zhihu.com/p/135405141
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
y1 = []
for i in range(50):
    y1.append(i)  # 每迭代一次，将i放入y1中画出来
    ax.cla()   # 清除键
    ax.bar(y1, label='test', height=y1, width=0.3)
    ax.legend()
    plt.pause(0.1)

import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 100, 0, 1])
plt.ion()

xs = [0, 0]
ys = [1, 1]

for i in range(100):
    y = np.random.random()
    xs[0] = xs[1]
    ys[0] = ys[1]
    xs[1] = i
    ys[1] = y
    plt.plot(xs, ys)
    plt.pause(0.1)
