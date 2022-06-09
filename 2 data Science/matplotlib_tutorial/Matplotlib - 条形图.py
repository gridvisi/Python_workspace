

import numpy as np
import matplotlib.pyplot as plt

#%matplotlib inline
plt.style.use('seaborn')

x = np.arange(5)
y = np.array([-5,-3,-2,6,4])

fig,axes = plt.subplots(ncols = 2)
v_bars = axes[0].bar(x,y)
h_bars = axes[1].barh(x,y)

x = np.arange(5)
y = np.array([-5,-3,-2,6,4])

fig,axes = plt.subplots(ncols = 2)
v_bars = axes[0].bar(x,y)
h_bars = axes[1].barh(x,y)

axes[0].axhline(0,color='red',linewidth=2)
axes[1].axvline(0,color='red',linewidth=2)

x = np.arange(5)
y = np.array([-5,-3,-2,6,4])

fig,axes = plt.subplots(ncols = 2)
v_bars = axes[0].bar(x,y)
h_bars = axes[1].barh(x,y)

for i,height in enumerate(y):
    if height < 0:
        v_bars[i].set(color='red')
        h_bars[i].set(color='red')


x = np.linspace(0,10,100)
y = 2 * x

ax = plt.subplot()
ax.fill_between(x,y,color='lightblue')

x = np.linspace(0,10,200)
y1 = 2*x +1
y2 = 3*x +1.2
y_mean = 0.5*x*np.cos(2*x) + 2.5*x +1.1

ax = plt.subplot()
ax.fill_between(x,y1,y2,color='red')
ax.plot(x,y_mean,color='white')