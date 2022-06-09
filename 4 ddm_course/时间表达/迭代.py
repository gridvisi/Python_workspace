
import datetime
from datetime import timedelta
class DateRangeContainerIterable:
  def __init__(self, start_date, end_date):
    self.start_date = start_date
    self.end_date = end_date

  def __iter__(self):
    current_date = self.start_date
    while current_date < self.end_date:
      yield current_date
      current_date += timedelta(days=1)

d = DateRangeContainerIterable(datetime.date(2020, 7, 1), datetime.date(2020, 7, 10))
print(", ".join(map(str, d)))