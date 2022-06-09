import time


# demo1
def process_bar(percent, start_str='', end_str='', total_length=0):
    bar = ''.join(["\033[31m%s\033[0m" % '▓▓'] * int(percent * total_length)) + ''
    bar = '\r' + start_str + bar.ljust(total_length) + ' {:0>4.1f}%|'.format(percent * 100) + end_str
    print(bar, end='', flush=True)


'''
for i in range(17):
    time.sleep(0.1)
    end_str = '100%'
    process_bar(i / 100, start_str='', end_str=end_str, total_length=15)
'''
import time
import datetime
year = int(input("请输入4位数的年份:\n"))
month = int(input("请输入月份:\n"))
day = int(input("请输入当月哪一天：\n"))

targetDay = datetime.date(year, month, day)
dayCount = targetDay - datetime.date(targetDay.year - 1 ,12, 31)
print("%s是%s年的第%s天." % (targetDay, targetDay.year, dayCount))
print("---RUNOOB EXAMPLE ： Loading 效果---")
print("Loading ",end = "")
#print('░'*100,end = "")
x = 6
for i in range(x):
    print('▓',end = '',flush =True)
    time.sleep(0.2)
print('░' * (20 - x), end="")