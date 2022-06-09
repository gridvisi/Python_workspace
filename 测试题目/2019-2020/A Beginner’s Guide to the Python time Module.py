
#https://realpython.com/python-time-module/#suspending-execution

import time
print(time.gmtime(0))
#time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

from time import time
print(time()) #1551143536.9323719

from time import time, ctime
t = time()
print(ctime(t))

from time import asctime
print(asctime())

from datetime import date
print(date(year=2019, month=3, day=1).isoformat())

from time import strftime, localtime
print(strftime('%c', localtime()))

from time import strptime
print(strptime('2020-02-17', '%Y-%m-%d'))

from time import sleep, strftime
print(strftime('%c'))
'Fri Mar  1 23:49:26 2019'
print(sleep(10))
print(strftime('%c'))
'Fri Mar  1 23:49:36 2019'

import locale
print(locale.setlocale(locale.LC_TIME, 'zh_HK'))  # Chinese - Hong Kong'zh_HK'
print(asctime())
print(strftime('%c', localtime()))
'Sat Mar  2 15:58:49 2019'