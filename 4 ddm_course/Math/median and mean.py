'''
https://brilliant.org/daily-problems/weighty-dogs/

什么是中位数：
中位数：是指一组数据从小到大排列，位于中间的那个数。可以是一个（数据为奇数），也可以是2个的平均（数据为偶数）

技能点：python 生成n个随机数，其和为给定的数
'''
n = 8
mean_value = 50
d1,d2 = 80,220

def mean2median(mean_value,n,d1,d2):
    # all = [80,220,sum([x])]
    # mean = sum([all]) / n == mean_value
    # so that conclude x
    x = len((mean_value,n,d1,d2)) - 2
    all_sum = mean_value * n
    x_Sum = all_sum - sum((mean_value,n,d1,d2)[2:])
    print(x,x_Sum)
    x_Mean = x_Sum / (n - x)
    #median = [sorted(all)[len(all)//2-1:len(all)//2+1] if len(all)%2 ==0 else sorted(all)]
    return int(x_Mean)
print(mean2median(mean_value,n,d1,d2))

# 问题等价于6只狗共300斤，那么median概率最大的分布在哪里？
# 下面算法问题是无法有效的定义max_w，确保随机数之和落在100之内！！

import random
#choice = random.choice
n = 8
for _ in range(1000):
    x = len((mean_value,n,d1,d2)) - 2
    ans = []
    max_w = mean_value * n - sum((mean_value,n,d1,d2)[2:])
    all = [random.randint(1,max_w) for _ in range(6)]
    #print(max_w,all)
    if sum(all) == 100:
        ans.append([sorted(all)[len(all)//2-1:len(all)//2+1] if len(all)%2 ==0 else sorted(all)])
        #print(ans)
#print(ans)


#python 生成n个随机数，其和为给定的数

import random

def func(amount,num):
    list1 = []
    for i in range(0,num-1):
        a = random.randint(1,amount)    # 生成 n-1 个随机节点
        list1.append(a)
    list1.sort()                        # 节点排序
    list1.append(amount)                # 设置第 n 个节点为amount，即总金额

    list2 = []
    for i in range(len(list1)):
        if i == 0:
            b = list1[i]                # 第一段长度为第 1 个节点 - 0
        else:
            b = list1[i] - list1[i-1]   # 其余段为第 n 个节点 - 第 n-1 个节点
        list2.append(b)

    return list2

#amount = mean_value*n
#num  = n

amount = mean_value*n - sum((mean_value,n,d1,d2)[2:])
num  = n - len((mean_value,n,d1,d2)[2:])

all = func(amount,num)

#print('func:',func(amount,num),amount,num)
#print(all)
ans = []
for i in range(100):
    all = func(amount, num)
    #
    all.append(d1)
    all.append(d2)
    print(all,sum(all))
    medi = [sorted(all)[len(all)//2 - 1:len(all)//2 + 1] if len(all) % 2 == 0 else sorted(all)[len(all)//2]]
    print(medi,amount, num)
    ans.append(sum(medi[0])/len(medi[0]))
print('average median:',sum(ans)/len(ans))

# largest median not equal to average median!!!

for i in range(100):
    all = func(amount, num)
    #
    all.append(d1)
    all.append(d2)
    print(all,sum(all))
    medi = [sorted(all)[len(all)//2 - 1:len(all)//2 + 1] if len(all) % 2 == 0 else sorted(all)[len(all)//2]]
    print(medi,amount, num)
    ans.append(max(medi[0]))
print('largest median:',max(ans))

# why code solution is not true? because random.weight maybe 0 !!
max_all = [0,0,0,32,32,36,80,220]
ans = [sorted(max_all)[len(max_all)//2 - 1:len(max_all)//2 + 1] if len(max_all) % 2 == 0 else sorted(max_all)[len(max_all)//2]]
print(sum(ans[0]),len(ans[0]))
print(sum(ans[0])/len(ans[0]))
# so math solve right answer is {1,1,1,32,32,33,80,220}


# Brilliant solution
solutions = set()

from functools import lru_cache
#@lru_cache
def calc(n, dogs, last):
    if n == 6:
        if sum(dogs) == 100:
            d = sorted(dogs, reverse=True)
            solutions.add((tuple(d), (d[1]+d[2])/2))
        print(n)
        #print(solutions,n,end=',',flush=10)
        return      #由于此处设置退出条件是n == 6，sum(dogs) 不等于 100,中断时n= 6

    else:
        print(n)
        for i in range(last, 100):
            dogs[n] = i
            #print(dogs,end=' ')
            #print(calc(n, dogs, last),end=' ') #maximum recursion depth exceeded in comparison
            if sum(dogs[:n+1]) > 100:
                return
            else:
                calc(n+1, dogs, i)

calc(0, [0, 0, 0, 0, 0, 0], 1)

maximum = max(solutions, key=lambda x: x[1])[0]
minimum = min(solutions, key=lambda x: x[1])[0]
nonEqual = [(d, m) for d, m in solutions if len(d) == len(set(d))]
max_nonEqual = max(nonEqual, key=lambda x: x[1])[0]
min_nonEqual = min(nonEqual, key=lambda x: x[1])[0]
for criterion, value in [("max median:", maximum), ("min median", minimum),
                  ("max median distinct:", max_nonEqual),
                  ("min median distinct:", min_nonEqual)]:
    dogs = [220, 80]
    dogs.extend(value)
    print(f"{criterion:11} {(dogs[3] + dogs[4])/2:4}  {sorted(dogs, reverse=True)}")

'''
max median: 32.0  [220, 80, 33, 32, 32, 1, 1, 1]
min median   1.0  [220, 95, 80, 1, 1, 1, 1, 1]
max median distinct: 30.5  [220, 80, 33, 31, 30, 3, 2, 1]
min median distinct:  4.5  [220, 85, 80, 5, 4, 3, 2, 1]


'''