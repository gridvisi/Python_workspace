'''
https://brilliant.org/daily-problems/cryptogram-4a3b2c1d/


'''

import itertools
for (a,b,c,d) in itertools.permutations(range(10), 4):
    if a*1111 - b*111 + c*11 - d == 8765 and a*b*c != 0:
         print(a,b,c,d, sum((a,b,c,d)))

#2nd

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
           for l in range(10):
                a=i*1000+i*100+i*10+i
                b=j*100+j*10+j
                c=k*10+k
                if a-b+c-l==8765:
                    print(i,j,k,l,i+j+k+l)

#Output:8 2 9 0 19