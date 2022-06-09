__author__ = 'Administrator'
'''
round() 遵循四舍五入把原值转化为指定小数位数，如：round(1.45,0) = 1;round(1.55,0)=2
floor()向下舍入为指定小数位数 如：floor(1.45,0)= 1;floor(1.55,0) = 1
ceiling()向上舍入为指定小数位数 如：ceiling(1.45,0) = 2;ceiling(1.55,0)=2
'''
counter = 0
for i in range(1,360):

    if int(360/i) == 360/i:
        counter += 1
        print(counter,i)

for i in range(1,360):

    if int(360/i) == 360/i:
        counter += 1
        print(counter,i)


def isdigit(x):
    str1 = str(x)
    #print(str1)
    distance = len(str1)
    #print(distance )
    perfect = []

    for i in range(distance):
        #print(i)
        perfect.append((int(str1[i])))
    #print(perfect)
    if perfect.count('False') == 0:
        return sum(perfect)
    return False

a = 1
n = 2017
for i in range(1,n+1):
    a = a * i
    x = isdigit(a)
print('digit total = ',isdigit(x),n,'!','=',a)