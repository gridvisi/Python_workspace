'''

众所周知, 名人、伟人都有不寻常的个人特性。如果你学代数，算一算他们的生日, 你就会发现，所有的名人和伟人的生日都具有如下的一个特点：
如：爱因斯坦的生日是：1879年3月14日，将年月日写在一起是 1879314。把这个数随意排列一下，可得到另一个数，比如： 4187139。
用大的数减去小的数得到一个差：4187139-1879314 = 2307825。将差的各个位数相加得到一个数，2+3+0+7+8+2+5 = 27，
再将这个数的位数相加，其和是9。即最后得到一个最大的一位数9。
按上述方法来计算数学家高斯的生日：高斯生于1867年11月7日，于是可得一个数 1867117， 重新排列后的数比如是1167781，
差数为 1867117-1167781 = 669336，算其位数和可得： 6+9+9+3+3+6 = 36，再算位数之和, 最后得 3+6 = 9。
同样,最后得到一个最大的一位数9。
所有的著名人物的生日都有这样的特点。这是成为著名人物的“必要条件”。

year = int(input("出生年份4位："))
month = int(input("出生月份2位："))
day = int(input("出生日期1-2位："))
'''
import random
ymd = 19720903
ymd = 19740906
ymd = 20060813
ymd = 20130923
#sort random
list_name = ["龙", "刘", "李", "周", "张"]
random.shuffle(list_name)
print(list_name)

list_year = list(str(ymd))  # 整数类型转换数组散列
random.shuffle(list_year)   # 数随意排列一下，可得到另一个数，
x = ''.join(list_year)      # 列表散列转为字符串
minu = abs(int(x) - ymd)    # 用大的数减去小的数得到一个差
print(list_year,x,minu)
total = sum([int(i) for i in str(minu)])
l = len(str(total))

while l > 1:
    total, minu = sum([int(i) for i in str(minu)]), total
    l = len(str(total))
print(total)