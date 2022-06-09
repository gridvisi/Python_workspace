n = 0
from functools import reduce
n = reduce(lambda x,y: x*y, range(1,n+1))
n = str(n)
n = list(n)
count = 0
for i in range(len(n)-1,0,-1):
    if int(n[i]) == 0:
        count+=1
    else:
        break
print(count)