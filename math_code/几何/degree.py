__author__ = 'Administrator'
# A1(15,-15*√3)
# Be carefull! sin(40 degree) is not sin 40,actually 40 degree is 2*pi/9
import math

print((1-0.36)*5*9.8)
print('sin 37:',math.sin((37/180)*math.pi),math.cos((37/180)*math.pi),math.sin((37/180)*math.pi)*math.sin((37/180)*math.pi))
print(math.sin(40),math.cos(40))
print(math.sin(2*math.pi/9),math.cos(2*math.pi/9))
xc = 30*math.cos(2*math.pi/9)
yc = 30*math.sin(2*math.pi/9)

xb = 30
yb = 0

xA1 = 15
yA1 = -15*math.sqrt(3)
print(xc,yc,xA1,yA1)
print(-xc-xA1)
print(yc-yA1)
temp = (xc-xA1)**2 + (yc-yA1)**2
print((-xc-xA1)**2 ,(yc-yA1)**2)
CA1_lenth = math.sqrt(temp)
print(CA1_lenth)


# m = 2r*sin(0.5*pi/11)*(for i in range (1-5))
abc=[]
for i in range (1,6):
    m = 2*math.sin(i*0.5*math.pi/11)
    #m *= m
    abc.append(m)
print(abc)
i = 0
if i == 0:
    temp = abc[i]*abc[i+1]*abc[i+2]*abc[i+3]*abc[i+4]
print(temp*temp)

print(math.sqrt(temp))