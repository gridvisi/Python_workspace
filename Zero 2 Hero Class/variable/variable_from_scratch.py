
x, y = 1,1
x = 2
y = 2
print(x is y)
print(x == y)

'''
def add(a, b):
return a + b

def subtract(a, b):
pass

def multiply(a, b):
pass

def divide(a, b):
pass

'''


def add(a, b):
    return a + b


def subtract(a, b):
    pass


def multiply(a, b):
    pass


def divide(a, b):
    pass


# 配合slide python编程和中小学数学融合

def add(a, b):
    return a + b


# Q1:已知出生在x年，计算n岁时是哪一年？


def subtract(a, b):
    pass
    return a - b


# Q2: 已知出生在x年，计算2021年是几岁？


def multiply(a, b):
    pass
    return a * b


# Q3：已知操场每圈是400米，你跑了3圈半，问跑了有多少米？


def divide(a, b):
    pass
    return a / b


# Q4: 父母给了100元零花钱，每天花15元，够用几天？


# Q5: 妈妈改为每天给你10元，连续10天，第10天时你从收到的10元取出一半借给同桌
# 同桌第11天多还你2元，问你总共有多少钱？

# 10 * 10  -  10/2  +  (10/2+2) = ?
# x,y,z 变量赋值
x = 10 * 10
y = 10 / 2
z = 7
print(x - y + z)

# Q6: 妈妈每天给你n元，连续d天，你分给同桌一半，同桌还你多了两元
# 请编写函数输出你总共有多少钱？

# Input:
n = 10
d = 10

x = multiply(n, d)
y = divide(n, 2)
z = y + 2
result = add(subtract(x, y), z)

# Output:
print('结果一:', result)

# 可以这些写吗？
result = add(subtract(multiply(n, d), divide(n, 2)), divide(n, 2) + 2)
print('结果二:', result)

# Q：找出三条边可以组成直角三角形Right Angle Triangle的数组
# triangle = [3,4,5]

print('勾股定理：', 3 ** 2 + 4 ** 2 == 5 ** 2)


def right_angle(arr):
    sq = 0
    arr = sorted(arr)
    xiebian = arr[-1]
    for i in arr[:-1]:
        sq += i ** 2
    return sq == xiebian ** 2


arr = [3, 4, 5]
arr = [3, 5, 4]
print(right_angle(arr))

#Q8:num_plate = ['渝A9919','渝C5072','渝A2966','渝D8371','渝A3417','渝A5255','渝AD9919']
# 今天是单号，限行双号，请判断哪些车号不能上路？
car_plate = ['渝A9919','渝C5072','渝A2966','渝D8371','渝A3417','渝A5255','渝AD9919']

no_way = []
for num in car_plate:
    if int(num[-1]) % 2 == 0:
        no_way.append(num)
print(no_way)

'''
Python
Keywords	 	 
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
'''



''''
使用方法：round(number,digits)

digits>0，四舍五入到指定的小数位
digits=0, 四舍五入到最接近的整数
digits<0 ，在小数点左侧进行四舍五入
如果round()函数只有number这个参数，等同于digits=0
四舍五入规则：

要求保留位数的后一位<=4，则舍去3，如5.214保留小数点后两位，结果是5.21
要求保留位数的后一位“=5”，且该位数后面没有数字，则不进位，如5.215，结果为5.21
要求保留位数的最后一位“=5”，且该位数后面有数字，则进位，如5.2151，结果为5.22
要求保留位数的最后一位“>=6”，则进位。如5.216，结果为5.22
'''
alex = 11
ada = 11

print('id of ada and alex:',id(alex),id(ada))
print(id(ada) == id(alex))



x = 1.73
print(int(x))
print(x)
print(round(x))
print(round(x,1))

y = -2.961

print(round(y,2))
print(round(y))
print(round(y,1))

z = 5.1415
z = 3.1415
print('z-1',round(z,-1))
data = [0.15, -1.45, 3.65, -7.05, 2.45]

