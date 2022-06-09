import math
s1,s2 = 150,96

side_range = [i for i in range(150)]
side1,side2 = [],[]

def slantededge(x,y):# 定义直角三角形知道直边求斜边的函数
    return math.sqrt(x*x + y*y)

for x in side_range:
    for y in side_range:
        if (x*y)/2 == s1 and slantededge(x,y).is_integer():
            side1.append([x, y])
        #print(side2)
        if (x*y)/2 == s2 and slantededge(x,y).is_integer():
            side2.append([x, y])
print(side1,'end\n',side2)

for s1 in side1:
    for s2 in side2:
        if s1[0] < s2[0] and s1[1] > s2[1]:
            print(s1,s2,s1[1]-s2[1])





'''
side_range = [i for i in range(150)]
print(list(zip(side_range,side_range)))
triangle1 = [(x,y) for x,y in zip(side_range,side_range) if int((x*y)/2) == s1]
triangle2 = [(x,y) for x,y in zip(side_range,side_range) if int((x*y)/2) == s2]
print(triangle1,triangle2)
'''



