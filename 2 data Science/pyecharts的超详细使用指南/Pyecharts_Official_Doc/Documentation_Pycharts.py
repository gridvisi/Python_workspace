'''
https://pyecharts.readthedocs.io/projects/pyecharts-en/en/latest/en-us/documentation/

pyecharts Documentation
pyecharts is a library to generate charts using Echarts. It simply provides the interface between Echarts and Python.

Build Status codecov PyPI version License: MIT

First-steps
Global-options
xyAxis：x, y axis in cartesian coordinate system(Line, Bar, Scatter, EffectScatter, Kline)
dataZoom：dataZoom components for zoom-in and zoom-out. With them, it is possible to magnify a small area, to see the overall picture or to stay away from scattered points(Line, Bar, Scatter, EffectScatter, Kline)
legend：legend component has different symbol, colour and name, and provide the interactive clicking functions to show or hide its associated data series.
label：text string on the chart, for marking the charts with sensible details, such as value, name.
lineStyle：line style for Line, Polar, Radar, Graph, Parallel.
grid3D：gird3D components in cartesian coordinate system(Bar3D, Line3D, Scatter3D)
visualMap：It is a type of component for visual encoding, which maps the data to visual channels
Chart-types
Bar
Bar3D
EffectScatter
Funnel
Gauge
Geo
Graph
HeatMap
Kline
Line
Line3D
Liquid
Map
Parallel
Pie
Polar
Radar
Scatter
Scatter3D
WordCloud
Customize
Example
About
First-steps
Make sure you have installed the latest version pyecharts
Now, you are ready to make your first chart!
'''


#导入柱状图-Bar
from pyecharts import Bar
#设置行名
columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#设置数据
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
#设置柱状图的主标题与副标题
bar = Bar("柱状图", "一年的降水量与蒸发量")
#添加柱状图的数据及配置项
bar.add("降水量", columns, data1, mark_line=["average"], mark_point=["max", "min"])
bar.add("蒸发量", columns, data2, mark_line=["average"], mark_point=["max", "min"])
#生成本地文件（默认为.html文件）
bar.render()

from pyecharts import Funnel

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [20, 40, 60, 80, 100, 120]
funnel = Funnel("漏斗图示例")
funnel.add("商品", attr, value, is_label_show=True, label_pos="inside", label_text_color="#fff")
funnel.render()


from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.show_config()
bar.render()


from pyecharts import Bar
import pandas as pd

pddata = pd.Series([1, 2, 3, 4], index=[1, 'b', 'c', 'd'])
#vlst, ilst = Bar.pdcast(pddata)

#print(vlst)