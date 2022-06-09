__author__ = 'Administrator'

#f(n) = f(n-1) + 2n-1

def split(n):
    if n == 2:
        return 3
    return split(n-1)+2*n-1
print(split(8))

def split_old(n,m,counter,i):
    N = n
    M = m
    if n>1 and m > 1:
        i += 4
        n = n/2
        counter += 1
        m = m/2
        counter += 1
        counter = counter*(M*N)/(m*n)
        print(counter/4,int(m),int(n),i)
        return split (n,m,counter,i)
split(8,8,0,0)
