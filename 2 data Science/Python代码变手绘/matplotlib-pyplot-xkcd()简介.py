'''
matplotlib-pyplot-xkcd()简介

前景提要： 之前介绍过一个绘制手绘风格图形的工具cutecharts：一款蠢萌蠢萌的
可视化工具

但是，其功能有限，今天再介绍一个手绘工具（matplotlib.pyplot.xkcd()），
一行代码可将所有Matplotlib和Seaborn绘制的图形变为手绘风格。

matplotlib.pyplot.xkcd()简介
这个Matplotlib子函数特别简单，只有三个参数，别看参数少，但功能可不小

matplotlib.pyplot.xkcd(scale=1, #相对于不使用xkcd的风格图，褶皱的幅度
                       length=100, #褶皱长度
                       randomness=2#褶皱的随机性
                      )
matplotlib.pyplot.xkcd()使用
如下，加with行代码即可，括号中参数按个人喜好决定是否设置～

with plt.xkcd(scale=1, length=100, randomness=2):
#with是临时使用一下，不影响其它图使用正常样式
    绘图代码
    。。。。。。
    plt.show()
matplotlib.pyplot.xkcd()使用实例
以下参考：Python可视化25|seaborn绘制矩阵图
'''

import matplotlib.pyplot as plt
with plt.xkcd(
        scale=4,  #相对于不使用xkcd的风格图，褶皱的幅度
        length=120,  #褶皱长度
        randomness=2):  #褶皱的随机性
    plt.figure(dpi=150)
    patches, texts, autotexts = plt.pie(
        x=[1, 1, 1],  #返回三个对象
        labels=['A', 'B', 'C'],
        colors=['#dc2624', '#2b4750', '#45a0a2'],
        autopct='%.2f%%',
        explode=(0.1, 0, 0))
    texts[1].set_size('20')  #修改B的大小

    #matplotlib.patches.Wedge
    patches[0].set_alpha(0.3)  #A组分设置透明度
    patches[2].set_hatch('|')  #C组分添加网格线
    patches[1].set_hatch('x')

    plt.legend(
        patches,
        ['A', 'B', 'C'],  #添加图例
        title="Pie Learning",
        loc="center left",
        fontsize=15,
        bbox_to_anchor=(1, 0, 0.5, 1))

    plt.title('Lovely pie', size=20)
    plt.show()

with plt.xkcd():
    from string import ascii_letters
    plt.figure(dpi=150)
    patches, texts, autotexts = plt.pie(
        x = range(1, 12),
        labels=list(ascii_letters[26:])[0:11],
        colors=[
            '#dc2624', '#2b4750', '#45a0a2', '#e87a59', '#7dcaa9', '#649E7D',
            '#dc8018', '#C89F91', '#6c6d6c', '#4f6268', '#c7cccf'
        ],
        autopct='%.2f%%',
    )
    plt.legend(
        patches,
        list(ascii_letters[26:])[0:11],  #添加图例
        title="Pie Learning",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        ncol=2,  #控制图例中按照两列显示，默认为一列显示，
    )
#支持seaborn
import seaborn as sns
iris_sns = sns.load_dataset("iris")
with plt.xkcd():
    g = sns.pairplot(
        iris_sns,
        hue='species',  #按照三种花分类
        palette=['#dc2624', '#2b4750', '#45a0a2'])
    sns.set(style='whitegrid')
    g.fig.set_size_inches(12, 12)
    sns.set(style='whitegrid', font_scale=1.5)