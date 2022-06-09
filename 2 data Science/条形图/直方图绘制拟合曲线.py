
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pandas

# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width','petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
print(dataset.head(10))
# descriptions
print(dataset.describe())
x = dataset.iloc[:,0] #提取第一列的sepal-length变量
mu =np.mean(x) #计算均值
sigma =np.std(x)
mu,sigma


#2
import seaborn as sns
sns.set_palette("hls") #设置所有图的颜色，使用hls色彩空间
sns.distplot(x,color="r",bins=30,kde=True)
plt.show()

import seaborn as sns
import matplotlib as mpl
sns.set_palette("hls")
mpl.rc("figure", figsize=(6,4))
sns.distplot(x,bins=30,kde_kws={"color":"seagreen", "lw":3 }, hist_kws={ "color": "b" })
plt.show()



# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width','petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
print(dataset.head(10))
# descriptions
print(dataset.describe())
x = dataset.iloc[:,0] #提取第一列的sepal-length变量
mu =np.mean(x) #计算均值
sigma =np.std(x)
mu,sigma


num_bins = 30 #直方图柱子的数量

n, bins, patches = plt.hist(x, num_bins,normed=1, facecolor='blue', alpha=0.5)
#直方图函数，x为x轴的值，normed=1表示为概率密度，即和为一，绿色方块，色深参数0.5.返回n个概率，直方块左边线的x值，及各个方块对象
y = mlab.normpdf(bins, mu, sigma)#拟合一条最佳正态分布曲线y
plt.plot(bins, y, 'r--') #绘制y的曲线
plt.xlabel('sepal-length') #绘制x轴
plt.ylabel('Probability') #绘制y轴
plt.title(r'Histogram : $\mu=5.8433$,$\sigma=0.8253$')#中文标题 u'xxx'

plt.subplots_adjust(left=0.15)#左边距
plt.show()