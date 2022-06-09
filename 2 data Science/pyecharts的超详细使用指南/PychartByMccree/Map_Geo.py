from pyecharts import Gauge

gauge = Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 66.66)
gauge.render()

from pyecharts import Map
"""
世界地图
"""
value = [95.1, 23.2, 43.3, 66.4, 88.5, 36.5, 2.5, 78.5]
attr = ["China", "Canada", "Brazil", "Russia", "United States", "India", 'Sudan', 'Australia']
map0 = Map("viz的世界", width=1200, height=600)
map0.add("世界地图", attr, value, maptype="world", is_visualmap=True)
map0.render(path="世界地图.html")



from pyecharts import Gauge
gauge=Gauge("指标完成率")
gauge.add("业务指标","完成率",95)
gauge.render()
'''

#from pyecharts.charts import Map
from pyecharts import Map
import random

province_city = ["江北区"]
data_province_city = [(i, random.randint(0, 500)) for i in province_city]

cq_map = Map()
cq_map.add("", data_province_city, "重庆")
cq_map.render("cq.html")



#-----------------------
def map_world() ->Map:
    c = (
        Map()
        .add("",[list(z) for z in zip(country,value)],"world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="世界地图"),
            visualmap_opts=opts.VisualMapOpts(max_=2000)
        )

    )


'''