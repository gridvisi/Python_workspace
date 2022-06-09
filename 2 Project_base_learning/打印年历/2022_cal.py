
import calendar
from datetime import datetime
now = datetime.now()
print(now.year, now.month)
from pprint import pprint as pp
cal = calendar.monthcalendar(now.year,now.month)
print(cal)