'''
https://www.codewars.com/kata/5f882dcc272e7a00287743f5/train/python


'''

always_odd=lambda n:n-(n%2==0)

'''
今天的任务是练手常用的函数

北京车辆出行早期是分单双号限行，尾号为单数的单号可以上路，双号结尾的双号上路。​
你要写一个程序，输入车牌尾号和当前日期，返回判断这辆车是否可以上路。

​车牌尾号是3，今天是元月5号，那么可以上路​
'''

car_plate = '渝A9919'
today = '20210105'
print((eval(car_plate[-1]) + eval(today[-1]))%2==0)

car_plate = ['渝A9919','渝C5072']
today = '20210105'

always_odd=lambda n:n-(n%2==0)

a = eval(car_plate[0][-1])
b = eval(car_plate[1][-1])
t = eval(today[-1])%2
print([n for n in car_plate if eval(n[-1])%2 == t])

# 往往遇到判断奇偶只会用 x% 2==0，如果引入二进制会多一种角度看待问题​
x = 234
print(bin(x)[-1])
print(bin(x)[-1] == '0')

#1st
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))

'''
进一步，寻找一个数附近的平方数：例如3，3最接近的平方数是4，因为4是2的平方而且没有比4更接近的了，3-1=2，4-3=1
'''


'''
进一步，寻找一定范围内，有多少个数恰好是2的整数幂，​如：0-10之间有2，4，8满足，即有3个​！
'''
a = 1
b = 1000
print(bin(a),bin(b))

# 观察2的整数次幂，只有一个位是1，右边全是0
# 比0b1100100大的数，并且满足上面特征的是0b1100100中，0b1后面的1都换成0，并且在添加1个0
# 结论是符合0b1*****,*代表若干个0,既大于a，又小于b的二进制数有多少个
# 问题转换为：比a的长度多1位，比b的长度少一位，这中间有多少个整数？

#a, b = 1,33
print(len(bin(b)) - len(bin(a)))

# 效率比较差的写法
cunt = 0
for i in range(a,b+1):
    if bin(i).count('1') == 1 and bin(i)[-1] == '0':
        cunt += 1
print(cunt)
