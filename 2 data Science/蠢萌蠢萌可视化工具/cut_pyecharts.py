

from cutecharts.charts import Bar  #绘制bar图


#语法和pyecharts是不是一样的～
def bar_base() -> Bar:
    chart = Bar("MVP of LOL Bar")
    chart.set_options(
        labels=['Faker', 'Easyhoon', 'Pawn'],  #柱子下方标签
        x_label='LOLers',  #x轴名称
        y_label='MVPs')  #y轴名称
    chart.add_series('MVP', [3, 2, 1])  #柱子高度数据
    return chart

print(bar_base())
bar_base().render_notebook()  #在jupyter notebook中渲染