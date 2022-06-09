

from pyecharts.charts import Map
from pyecharts import options
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