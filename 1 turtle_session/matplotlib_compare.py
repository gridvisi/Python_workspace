'''
https://zhuanlan.zhihu.com/p/337172337

python matplotlib画图使用colorbar工具自定义颜色 colorbar（draw colorbar without any mapple/plot）
自定义colorbar可以画出任何自己想要的colorbar，自由自在、不受约束，不依赖于任何已有的图(plot/mappable)。这里使用的是mpl.colorbar.ColorbarBase类，而colorbar类必须依赖于已有的图。
参数可以参考下面的描述->matplotlib：
class matplotlib.colorbar.ColorbarBase(ax, cmap=None, norm=None, alpha=None, values=None, boundaries=None, orientation=‘vertical', ticklocation=‘auto', extend=‘neither', spacing=‘uniform', ticks=None, format=None, drawedges=False, filled=True, extendfrac=None, extendrect=False, label='')[source]

参数简单描述

ax :可用于设置colorbar的位置、长、宽
norm :用于规范化–设置颜色条最大最小值
cmap：颜色（可参考本篇博文的最后部分——推荐色带与自定义色带）
boundaries：要想使用extend，在norm之外，必须要有两个额外的boundaries
orientation：colorbar方向，躺平or垂直
extend：延伸方向(在norm之外colorbar可延伸)
ticks：自定义各段的tick（记号）给一个例子，首先定义一下横纵坐标的名称，以及df_int：
给一个例子，首先定义一下横纵坐标的名称，以及df_int：

labels_int = ['A', 'B', 'C', 'D']

variables_int = ['A', 'B', 'C', 'D']



# x_normed_int 可以是一个4*4的数组，经过归一化的

df_int = pd.DataFrame(, columns=variables_int, index=labels_int)

接下来就是画图了：

fig = plt.figure()

ax = fig.add_subplot(111)

cax = ax.matshow(df, interpolation='nearest', cmap='GnBu')

fig.colorbar(cax)



tick_spacing = 1

ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))



ax.set_xticklabels([''] + list(df.columns))

ax.set_yticklabels([''] + list(df.index))

plt.show()

其中：

cax = ax.matshow(df, interpolation='nearest', cmap='GnBu')

可以通过cmap修改，得到不同的颜色带
'''

import matplotlib.pyplot as plt
from matplotlib import colors as mcolors


colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

# Sort colors by hue, saturation, value and name.
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
sorted_names = [name for hsv, name in by_hsv]

n = len(sorted_names)
ncols = 4
nrows = n // ncols

fig, ax = plt.subplots(figsize=(12, 10))

# Get height and width
X, Y = fig.get_dpi() * fig.get_size_inches()
h = Y / (nrows + 1)
w = X / ncols

for i, name in enumerate(sorted_names):
    row = i % nrows
    col = i // nrows
    y = Y - (row * h) - h

    xi_line = w * (col + 0.05)
    xf_line = w * (col + 0.25)
    xi_text = w * (col + 0.3)

    ax.text(xi_text, y, name, fontsize=(h * 0.8),
            horizontalalignment='left',
            verticalalignment='center')

    ax.hlines(y + h * 0.1, xi_line, xf_line,
              color=colors[name], linewidth=(h * 0.8))

ax.set_xlim(0, X)
ax.set_ylim(0, Y)
ax.set_axis_off()

fig.subplots_adjust(left=0, right=1,
                    top=1, bottom=0,
                    hspace=0, wspace=0)
plt.show()



'''



import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = pd.read_csv('./seaborn-data-master/tips.csv')
plt.figure(dpi=120)
plt.style.use('bmh')
sns.boxplot(x="day",
            y="total_bill",
            hue="smoker",
            palette=[rgb_list[3], rgb_list[6]],  # 传入Haishoku提取的颜色号
            data=tips)
sns.despine(offset=10, trim=True)



# https://zhuanlan.zhihu.com/p/447548260

from haishoku.haishoku import Haishoku
image='./life_is_b.png'
haishoku = Haishoku.loadHaishoku(image)
haishoku.palette  #palette函数输出配色色号

color = [(0.77, (244, 247, 244)), (0.09, (116, 165, 96)), (0.06, (193, 214, 168)), (0.03, (148, 184, 124)), (0.02, (165, 196, 134)), (0.02, (86, 144, 81)), (0.01, (54, 113, 65)), (0.0, (184, 185, 148))]

rgb_list = [[i[1][0] / 255, i[1][1] / 255, i[1][2] / 255]
            for i in haishoku.palette]  # 色号简单转化为matplotlib可用的0～1之间RGB色号
plt.figure(dpi=120)
plt.style.use('bmh')
plt.bar(range(2, 10), range(2, 10), color=rgb_list)  # 传入Haishoku提取的颜色号
plt.title('Colored with Haishoku', size=10)
plt.show()
'''


