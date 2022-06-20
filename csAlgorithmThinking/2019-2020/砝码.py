__author__ = 'Administrator'
'''
 用质量为1g,3g,9g,27g和81g的砝码称物体的质量,最大可称121g.如果砝码允许放在天平的两边,编程输出称不同物体时砝码应该怎样安排?
 例如m=14时,m+9+3+1=27或m=27-9-3-1.即天平一端放m=14克的物体和9g,3g,1g的砝码,另一端放27g的砝码.
'''
'''
def fun(m, n):
    a = []
    while n > 1:
        k = 2 * sum(a) + 1
        a.append(k)
        n -= 1

    k = m - sum(a)
    if k - 2 * sum(a) < 2:
        a.append(k)
        return a

    return None

print (fun(40, 4))

fun(40, 4)
print(fun(121, 5))

'''

class fama:
    #def _init_(self,m,a,b,c,d,e):
    def __init__(self,total,a,i):
        self.total=total
        self.a=a
        self.i=i

        #return i*81+i*27+i*9+i*3+i*1

#w=fama(121,5,1)
#print (w.total)

def func(j):
    #for i in range(-1,2):
    #print(i)
    #if j=0: return 1
    #else:
    k=0
    while k < j or k == j:
        if j == 0:
            return -1,0,1
        else:

            n=3**j
            k+=1
            return n*(-1),0,n*1
j=0
while j < 5:
    w = func(j)
    j +=1
    print(w)

    #w=fama(121,5,i)
    #m=w.i*81+w.i*27+w.i*9+w.i*3+w.i*1
    # m=i*81+i*27+i*9+i*3+i*1
    #n=n.append(m)
    #print(m)

'''
for m in range(1,121):
    for a in range (-1,2):
        for b in range (-1,2):
            for c in range (-1,2):
                for d in range (-1,2):
                    for e in range (-1,2):
                        m=a*81+b*27+c*9+d*3+e*1
                        #print(m)
                        print(m,"=",a*81,"+",b*27,"+",c*9,"+",d*3,"+",e);
'''

