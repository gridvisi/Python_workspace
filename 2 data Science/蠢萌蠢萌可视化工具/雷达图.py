

from cutecharts.charts import Radar  #雷达图


def radar_base() -> Radar:
    chart = Radar("Power Radar")
    chart.set_options(labels=[i for i in range(3)])
    chart.add_series("Faker", [4.1, 7.2, 3, 5.5])
    chart.add_series("Easyhoon", [5, 8, 2, 6])
    return chart


radar_base().render_notebook()