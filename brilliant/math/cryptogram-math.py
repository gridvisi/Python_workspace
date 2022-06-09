'''
https://brilliant.org/daily-problems/cryptogram-math/
'''
from itertools import permutations
for m,a,t,h in permutations([i for i in range(10)],4):
    #print(m, a, t, h)
    if m != 0 and (m+a+t+h)**4 == m*1000+a*100+t*10+h:
        print(m,a,t,h)
        print(m+a+t+h)

from itertools import combinations  #permutations
for m,a,t,h in combinations([i for i in range(10)],4):
    #print(m, a, t, h)
    if m != 0 and (m+a+t+h)**4 == m*1000+a*100+t*10+h:
        #print(m,a,t,h)
        print(m+a+t+h)

# Math solution
import math
lowest = math.pow(1023,1/4)
highest = math.pow(9876,1/4)
print(lowest,highest)
'''
5.6 < m+a+t+h < 9.9 
if m+a+t+h == 6: 
so that: h == 6  m+a+t == 0

if m+a+t+h == 7:
    7^4 == 49^2 = (50 - 1)**2 = 
for math in range(6,10):
    if math**4 == m*1000+a*100+t*10+h:

'''