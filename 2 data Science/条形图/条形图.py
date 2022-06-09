
# 导入模块

import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

# 导入数据

traffic_volume = {'Index': ['railway','green','water transport','air transport'],

'Jan': [31058, 255802, 52244, 57],

'Feb': [28121, 179276, 46482, 42],

'Mar': [32185, 285446, 50688, 59],

'Api': [30133, 309576, 54728, 57],

'May': [30304, 319713, 55813, 60],

'Jun': [29934, 320028, 59054, 58],

'Jul': [31002, 319809, 57353, 55],

'Aug': [31590, 331077, 57583, 57]}

data = pd.DataFrame(traffic_volume)

print(data)

# 绘图

plt.bar(np.arange(8), data.loc[0, :][1:], color='red', alpha=0.8, label='railway', align='center')

plt.bar(np.arange(8), data.loc[1, :][1:], bottom=data.loc[0, :][1:], color='green', alpha=0.8, label='highway',

align='center')

plt.bar(np.arange(8), data.loc[2, :][1:], bottom=data.loc[0, :][1:] + data.loc[1, :][1:], color='m', alpha=0.8,

label='water transport', align='center')

plt.bar(np.arange(8), data.loc[3, :][1:], bottom=data.loc[0, :][1:] + data.loc[1, :][1:] + data.loc[2, :][1:],

color='black', alpha=0.8, label='air transport', align='center')

# 添加轴标签

plt.xlabel('month')

plt.ylabel('Cargo volume (10,000 tons)')

# 添加标题

plt.title('Monthly logistics volume in 2017')

# 添加刻度标签

plt.xticks(np.arange(8), data.columns[1:])

# 设置Y轴的刻度范围

plt.ylim([0, 500000])

# 为每个条形图添加数值标签

for x_t, y_t in enumerate(data.loc[0, :][1:]):

    plt.text(x_t, y_t / 2, '%sW'% (round(y_t / 10000, 2)), ha='center', color='white', fontsize=8)

for x_g, y_g in enumerate(data.loc[0, :][1:] + data.loc[1, :][1:]):

    plt.text(x_g, y_g / 2, '%sW'% (round(y_g / 10000, 2)), ha='center', color='white', fontsize=8)

for x_s, y_s in enumerate(data.loc[0, :][1:] + data.loc[1, :][1:] + data.loc[2, :][1:]):

    plt.text(x_s, y_s - 20000, '%sW'% (round(y_s / 10000, 2)), ha='center', color='white', fontsize=8)

# 显示图例

plt.legend(loc='upper center', ncol=4)

# 显示图形

plt.show()