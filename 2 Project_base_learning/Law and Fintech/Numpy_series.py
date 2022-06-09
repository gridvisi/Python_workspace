'''
关于时间的处理，Python中自带的处理时间的模块就有time 、datetime、calendar，另外还有扩展的第三方库，
如dateutil等等。通过这些途径可以随心所欲地用Python去处理时间。当我们用NumPy库做数据分析时，如何转换时间呢？

在NumPy 1.7版本开始，它的核心数组（ndarray）对象支持datetime相关功能，由于’datetime’这个数据类型名称已经
在Python自带的datetime模块中使用了， NumPy中时间数据的类型称为’datetime64’。

单个时间格式字符串转换为numpy的datetime对象，可使用datetime64实例化一个对象，如下所示：

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datetime_nd = np.datetime64('2019-01-01')
print(type(datetime_nd))  #<class 'numpy.datetime64'>

datetime_str=np.datetime_as_string(datetime_nd)
print(type(datetime_str))

datetime_array = np.array(['2019-01-05','2019-01-02','2019-01-03'], dtype='datetime64')
print(datetime_array)#['2019-01-05' '2019-01-02' '2019-01-03']
print(type(datetime_array))#<class 'numpy.ndarray'>
print(type(datetime_array[0]))#<class 'numpy.datetime64'>


datetime_array = np.arange('2019-01-05','2019-01-10', dtype='datetime64')
print(datetime_array)#['2019-01-05' '2019-01-06' '2019-01-07' '2019-01-08' '2019-01-09']

# generate year datetime array
datetime_array = np.arange('2018-01-01','2020-01-01', dtype='datetime64[Y]')
print(datetime_array)#['2018' '2019']
# generate month datetime array
datetime_array = np.arange('2019-01-01','2019-10-01', dtype='datetime64[M]')
print(datetime_array)#['2019-01' '2019-02' '2019-03' '2019-04' '2019-05' '2019-06' '2019-07' '2019-08' '2019-09']
# generate week datetime array
datetime_array = np.arange('2019-01-05','2019-02-10', dtype='datetime64[W]')
print(datetime_array)#['2019-01-03' '2019-01-10' '2019-01-17' '2019-01-24' '2019-01-31']
# generate ms datetime array
datetime_array = np.arange('2019-01-05','2019-01-10', dtype='datetime64[ms]')
print(datetime_array)
#['2019-01-05T00:00:00.000' '2019-01-05T00:00:00.001'
# '2019-01-05T00:00:00.002' ... '2019-01-09T23:59:59.997'
# '2019-01-09T23:59:59.998' '2019-01-09T23:59:59.999']

# 将numpy.datetime64转化为datetime格式转换为datetime格式，可使用astype()方法转换数据类型，如下所示：
import datetime
datetime_df=datetime_nd.astype(datetime.datetime)
print(type(datetime_df))#<class 'datetime.date'>

'''
numpy也提供了datetime.timedelta类的功能，支持两个时间对象的运算，得到一个时间单位形式的数值。
因为numpy的核心数组（ndarray）对象没有物理量系统（physical quantities system），
所以创建了timedelta64数据类型来补充datetime64。
datetime和timedelta结合提供了更简单的datetime计算方法
'''
# numpy.datetime64 calculations
datetime_delta = np.datetime64('2009-01-01') - np.datetime64('2008-01-01')
print(datetime_delta)#366 days
print(type(datetime_delta))#<class 'numpy.timedelta64'>
datetime_delta = np.datetime64('2009') + np.timedelta64(20, 'D')
print(datetime_delta)#2009-01-21
datetime_delta = np.datetime64('2011-06-15T00:00') + np.timedelta64(12, 'h')
print(datetime_delta)#2011-06-15T12:00
datetime_delta = np.timedelta64(1,'W') / np.timedelta64(1,'D')
print(datetime_delta)#7.0

