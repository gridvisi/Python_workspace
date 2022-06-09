'''
在本教程中，您将学习如何在Python中使用ggplot来使用图形语法创建数据可视化。图形语法是一个高级工具，它允许您以高效和一致的方式创建数据图。它抽象了大部分的低级细节，让你专注于为数据创建有意义的、漂亮的可视化。
有几个Python包提供了图形的语法。plotnine 是基于 R 编程语言中的 ggplot2，所以如果你有 R 的背景，那么你可以将 plotnine 视为相当于 Python 中的 ggplot2。
在本教程中，你将学习如何。
安装 plotnine 和 Jupyter Notebook
结合图形语法的不同要素。
使用 plotnine 以高效和一致的方式创建可视化。
将数据可视化导出到文件
本教程假设你已经有一些Python的经验，至少对Jupyter Notebook和pandas有一些了解。要了解这些主题，请查看 Jupyter Notebook: An Introduction and Using Pandas and Python to Explore Your Dataset.
免费下载。获取《Python Tricks》中的一个样本章节。这本书用简单的例子向你展示了Python的最佳实践，你可以立即应用，写出更多漂亮的+Pythonic代码。
 移除广告
设置您的环境
在本节中，您将学习如何设置环境。你将涵盖以下主题。
创建一个虚拟环境
安装 plotnine
安装Juptyer笔记本
虚拟环境使您能够在隔离的环境中安装软件包。当您想在不影响系统安装的情况下试用一些包或项目时，它们非常有用。
您可以在 Python 虚拟环境中了解更多关于它们的信息。A Primer 中了解更多。
运行下面的命令来创建一个名为 data-visualization 的目录和一个虚拟环境

通过www.DeepL.com/Translator（免费版）翻译
'''

from plotnine.data import mpg
from plotnine import ggplot, aes, labs, geom_point

(
    ggplot(mpg)
    + aes(x="cyl", y="hwy", color="class")
    + labs(
        x="Engine Cylinders",
        y="Miles per Gallon",
        color="Vehicle Class",
        title="Miles per Gallon for Engine Cylinders and Vehicle Classes",
    )
    + geom_point()
)

from plotnine.data import economics

from plotnine import ggplot, aes, geom_line
ggplot(economics)  # What data to use
6 + aes(x="date", y="pop")  # What variable to use
7 + geom_line()  # Geometric object to use for drawing


from plotnine.data import economics
from plotnine import ggplot, aes, geom_line

myPlot = ggplot(economics) + aes(x="date", y="pop") + geom_line()
myPlot.save("myplot.png", dpi=600)