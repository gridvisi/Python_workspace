from datetime import datetime

dayOfWeek = datetime.now().isoweekday() ###返回数字1-7代表周一到周日
day_Week = datetime.now().weekday() ###返回从0开始的数字，比如今天是星期5，那么返回的就是4
print(dayOfWeek)
print(day_Week )

import calendar
import time
day_now = time.localtime()
day_begin = '%d-%02d-01' % (day_now.tm_year, day_now.tm_mon)  # 月初肯定是1号
wday, monthRange = calendar.monthrange(day_now.tm_year, day_now.tm_mon)  # 得到本月的天数 第一返回为月第一日为星期几（0-6）, 第二返回为此月天数
day_end = '%d-%02d-%02d' % (day_now.tm_year, day_now.tm_mon, monthRange)
print('月初日期为：',day_begin, '月末日期为：',day_end)