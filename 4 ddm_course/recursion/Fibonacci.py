__author__ = 'Administrator'
def Fibonacci_Yield_tool(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


def Fibonacci_Yield(n):
    # return [f for i, f in enumerate(Fibonacci_Yield_tool(n))]
    return list(Fibonacci_Yield_tool(n))
print(Fibonacci_Yield(100))

# no recrusion
from time import clock
x = int ( input ("输入一个数：") )
clock()
arr = [ 0, 1, 1 ]
for i in range(0 , x ):
	print ( str(arr[i%3])+"   " )
	arr[i%3]=arr[(i+1)%3] + arr[(i+2)%3]
print("running time is %-5.5ss" %clock())
