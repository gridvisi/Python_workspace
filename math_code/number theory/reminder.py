__author__ = 'Administrator'


'''
P=[2]
for i in range(1,30):
    p = 2*i
    #p += p
    P.append(p)
    print('第',i+1,'刀,共计可以切出:',sum(P),'块')

'''

import math
def isSqr(n):
    a = int((math.sqrt(n)))
    return a * a == n
i = 0
while isSqr(20170000 + i) == False:
    i += 1
print(20170000+i,math.sqrt(20170000+i))

'''
for i in range(100):
    if isSqr(201700+i) == True:
        print(201700+i)
'''