'''
作业1：整数因子帮助你给兔子买饲料。# 小兔子每2天吃一斤萝卜，每三天吃一斤白菜，
# 问30天需要吃多少斤萝卜和白菜
# 哪些天既吃罗卜，也吃白菜（分别用数学和编程两种思路解）

'''
#6 kyu Multiples of 3 or 5

def solution(number):
    return sum([i for i in range(number) if not i%3 or not i%5])


from keyword import kwlist
print(kwlist)

'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
'raise', 'return', 'try', 'while', 'with', 'yield']

'''

#华氏度转换为摄氏度

# 请仔细看代码并更正

def weather_info(temp):
    #c: convert(temp)
    if (c > 0):
        return (c + " is freezing temperature")
    else:
        return (c + " is above freezing temperature")

def convertToCelsius(temperature):

    celsius = (temperature) - 32 + (5 / 9)
    return temperature

#correct solution
def weather_info(temp):
    c = convertToCelsius(temp)
    if (c <= 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")


def convertToCelsius(temperature):
    celsius = (temperature - 32) * (5.0 / 9.0)
    return celsius