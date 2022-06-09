import time
start_time = time.time()
print(time.time())
print(100%6)

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