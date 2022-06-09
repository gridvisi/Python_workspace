
import datetime

date1 = '2018-11-26 09:30:45'
date2 = '16/Nov/2018:08:44:34'

# 定义的日期格式需与当前时间格式一致
d1 = datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime(date2, '%d/%b/%Y:%H:%M:%S')

d = d1 - d2

print('相差的天数：{}'.format(d.days))
print('相差的秒数：{}'.format(d.seconds))

#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nd = np.datetime64('2019-01-10')
print(np.datetime64('2019-01-10'))

#转化为字符串
np.datetime_as_string(nd)
#'2019-01-10'
np.datetime64('1901')

#np.datetime64('1901')
#转化为datetime格式

nd.astype(datetime)
datetime.date(2019, 1, 10)

#生成时间序列
#默认以日为间隔，算头不算尾
print(np.arange('2019-01-05','2019-01-10',dtype='datetime64'))
#array(['2019-01-05', '2019-01-06', '2019-01-07', '2019-01-08','2019-01-09'], dtype='datetime64[D]')
#以月为间隔，生成2018年12个月

print(np.arange('2018-01-01','2019-01-01',dtype='datetime64[M]'))
#array(['2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06',
#       '2018-07', '2018-08', '2018-09', '2018-10', '2018-11', '2018-12'], dtype='datetime64[M]')

#以年为间隔
np.arange('2015-01-01','2019-01-20',dtype='datetime64[Y]')

#array(['2015', '2016', '2017', '2018'], dtype='datetime64[Y]')
#以周为间隔
np.arange('2018-12-01','2018-12-20',dtype='datetime64[W]')
#array(['2018-11-29', '2018-12-06', '2018-12-13'], dtype='datetime64[W]')
#设定随机种子（括号里的数字只是起标记作用）
np.random.seed(1)
#h:小时，m:分，s：秒，ms微秒
#生成分时
x = np.arange('2019-01-10T00:00:00','2019-01-10T23:00:00',dtype='datetime64[m]')

#生成标准正态分布时间序列
y = np.random.standard_normal(len(x))
#设置图片大小
fig = plt.figure(figsize=(12,6))
#将x的np.datetime转换为datetime.datetime
plt.plot(x.astype(datetime),y)
fig.autofmt_xdate()
plt.title('模拟23小时内每分钟正态分布的随机数分布')
# 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()