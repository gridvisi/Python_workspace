
from cutecharts.charts import Line  #折线图


def line_base() -> Line:
    chart = Line("Line")
    chart.set_options(labels=[i for i in 'ABCDE'])
    chart.add_series("day", [1, 3, 0, 7, 1])  #A类数据
    chart.add_series("night", [1, 7, 0, 3, 1])  #B类数据
    return chart


line_base().render_notebook()