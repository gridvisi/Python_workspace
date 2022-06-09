'''
https://github.com/hangsz/pandas-tutorial
https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html

教程目录
详细信息
教程说明
当今最热的职业是数据科学，数据科学领域应用最广泛的编程语言是python，python这么火的原因就是其有一个功能强大的数据科学库：pandas。

为什么写这套教程
然而，作为一名数据科学行业从业者，即使在pandas中浸淫日久，我常常还需要去查询官方文档，这严重影响了我的工作效率；甚至有时候迫不得已还得写循环操作，非常不pandas，这我忍不了，所以我觉得我得做点什么。

经过多次通读官方文档后，我认为问题根因在于：

官方文档组织杂而乱，知识框架不够精炼一致；
面面俱到，高价值信息被为了完整性而稀释；
文档更新不及时，API功能有时与文档描述不符。
与此同时，我也通读了国内外各种pandas教程，不过总体而言这些教程多数浅尝辄止，不够实用。所以，我决定编写一套pandas教程，提高自己能力的同时，也能帮助大家少走弯路。

教程编写核心原则
这套教程编写的核心原则是：

首重知识体系逻辑，没有组织、不成体系的信息是无效信息，很难记住和使用；
知识粒度大小适中，即不流于表面也不深入过多细节;
示例精炼短小（能看出操作效果），方便手打练习；
在示例位置都会注上解释，辅助理解。
这套教程适合谁
这套教程包含从初级到进阶的内容，适合初学者和希望进阶建立知识体系的数据科学从业者阅读。为确保教程的高可用性和准确性，我花了大量时间精心准备，但仍难免有错漏，非常欢迎各位读者能够跟我反馈。

感觉有收货，可以请我喝杯咖啡


准备
在 Jupyter Notebook 中执行 %matplotlib inline 魔法指令，可以方便地在 Jupyter Notebook 中绘制 matplot 图形。

绘图
在 pandas 中绘图非常方便，只需要一个简单的 plot 方法，即可绘制出折线图。下面，我们首先构造一个 Series：

作者：山药鱼儿
链接：https://www.jianshu.com/p/730b7debaa99
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

import pandas as pd
import numpy as np

index = np.arange(-100,100,10)
data = index ** 2

s = pd.Series(data, index=index)
print(s)

print(s.plot())
s.plot()

df = pd.DataFrame({
    'x': index,
    '2*x': index*2,
    '3*x': index*3,
})

print(df)



#2nd case
#https://www.cnblogs.com/chenhuabin/archive/2019/03/06/10485549.html
import pandas as pd
import numpy as np

data = {'name': ['Joe', 'Mike', 'Jack', 'Rose', 'David',
                 'Marry', 'Wansi', 'Sidy', 'Jason', 'Even'],

        'age': [25, 32, 18, np.nan, 15, 20, 41, np.nan, 37, 32],

        'gender': [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],

        'isMarried': ['yes', 'yes', 'no', 'yes', 'no', 'no',
                      'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)

df