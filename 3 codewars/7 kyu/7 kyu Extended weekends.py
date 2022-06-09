#https://www.codewars.com/kata/5be7f613f59e0355ee00000f/train/python

'''
如果这个月的第一天是星期五，那么这个月很可能会有一个延长的周末。也就是说，这个月可能有五个星期五、五个星期六和五个星期日。
在这个卡塔中，你将得到一个起始年和结束年。你的任务将是找到有延长周末的月份并返回。

- 第一个月和最后一个月在这个范围内有一个延长的周末。
- 范围内有延长周末的月份数，包括起始年和结束年。
例如solve(2016,2020) = ("Jan", "May",5).
#这几个月是。2016年1月，2016年7月，2017年12月，2019年3月，2020年5月。
多用测试用例。祝您好运!
'''
from datetime import datetime

dayOfWeek = datetime.now().isoweekday() ###返回数字1-7代表周一到周日
#day_Week = datetime.now().weekday() ###返回从0开始的数字，比如今天是星期5，那么返回的就是4
print(dayOfWeek )
#print(day_Week )


#满足月首日是周五的月份
#满足31天每月的月份，4*7 + 3 = 31
import calendar
monthRange = calendar.monthrange(2020,8)
print('range:',monthRange)
def solve(a,b):
    cunt = 0
    shortMon = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec"
    lenofmonth = []
    for year in range(a, b+1):
        for m in range(1, 13):
            x = calendar.monthrange(year,m)
            if x[0] == 4 and x[1] == 31:
                cunt += 1
                lenofmonth.append(m)
    st = shortMon.split(' ')[lenofmonth[0] - 1]
    nd = shortMon.split(' ')[lenofmonth[-1] - 1]
    return st,nd,cunt,lenofmonth

a, b = 1800,2500
#a, b = 2016,2020


#1st solution
from calendar import month_abbr
from datetime import datetime
def solve(a,b):
  res = [month_abbr[month]
      for year in range(a, b+1)
      for month in [1,3,5,7,8,10,12]
      if datetime(year, month, 1).weekday() == 4]
  return (res[0],res[-1], len(res))
print(solve(a,b))

#2nd solution
import calendar

DICT = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}


def solve(a, b):
    extended_weekends_list = []
    for year in range(a, b + 1):
        for month in range(1, 13):
            if calendar.monthrange(year, month) == (4, 31):
                extended_weekends_list.append([year, month])

    result = (DICT[extended_weekends_list[0][1]], DICT[extended_weekends_list[-1][1]], len(extended_weekends_list))
    return result

#3rd solution
from calendar import FRIDAY
from datetime import datetime


def solve(a, b):
    ds = (datetime(year, month, 1) for year in range(a, b + 1) for month in [1, 3, 5, 7, 8, 10, 12])
    ds = [d for d in ds if d.weekday() == FRIDAY]
    return format(ds[0], '%b'), format(ds[-1], '%b'), len(ds)
