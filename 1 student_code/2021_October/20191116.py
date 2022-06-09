# 执行结果是否争取，cpu耗时多长，内存

# 输出一千万内的偶数，比较两种写法的时间效率
import time
#第一种数组切片
start_time = time.time()
num = [i for i in range(0,10000000,2)]
end_time = time.time()
print(end_time - start_time)

#第二种偶数的条件判断
start_time = time.time()
num = [i for i in range(0,10000000) if i % 2 == 0]
end_time = time.time()
print(end_time - start_time)

#2 寻找素数
#lengthen
def chenfa(x,y):
    return x**y
print(chenfa(3,5))

n = 17
res = []
for i in range(1,n+1):
    if n % i == 0:
        res.append(i)
print(res,len(res))


#0.26999783515930176
#0.755185604095459
#第一种写法耗时是第二种写法的三分之一

name = 'liuchenxing'
ls = [2,4,6]
num = len(name)
num_2 = len(ls)

for i,e in enumerate(name):
    print(i,e)


s = 'abc,summerdefg'
print(list(s))
print(s.split(","))

s = [1,2,3,4]  #john
ls = 'abcd'
ls = list(ls)
print(list(ls))

#split
city = '重庆'
m = ['i','love','you']
city = list(city)
c = ['重', '庆']
city = list(c)
print('9999888',city)
print(''.join(city))

re = 0
for i in range(100000):
    re += i
print(re)
new = 'alan'
name = ['tang','hong','han','liu']
name.append(new)
print(name)

end_time = time.time()
print(end_time - start_time)