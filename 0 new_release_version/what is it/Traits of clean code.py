
import contextlib

def stop_db_service():
  print("systemctrl stop service cassandra")

def start_db_service():
  print("systemctrl start service cassandra")

class DbHandler:
    def __exit__(self):
      stop_database()
      return self

    def __enter__(self):
        start_database()

def db_print_keyspaces():
    print_desc_keyspace("localhost:6042")

def main():
    with DbHander():
      db_print_keyspaces

@contextlib.contextmanager
def db_handler():
    stop_database()
    yield
    start_database()

with db_hander():
  db_backup()



class Items:

  def __init__(self, values):
    self._values = list(values)

  def __len__(self):
    return len(self._values)

  def __getitem__(self, item):
    return self.__values.__getitem__(item)




'''
Python中的下划线
在Ptyhon中，对象的所有默认属性都是公开的。对象应该只公开那些与外部调用者对象相关的属性和方法。所有严格意义上不属于对象的interfact的东西都应该保留一个单下划线的前缀。
双下划线是非Pythonic的方法。如果你需要将属性定义为私有属性，请使用单下划线，并尊重Pythonic惯例，即它是一个私有属性。

'''
import time
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

d = DateRangeContainerIterable(datetime.date(2019, 1, 1), datetime.date(2019, 1, 20))
print(", ".join(map(str, d)))

'''
可调用对象
它可以定义可以作为函数的对象。最常见的应用之一是创建更好的装饰器。当我们试图像执行普通函数一样执行我们的对象时，
将调用神奇的方法。传递给它的每一个参数都会传递给调用方法。当我们想要创建可调用的对象时，这种方法是很有用的，
这些对象将作为参数化函数工作，或者在某些情况下是带有内存的函数。
'''
from collections import defaultdict
class CallCount:
  def __init__(self):
    self._counts = defaultdict(int)

  def __call__(self):
    self._counts[argument] += 1
    return self._counts[argument]

def stop_db_service():
  print("systemctrl stop service cassandra")

def start_db_service():
  print("systemctrl start service cassandra")


'''

class DbHandler:
    def __exit__(self):
        stop_database()
        return self

    def __enter__(self):
        start_database()

def db_print_keyspaces():
    print_desc_keyspace("localhost:6042")

def main():
    with DbHander():
    db_print_keyspaces

'''