

from pandas import date
from pandas_datareaders_unofficial import data
import datetime as dt
zm = data.DataReader(
    "ZM",
    start='2019-1-1',
    end=dt.datetime.today(),
    data_source='yahoo'
).reset_index()
zm.head()