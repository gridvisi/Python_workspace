'''
死也想分享给你们一句话，谁说的我忘了：It's not what we do once in a while that shapes our lives.
It's what we do consistently.

我们过着的生活，是由那些持之以恒的事情造就的；而不是一时兴起、偶尔为之的新鲜刺激的事。

'''

#时间序列分析之日期处理

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False
#datetime处理日期
#python常用的处理时间的库有：datetime,time,calendar。
# datetime库包括了date（储存日期：(年、月、日),time(储存时间：(小时、分、秒和微秒)，
# datetime同时包含了data和time，timedelta代表两个datetime之间的差（天、秒、微秒）。

from datetime import datetime
now=datetime.now()
print(f'当前时间：{now}')
print(f'{now.year}年{now.month}月{now.day}日')

#当前时间：2019-01-11 10:25:21.445490
#2019年1月11日
#now.strftime('%Y-%m-%d')
#'2019-01-10'
#timedelta计算相差天数和秒数

import datetime
delta = datetime(2019,1,10)-datetime(2019,1,1,12,30)
#delta
datetime.timedelta(days=8, seconds=41400)

'''
python报错：type object ‘datetime.datetime’ has no attribute ‘datetime’
描述：在第一个python程序里还未报错，第二个程序完全复制过来，导入模块from datetime import datetime ，运行就报错了
原因：被2个相同的datetime给迷惑了，其实2个datetime不是在一个级别上的东西，一个是模块，一个是类。
解决办法：导入模块的from datetime import datetime改成import datetime。

'''

from datetime import timedelta
start = datetime(2018,1,1)
#计算50天后是哪一天
start+timedelta(50)
datetime.datetime(2018, 2, 20, 0, 0)
#字符串和时间的转化
#比如想要知道列表里两个时间字符串之间相差多少天
datestr = ['12/20/2018','12/11/2018']
new_date = [datetime.strptime(d,'%m/%d/%Y') for d in datestr]
#new_date[0]-new_date[1]
datetime.timedelta(days=9)
#将datetime格式转换为常见的年（Y）月（m）日（d）格式表示
[date.strftime('%Y-%m-%d') for date in new_date]

#['2018-12-20', '2018-12-11']
#datetime.strptime只能根据设定的时间格式来处理指定的字符串，如果列表里(list)包含不止一种格式的字符串，如datestr=['12/20/2018','12/11/2018','2018-10-18'],使用datetime.strptime就很难处理了。遇到这种情况可以引入第三方时间处理包dateutil，可以处理任意格式字符串。

from dateutil.parser import parse
datestr=['12/20/2018','20180210','2019-01-10']
#转换成datetime格式
new_d=[parse(d) for d in datestr]
#统一为12/20/2018格式
d1=[d.strftime('%m/%d/%Y') for d in new_d]
d2=[d.strftime('%Y%m%d') for d in new_d]
d3=[d.strftime('%Y-%m-%d') for d in new_d]
d4=[d.strftime('%y-%m-%d') for d in new_d]
print(f'datetime格式：\n{new_d}')
print(f'"月/日/年"格式：\n {d1}')
print(f'"年月日"格式：\n{d2}')
print(f'"年-月-日格式"：\n{d3}')
print(f'"年（后两位）-月-日"格式：\n{d4}')
#datetime格式：
#[datetime.datetime(2018, 12, 20, 0, 0), datetime.datetime(2018, 2, 10, 0, 0), datetime.datetime(2019, 1, 10, 0, 0)]
"月/日/年"
# ['12/20/2018', '02/10/2018', '01/10/2019']
"年月日"
#['20181220', '20180210', '20190110']
"年-月-日格式"
#['2018-12-20', '2018-02-10', '2019-01-10']
"年（后两位）-月-日"
#['18-12-20', '18-02-10', '19-01-10']
#使用NumPy库处理日期
#numpy库的时间格式是datetime64

#将字符串转换成numpy格式时间
#注意个位前补0，如1月写成01
import numpy
nd=np.datetime64('2019-01-10')

numpy.datetime64('2019-01-10')
#转化为字符串
np.datetime_as_string(nd)
'2019-01-10'
np.datetime64('1901')
numpy.datetime64('1901')
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
x=np.arange('2019-01-10T00:00:00','2019-01-10T23:00:00',dtype='datetime64[m]')

#生成标准正态分布时间序列
y=np.random.standard_normal(len(x))
#设置图片大小
fig=plt.figure(figsize=(12,6))
#将x的np.datetime转换为datetime.datetime
plt.plot(x.astype(datetime),y)
fig.autofmt_xdate()
plt.title('模拟23小时内每分钟正态分布的随机数分布')
# 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()

'''
Pandas库处理日期
Pandas库是处理时间序列的利器，pandas有着强大的日期数据处理功能，可以按日期筛选数据、按日期显示数据、按日期统计数据。pandas的实际类型主要分为timestamp（时间戳）、period（时期）和时间间隔（timedelta）,常用的日期处理函数有：pd.to_datetime(),pd.to_period(),pd.date_range(),pd.period_range；pandas的resample函数还提供了对日期样本的转换，如高低频数据转化等。
时间格式处理及转换
定义时间格式
常用函数：
'''
import pandas
pd.Timestamp(),pd.Period(),pd.to_timestamp(),pd.to_datetime(),pd.to_period()

#定义timestamp
t1=pd.Timestamp('2019-01-10')
t2=pd.Timestamp('2018-12-10')
print(f't1= {t1}')
print(f't2= {t2}')
print(f't1与t2时间间隔：{(t1-t2).days}天')
#t1= 2019-01-10 00:00:00
#t2= 2018-12-10 00:00:00
#t1与t2时间间隔：31天
#获取当前时间
now=pd.datetime.now()
print(now)
print(now.strftime('%Y-%m-%d'))

#时间间隔
pd.Timedelta(days=5, minutes=50, seconds=20,
   milliseconds=10, microseconds=10, nanoseconds=10)
#Timedelta('5 days 00:50:20.010010')
#计算当前时间往后100天的日期
dt=now+pd.Timedelta(days=100)
#只显示年月日
dt.strftime('%Y-%m-%d')
'2019-04-21'
#定义时期period，默认是A-DEC，代表年份，以12月作为最后一个月
p1=pd.Period('2019')
p2=pd.Period('2018')
print(f'p1={p1}年')
print(f'p2={p2}年')
print(f'p1和p2间隔{p1-p2}年')
#可以直接+、-整数（代表年）
print(f'十年前是{p-10}年')
#p1=2019年
#p2=2018年

#p1和p2间隔1年
#十年前是2009年
#通过asfreq转换时期频率
#以第一个月算,p1前面已赋值为2019年
p1.asfreq('M','start')
#Period('2019-01', 'M')
#以最后一个月算
p1.asfreq('M','end')
#Period('2019-12', 'M')
#财报季度
p=pd.Period('2019Q3',freq='Q-DEC')
#起始月日
print(p.asfreq('D','start'))
#结束月日
print(p.asfreq('D','end'))
'''
2019-07-01
2019-09-30
'''


#时间戳和时期相互转换
print(p1.to_timestamp(how='end'))
print(p1.to_timestamp(how='start'))
'''
2019-12-31 00:00:00
2019-01-01 00:00:00
'''
#t1前面赋值为'2019-1-10'
#转换为月时期
print(t1.to_period('M'))
#转换为日时期
print(t1.to_period('D'))
print(t1.to_period('W'))

'''
2019-01
2019-01-10
2019-01-07/2019-01-13
生成日期序列
常用函数：pd.date_range()，生成的是DatetimeIndex格式的日期序列；pd.period_range()，
生成PeriodIndex的时期日期序列。

'''

#使用date_range生成日期序列
#如要详细了解该函数，可以使用help(pd.date_range)
#参数四选三：起始时间，结束时间，freq，periods
#freq='M'月，'D'天，'W'，周，'Y'年
#生成月时间序列
dm = pd.date_range('2018/01/01', freq='M', periods=12)
print(f'生成月时间序列：\n{dm}')
#算头不算尾
#生成年时间序列,默认是以12月结尾，freq='Y-DEC'
dy=pd.date_range('2008-01-01','2019-01-10',freq='Y')
print(f'生成年时间序列：\n{dy}')
#生成日时间序列
dd=pd.date_range('2018-01-01',freq='D',periods=10)
print(f'生成日时间序列：\n{dd}')
#生成周时间序列,默认以sunday周日作为一周最后一日
#如要改成周一作为第一天，freq='W-SAT'
dw=pd.date_range('2018-01-01',freq='W',periods=10)
print(f'生成周时间序列：\n{dw}')
#生成月时间序列：

'''
DatetimeIndex(['2018-01-31', '2018-02-28', '2018-03-31', '2018-04-30',
               '2018-05-31', '2018-06-30', '2018-07-31', '2018-08-31',
               '2018-09-30', '2018-10-31', '2018-11-30', '2018-12-31'],
              dtype='datetime64[ns]', freq='M')
'''
#生成年时间序列：
'''
#DatetimeIndex(['2008-12-31', '2009-12-31', '2010-12-31', '2011-12-31',
               '2012-12-31', '2013-12-31', '2014-12-31', '2015-12-31',
               '2016-12-31', '2017-12-31', '2018-12-31'],
              dtype='datetime64[ns]', freq='A-DEC')
'''
#生成日时间序列：
'''
DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',
               '2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08',
               '2018-01-09', '2018-01-10'],
              dtype='datetime64[ns]', freq='D')
'''
#生成周时间序列：
'''
DatetimeIndex(['2018-01-07', '2018-01-14', '2018-01-21', '2018-01-28',
               '2018-02-04', '2018-02-11', '2018-02-18', '2018-02-25',
               '2018-03-04', '2018-03-11'],
              dtype='datetime64[ns]', freq='W-SUN')
'''
#使用period_range生成日期序列
#参数四选三：起始时间，结束时间，freq，periods
#freq='M'月，'D'天，'W'，周，'Y'年
#生成月时期序列
dpm = pd.period_range('2019/01/01', freq='M', periods=12)
print(f'生成月时间序列：\n{dpm}')
#生成年时期序列,默认是以12月结尾，freq='Y-DEC'
dpy=pd.period_range('2008-01-01','2019-01-10',freq='Y')
print(f'生成年时间序列：\n{dpy}')
#生成日时期序列
dpd=pd.period_range('2018-01-01',freq='D',periods=10)
print(f'生成日时间序列：\n{dpd}')
#生成周时期序列,默认以sunday周日作为一周最后一日
#如要改成周一作为第一天，freq='W-SAT'
dpw=pd.period_range('2018-01-01',freq='W-SUN',periods=10)
print(f'生成周时间序列：\n{dpw}')
#生成月时间序列：
'''
#PeriodIndex(['2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06',
             '2019-07', '2019-08', '2019-09', '2019-10', '2019-11', '2019-12'],
            dtype='period[M]', freq='M')
'''
#生成年时间序列：
#PeriodIndex(['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],dtype='period[A-DEC]', freq='A-DEC')
#生成日时间序列：
#PeriodIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04','2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08','2018-01-09', '2018-01-10'],dtype='period[D]', freq='D')
#生成周时间序列：
'''
PeriodIndex(['2018-01-01/2018-01-07', '2018-01-08/2018-01-14',
             '2018-01-15/2018-01-21', '2018-01-22/2018-01-28',
             '2018-01-29/2018-02-04', '2018-02-05/2018-02-11',
             '2018-02-12/2018-02-18', '2018-02-19/2018-02-25',
             '2018-02-26/2018-03-04', '2018-03-05/2018-03-11'],
            dtype='period[W-SUN]', freq='W-SUN')
'''
#画以时间为x轴的图,pandas的DataFrame自动将index列作为x轴
np.random.seed(2)
#生成日期序列
x=pd.date_range('2018/01/01','2019/12/31', freq='d')
#x=pd.period_range('2018/01/01','2019/12/31', freq='d')
#标准正态分布时间序列
y=np.random.standard_normal(len(x))
#将二者转换为pandas的数据格式
df=pd.DataFrame(y,columns=['标准正态分布'],index=x)
df.plot(figsize=(12,6))
plt.title('模拟标准正态分布随机数')

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()
'''
时间样本频率转换
时间序列样本转换主要分两种：即高频数据向低频数据转换；低频数据向高频数据转换。应用场景：行情交易数据一般是高频，基本面一般是月度、季度、年度等低频数据，量化分析的时候，常常要将基本面数据和行情交易数据结合起来进行统计回归分析，这时候就要用到样本数据频率的转换了。
主要函数:df.resample()，df代表pandas的DataFrame格式数据，resample方法的参数参数中，freq表示重采样频率,例如‘M’、‘5min’,Second(15)，用于产生聚合值的函数名或数组函数,例如‘mean’、‘ohlc’、np.max等,默认是‘mean’,其他常用的有:‘first’、‘last’、‘median’、‘max’、‘min’axis=0默认是纵轴,横轴设置axis=1

高频数据向低频数据转化
'''

#导入2019年1月10日上证指数的分时数据
#数据来源：同花顺
df=pd.read_excel('Table.xlsx')
df.head()
#设置时间作为索引
df=df.set_index(df['时间'])
#画图，pandas数据表自动将索引作为x轴
df['成交'].plot(figsize=(16,6),label='成交价格')
plt.title('上证综指2019年1月10日分时图',fontsize=15)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()
#由于时间索引列只有时分秒，是object格式，加入年月日再进行样本变换
d=datetime(2019,1,10)
dt=pd.to_datetime([datetime.combine(d,t) for t in df['时间'].values])
#构建新的数据框
ts=pd.DataFrame(df['成交'].values,columns=['成交'],index=dt)
ts.head()
#5分钟样本,取最后一个数，标志默认左侧，所以第一个区间[9:20-9:25],显示9:20
ts.resample('5min',closed='right').last().head()
#5分钟采用，取最后一个数，
ts.resample('5min',closed='right',label='right').last().head()
#将其转换为每小时样本,默认closed='left',label='left'
#可以使用均值mean(),或取第一个数first(),或最后一个last()
ts.resample('H').mean()

#低频数据向高频数据转换
#frq='W'代表周
df=pd.DataFrame(np.random.randn(5,4),
            index=pd.date_range('1/4/2019',periods=5,freq='W'),
            columns=['GZ','BJ','SH','SZ'])


#将上述样本转换为日序列,缺失值使用前值补上
#如使用后值则用bfill()
df_daily=df.resample('D').ffill()
df_daily.head()
#根据period来重采样
df1=pd.DataFrame(np.random.randn(2,4),
            index=pd.period_range('1-2017','12-2018',freq='A'),
            columns=['GZ','BJ','SH','SZ'])
df1.head()
日期数据分组统计
#注意pd是pandas的简称，np是numpy的简称，使用之前先import
date=pd.date_range('1/1/2018', periods=500, freq='D')
ts=pd.Series(np.random.standard_normal(500),index=date)
ts.head()
'''
2018-01-01    0.681604
2018-01-02    1.006493
2018-01-03   -0.942035
2018-01-04   -0.733425
2018-01-05   -1.035250
Freq: D, dtype: float64
'''
#按月显示，不统计
#按年是A，季度是Q
tsp=ts.to_period('D')
tsp.head()
'''
2018-01-01    0.681604
2018-01-02    1.006493
2018-01-03   -0.942035
2018-01-04   -0.733425
2018-01-05   -1.035250
Freq: D, dtype: float64
'''
#根据不同时期显示索引值
#按季度频率Q，月度M，年度A

tsp.index.asfreq('Q')
'''
PeriodIndex(['2018Q1', '2018Q1', '2018Q1', '2018Q1', '2018Q1', '2018Q1',
             '2018Q1', '2018Q1', '2018Q1', '2018Q1',
             ...
             '2019Q2', '2019Q2', '2019Q2', '2019Q2', '2019Q2', '2019Q2',
             '2019Q2', '2019Q2', '2019Q2', '2019Q2'],
            dtype='period[Q-DEC]', length=500, freq='Q-DEC')
'''
#按工作日统计
tsp.index.asfreq('B')
'''
PeriodIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',
             '2018-01-05', '2018-01-08', '2018-01-08', '2018-01-08',
             '2018-01-09', '2018-01-10',
             ...
             '2019-05-06', '2019-05-07', '2019-05-08', '2019-05-09',
             '2019-05-10', '2019-05-13', '2019-05-13', '2019-05-13',
             '2019-05-14', '2019-05-15'],
            dtype='period[B]', length=500, freq='B')
'''
#按周进行显示，求和汇总
#月：M，年：A，季度：Q
#sum()、mean（）,first(),last()
print(ts.resample('W').sum().head())
'''
2018-01-07   -0.532703
2018-01-14   -3.905250
2018-01-21   -0.037820
2018-01-28   -4.010447
2018-02-04   -2.165019
Freq: W-SUN, dtype: float64
'''
print(ts.resample('AS').sum())
# "AS"是每年第一天为开始日期, "A是每年最后一天
'''
2018-01-01    0.434155
2019-01-01    0.171082
Freq: AS-JAN, dtype: float64
'''
# 按年统计并显示
print(ts.resample('AS').sum().to_period('A'))
'''
2018    0.434155
2019    0.171082
Freq: A-DEC, dtype: float64
'''
# 按季度统计并显示
print(ts.resample('Q').sum().to_period('Q'))
#按月进行汇总求平均值

'''
2018Q1   -23.716613
2018Q2    -3.304391
2018Q3    15.039522
2018Q4    12.415637
2019Q1     1.153160
2019Q2    -0.982078
Freq: Q-DEC, dtype: float64
根据groupby进行resampling

'''

ts.groupby(lambda x:x.year).mean()
'''

2018    0.001189
2019    0.001267
dtype: float64
#按周进行汇总求平均值
'''
ts.groupby(lambda x:x.weekday).mean()
'''
0   -0.021922
1   -0.005215
2   -0.002857
3   -0.037211
4   -0.133802
5    0.011450
6    0.198504
dtype: float64

'''
#作者：CuteHand
#链接：https://www.jianshu.com/p/81734e4fc0e7
