'''
https://www.geeksforgeeks.org/tracking-bird-migration-using-python-3/


dataset
D:\data_science\dataset\Data-Analysis-master\data-analysis project - 1 - bird_migration_cartopy
'''



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
path = "D://data_science//datase//Data-Analysis-master//data-analysis project - 1 - bird_migration_cartopy//bird_tracking.csv"
path = "bird_tracking.csv"
birddata = pd.read_csv(path)
bird_names = pd.unique(birddata.bird_name)

# storing the indices of the bird Eric
ix = birddata.bird_name == "Eric"
x, y = birddata.longitude[ix], birddata.latitude[ix]
plt.figure(figsize=(7, 7))
plt.plot(x, y, "b.")

''' To look at all the birds trajectories,
    we plot each bird in the same plot '''
plt.figure(figsize=(7, 7))
for bird_name in bird_names:
    # storing the indices of the bird Eric
    ix = birddata.bird_name == bird_name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x, y, ".", label=bird_name)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.show()

'''
PART (2/5): 2D Speed Vs Frequency 
In this second part of the case study, we are going to visualize 2D speed vs Frequency for the gull named “Eric”.
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

birddata = pd.read_csv("bird_tracking.csv")
bird_names = pd.unique(birddata.bird_name)

# storing the indices of the bird Eric
ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]

plt.figure(figsize = (8,4))
ind = np.isnan(speed)
plt.hist(speed[~ind], bins = np.linspace(0,30,20), normed=True)
plt.xlabel(" 2D speed (m/s) ")
plt.ylabel(" Frequency ")
plt.show()
'''
参数speed[~ind]表示我们只包括那些ind != True的条目，
bins=np.linspace(0,30,20)表示沿x轴的bin将从0到30变化，
其中有20个bin，线性间隔。最后，我们用
xlabel()和ylabel()函数分别绘制沿x轴的二维速度（米/秒）和沿y轴的频率，
并用plt.show()绘制数据。

输出 : 
'''

'''
第（3/5）部分。时间和日期 
第三部分是与日期和时间有关。我们将直观地看到埃里克在旅途中走完固定距离所需的时间（以天为单位）。
如果他在相同的时间内走完相同的距离，那么耗时与观察曲线将是线性的。
'''

import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

birddata = pd.read_csv("bird_tracking.csv")
bird_names = pd.unique(birddata.bird_name)

timestamps = []
for k in range(len(birddata)):
	timestamps.append(datetime.datetime.strptime(birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))

birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)

times = birddata.timestamp[birddata.bird_name == "Eric"]
elapsed_time = [time-times[0] for time in times]

plt.plot(np.array(elapsed_time)/datetime.timedelta(days=1))
plt.xlabel(" Observation ")
plt.ylabel(" Elapsed time (days) ")
plt.show()


'''
第(4/5)部分。日平均速度 
我们将直观地看到名为 "埃里克 "的海鸥在飞行记录的总天数中的日平均速度。
'''
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

birddata = pd.read_csv("bird_tracking.csv")
bird_names = pd.unique(birddata.bird_name)

timestamps = []
for k in range(len(birddata)):
	timestamps.append(datetime.datetime.strptime(birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))
birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)

data = birddata[birddata.bird_name == "Eric"]
times = data.timestamp
elapsed_time = [time-times[0] for time in times]
elapsed_days = np.array(elapsed_time)/datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []
for (i,t) in enumerate(elapsed_days):
	if t < next_day:
		inds.append(i)
	else:
		daily_mean_speed.append(np.mean(data.speed_2d[inds]))
		next_day += 1
		inds = []

plt.figure(figsize = (8,6))
plt.plot(daily_mean_speed, "rs-")
plt.xlabel(" Day ")
plt.ylabel(" Mean Speed (m/s) ");
plt.show()

'''
PART (5/5): Cartographic View 
In this last part, we are going to track the Birds over a map. 

PART (5/5): 地图视图 
在这最后一部分，我们将在地图上追踪鸟类。

'''

import pandas as pd
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

birddata = pd.read_csv("bird_tracking.csv")
bird_names = pd.unique(birddata.bird_name)

# To move forward, we need to specify a
# specific projection that we're interested
# in using.
proj = ccrs.Mercator()

plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
for name in bird_names:
	ix = birddata['bird_name'] == name
	x,y = birddata.longitude[ix], birddata.latitude[ix]
	ax.plot(x,y,'.', transform=ccrs.Geodetic(), label=name)
plt.legend(loc="upper left")
plt.show()
