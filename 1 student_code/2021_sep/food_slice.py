
hz = "火锅  鸡腿  蜜蜂 "
#使用列表切片，重新组合看，能组合出几种食物？举粟子

print('1:',hz[0] + hz[5]) #火腿
print('2:',hz[1 : 6 : 2])
print('3:',hz[::5])
print('4:',hz[-3:-1])

#20210925 B04 ROOM
names = []
names.append('zhouhongyu')
names.append('zhangzhanming')
names.append('liuzhimo')
names.append('xingtianrui')
print(names)
print(names[::-1])
print('12345'[6:0:-1])

print('loop')
for name in names:
    print(name)

#while do you get up today?
#when do you get up today?

#alarm for
#10:30 - 6:30
for hour in range(9):
    print(hour)


#while "mother reach 17school":
    #xingtianshui stop watching ipad

lift = 9
dingdingmao = 8

while lift < 8:
    lift += 1
    print('lift:',lift)

