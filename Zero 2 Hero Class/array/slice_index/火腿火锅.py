
#学过了Python的列表切片操作

#汉字组成的字符串，挑其中的字可以重新组合成一种食物。看看能组成多少种

hz = "火锅  鸡腿  蜜蜂 "
#使用列表切片，重新组合看，能组合出几种食物？举粟子
print(hz.index('蜜蜂'))
start,end,step = 1,len(hz),2
print(hz[ start : end : step])

hz_list = list(hz)
print(hz_list)
hz_list[8] = "蜂"
hz_list[9] = "蜜"
print(hz_list)

print(hz[0] + hz[5])
#火鸡

print(hz[::2])
print(hz[::5])
print(hz[-3:-1])

#
print([i for i in range(101)][0:101:5])
print(list(range(101))[0:101:5])

#365
print(list(range(366))[0:366:15])
print(list(range(366))[100:200:15])