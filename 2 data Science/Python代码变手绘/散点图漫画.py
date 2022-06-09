

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
#数据准备
from sklearn import datasets

iris = datasets.load_iris()
x, y = iris.data, iris.target
pd_iris = pd.DataFrame(np.hstack((x, y.reshape(150, 1))),
                       columns=[
                           'sepal length(cm)', 'sepal width(cm)',
                           'petal length(cm)', 'petal width(cm)', 'class'
                       ])
with plt.xkcd():

    plt.figure(dpi=150)  #设置图的分辨率
    #plt.style.use('Solarize_Light2')  #使用Solarize_Light2风格绘图
    iris_type = pd_iris['class'].unique()  #根据class列将点分为三类
    iris_name = iris.target_names  #获取每一类的名称
    colors = ['#dc2624', '#2b4750', '#45a0a2']  #三种不同颜色
    markers = ['$\clubsuit '"."', '"+"]  #三种不同图形

    for i in range(len(iris_type)):
        plt.scatter(
            pd_iris.loc[pd_iris['class'] == iris_type[i],
                        'sepal length(cm)'],  #传入数据x
            pd_iris.loc[pd_iris['class'] == iris_type[i],
                        'sepal width(cm)'],  #传入数据y
            s=50,  #散点图形（marker）的大小
            c=colors[i],  #marker颜色
            marker=markers[i],  #marker形状
            #marker=matplotlib.markers.MarkerStyle(marker = markers[i],fillstyle='full'),#设置marker的填充
            alpha=0.8,  #marker透明度，范围为0-1
            facecolors='r',  #marker的填充颜色，当上面c参数设置了颜色，优先c
            edgecolors='none',  #marker的边缘线色
            linewidths=1,  #marker边缘线宽度，edgecolors不设置时，该参数不起作用
            label=iris_name[i])  #后面图例的名称取自label

    plt.legend(loc='upper right')
