__author__ = 'Administrator'
'''
Marie shops at a store where all prices end in 99 cents 
($0.99, $1.99, $2.99, etc.). 
She ends up spending $33.89.
How many items did she purchase?
'''

#from rich.progress
#import track
#import time
# N<0 F(N) =1 ,IF N>=0 then F(n)=1-F(N-1)*F(N-3)*F(N-4)

from time import clock

clock()

def f(x,load):
    if x < 0:
        return 1
    else:
        arr = [ 0, 1, 0, 1, 0 ]
        for i in range(x):
            print ('f(',i,'):', str(arr[i%5])+"   " )
            load += arr[i%5]
            arr[(i)%5]=1-arr[(i-1)%5] * arr[(i-3)%5] * arr[(i-4)%5]
        print(load)

x = int(input("please input number:"))
load = 0
f(x,load)

'''
def f(n):
    a,b,c,d,e = 0,1,0,1,0
    while n < 0:
        yield 1

    a, b = b, a + b
        n -= 1


def Fibonacci_Yield(n):
    # return [f for i, f in enumerate(Fibonacci_Yield_tool(n))]
    return list(Fibonacci_Yield_tool(n))
'''

'''
def f(x):
    if x < 0:
        return 1
    if x >= 0:
        return 1-f(x-1)*f(x-3)*f(x-4)
print(f(40))

total = 0
for i in range(2018):
    total += f(i)
print(total)
'''