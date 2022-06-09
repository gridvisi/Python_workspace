
'''

Phil去学校有两趟公交车可选，两趟车走的路线不太一样，还好等候站点在同一个地方，而且
A,B两趟车都是始发站：
A、每天6：00准时发车，每5分钟一班，路上需要花费40分钟
B、每天6：00准时发车，每8分钟一班，路上需要花费30分钟

如果学校要求8：30到校，Phil每天在7：30 - 8：10之间的到达车站，精确到分钟
输入：到达公交车站的时间
输出：A或者B
#比较A,B之间的哪一趟车较早到达学校？
'''

#首先看出这是一道非常适合编程解决的任务

# 学过的range函数，设置两种步长，罗列出A,B在7：30-8：30之间的各有多少趟车发车，
# A和B时间段内发车的时间列表

#第1步： 6：00-8：30 之间共150分钟，range的范围就是150

A = list(range(0,151,5))
B = list(range(0,151,8))
print(A)
print(B)
'''
A: [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 
    70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 
    130, 135, 140, 145, 150]
    
B: [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 
    112, 120, 128, 136, 144]
'''

# 第2步 考虑以上车次哪些保证在8：30之前到达？
# 简洁smart的做法是将range函数的终止提前，分别提前20分钟和17分钟，
# 思考为什么这样处理？


A = list(range(0,151-40,5))
B = list(range(0,151-30,8))
print('A路公车能够准时到达的车次发车时间：',A)
print('B路公车能够准时到达的车次发车时间：',B)
'''
A路公车能够准时到达的车次发车时间： 
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 
75, 80, 85, 90, 95, 100, 105, 110]

B路公车能够准时到达的车次发车时间： 
[0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120]
'''

#第3步 phil到达始发站的时间为start，判断即将迎来的A公交车和B公交车各是几点发车
#设置Phil到达始发站的时间距离6：00过去了start分钟，是变量！！

# 逻辑成立：phil有且只有两种选择，最近始发的A或B
# 问题就转换为到达开始算，下一趟A和B都是几点出发

# 比较 for循环 vs while循环哪个更适合？

start = 90
# phil是7：35到始发站，距离6：00过去了65分钟
# 思考start超过多少，phil绝无可能准时到学校？
# 如何将实现已知前后两个时刻，计算返回两个时刻之间的时长

#for循环
for t in A:
    if t >= start:
        print('for:',t)
        break

for t in A:
    if t >= start:pass
else: print('for:',t) # 为什么t是130？改用enumerate


for i,t in enumerate(A):
    if t >= start:
        end = i
else: print('for:',A[end]) # 为什么A[end]还是130！！


for i,t in enumerate(A):
    if t > start: #思考此处用 > 还是 >= ? 试试结果不同的原因
        end = i
        break  # 尽量避免break，思考函数写法
    print(A[i],t)

print('for:',f"第{end}趟，距6：00以后{A[end]}分钟是phil最近能搭乘的A路公车！")
# 为什么必须用break？不用break改用函数return

def nearest(st):  # st 是phil到达始发站的时间
    for i, t in enumerate(A):
        if t > start:  # 思考此处用 > 还是 >= ? 试试结果不同的原因
            end = i
            #break  # 尽量避免break，思考函数写法
            return f"第{end}趟，距6：00以后{A[end]}分钟是phil最近能搭乘的A路公车！"
st = 96
print('for循环的函数实现：',nearest(st))

#而且，改用函数后，轻松增加参数：timetable = A,B的时刻表


def nearest(st,timetable):  # st 是phil到达始发站的时间,timetable是任意路公车的时刻表
    for i, t in enumerate(timetable):
        if t > start:  # 思考此处用 > 还是 >= ? 试试结果不同的原因
            end = i
            #break  # 尽量避免break，思考函数写法
            return f"第{end}趟，距6：00以后{timetable[end]}分钟是phil最近能搭乘的A路公车！"
st,timetable = 96,A
print('for循环的函数+增加参数：',nearest(st,timetable))

def nearest(st,timetable):
    # st 是phil到达始发站的时间距离始发车时间的时长,timetable是任意路公车的时刻表
    for i, t in enumerate(timetable):
        if t > start:  # 思考此处用 > 还是 >= ? 试试结果不同的原因
            end = i
            #break  # 尽量避免break，思考函数写法
            return f"第{end}趟，距6：00以后{timetable[end]}分钟是phil最近能搭乘的B路公车！"
st,timetable = 66,B
print('for循环的函数实现：',nearest(st,timetable))

# while循环写法一：
'''
i = 0
while i < len(A):
    if A[i] < start:  #思考此处用 > 还是 >= ? 试试结果不同的原因
        i += 1
        #print('test:',A[i])
#print('while:',A[i])
#为什么以上写法最后一行print不执行？！！！

'''

#while loop正确的写法如下
i = 0
while A[i] < start: #思考此处用 > 还是 >= ? 试试结果不同的原因
    i += 1
    #print('test:',A[i])
#print('while:',f"第{i}趟，距6：00以后{A[i]}分钟是phil最近能搭乘的A路公车！")

#课后作业：模仿上述函数写法，改用while实现，函数输入参数与上述一致


'''
#for循环的函数+增加参数： 第14趟，距6：00以后70分钟是phil最近能搭乘的A路公车！
#for循环的函数实现： 第9趟，距6：00以后72分钟是phil最近能搭乘的B路公车！
'''

#第4步 确认最近的一趟A，B后，计算A,B各自到达学校的时间
#由第3步可知,如果Phil是 7：36分到达始发站,那么：

#如果选择A路车：Phil能够赶上A路公车的第14趟，距离6：00过去了70分钟
#如果选择B路车：Phil能够赶上B路公车的第9趟，距离6：00过去了72分钟

#那么，分别计算A的第14趟,B的第9趟车到达学校的时间

def nearest(st,timetable):
    # st 是phil到达始发站的时间,timetable是任意路公车的时刻表
    for i, t in enumerate(timetable):
        if t > start:  # 思考此处用 > 还是 >= ? 试试结果不同的原因
            end = i
            #break  # 尽量避免break，思考函数写法
            return end,timetable[end]
            #f"第{end}趟，距6：00以后{timetable[end]}分钟是phil最近能搭乘的B路公车！"

#去掉return返回结果中的注释部分，得到一个元组包含两个元素，取第2个元素

st,timetable,consume_A = 96,A,40
time_A = nearest(st,timetable)[1] + consume_A

st,timetable,consume_B = 96,B,35
time_B = nearest(st,timetable)[1] + consume_B
print(time_A,time_B)

#结论，Phil如果坐B路车比A路车早3分钟
# A路车可以在6：00开始计，110分钟后到学校
# B路车可以在6：00开始计，107分钟后到学校







# 函数timesheet返回结果是公车始发车开始计，
# 到最后一趟满足准时到校的车次，期间的发车时刻表
def timesheet(start,end,interval):
    return list(range(start,end+1,interval))


def nearest(st,timetable):
    # st是phil到达始发站的时间,timetable是timesheet函数返回结果任意路公车的时刻表
    for i, t in enumerate(timetable):
        if t > st:  # 思考此处用 > 还是 >= ? 试试结果不同的原因
            end = i
            return end,timetable[end]

#公交车在路上花费的时间consume，定义函数def compare_AB(a,b)
# a,b 参数分别是A,B路车，调用 earest(st,timetable)函数的返回结果

start,end,interval = 0,150,40
A = timesheet(start,end,interval)

start,end,interval = 0,150,35
B = timesheet(start,end,interval)

# A,B作为参数timetable，传入函数 nearest(st,timetable)
# nearest(st,timetable)的结果切片取第2个元素
a,b = nearest(st,A)[1],nearest(st,B)[1]

#继续努力，以上全部函数实现！！
#
# 定义函数:def timesheet(start,end,interval)
# 参数start,end是phil能够到达起始站的时间段，interval是发车间隔时间

# start是常量str：字符串格式 始发车时间，
# end是常量str：字符串格式 准时到校的时间
# interval整数int：整型格式，是常量，发车间隔的时间
# 注意输出结果是数组格式，包含的元素是整型int


'''子函数1: timelength'''
# 定义一个子函数timelength 计算两个时刻start,end之间的时长

def timelength(start,end):
    s = eval(start.split(":")[0]) * 60 + eval(start.split(":")[1])
    t = eval(end.split(":")[0]) * 60 + eval(end.split(":")[1])
    return int(t - s)  #

start,end = "6:00","7:36"
print('Phil到达车站时间距离始发车的时长:',timelength(start,end))

'''子函数2: arrival_time'''

# 引入新的参数公车始发车的时间：first->str 字符串格式如 "6:00"
# arrival(first,ontime,consume)
# ontime是phil坐上车的时间，注意要晚于抵达车站的时间
# consume函数是指路上耗费的时间，是常量而非变量，需初始化确定不变
# 函数返回结果是时钟格式表达如 ："8:10"

def arrival_time(first,ontime,consume): # ->str,int,int
    hour,minute = int(first.split(":")[0]),int(first.split(":")[1])
    h = hour + (minute + consume + ontime) // 60
    m = (minute + consume + ontime) % 60
    return ":".join([str(h),str(m)])
stime = "6:00" #始发车时间
st = 66  #距离stime的时间，以分钟单位

# 函数有助于灵活处理始发时间不同的情景了
# A路车的始发时间是6:10, B路车的始发时间是6:30
# 子函数转换习惯表达时间格式
# start变量是始发车时间，end是phil到达车站的时间"7:36"
# 需要用到的子函数之间的逻辑关系 -> 调用函数

#首先，函数需要初始化的常量参数有哪些？
first = "6:10"     # 常量 某路公交始发车时间
interval = 8       # 公车发车的间隔时间
consume = 40       # 路上耗费的时间

latest = "8:30"    # 常量 最迟不能晚于到校的时间
st = "7:30"        # 变量 Phil抵达车站的时间

#1、根据变量st的值，调用函数得到最近的到站公车


def nearest(st,first,latest,interval,consume):
    # st是phil到达始发站的时间,
    # first,latest 始发车时间，准时到校的时间
    start, end = 0,timelength(first,latest)
    timesheet = list(range(start, end + 1, interval))
    st = timelength(first,st)
    for i, t in enumerate(timesheet):
        if t > st:  # 思考此处用 > 还是 >= ? 试试结果不同的原因
            end = i
            ontime = timesheet[end]
            return arrival_time(first,ontime,consume)

'''
A,B两趟车都是始发站：
A、每天6：00准时发车，每5分钟一班，路上需要花费40分钟
B、每天6：00准时发车，每8分钟一班，路上需要花费30分钟
'''
# A路车
st,first,latest,interval,consume = "7:46","6:10","8:30",5,40
print('选A路车抵达:',nearest(st,first,latest,interval,consume))

# B路车
st,first,latest,interval,consume = "7:46","6:30","8:30",8,30
print('选B路车抵达:',nearest(st,first,latest,interval,consume))




#主函数


'''
def cal_time(begin,start,deadline,interval,consume):
    st = timelength(begin,start)
    deadline_consume = timelength(begin,deadline)

    print('deadline_consume:',deadline_consume)

    timetable = timesheet(begin,deadline_consume,interval)
    nearest_time = nearest(st,timetable)[1]
    return arrival(begin,nearest_time,consume)

begin,start,deadline = "6:10","7:36","8:30"
interval,consume = 5,40
print(cal_time(begin,start,deadline,interval,consume))
'''