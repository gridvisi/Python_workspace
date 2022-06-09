import calendar
calendar.setfirstweekday(firstweekday=6)
calendar.prmonth(2020,3)

"""
    获取年月日，计算这是这一年的第几天，2019,5,18
    算法：前几个月的总天数+当月天数
"""
# 定义函数
def get_days(year, month, day):
    day_of_Feb = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    day_of_month = (31, day_of_Feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    result = sum(day_of_month[:month - 1]) + day
    return result

#测试
print(get_days(2020, 3, 15))
