'''
https://cookieblues.github.io/guides/2021/02/15/bare-minimum-matplotlib/


Matplotlib的最低限度指南
2021年2月15日
Matplotlib的最低限度指南

如果你想在Python中处理数组，你可以使用NumPy。如果你想处理表格数据，你可以使用Pandas。用于数据可视化的典型的Python库是Matplotlib。它很容易使用，很灵活，而且很多其他的可视化库都是建立在Matplotlib的基础上。这意味着，学习Matplotlib将使我们更容易理解和使用一些更花哨的可视化库。

开始学习
你需要安装Matplotlib库。假设你有一些终端可以使用，并且安装了pip，你可以用下面的命令来安装Matplotlib：pip install matplotlib。你可以在Matplotlib的安装指南中阅读更多关于安装的内容。

两种方法
我们将首先用两种不同的方法制作一个简单的散点图："天真 "的方法和面向对象的方法。这两种方法都有其优点和缺点。一般来说，我们可以说，当你需要多个相邻的图时，面向对象的方法是最好的。但我几乎总是使用面向对象的方法，即使我不需要做多个图。

Naive
首先，我们必须导入matplotlib。plt框架是我们用于Python绘图的工具。
'''

import matplotlib.pyplot as plt
import numpy as np

#我们还导入了numpy，所以我们可以很容易地生成要绘制的点! 让我们在正弦函数上选择一些点。
# 我们选择一些x值，然后用np.sin计算出y值。


x = np.linspace(-3, 3, num=10)
y = np.sin(x)

#现在我们已经生成了我们的点，我们可以做我们的散点图了! 我们使用plt框架中的散点函数来
# 绘制，并使用show来可视化我们的图。

plt.scatter(x, y)
plt.show()

#通过运行这66行，应该会出现一个带有以下绘图的窗口。
#如果我们不想要散点图而想要直线图，我们可以把散点图换成绘图。


plt.plot(x, y)
plt.show()


#这样我们就得到了下面的图。
#然而，这条线是非常锯齿状的。我们可以通过生成更多的点来使其更加平滑。


x = np.linspace(-3, 3, num=100)
y = np.sin(x)

plt.plot(x, y)
plt.show()

'''

面向对象
现在我们知道了如何制作和可视化一个绘图，让我们来看看制作相同绘图的面向对象的方法。
然而，为什么我们要知道这些呢？仅仅是因为面向对象的方式更强大，可以制作更复杂的图，
当我们想制作多个图时，就会发现这一点。

如果我们想复制之前的图，我们首先要做一个Figure对象和一个Axes对象。我们假设，我们
已经生成了我们的数据。

'''

fig = plt.figure()
ax = fig.add_subplot()


#我们可以把Figure对象看作是框架，我们想把图放进去，而Axes对象是我们框架中的一个实际图。
# 然后，我们将直线图添加到Axes对象中，并再次使用show来可视化该图。


ax.plot(x, y)
plt.show()

'''

这就生成了与之前相同的图。

线形图
下面是我们可以使用的颜色的例子。我们可以用许多不同的方式来指定颜色；十六进制代码、
RGB、普通的名字。

'''

from scipy.stats import norm
x = np.linspace(-4, 4, num=100)
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.plot(x, norm.pdf(x, loc=-1, scale=1), color="magenta")
ax.plot(x, norm.pdf(x, loc=0, scale=1), color=(0.85, 0.64, 0.12))
ax.plot(x, norm.pdf(x, loc=1, scale=1), color="#228B22")

plt.show()


#还有许多预定义的线型，我们可以使用。注意，如果不定义颜色，Matplotlib会自动为我们的
# 线条选择一些明显的默认颜色。


x = np.linspace(-6, 6, num=100)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.plot(x, norm.pdf(x, loc=-3, scale=1), linestyle="solid")
ax.plot(x, norm.pdf(x, loc=-1, scale=1), linestyle="dotted")
ax.plot(x, norm.pdf(x, loc=1, scale=1), linestyle="虚线")
ax.plot(x, norm.pdf(x, loc=3, scale=1), linestyle="dashdot")

plt.show()


#我们还可以调整线的宽度!
x = np.linspace(-2, 9, num=100)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

for i in range(1,7):
    ax.plot(x, norm.pdf(x, loc=i, scale=1), color="black", lineewidth=i/2)

plt.show()

#散点图
#对于散点图，我们可以改变标记和它们的大小。下面是一个例子

x = np.linspace(-4, 4, num=20)
y1 = x
y2 = -y1
y3 = y1**2

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.scatter(x=x, y=y1, marker="v", s=1)
ax.scatter(x=x, y=y2, marker="X", s=5)
ax.scatter(x=x, y=y3, marker="s", s=10)

plt.show()

#我们还可以通过改变fmt参数，使用ax.plot函数将直线图和散点图结合起来。fmt参数由标记、
# 线和颜色的部分组成：fmt = [marker][line][color]。如果fmt = "s--m"，那么我们
# 就有正方形的标记，一条虚线，并且它们会被染成品红色。


x = np.linspace(-2, 2, num=20)
y = x ** 3 - x

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.plot(x, y, 'H-g')

plt.show()



#直方图我们可以制作直方图

x = np.random.randn(10000)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.hist(x)

plt.show()

x1 = np.random.randn(10000)-1
x2 = np.random.randn(10000)+1

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.hist(x1, color='turquoise', edgecolor='none', bins=50, alpha=0.5, density=True)
ax.hist(x2, color='magenta', edgecolor='none', bins=200, alpha=0.5, density=True)

plt.show()

#当然，我们要为我们的绘图添加一个图例。这可以通过ax.legend函数简单完成。

x = np.linspace(-2, 2, num=100)
y1 = x
y2 = x**2

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.plot(x, y1, color='turquoise', label='First')
ax.plot(x, y2, color='magenta', label='Second')

ax.legend()

plt.show()

#Matplotlib会自动为图例找到最佳位置，但我们可以通过为loc参数提供一个参数来改变它。
# 另外，一个常见的偏好是不在图例周围设置框架，我们可以通过设置frameon参数为False来禁用它。此外，Matplotlib在一列中列出了图例的元素，但我们可以在ncol参数中提供要使用的列数。

x = np.linspace(-2, 2, num=100)
y1 = x
y2 = np.sin(x)+np.cos(x)
y3 = x**2

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.plot(x, y1, color='turquoise', label='First')
ax.plot(x, y2, color='magenta', label='Second')
ax.plot(x, y3, color='森林绿', label='第三')

ax.legend(loc='lower center', frameon=False, ncol=3)

plt.show()


'''

最后的提示
你可以用Matplotlib做很多神奇的事情，不能在这里提供所有这些。不过，有几个准则可以让你开始使用。

你可以用plt.savefig()函数保存数字。
有一堆建立在Matplotlib肩膀上的库，可能对你试图创建的特定绘图有益，例如，Seaborn、Bokeh、Plotly，
'''