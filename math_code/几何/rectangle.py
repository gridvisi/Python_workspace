__author__ = 'Administrator'

counter = 0
for x in range(1,100):
    for y in range(1,100):
        for z in range(1000):
            if x**2 + y**2 == z**2:
                if x<y:
                    if (x*y)%10 == 0 or (x*y)%10 == 5:
                        counter +=1
                        print('第',counter,'行:',x,y,z)



'''
for x in range(100):
    for y in range(100):
        for z in range(100):
            p = (x + y + z)/2
            if 4*(x + y + z) == (p - x)*(p - y)*(p - z):
                print(x,y,z,2*p)
'''

