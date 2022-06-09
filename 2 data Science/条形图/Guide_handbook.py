'''
https://chenzhen.blog.csdn.net/article/details/100047692?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_default&utm_relevant_index=5

1. 竖放条形图
bar(x, height, [width], **kwargs)
2. 横放条形图
bar(x, width, [height], **kwargs)
3. 并列条形图
'''

import matplotlib.pyplot as plt

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

waters = ('碳酸饮料', '绿茶', '矿泉水', '果汁', '其他')
buy_number = [6, 7, 6, 1, 2]

plt.bar(waters, buy_number)
plt.title('男性购买饮用水情况的调查结果')

plt.show()


#

import matplotlib.pyplot as plt

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

waters = ('碳酸饮料', '绿茶', '矿泉水', '果汁', '其他')
buy_number = [6, 7, 6, 1, 2]

plt.barh(waters, buy_number)  # 横放条形图函数 barh
plt.title('男性购买饮用水情况的调查结果')

plt.show()

'''
3. 并列条形图
若要将男生与女生的调查情况画出两个条形图一块显示，则可以使用 bar 或 barh 函数两次，
并调整 bar 或 barh 函数的条形图位置坐标以及相应刻度，使得两组条形图能够并排显示。
'''

import matplotlib.pyplot as plt
import numpy as np

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 输入统计数据
waters = ('碳酸饮料', '绿茶', '矿泉水', '果汁', '其他')
buy_number_male = [6, 7, 6, 1, 2]
buy_number_female = [9, 4, 4, 5, 6]

bar_width = 0.3  # 条形宽度
index_male = np.arange(len(waters))  # 男生条形图的横坐标
index_female = index_male + bar_width  # 女生条形图的横坐标

# 使用两次 bar 函数画出两组条形图
plt.bar(index_male, height=buy_number_male, width=bar_width, color='b', label='男性')
plt.bar(index_female, height=buy_number_female, width=bar_width, color='g', label='女性')

plt.legend()  # 显示图例
plt.xticks(index_male + bar_width/2, waters)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.ylabel('购买量')  # 纵坐标轴标题
plt.title('购买饮用水情况的调查结果')  # 图形标题

plt.show()

'''
主要用的方法为：


atplotlib.pyplot.bar(left, height, width=0.8, bottom=None, hold=None, data=None, **kwargs)
参数说明：

left: 每一个柱形左侧的X坐标

height:每一个柱形的高度

width: 柱形之间的宽度

bottom: 柱形的Y坐标

color: 柱形的颜色

下面是代码示例：

'''

# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

X = [0, 1, 2, 3, 4, 5]
Y = [222, 42, 455, 664, 454, 334]
fig = plt.figure()
plt.bar(X, Y, 0.4, color="green")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("bar chart")

plt.show()
plt.savefig("barChart.jpg")


#4
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# 数据
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(10000)

num_bins = 50
# the histogram of the data
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='blue', alpha=0.5)

# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
plt.savefig("hist.jpg")




# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def draw_bar(labels, quants):
    width = 0.4
    ind = np.linspace(0.5, 9.5, 10)
    # make a square figure
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    # Bar Plot
    ax.bar(ind - width / 2, quants, width, color='green')
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    # labels
    ax.set_xlabel('Country')
    ax.set_ylabel('GDP (Billion US dollar)')
    # title
    ax.set_title('Top 10 GDP Countries', bbox={'facecolor': '0.8', 'pad': 5})
    plt.grid(True)
    plt.show()
    plt.savefig("bar.jpg")
    plt.close()


labels = ['USA', 'China', 'India', 'Japan', 'Germany', 'Russia', 'Brazil', 'UK', 'France', 'Italy']

quants = [15094025.0, 11299967.0, 4457784.0, 4440376.0, 3099080.0, 2383402.0, 2293954.0, 2260803.0, 2217900.0,
          1846950.0]

#draw_pie(labels, quants)
