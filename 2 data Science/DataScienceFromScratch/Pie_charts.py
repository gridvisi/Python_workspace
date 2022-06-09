'''
python-关于报错cannot import *** from pyecharts的问题解决

ⓟ Paradise  于 2018-12-16 00:55:44 发布  30325  收藏 6
版权
可以尝试先卸载，然后换个镜像重新安装：

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts

重装完再imoprt pyecharts可能出现no module named 'pyecharts_snapshot’的报错：
这时同样安装上面的方法安装pyecharts_snapshot即可：

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts_snapshot

具体原因不详（难道是因为清华的名校光环？），但是实测有效，大神看到解答一下！
————————————————

pip install pyecharts
显示版本为1.8.1

pycurl                             7.43.0.2

pyecharts                          1.8.1

pyflakes                           2.1.1

Pygments                           2.3.1

当调用模块时很多人使用的语句是

from pyecharts import Pie
form pyecharts import Bar
然后就会报错：importError:cannot import 'Pie' pyecharts

这是因为版本的问题调用语句不匹配。

更换调用语句为

from pyecharts.charts import Pie
from pyecharts.charts import Bar
接下来就不会报错了，


————————————————
版权声明：本文为CSDN博主「帅气地沉迷于学习无法自拔」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/u010687164/article/details/108222892
'''

from pyecharts.charts import Bar

bar = Bar("first bar", "2nd bar")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])


# Case 2nd
import random
from pyecharts.charts import Pie
from pyecharts.charts import Bar
#from pyecharts import Pie

attr = [ 'A', 'B', 'C', 'D', 'E', 'F']

pie = Pie( "饼图示例", width= 1000, height= 600)

pie.add(

"",

attr,

[random.randint( 0, 100) for _ in range( 6)],

radius=[ 50, 55],

center=[ 25, 50],

is_random= True,

)

pie.add(

"",

attr,

[random.randint( 20, 100) for _ in range( 6)],

radius=[ 0, 45],

center=[ 25, 50],

rosetype= "area",

)

pie.add(

"",

attr,

[random.randint( 0, 100) for _ in range( 6)],

radius=[ 50, 55],

center=[ 65, 50],

is_random= True,

)

pie.add(

"",

attr,

[random.randint( 20, 100) for _ in range( 6)],

radius=[ 0, 45],

center=[ 65, 50],

rosetype= "radius",

)

#pie.render()