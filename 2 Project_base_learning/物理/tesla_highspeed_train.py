__author__ = 'Administrator'
import math
a = math.sqrt(21)*(2/63)
b = 1 + (math.sqrt(7)/21)
print (10*math.sqrt(a**2 + b**2))

print('air force:',0.15 * 1.22 * 19.63495 * 150 * 150 /2)
print(40.42345 * 9.8 * 600*1000)
print((196349.5*(1-0.001)/2)*600*1000*9.8,math.pi * 250*250,)
print(('rate =',196349.5*(1-0.001)/(2*4042345 *(1-0.001))))


print('H(v)=',- 2 + 5/(1+math.e) + 1/(1+math.e** -1) + 2/(1 + math.e**-2))
'''

1立方米10MPa的压缩空气完全释放出来放出的能量能否如下计算：
1，空气朝一个方向膨胀，膨胀到无能量时为100米长。
2，压力和膨胀体积成反比（也就是膨胀的距离成反比）P=100/L
从1到100积分
做功=∫（10MPa/L）*dL=ln100-ln1=4.6*10MPa=1.27KW*h

不知计算的对不对？
快速城市间运输的最新建议是超环线，在2012由Eon Mask推广。这个想法是通过一个从城市到城市运行的部分真空管将人运送到漂浮的吊舱内。
广告宣传的好处之一是它的高速（接近声音的速度）以及利用太阳能为超级环路供电的潜力。

在管子内部，舱内的空气减少，压力约为海平面气压。由于疏散的隧道和用于提升和推进列车的磁悬浮，维持列车的巡航速度对抗阻力所需的能量非常低。
然而，这一恩惠需要一个最大的能量消耗，即疏散一个足够长的适合隧道的长隧道。
一列相当的露天（即不在地铁内）的高速列车，大约需要多少次单程行程才能收回抽真空的初始能量消耗？
假定吊舱和超环管有一个空气密度的半径，从洛杉矶到旧金山的距离就是阻力系数。
一旦拉出，超环管保持部分真空状态。
'''

rate = 84.26083*2/180
print(math.pi * (1-rate) * 25)
print(math.pi)
for y in range(3610):
    if math.cos((y/180)*math.pi) == 0.1:
        print('y=',y)

i =1
while True:
    x = math.sqrt(i**2+9*i)
    if x%(int(x)) == 0:
        print (x,i)
    i +=1

"""
Created on Wed Dec 06 10:31:23 2017

@author: Michael Fitzgerald

"""
# https://brilliant.org/weekly-problems/2017-12-04/intermediate/?p=2
# Find the largest possible integer value of such that the expression is also an integer:

i = 1
limit = 1000

i_cubed_coeff = 0
i_squared_coeff = 1
i_coeff = 9
root = 1./2

while i  <= limit:
    i += 1
    x = (i_cubed_coeff*i**3 + i_squared_coeff*i**2 + i_coeff*i)**root
    if x == int(x):
        k = i

print ('\nThe largest possible integer value of such that the expression is also an integer:  %d' % k)
