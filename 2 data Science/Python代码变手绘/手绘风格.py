# ：Python可视化|matplotlib12-垂直|水平|堆积条形图详解
import matplotlib.pyplot as plt
import numpy as np
with plt.xkcd():
    plt.figure(dpi=150)
    labels = ['Jack', 'Rose', 'Jimmy']
    year_2019 = np.arange(1, 4)
    year_2020 = np.arange(1, 4) + 1
    bar_width = 0.4

    plt.bar(
        np.arange(len(labels)) - bar_width / 2,  #为了两个柱子一样宽
        year_2019,
        color='#dc2624',
        width=bar_width,
        label='year_2019'  #图例
    )
    plt.bar(
        np.arange(len(labels)) + bar_width / 2,
        year_2020,
        color='#45a0a2',
        width=bar_width,
        label='year_2020'  #图例
    )
    plt.xticks(np.arange(0, 3, step=1), labels, rotation=45)  #定义柱子名称
    plt.legend(loc=2)  #图例在左边


    
import matplotlib.pyplot as plt

with plt.xkcd():
    from string import ascii_letters
    plt.figure(dpi=150)
    patches, texts, autotexts = plt.pie(
        x=range(1, 12),
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