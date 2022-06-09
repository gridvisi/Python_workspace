# 输入 input
a = 11  #int
print(a/2, a*2, a+2, a-2, a//2) #

# 100 分钟是多少小时，分钟？
m = 100
# f output 输出 f输出
print(f"100分钟是：{m//60}小时,{m % 60}分钟")

print( 100 % 60) #取余运算
print(10 % 3)

#11除以5，等于2，余数=1？ )
print(11//5, 11 % 2)

'''

Write a function, which takes a non-negative integer (seconds) 
as input and returns the time in a
human-readable format (HH:MM:SS)
编写一个函数，它以非负整数（秒）作为输入，并以可读格式（HH:MM:SS）返回时间
HH = hours, padded to 2 digits, range: 00 – 99
HH=小时，填充到 2 位数，范围：00-99
MM = minutes, padded to 2 digits, range: 00 – 59
MM=分钟，填充到 2 位数，范围：00-59
SS = seconds, padded to 2 digits, range: 00 – 59
SS=秒，填充到 2 位数，范围：00-59
The maximum time never exceeds 359999 (99:59:59)
最大时间从不超过 359999（99∶59∶59）
'''
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60)




#11除以5，等于2，余数等于？？？
print(11//5, 11 % 2)

mi = 1033
print(f"1033 米是多少千米·:{mi//1000}千米,{mi%1000}米")

#'=========================================================='

hav = 2560
print(f"2560 千克·是多少吨:{hav//1000}吨,{hav%1000}千克")

#wangzijie
m=100
print(f"100分钟是多少小时：{m//60}小时,{m%60}分钟")
#买菜花了112角，112角是多少元，角？
m=112
print(f"112角是多少元，角:{m//10}元，{m%10}角")
#浣熊是7.5千克，7.5千克是多少克?
m=7.5
print(f"7.5千克是多少克:{m*1000}克")

#


a = 'qingzidong'
a = ['10',10]

#
#a = input('我在输出：',)