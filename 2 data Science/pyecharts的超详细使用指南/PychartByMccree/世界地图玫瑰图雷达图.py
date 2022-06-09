'''
https://blog.csdn.net/zhu_rui/article/details/105888192

我之前发过一篇博文基本讲解了基本绘制地图的方法。
我这里打算直接调用api来创建实时动态地图，并且分析数据绘制了玫瑰图，雷达图。

步骤
配套资源下载：
第一步：配置环境
第二步：爬取数据
第三步：创建列表和字典
第四步：将数据添加到列表中
第五步：键值互换，中英文国名映射
第六步：添加中文数据
第七步：随机配色（给玫瑰图用的）
第八步：绘图
8.1 绘制世界地图（Map）
8.2 玫瑰图（Pie）
8.3 雷达图（Radar）
配套资源下载：
1.the_work.py
2.namemap.py

第一步：配置环境
首先，让我们配置一下环境：
python版本需要3.6.x ，pyecharts版本1.x
使用pip自动安装最新版本（这里的版本是1.7.1）
全球国家地图: echarts-countries-pypkg

pip install pyecharts
pip install echarts-countries-pypkg

调用的包：（下载配套资源，里面有namemap中英文国名映射文件）
————————————————

'''


from pyecharts.charts import Map,Pie,Radar#地图，饼形图，雷达图
from pyecharts import options as opts
from namemap import nameMap  #自定义包，配套资源里面下载
import json
import requests
import random


#第二步：爬取数据 从api调取数据并存储
#全球国家除中国
url1 = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
#中国
url2='https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
#读取数据转换成json格式
data_1=requests.get(url1).json()
#读取数据，转换成json格式，将['data']键所对应的值存储在data_2中
data_2 = requests.get(url2).json()['data']
#loads方法是把json对象转化为python对象，就是把数据里面的双引号变成单引号
all = json.loads(data_2)


#第三步：创建列表和字典
#
name=[]#国家名
confirm=[]#确x人数
dead=[]#死x人数
heal=[]#治x人数
nameMap_new={}#新中英文国名映射字典
names_new=[]#新国家名列表
ds={}#死x人数字典
hs={}#治x人数字典


'''
第四步：将数据添加到列表中
通过读取数据向列表中添加数据，然后进行对数据的筛选，例如想要得到死亡人数>4000的国家有哪些，
通过for循环遍历列表，用if条件语句实现字典的更新。
'''
for a_dict in data_1['data']:
    name.append(a_dict['name'])
    confirm.append(a_dict['confirm'])
    dead.append(a_dict['dead'])
    heal.append(a_dict['heal'])
    #如果死亡人数>4000，则更新死亡人数字典
    if a_dict['dead'] is not None and a_dict['name'] is not None:
        if int(a_dict['dead']) > 4000:
            d = {a_dict['name']:a_dict['dead']}
            h = {a_dict['name']:a_dict['heal']}
            ds.update(d)#更新字典
            hs.update(h)
ds = dict(sorted(ds.items(), key = lambda k: k[1]))#根据字典中值的大小，对字典中的项排序
hs = dict(sorted(hs.items(), key = lambda k: k[1]))
country_list = ds.keys()#把ds的键赋给country_list
dead_list = ds.values()#把ds的值赋给dead_list
heal_list = hs.values()#把hs的值赋给heal_list

#第五步：键值互换，中英文国名映射键值互换
for a,b in nameMap.items():
    nameMap_new[b]=a
#中英文国名映射
for i in range(len(name)):
    name_new=nameMap_new[name[i]]
    names_new.append(name_new)

#第六步：添加中文数据
chinaTotal=all['chinaTotal']
confirm.append(chinaTotal['confirm'])
dead.append(chinaTotal['dead'])
heal.append(chinaTotal['heal'])
names_new.append('China')


# 第七步：随机配色（给玫瑰图用的）
def randomcolor(lenth):
    colors = []
    for i in range(lenth):
        color_ = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        color = ""
        for i in range(6):
            color += color_[random.randint(0, 14)]#生成一个指定范围内的整数
        colors.append("#" + color)
    return colors
color_matching = randomcolor(len(dead_list))



'''
第八步：绘图
绘制世界地图（Map），玫瑰图（Pie），雷达图（Radar），并且输出为三个html文件。
其中：

世界地图里面有几个国家没有数据
Radar()函数的数据的传入，需要将数据升级为多维数据，并且通过输出的值判断给定数据的大小
8.1 绘制世界地图（Map）
里面具体的参数配置，

'''
map = Map( init_opts=opts.InitOpts(width="1900px", height="900px", bg_color="#d0effa", page_title="全xxxx_2"))
map.add("确x人数",[list(z) for z in zip(names_new, confirm)],is_map_symbol_show=False,
            maptype="world",label_opts=opts.LabelOpts(is_show=False),itemstyle_opts=opts.ItemStyleOpts(color="rgb(98,121,146)"))#地图区域颜色
map.set_global_opts(title_opts = opts.TitleOpts(title='全xxxx诊人数'),legend_opts=opts.LegendOpts(is_show=False),
                     visualmap_opts=opts.VisualMapOpts(max_=10000000, is_piecewise=True,
                                      pieces=[
                                        {"max": 10000000, "min": 100001, "label": ">1000", "color": "#8A0808"},
                                        {"max": 100000, "min": 10001, "label": "500-1000", "color": "#B40404"},
                                        {"max": 10000, "min": 1001, "label": "100-499", "color": "#DF0101"},
                                        {"max": 1000, "min": 101, "label": "10-99", "color": "#F78181"},
                                        {"max": 100, "min": 1, "label": "1-9", "color": "#F5A9A9"},
                                        {"max": 0, "min": 0, "label": "0", "color": "#fababa"},
                                        ])
                     )
map.render('Global_new_crown_epidemic_map.html')


#8.2 玫瑰图（Pie）
pie = Pie(init_opts=opts.InitOpts(width='1900px', height='900px', page_title="全xx情_1", bg_color="#fee4e7"))
# 添加数据
pie.add("", [list(z) for z in zip(country_list, dead_list)],
        radius=['20%', '100%'],  # 设置内径外径
        center=['60%', '65%'],  # 中心点占比
        rosetype='area')  # 圆心角相同，通过半径展现数据大小#rosetype='radius'圆心角展现数据百分比，半径展现数据大小

# 设置全局配置
pie.set_global_opts(title_opts=opts.TitleOpts(title='全球xxxx', subtitle='x亡人数超过\n4000的国家\n  (除中国)',
                                              title_textstyle_opts=opts.TextStyleOpts(font_size=15, color='#f40909'),
                                              subtitle_textstyle_opts=opts.TextStyleOpts(font_size=15, color='#8a0b0b'),
                                              pos_right='center', pos_left='57%', pos_top='60%', pos_bottom='center'),
                    legend_opts=opts.LegendOpts(is_show=False))
# 设置系列配置和颜色
pie.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='inside', font_size=13,
                                              formatter='{b}：{c}', font_style='italic',
                                              font_family='Microsoft YaHei'))
pie.set_colors(color_matching)
pie.render('Global_new_crown_epidemic_Rose.html')



#8.3 雷达图（Radar）
radar = Radar(init_opts=opts.InitOpts(width='1900px',height='900px',page_title="全球xxx_3",bg_color="#d1eff3"))
    #由于雷达图传入的数据得为多维数据，所以这里需要做一下处理
radar_data1 = [list(dead_list)]
radar_data2 = [list(heal_list)]
radar.add_schema(
            schema=[#这里的数据是在之前，调试运行一下看一下输出哪几个国家、人数
                opts.RadarIndicatorItem(name='巴xi', max_=8000),
                opts.RadarIndicatorItem(name='荷lan', max_=8000),
                opts.RadarIndicatorItem(name='伊lang', max_=20000),
                opts.RadarIndicatorItem(name='德guo', max_=40000),
                opts.RadarIndicatorItem(name='比利shi', max_=60000),
                opts.RadarIndicatorItem(name='英guo', max_=80000),
                opts.RadarIndicatorItem(name='法guo', max_=80000),
                opts.RadarIndicatorItem(name='西班ya', max_=150000),
                opts.RadarIndicatorItem(name='意大li', max_=150000),
                opts.RadarIndicatorItem(name='美guo', max_=150000),
            ]
        )
radar.add("x亡人数",radar_data1,color='blue',areastyle_opts = opts.AreaStyleOpts(opacity = 0.2,color='blue'))
radar.add("治x人数",radar_data2,color='red',areastyle_opts=opts.AreaStyleOpts(opacity=0.3,color='red'))
radar.set_series_opts(label_opts=opts.LabelOpts(is_show=True))
radar.set_global_opts(title_opts=opts.TitleOpts(title="X亡人数与治X人数对比"))
radar.render("Death_Versus_Heal.html")

