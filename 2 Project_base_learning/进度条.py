#https://blog.csdn.net/sinat_28576553/article/details/81154912?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
import sys
from time import sleep
import time
print("Loading",end = "")
for i in range(6):
    print(".",end = '',flush = True)
    time.sleep(0.2)

def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print(
        '[', '#' * left, ' ' * right, ']',
        f'{percent:.0f}%',sep='',end="",flush=True)
    sys.stdout.flush()

#print(progress(30,10))

for i in range(63):
    progress(i)
    sys.stdout.flush()
    sleep(0.01)

import sys,time
print('打印进度条：')
for i in range(20):
    sys.stdout.write('#') #标准化输出，类似print,print默认换行
    sys.stdout.flush() #强制刷新，将内存中的内容写入硬盘
    time.sleep(0.1) #推迟执行的秒数
    if i == 10:
        sys.stdout.write('100%')