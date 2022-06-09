'''
原文链接：https://blog.csdn.net/Chihwei_Hsu/java/article/details/83589309
'''

import time
import random

def birthday(n):
    st=(2006,1,1,0,0,0,0,0,0)
#设置开始日期时间元组（1976-01-01 00：00：00）
    nd=(2006,12,31,23,59,59,0,0,0)
#设置结束日期时间元组（1990-12-31 23：59：59）
    start=time.mktime(st)
#生成开始时间戳
    end=time.mktime(nd)
#生成结束时间戳
#随机生成60个日期字符串
    arr = []
    for i in range(n):
        t=random.randint(start,end)
    #在开始和结束时间戳中随机取出一个
        date_touple=time.localtime(t)
    #将时间戳生成时间元组
        date=time.strftime("%Y-%m-%d",date_touple)
    #将时间元组转成格式化字符串（1976-05-21）
        arr.append(date)
    return arr
#print(len(arr),len(set(arr)))

def tipping_point():
    n, dup = 0, []
    while True:
        arr = birthday(n)
        for i in range(len(arr)):
            if arr[i] not in dup:
                dup.append(arr[i])
        #print(dup)
        if len(arr) == len(set(arr)):
            n += 1
        else:return n  #,len(arr)-len(set(arr))
print("人数增加到"+ f'{tipping_point()}'+'时出现重复')

def tipping(n):
    re, dup = [], []
    while True:
        arr = birthday(n)
        '''        
        for i in range(len(arr)):
            if arr[i] not in dup:
                dup.append(arr[i])
        #print(dup)        
        '''
        if len(arr) == len(set(arr)):
            return 0
        else:return len(arr)-len(set(arr))
n = 28
ct = 0
print("生日重复的人数",tipping(n))
for _ in range(1000):
    ct += tipping(n)
print("班级人数为"+f'{n}'+"出现生日重复的平均次数是",ct/1000)



from decimal import Decimal
ct = 0
x = 28
p = 1
for i in range(364, 364 - x, -1):
    p *= Decimal(i / 365)
print('班上有'+f'{x}'+"人时，相同生日的概率是"+f'{round(1-p,3)}')

from decimal import Decimal
ct = 0
x = 60
p = 1
x = 1
while True:
    for i in range(364,364-x,-1):
        p *= Decimal(i/365)
    #print(p)
    if round(1-p,5) == round(0.999999,5):
        print(x-1)
        break
    else:
        x += 1




#s = lambda x:1*x,[x+1 for x in range(365)]



x_data = []
y_data = []
# start simultion for biased permutations
from random import randint
import matplotlib.pyplot as plt
# plot
fig, axs = plt.subplots(ncols = 2, sharey=True, figsize=(14, 6))
fig.subplots_adjust(hspace=0.5, left=0.07, right=0.93)
hb = axs[0].hexbin(x_data, y_data, gridsize=50, cmap='inferno')
axs[0].axis([0, 1000, 0, 1000])
axs[0].set_title("Distributed Permutation")
cb = fig.colorbar(hb, ax=axs[0])
cb.set_label('frequency')

x_data = []
y_data = []
# start simultion for 100 times

for simulation in range(100):
    x = [i for i in range(2,60)]
    y = [tipping(i) for i in x]
#print(y)
'''

                
import time
n = 23
print([time.strftime("%Y-%m-%d") for _ in range(n)])



# python2 不兼容，python3正常
import datetime,random
def randomtimes(start, end, n, frmt="%Y-%m-%d"):
    st = datetime.datetime.strptime(start, frmt)
    nd = datetime.datetime.strptime(end, frmt)
    return [([random.random() * (st - nd) + st])[:3] for _ in range(n)]
#print(randomtimes(start, end, n, frmt="%Y-%m-%d"))
print(randomtimes('2018-06-01','2018-11-01',10))
'''


