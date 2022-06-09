

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
