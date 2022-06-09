from cutecharts.charts import Bar
def pie_radius():
    chart = Pie("Pie")
    chart.set_options(
        labels=['我是卢本伟2号', 'Faker', 'Easyhoon', 'Pawn', 'Dopa'],
        inner_radius=0,
    )
    chart.add_series([6, 5, 1, 2, 4])
    return chart


pie_radius().render_notebook()


def pie_radius():
    chart = Pie("Pie")
    chart.set_options(
        labels=['我是卢本伟2号', 'Faker', 'Easyhoon', 'Pawn', 'Dopa'],
        inner_radius=0,
    )
    chart.add_series([6, 5, 1, 2, 4])
    return chart


pie_radius().render_notebook()

from cutecharts.charts import Pie  #绘制Pie图


def pie_base() -> Pie:
    chart = Pie("MVP Pie")
    chart.set_options(labels=['我是卢本伟1号', 'Faker', 'Easyhoon', 'Pawn', 'Dopa'])
    chart.add_series([6, 5, 1, 2, 4])
    return chart


pie_base().render_notebook()  #jupyter notebook渲染