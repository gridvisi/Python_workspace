
import math
import statistics
#import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy
#  matplotlib.axes.Axes.hist() 方法的接口
n, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My Very Own Histogram')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# 设置y轴的上限
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
import pandas as pd



size, scale = 1000, 10
commutes = pd.Series(np.random.gamma(scale, size=size) ** 1.5)

commutes.plot.hist(grid=True, bins=20, rwidth=0.9,
                   color='#607c8e')
plt.title('Commute Times for 1,000 Commuters')
plt.xlabel('Counts')
plt.ylabel('Commute Time')
plt.grid(axis='y', alpha=0.75)



'''
salary = [2500, 3300, 2700, 5600, 6700, 5400, 3100, 3500, 7600, 7800,
          8700, 9800, 10400]

group = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000]

plt.hist(salary, group, histtype='bar', rwidth=0.8)
plt.legend()
plt.xlabel('salary-group')
plt.ylabel('salary')
plt.title(u'测试例子——直方图', FontProperties=font)
plt.show()
'''
'''

from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
import matplotlib.pyplot as plt

#  matplotlib.axes.Axes.hist() 方法的接口
n, bins, patches = plt.hist(x=5, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My Very Own Histogram')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# 设置y轴的上限
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
'''
