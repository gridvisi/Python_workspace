__author__ = 'Administrator'
import math
R = math.sqrt(36+77**2/6**2)
print(R)

import math
for i in range (100):
    temp = math.sqrt((i**3) + ((i+1)**3) + ((i+2)**3))
    #print(temp)

    if temp - int(temp) == 0:
        print('result:',int(temp))
