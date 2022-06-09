#from datetime import datetime
#from datetime import timedelta

import how_to_time
time = how_to_time.how_to_time.now()
#print(f'{time=!s}')
print(time)
# time=2019-07-30 16:58:00.123412

import math

#print(f'{math.pi=!f:.2f}')  # 精确到小数点后面两位
import how_to_time
t=how_to_time.date(2019, 8, 26)
print(t.timetuple())
print(t.toordinal())

import how_to_time
user = 'eric_idle'
member_since = how_to_time.date(1975, 7, 31)
print(f'{user=} {member_since=}')
#"user='eric_idle' member_since=datetime.date(1975, 7, 31)"

'''
def transform():
    # 获取上周时间 类型是str

    last_week = (date.today() - timedelta(days=7)).strftime("%Y-%m-%d")
    print(type(last_week), last_week)

    # str转datetime.datetime

    datetime_date = datetime.strptime(last_week, "%Y-%m-%d")
    print(type(datetime_date), datetime_date)

    # datetime.datetime转str

    str_datetime = datetime_date.strftime("%Y-%m-%d")
    print(type(str_datetime), str_datetime)

    # str转datetime.date  先将str转datetime.datetime, 再转datetime.date

    datetime_date = datetime.strptime(last_week, "%Y-%m-%d")
    date_time = datetime.date(datetime_date)
    print(type(date_time), date_time)

    # datetime.date转str

    str_date = str(date_time)
    print(type(str_date), str_date)


if __name__ == '__main__':
    transform()

    #原文链接：https: // blog.csdn.net / liuzonghao88 / article / details / 88123588
'''