'''
https://blog.csdn.net/zhuiqiuuuu/article/details/84642311

'''
from datetime import datetime
from datetime import timedelta


def get_day(dt_obj, week_day="monday"):
    # 获取当周的星期x
    d = dict(zip(("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"), range(7)))
    # datetime 模块中，星期一到星期天对应数字 0 到 6
    delta_hour = timedelta(days=1)  # 改变幅度为 1 天
    while dt_obj.weekday() != d.get(week_day):
        if dt_obj.weekday() > d.get(week_day):
            dt_obj -= delta_hour
        elif dt_obj.weekday() < d.get(week_day):
            dt_obj += delta_hour
        else:
            pass
    return dt_obj.strftime("%Y-%m-%d")

dt_obj = datetime.now()
print(dt_obj)  # 2019-06-24 00:36:44.325083
print(get_day(dt_obj, "friday"))