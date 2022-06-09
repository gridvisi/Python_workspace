'''
距2018年3月31日算起，科比去世666天
3312018等于666乘以第666个素数

科比拿到81分的单场最高得分是他的第666场比赛
'''
import time
import datetime
string = '2014-01-08' # 11:59:58
time1 = datetime.datetime.strptime(string,'%Y-%m-%d') # %H:%M:%S
print('time1',time1)

today = datetime.date.today()
print(today)
# General functions
print("Year: %d" % today.year)
print("Month: %d" % today.month)
print("Day: %d" % today.day)
print("Weekday: %d" % today.weekday())# Day of week Monday = 0, Sunday = 6

def days(str1,str2):
    date1=datetime.datetime.strptime(str1[0:10],"%Y-%m-%d")
    date2=datetime.datetime.strptime(str2[0:10],"%Y-%m-%d")
    num=(date1-date2).days
    return num

str1 = '2018-03-31 08:18:09'
str2 = '2020-01-26 10:19:33'
#str1 = '2020-0331'
str_now = time.localtime(time.time())
#print(time.localtime(time.time().strptime(str1[0:10],"%Y-%m-%d")))
#str2 = str_now
print('kobi',days(str1,str2))

# 666th prime

def isprime(n):
    if n == 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

start,stop,res = 1,10000,[]
for i in range(start, stop):
    if isprime(i):
        res.append(i)
    if len(res) == 666:
        print(res[-1],666*res[-1])


'''

def nthPrime(start, stop):
    is_prime = lambda n : all(n % a for a in range(3, 1 + int(n ** 0.5), 2)) if n > 2 and n % 2 else n == 2
    return is_prime
import math
def is_th_Prime(end):
    res = []
    for i in range(1,end+1):
        if i == 2: res.append(i)
        if i < 2 or i % 2 == 0: pass
        if not any(i % d == 0 for d in range(3, int(i**0.5) + 1)):

            print(i)
            res.append(i)
    return res,len(res)



python获取当前时间的用法
1.先导入库：import datetime
2.获取当前日期和时间：now_time = datetime.datetime.now()
3.格式化成我们想要的日期：strftime（）
比如：“2016-09-21”：datetime.datetime.now().strftime('%Y-%m-%d')

4.在当前时间增加1小时：add_hour=datetime.datetime.now()+datetime.timedelta(hours=1)   #需要导入timedelta库
格式“小时”：now_hour=add_hour.strftime('%H')
5.时间的三种存在方式：时间对象，时间字符串，时间戳。

(1)字符串转datetime：
>>> string = '2014-01-08 11:59:58'
>>> time1 = datetime.datetime.strptime(string,'%Y-%m-%d %H:%M:%S')
>>> print time1
2014-01-08 11:59:58

(2)datetime转字符串：
>>> time1_str = datetime.datetime.strftime(time1,'%Y-%m-%d %H:%M:%S')
>>> time1_str
'2014-01-08 11:59:58'

(3)时间戳转时间对象：
>>>time1 = time.localtime()
>>>time1_str = datetime.datetime.fromtimestamp(time1)

import datetime
# Get a date object
today = datetime.date.today()

# General functions
print "Year: %d" % today.year
print "Month: %d" % today.month
print "Day: %d" % today.day
print "Weekday: %d" % today.weekday() # Day of week Monday = 0, Sunday = 6

# ISO Functions
print "ISO Weekday: %d" % today.isoweekday() # Day of week Monday = 1, Sunday = 7
print "ISO Format: %s" % today.isoformat() # YYYY-MM-DD format
print "ISO Calendar: %s" % str(today.isocalendar()) # Tuple of (ISO year, ISO week number, ISO weekday)

# Formatted date
print today.strftime("%Y/%m/%d") #
作者：pollen555
链接：https://www.jianshu.com/p/4c4436d749ee
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

6.格式参数：

%a 星期几的简写
%A 星期几的全称
%b 月分的简写
%B 月份的全称
%c 标准的日期的时间串
%C 年份的后两位数字
%d 十进制表示的每月的第几天
%D 月/天/年
%e 在两字符域中，十进制表示的每月的第几天
%F 年-月-日
%g 年份的后两位数字，使用基于周的年
%G 年分，使用基于周的年
%h 简写的月份名
%H 24小时制的小时
%I 12小时制的小时
%j 十进制表示的每年的第几天
%m 十进制表示的月份
%M 十时制表示的分钟数
%n 新行符
%p 本地的AM或PM的等价显示
%r 12小时的时间
%R 显示小时和分钟：hh:mm
%S 十进制的秒数
%t 水平制表符
%T 显示时分秒：hh:mm:ss
%u 每周的第几天，星期一为第一天 （值从0到6，星期一为0）
%U 第年的第几周，把星期日做为第一天（值从0到53）
%V 每年的第几周，使用基于周的年
%w 十进制表示的星期几（值从0到6，星期天为0）
%W 每年的第几周，把星期一做为第一天（值从0到53）
%x 标准的日期串
%X 标准的时间串
%y 不带世纪的十进制年份（值从0到99）
%Y 带世纪部分的十制年份
%z，%Z 时区名称，如果不能得到时区名称则返回空字符。
%% 百分号
'''

