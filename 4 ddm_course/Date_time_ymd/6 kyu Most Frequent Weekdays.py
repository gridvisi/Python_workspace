'''
https://www.codewars.com/kata/56eb16655250549e4b0013f4/train/python

https://blog.csdn.net/p9bl5bxp/article/details/54945920
https://blog.csdn.net/tz_zs/article/details/93425782?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3.nonecase
原文链接：https://blog.csdn.net/sun2333/java/article/details/78740435

most_frequent_days(2427) == ['Friday']
most_frequent_days(2185) == ['Saturday']
most_frequent_days(2860) == ['Thursday', 'Friday']
'''


import datetime
from datetime import date
from datetime import datetime
week = datetime.strptime("2019-03-04","%Y-%m-%d").weekday()
print("2019-03-04","是星期 " + f"{week+1}")
x = datetime.strptime("2020-12-18","%Y-%m-%d").weekday()
print('x = ',x)

#datetime 转 str
print('datetime.now()',datetime.now())
str_date = datetime.now().strftime("%Y-%m-%d") #(%04d%02d%02d)此种格式化注意

#str 转 datetime
start_date = datetime.strptime("2016-06-07", "%Y-%m-%d")

#d = datetime.date(2020, 1, 1)
#print(str(d))

# Get date list from begin_date to end_date
import datetime, timedelta
from datetime import datetime
import pandas as pd

#print(e.date) #获取日期列表
#for day in e:#print(day.strftime("%Y%M%D"))


def most_frequent_days(year):
    w = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    dw = dict(zip([i for i in range(1,8)],[0]*7))
    nw = dict(zip([i for i in range(1,8)],w))
    #d = pd.bdate_range('1/1/'+str(year), '12/31/'+str(year)) 完美避开周六日？！
    d = pd.bdate_range('1/1/'+f'{year}', '12/31/'+f'{year}',freq='D')
    print('Days', len(d))

    '''
    d['daynameofweek'] = d['time_slot1'].dt.weekday_name
    print(d['daynameofweek'])
    #https://blog.csdn.net/qq_36076233/article/details/66969108
    '''
    for i in d:
        date_str = i.strftime("%Y-%m-%d")
        key = datetime.strptime(date_str,"%Y-%m-%d").isoweekday()
        print(key)
        dw[key] += 1
        mx = max([v for k,v in dw.items()])
        re = [nw[k] for k,v in dw.items() if v==mx]
        #re = sorted(dw.items(), key=lambda kv: (kv[1], kv[0]))
    return re,mx

year = '2000'
print(most_frequent_days(year))
print('today',datetime.strptime("2020-05-16","%Y-%m-%d").isoweekday())

# Top 1st
from datetime import datetime
from calendar import day_name

def most_frequent_days(year):
    first = set(range(datetime(year, 1, 1).weekday(), 7))
    last = set(range(datetime(year, 12, 31).isoweekday()))
    return [day_name[day] for day in sorted((first & last) or (first | last))]

year = 2020
print(most_frequent_days(year))
first = set(range(datetime(2020, 1, 1).weekday(), 7))
last = set(range(datetime(2020, 12, 31).isoweekday()))
print('first,last',first,last)

first,last = {2, 3, 4, 5, 6}, {0, 1, 2, 3}
print(first & last, first | last)
print((first & last) or (first | last))

print(range(datetime(2020, 1, 1).weekday(), 7))
print(range(datetime(2020, 12, 31).isoweekday()))

#Top 2nd
from calendar import weekday
week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def most_frequent_days(year):
    beg = weekday(year, 1, 1)
    end = weekday(year, 12, 31)
    if beg == end:
        return [week[beg]]
    else:
        if beg < end:
            return [week[beg], week[end]]
        else:
            return [week[end], week[beg]]

#Top 3rd
import calendar
def most_frequent_days(year):
    weekdays = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday Monday'.split()
    weekday = calendar.weekday(year, 1, 1)
    is_leap = calendar.isleap(year)
    return sorted(weekdays[weekday:weekday + 1 + is_leap], key=weekdays.index)

#Top 4th
from calendar import weekday, day_name

def most_frequent_days(year):
    return [ day_name[day] for day in sorted( {weekday(year, 1, 1), weekday(year, 12, 31)} ) ]


#Top 5th
from calendar import weekday, day_name
def most_frequent_days(year):
    days = [weekday(year, 1, 1), weekday(year, 12, 31)]
    return [day_name[i] for i in sorted(list(set(days)))]

'''
d = str(date.today())
print(d)
print(datetime.date)

import datetime
today = datetime.date.today()
oneday = datetime.timedelta(days=1)
yesterday = today - oneday
tommorrow = today + oneday
print(yesterday, today, tommorrow)




def get_date_list(begin_date, end_date):
    dates = [] # Get the time tuple : dt
    #dt = datetime.strptime(begin_date,"%Y-%m-%d")
    date = begin_date[:]

    while date <= end_date:
        dates.append(date)
        dt += timedelta(days=1)
        #date = dt.strftime("%Y-%m-%d")
        return dates
print(get_date_list('2020-1-1','2020-12-31'))
'''