
ls,k = [1,2,3,7,9],9
#ls,k = [1,2,3,5,6,7],10  #([8, 8, 10, 12, 12, 14], [14, 8, 8, 10, 12, 12])
ls,k = [1,4,5,7,9,9],9

import time
import random

def dual(ls,k):
    st,step,i = sorted(ls),0,0

    for i in range(len(ls)-1):
        while st[i] <= st[i+1]:
            st[i] = 2*st[i]
            step+=1
            print(step,st)
        if step < k:return dual(st,k-step)
        else:return sorted(st),st
st = time.time()
print(dual(ls,k))
end = time.time()
print(end - st)

