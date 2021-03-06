
from pyecharts import options as opts
from pyecharts.charts import Geo
#from pyecharts import import Geo
from pyecharts.faker import Faker
from pyecharts.globals import ChartType
c = (
    Geo()
    .add_schema(maptype="china")
    .add(
        "",
        [list(z) for z in zip(Faker.provinces, Faker.values())],
        type_=ChartType.HEATMAP,
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="Geo-热力地图"),
    )
)
c.render("china.html")