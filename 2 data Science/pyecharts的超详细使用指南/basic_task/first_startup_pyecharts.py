'''
http://www.361way.com/cannot-import-pie/6595.html

https://www.jianshu.com/p/554d64470ec9
'''

#from pyecharts.charts import Bar, Grid, Pie, Map, WordCloud

'''
pip install pyecharts==0.5.11
# 豆瓣源
pip install -i https://pypi.doubanio.com/simple/ pyecharts==0.5.11
'''

from pyecharts import Radar
radar = Radar("雷达图", "一年的降水量与蒸发量")
#由于雷达图传入的数据得为多维数据，所以这里需要做一下处理
radar_data1 = [[2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]]
radar_data2 = [[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]]
#设置column的最大值，为了雷达图更为直观，这里的月份最大值设置有所不同
schema = [
    ("Jan", 5), ("Feb",10), ("Mar", 10),
    ("Apr", 50), ("May", 50), ("Jun", 200),
    ("Jul", 200), ("Aug", 200), ("Sep", 50),
    ("Oct", 50), ("Nov", 10), ("Dec", 5)
]
#传入坐标
radar.config(schema)
radar.add("降水量",radar_data1)
#一般默认为同一种颜色，这里为了便于区分，需要设置item的颜色
radar.add("蒸发量",radar_data2,item_color="#1C86EE")
radar.render()


from pyecharts import Scatter
scatter = Scatter("散点图", "一年的降水量与蒸发量")
#xais_name是设置横坐标名称，这里由于显示问题，还需要将y轴名称与y轴的距离进行设置
scatter.add("降水量与蒸发量的散点分布", data1,data2,xaxis_name="降水量",yaxis_name="蒸发量",
            yaxis_name_gap=40)
scatter.render()



from pyecharts import Grid
#设置折线图标题位置
line = Line("折线图","一年的降水量与蒸发量",title_top="45%")
line.add("降水量", columns, data1, is_label_show=True)
line.add("蒸发量", columns, data2, is_label_show=True)
grid = Grid()
#设置两个图表的相对位置
grid.add(bar, grid_bottom="60%")
grid.add(line, grid_top="60%")
grid.render()


from pyecharts import Overlap
overlap = Overlap()
bar = Bar("柱状图-折线图合并", "一年的降水量与蒸发量")
bar.add("降水量", columns, data1, mark_point=["max", "min"])
bar.add("蒸发量", columns, data2, mark_point=["max", "min"])
overlap.add(bar)
overlap.add(line)
overlap.render()



from pyecharts import Pie
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例")
pie.add(
    "",
    attr,
    v1,
    is_label_show=True,
    is_more_utils=True
)
pie.render(path="Bing1.html")