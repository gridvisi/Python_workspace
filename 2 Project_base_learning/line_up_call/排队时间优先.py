import math,random

jobs=[math.floor(random.random()*100) for i in range(999)]
print((jobs),len(jobs))#999

workers=[0]*15
len(workers)#15

ajobs=[0]*((len(jobs)//len(workers)+1)*len(workers))


ajobs[:len(jobs)]=jobs[:]
print('ajobs:',ajobs,len(ajobs))#1005


re=[]
for i in range(0,len(ajobs),len(workers)):
    re.append(sorted(ajobs[i:i+len(workers)],reverse=True))
    len(re)#67

for j in range(len(re)):
    workers=[workers[i]+re[j][i] for i in range(len(workers))]
    workers.sort()

print(max(workers)) #3340

# customer是每人办理业务需要的时间
# n是窗口的数量

customers = [44, 44, 32, 41, 30, 14, 50, 19, 46, 36, 23, 30, 47, 7, 49, 7, 48]
n = 6

def queue_time(customers, n):
    re,res,step = [],[[0]*n],0  #初始化变量
    if len(customers) == 1:return customers[0]
    elif len(customers) == 0:return 0
    elif n > len(customers): return max(customers)
    # 以上是几种特殊情况的输出
    #1 排队的人数小于窗口数量
    #2 只有一个窗口办理业务 ...

    customer = [0] * (1+len(customers)//n)*n
    customer[:len(customers)] = customers[:]
    for i in range(0,len(customer),n):

        re.append(sorted(customer[i:i+n]))
     # 每n个顾客为一组，最后一组不足n个则以0补齐

    for j in range(len(re)):
        re[j].sort(reverse=True)  #耗时最长的顾客先办理
        res[0] = [res[0][i]+re[j][i] for i in range(n)]
        res[0].sort()
    return max(res[0])
print(queue_time(customers, n))