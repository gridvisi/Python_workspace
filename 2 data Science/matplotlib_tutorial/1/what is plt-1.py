'''
https://matplotlib.org/stable/gallery/pyplots/boxplot_demo_pyplot.html#sphx-glr-gallery-pyplots-boxplot-demo-pyplot-py

https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
'''
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery')

# make data:
np.random.seed(10)
D = np.random.normal((3, 5, 4), (1.25, 1.00, 1.25), (100, 3))

# plot
fig, ax = plt.subplots()
VP = ax.boxplot(D, positions=[2, 4, 6], widths=1.5, patch_artist=True,
                showmeans=False, showfliers=False,
                medianprops={"color": "white", "linewidth": 0.5},
                boxprops={"facecolor": "C0", "edgecolor": "white",
                          "linewidth": 0.5},
                whiskerprops={"color": "C0", "linewidth": 1.5},
                capprops={"color": "C0", "linewidth": 1.5})

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()


#语法 matplotlib模块

'''
，关于该函数的语法和参数含义如下：

bar(x, height, width=0.8, bottom=None, color=None, edgecolor=None,
   linewidth=None, tick_label=None, xerr=None, yerr=None,
   label = None, ecolor=None, align, log=False, **kwargs)
1
2
3
x：传递数值序列，指定条形图中x轴上的刻度值。
height：传递数值序列，指定条形图y轴上的高度。
width：指定条形图的宽度，默认为0.8。 bottom：用于绘制堆叠条形图。
color：指定条形图的填充色。
edgecolor：指定条形图的边框色。
linewidth：指定条形图边框的宽度，如果指定为0，表示不绘制边框。
tick_label：指定条形图的刻度标签。
xerr：如果参数不为None，表示在条形图的基础上添加误差棒。
yerr：参数含义同xerr。
label：指定条形图的标签，一般用以添加图例。
ecolor：指定条形图误差棒的颜色。
align：指定x轴刻度标签的对齐方式，默认为center，表示刻度标签居中对齐，如果设置为edge，则表示在每个条形的左下角呈现刻度标签。
log：bool类型参数，是否对坐标轴进行log变换，默认为False。
**kwargs：关键字参数，用于对条形图进行其他设置，如透明度等。

https://blog.csdn.net/weixin_48615832/article/details/108028198?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_default&utm_relevant_index=4
'''



import matplotlib.pyplot as plt


x = [1, 2, 3, 4]
y = [1, 4, 9, 6]
labels = ['Frogs', 'Hogs', 'Bogs', 'Slogs']

plt.plot(x, y)
# You can specify a rotation for the tick labels in degrees or with keywords.
plt.xticks(x, labels, rotation='vertical')
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)
plt.show()
