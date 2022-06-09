# https://seaborn.pydata.org/

'''
 heatmap(热力图)是识别预测变量与目标变量相关性的方法，同时，也是发现变量间是否存在多重共线性的好方法。
中文文档

seaborn.heatmap(data, vmin=None, vmax=None, cmap=None, center=None, robust=False, annot=None, fmt='.2g',
annot_kws=None,linewidths=0, linecolor='white', cbar=True, cbar_kws=None, cbar_ax=None, square=False,
xticklabels='auto', yticklabels='auto',mask=None, ax=None, **kwargs)
1
2
3
这些参数具体什么含义，怎么使用见中文文档
常用参数：

data:矩形数据集
可以强制转换为ndarray格式数据的2维数据集。如果提供了Pandas DataFrame数据，索引/列信息将用于标记列和行。那么如果提供了关系矩阵就可以显示变量之间的相关性。
vmin, vmax：浮点型数据，可选参数
用于锚定色彩映射的值，否则它们是从数据和其他关键字参数推断出来的
cmap：matplotlib 颜色条名称或者对象，或者是颜色列表，可选参数
从数据值到颜色空间的映射。 如果没有提供，默认值将取决于是否设置了“center”
center：浮点数，可选参数
绘制有色数据时将色彩映射居中的值。 如果没有指定，则使用此参数将更改默认的cmap
annot:布尔值或者矩形数据，可选参数
如果为True，则在每个热力图单元格中写入数据值。 如果数组的形状与data相同，则使用它来代替原始数据注释热力图
mask：布尔数组或者DataFrame数据，可选参数
如果为空值，数据将不会显示在mask为True的单元格中。 具有缺失值的单元格将自动被屏蔽
cbar：布尔值，可选参数
描述是否绘制颜色条
square：布尔值，可选参数
如果为True，则将坐标轴方向设置为“equal”，以使每个单元格为方形
xticklabels, yticklabels：“auto”，布尔值，类列表值，或者整形数值，可选参数
如果为True，则绘制数据框的列名称。如果为False，则不绘制列名称。如果是列表，则将这些替代标签绘制为xticklabels。如果是整数，则使用列名称，但仅绘制每个n标签。如果是“auto”，将尝试密集绘制不重叠的标签。
fmt：字符串，可选参数
添加注释时要使用的字符串格式代码
annot_kws：字典或者键值对，可选参数
当annot为True时，ax.text的关键字参数
ax：matplotlib Axes，可选参数
绘制图的坐标轴，否则使用当前活动的坐标轴
返回热力图对象

使用1：关系矩阵
这个函数将矩形数据绘制为颜色编码矩阵。所以得先通过pandas中corr()方法获得关系矩阵。
————————————————
版权声明：本文为CSDN博主「哎呦-_-不错」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_46649052/article/details/115231716


使用时有两个小技巧，

（1）先用sns.set(font_scale)修改字体比例:

sns.set(font_scale=1.5)
（2）再用plt.rc对全图字体进行统一修改:

plt.rc('font',family='Times New Roman',size=12)

2. 颜色效果
cmap的参数如下：

Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu(绿到蓝), GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd（橘色到红色）, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia（蓝绿黄）, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd（红橙黄）, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm（蓝到红）, coolwarm_r, copper（铜色）, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r（红黄）, hsv, hsv_r, icefire, icefire_r, inferno, inferno_r, jet, jet_r, magma, magma_r, mako, mako_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, rocket, rocket_r, seismic, seismic_r, spring, spring_r, summer (黄到绿), summer_r (绿到黄), tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, twilight, twilight_r, twilight_shifted, twilight_shifted_r, viridis, viridis_r, vlag, vlag_r, winter, winter_r

示范如下：

cmap="YlGnBu"：数字越大，颜色越深
————————————————
版权声明：本文为CSDN博主「兔子爱读书」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/ztf312/article/details/102474190
'''
import pandas as df
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(data, vmin=None, vmax=None, cmap=None, center=None, robust=False, annot=None, fmt='.2g',
annot_kws=None,linewidths=0, linecolor='white', cbar=True, cbar_kws=None, cbar_ax=None, square=False,
xticklabels='auto', yticklabels='auto',mask=None, ax=None, **kwargs)


# 设置绘图风格
style.use('ggplot')
sns.set_style('whitegrid')
# 设置画板尺寸
plt.subplots(figsize=(30, 20))

# 画热力图
# 为上三角矩阵生成掩码
mask = np.zeros_like(train.corr(), dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

sns.heatmap(train.corr(),
            cmap=sns.diverging_palette(20, 220, n=200),
            mask=mask,  # 数据显示在mask为False的单元格中
            annot=True,  # 注入数据
            center=0,  # 绘制有色数据时将色彩映射居中的值
            )
# Give title.
plt.title("Heatmap of all the Features", fontsize=30)