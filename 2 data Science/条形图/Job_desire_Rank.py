import numpy as np
import matplotlib.pyplot as plt

# 中文乱码和坐标轴负号处理。
plt.rc('font', family='SimHei', weight='bold')
plt.rcParams['axes.unicode_minus'] = False


job = ["data science", "artificial intelligence",
       "software develop", "machine learning",
       "analytic", "cloud computer", "management",
       "digital marketing", "cyber secruity",
       "sales", "design"
       ]

print(len(job))
percentage = [2 * i for i in range(10)]

# 绘图
fig, ax = plt.subplots()
b = ax.barh(range(len(job)), percentage, color='#6000CC')

# params

# x: 条形图x轴
# y：条形图的高度
# width：条形图的宽度 默认是0.8
# bottom：条形底部的y坐标值 默认是0
# align：center / edge 条形图是否以x轴坐标为中心点或者是以x轴坐标为边缘


yline = job

# 为横向水平的柱图右侧添加数据标签。


plt.xlabel('percentage of aspirants interest')
plt.ylabel('Domains')
plt.hist(job, percentage, histtype='bar', rwidth=0.8)

plt.legend()
plt.show()