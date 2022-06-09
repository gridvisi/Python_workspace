'''
https://blog.csdn.net/weixin_48615832/article/details/108028198?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_default&utm_relevant_index=4

1．matplotlib模块
应用matplotlib模块绘制条形图，需要调用bar函数，关于该函数的语法和参数含义如下：

bar(x, height, width=0.8, bottom=None, color=None, edgecolor=None,
   linewidth=None, tick_label=None, xerr=None, yerr=None,
   label = None, ecolor=None, align, log=False, **kwargs)
1
2
3
x：传递数值序列，指定条形图中x轴上的刻度值。
height：传递数值序列，指定条形图y轴上的高度。
width：指定条形图的宽度，默认为0.8。 bottom：用于绘制堆叠条形图。
color：指定条形图的填充色。
edgecolor：指定条形图的边框色。
linewidth：指定条形图边框的宽度，如果指定为0，表示不绘制边框。
tick_label：指定条形图的刻度标签。
xerr：如果参数不为None，表示在条形图的基础上添加误差棒。
yerr：参数含义同xerr。
label：指定条形图的标签，一般用以添加图例。
ecolor：指定条形图误差棒的颜色。
align：指定x轴刻度标签的对齐方式，默认为center，表示刻度标签居中对齐，如果设置为edge，则表示在每个条形的左下角呈现刻度标签。
log：bool类型参数，是否对坐标轴进行log变换，默认为False。
**kwargs：关键字参数，用于对条形图进行其他设置，如透明度等。
bar函数的参数同样很多，希望读者能够认真地掌握每个参数的含义，以便使用时得心应手。下面将基于该函数绘制三类条形图，分别是单变量的垂直或水平条形图、堆叠条形图和水平交错条形图。
（1）垂直或水平条形图
首先来绘制单个离散变量的垂直或水平条形图，数据来源于互联网，反映的是2017年中国六大省份的GDP:

垂直条形图

# 绘图 x= 起始位置， bottom= 水平条的底部(左侧), y轴， height 水平条的宽度， width 水平条的长度
p1 = plt.bar(x=0, bottom=y, height=0.5, width=x, orientation="horizontal")

'''

import matplotlib.pyplot as plt
import pandas as pd
GDP_data = pd.read_excel(r'GDP.xlsx')
#设置绘图风格
plt.style.use('ggplot')
#处理中文乱码
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
#对读入的数据做升序排序
GDP_data.sort_values(by='GDP', inplace=True)
#绘制条形图
plt.barh(y = range(GDP_data.shape[0]),  #指定条形图y轴的刻度值
         width = GDP_data.GDP,  #指定条形图x轴的数值
         tick_label = GDP_data.Province,  #指定条形图y轴的刻度标签
         color = 'lightblue',  #指定条形图的填充色
         )
#添加x轴的标签
plt.xlabel('GDP(万亿)')
#添加条形图的标题
plt.title('2017年度6个省份GDP分布')
#为每个条形图添加数值标签
for y,x in enumerate(GDP_data.GDP):
    plt.text(x+0.1,y,"%s"%round(x,1),va='center')  #round(y,1)是将y值四舍五入到一个小数位
#显示图形
plt.show()
#b————————————————



import matplotlib.pyplot as plt
import pandas as pd
GDP_data = pd.read_excel(r'GDP.xlsx')
#设置绘图风格
plt.style.use('ggplot')
#处理中文乱码
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
#绘制条形图
plt.bar(x = range(GDP_data.shape[0]),  #指定条形图x轴的刻度值(有的是用left，有的要用x)
        height = GDP_data.GDP,  #指定条形图y轴的数值（python3.7不能用y，而应该用height）
        tick_label = GDP_data.Province,  #指定条形图x轴的刻度标签
        color = 'steelblue',  #指定条形图的填充色
        )
#添加y轴的标签
plt.ylabel('GDP(万亿)')
#添加条形图的标题
plt.title('2017年度6个省份GDP分布')
#为每个条形图添加数值标签
for x,y in enumerate(GDP_data.GDP):
    plt.text(x,y+0.1,"%s"%round(y,1),ha='center')  #round(y,1)是将y值四舍五入到一个小数位
#显示图形
#plt.show()


