# https://www.codewars.com/kata/574b3b1599d8f897470018f6/solutions/python
'''
美国人很奇怪：在他们的建筑中，第一层实际上是底层，没有13层（由于迷信）。
写一个函数，给定一个美国系统的楼层，返回欧洲系统的楼层。
随着1楼被底层取代，13楼被删除，数字会向下移动以取代其位置。在13楼以上的情况下，
他们向下移动了两个，因为他们下面有两个被省略的数字。
地下室（负数）与通用层保持一致。

例子: lobby 大堂
1 => 0
0 => 0
5 => 4
15 => 13
-3 => -3
'''
def get_real_floor(n):
    if n <= 0: return n
    if n < 13: return n-1
    if n > 13: return n-2

def get_real_floor(n):
    return n if n < 1 else n - 1 if n < 13 else n - 2

def get_real_floor(n):
    return n - (n > 0) - (n > 13)

print([get_real_floor(n) for n in range(-3,18,1) if n!= 13])
print([n for n in range(-3,18,1) if n != 13])

name = 'chongqing'
name_1 = 'chongqin'

print(name_1 in name)
print(name in name_1)

a = [1,2,3,4]
b = 5
print(b in a)

print('eng  li  sh  ' in 'eng  li  sh  ')

s = 'EnGLish'
print(s.lower())

print('how to understand bool case 1st:')

print('CASE 1:',True == 1,False==1,False==0)
print(8 - True)
print(8 > 7, 8 < 7)

# control flow
# conditional statement

#light = 'green'
light = 'yellow'
light = None
light = 'white'

if light == 'red':
    print('stop')
elif light == 'green':
    print('pass')

elif light == None:
     print('110')

else:
    print('depend on')

# 小兔子每2天吃一斤萝卜，每三天吃一斤白菜，
# 问30天需要吃多少斤萝卜和白菜
# 哪些天既吃罗卜，也吃白菜（分别用数学和编程两种思路解）
carrot = 0
veg = 0
for day in range(1,31):
    if day%2 == 0:
        carrot += 1
    if day%3 == 0:
        veg += 1
print(carrot,veg)





