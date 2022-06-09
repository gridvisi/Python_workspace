__author__ = 'Administrator'
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if 122*a + 212*b + 221*c == 1223:
                print(a,b,c)

#https://brilliant.org/weekly-problems/2018-12-17/basic/?p=2
for x in range(1,9):
    for y in range(0,9):
        if (x*10 + 3) * (30 + y) > 300 and (x*10 + 3) * (30 + y) < 400:
            print(x,y,(x*10 + 3) * (30 + y))


print(int("11111111",2))
print(int("1111",2))

for X in range(0,9):
    for Y in range(0,9):
        for Z in range(0,9):
            if X + Y + Z == 12:
                if X*X + Y*Y + Z*Z == 12:
                    if X**3 + Y**3 + Y**3 == 12:
                        print(X,Y,Z)

'''
a = 1
b = 1
n = int(input("输入阶乘数："))
c = 1

for i in range(1,2*n):
    a = a * i

for j in range(1,2*n,2):
    b = b * j
    #c = c*2

rate = (c*b)/a
print(a,b,c,c*b,rate)

import math
x = int(input('144...:'))
n = int(input('digit num:'))
for i in range(1,n):
    x = x * 10 + 4
    print(x)
    if math.sqrt(x) == int(math.sqrt(x)):
        print(math.sqrt(x),x)
'''
import math
m = 4
if math.sqrt(m)- int(math.sqrt(m)) == 0:
    print('good:',math.sqrt(m)- int(math.sqrt(m)))

if isinstance(math.sqrt(m),int):
    print("int",math.sqrt(m))
else:
    print("float",(math.sqrt(m)))


for i in range(1,50):
    for j in range(1,50):

        for time in range(10):
            set = []
            if math.sqrt(i * time)- int(math.sqrt(i * time)) == 0 and math.sqrt(j * time)- int(math.sqrt(j * time)) == 0:
            #print('i=',i)
            #print('tag:',int(math.sqrt(i * time)))
                set.append(i)
                set.append(j)
                print ('time:',time,'i:',i,'j:',j,'sqrt:',math.sqrt(j * time),math.sqrt(i * time))

    #print(set)