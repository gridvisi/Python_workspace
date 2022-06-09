'''
电费调价表：
0点至8点0.31元
8点至12点1.08元
12点至17点0.64元
17点至21点1.08元
21点至0点0.64元
https://blog.csdn.net/weixin_42232219/article/details/89838580?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-2.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-2.no_search_link

'''
#print([i for i in range(25)])


from dateutil.parser import parse
#输入美式日期
print(parse('22nd,July,2009'))
#datetime.datetime(2009, 7, 22, 0, 0)

timing = [i for i in range(25)]
slices = [(0,8),(8,12),(12,17),(17,21),(21,24)]

price = [0.31,1.08,0.64,1.08,0.64]
def unit(slices,price):
    #prices = dict(zip(price,slices))         # key repeat?
    prices = dict(zip(slices,price))         # value repeat
    return prices
print(unit(slices,price))

#python求两个时间的时间差
def day_hour(start,end,days):
    if days < 1:
        if end >= start:
            return end - start
        else:return 24 - start + end
    else:
        return end - start + days * 24

#Solution 2nd

start = parse('2011-10-1 23:23:9')
end = parse('2012-1-1 23:23:10')
print('耗时：',(end - start).days,(end - start).seconds//3600)

#(a - b).seconds
#(a - b).total_seconds()

'''

priceMap = [
            {'s':0,'t':8,price:0.31},
            {'s':8,'t':12,price:1.08},
            {'s':12,'t':17,price:0.64},
            {'s':17,'t':21,price:1.08},
            {'s':21,'t':24,price:0.64}
            ]
'''

priceMap = [
            [0,8,0.31],
            [8,12,1.08],
            [12,17,0.64],
            [17,21,1.08],
            [21,24,0.64]
            ]
print(priceMap)

def oneDayscharge(priceMap,power=1):
    return round(sum([(h[1]-h[0])*h[2] for h in priceMap]) * power,2)

def chargeCal(s,t,days,priceMap,power): #start,end,days

    rangHour = list(range(0,25))*(days+1)
    print(rangHour)
    h, cost, rangHour= 0, 0,rangHour[s:-t]
    print('Oclock', rangHour)
    while h < len(rangHour):
        for s, t, p in priceMap:
            if s<= rangHour[h] <= t:
                cost += p * power

    return cost,end - start
s,t,days,priceMap,power = 21,6,0,priceMap,2
print(f"{days} 天电费：",chargeCal(s,t,days,priceMap,power))

print('oneday:',oneDayscharge(priceMap))
import time
from dateutil.rrule import *

def elecharge(start,end,priceMap,power):
    priceMap = [
        [0, 8, 0.31],
        [8, 12, 1.08],
        [12, 17, 0.64],
        [17, 21, 1.08],
        [21, 24, 0.64]
    ]
    cost = 0
    day,hour = (end - start).days,round((end - start).seconds/3600,2)
    print("day,hour,end-start:",day,hour,(end-start).seconds)

    '''    
    #hourst,hourend = start.split(" "),end.split(" ") Not work！！
    #n = rrule(rrule.byhour, dtstart=start, until=end).count()
    '''

    cost += day * oneDayscharge(priceMap)
    #print('starthour:',start.hour,end.hour)
    if end.hour < start.hour:
        workhour = list(range(start.hour, 25)) + list(range(0, end.hour + 1))
    else:
        workhour = list(range(start.hour, end.hour + 1))
    #print('workhour:',workhour)
    for s,t,p in priceMap:

        for h in workhour:
            print('h:',h)
            if h >=s and h <= t:
                cost += p * power

    return day,cost,end - start
start = parse('2021-12-12 23:32:9')
end = parse('2021-12-14 23:31:8')
print('耗时2：',(end - start).days,round((end - start).seconds/3600,2))
print(start,end)

#print('电费：',elecharge(start,end,priceMap,2))
'''
python中通过datetime模块可以很方便的计算两个时间的差,datetime的时间差单位可以是
天、小时、秒,甚至是微秒,下面我们就来详细看下datetime的强大功能:


from datetime import datetime 
a=datetime.now() 
b=datetime.now() 
>>> a
>>>datetime.datetime(2015, 4, 7, 4, 30, 3, 628556) 
>>>b
>>>datetime.datetime(2015, 4, 7, 4, 34, 41, 907292) 

 
>>>str(a) #字符串的转换，用户储存到文本或者数据库
'2015-04-07 04:30:03.628556' 
>>>datetime.strptime(str(a),"%Y-%m-%d %H:%M:%S.%f")
datetime.datetime(2015, 4, 7, 4, 30, 3, 628556) 

 
>>> (b-a)
Out: datetime.timedelta(0, 278, 278736) 

 
>>>(b-a).seconds #时间差的计算，单位为秒
278

 
Q:如何方便的计算两个时间的差，如两个时间相差几天，几小时等
 A:使用datetime模块可以很方便的解决这个问题，举例如下：
 
>>> import datetime>>> d1 = datetime.datetime(2005, 2, 16)
>>> d2 = datetime.datetime(2004, 12, 31)
>>> (d1 - d2).days47
上例演示了计算两个日期相差天数的计算。

>>>import datetime
>>>starttime = datetime.datetime.now()
#long running
>>>endtime = datetime.datetime.now()
>>>print (endtime - starttime).seconds
上例演示了计算运行时间的例子，以秒进行显示。

>>> d1 = datetime.datetime.now()
>>> d3 = d1 + datetime.timedelta(hours=10)
>>> d3.ctime()
上例演示了计算当前时间向后10小时的时间。

其本上常用的类有：datetime和timedelta两个。它们之间可以相互加减。每个类都有一些方法
和属性可以查看具体的值，
如datetime可以查看：天数(day)，小时数(hour)，星期几(weekday())等;timedelta可以
查看：天数(days)，秒数(seconds)等。
'''

print([i for i in range(10,100) if 149%i==5])