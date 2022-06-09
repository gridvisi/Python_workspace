# https://zhuanlan.zhihu.com/p/83231415






from example.commons import Faker
from pyecharts import options as opts 
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

c = (
    Geo()
    .add_schema(maptype="china")
    .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="Geo-基本示例"),
    )
)

c.render()# 输出html格式
c.render_notebook()# 显示地图

geo = Geo()
geo.add_schema(maptype="china")
geo.add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(),title_opts=opts.TitleOpts(title="Geo-基本示例"))

geo .render_notebook()# 显示地图