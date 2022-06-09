from pyecharts.charts import Gauge, Page
from pyecharts import options as opts
from pyecharts.charts import Gauge
from pyecharts import Page
c = Gauge()  # 绘制仪表盘图

# 设置仪表盘数据、颜色
c.add("业务指标", [("完成率", 60)], axisline_opts=opts.AxisLineOpts
(linestyle_opts=opts.LineStyleOpts(color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30)))

# 全局参数设置
c.set_global_opts(title_opts=opts.TitleOpts(title="Gauge - 不同颜色"), legend_opts=opts.LegendOpts(is_show=False))

# c.render_notebook()   # 在jupyter notebook中显示图表

#————————————————



from pyecharts import Gauge
from pyecharts import charts
gauge = Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 66.66)
gauge.render()

#pip install pyecharts-snapshot



from pyecharts import options as opts
from pyecharts.charts import Gauge

c = (
    Gauge()
    .add(
        "指示器",
        [("完成比率", 75.5)],
        radius="80%", # 设置比例大小
        min_=0,max_= 200, # 设置起始、终止刻度
        title_label_opts=opts.LabelOpts(
            font_size=20, color="black", font_family="Microsoft YaHei"  # 设置字体、颜色、大小
        ),
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30  # 设置区间颜色、仪表宽度
            )
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="自定义仪表盘"
        ),
        legend_opts=opts.LegendOpts(
            is_show=False
        ),
    )
#     .render("自定义仪表盘.html")
)
c.render_notebook()