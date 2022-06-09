
def mul(a,b):
    return a * b
a,b = 3,5
print(mul(a,b))

level = 1
ddm = 8

while level < ddm:
    level += 1
print('level:',level)



'''
The chocolate shopkeeper has an excellent recycling policy:
巧克力店老板推出了一个巧克力包装的回收政策 ：
1、I gives you 1 chocolate per every RMB you give him.
你每给我一元，我就给你一块巧克力。

2、He gives you 1 chocolate per every 3 wrappers you give him.
你每给我3个包装纸，我就送你1块巧克力。
'''

rmb = 10   #总共有多少钱  每块糖的价格变成3元
wrappers = 0  #糖纸
eaten = 0     #吃糖
while rmb > 2:
    rmb -= 3
    eaten += 1
    wrappers += 1
    if wrappers == 3:
        wrappers -= 3
        eaten += 1
        wrappers += 1
print("Answer:", eaten) #   Answer: 88573




rmb = 10000     #总共有多少钱  每块糖的价格变成3元
wrappers = 0  #糖纸
eaten = 0     #吃糖
for i in range(rmb,0,-3):
    #rmb -= 1
    eaten += 1
    wrappers += 1
    if wrappers == 3:
        wrappers -= 3
        eaten += 1
        wrappers += 1
#print("for loop Answer:", eaten)




end = 12
start = round(3 + 1/3,2)
print(start)

step = 0
while start + step < end:
    step += 1
print(step)

res = [i for i in range(int(start),end,1)]
print(res,len(res))

fabnacci_lst = [1,1,2,3,5,8,13]

f1,f2 = 1,1

f3 = f1 + f2
f4 = f3 + f2

def fabnacci(n):
    cn = 0
    a, b = 1, 1  #[1,1,2,3,5,8,13]
    fab = []
    while cn < n:
        a,b = b,a+b
        fab.append(a)
        cn += 1
    return fab
n = 17

fib = lambda n: n if n <= 1 else fib(n-1)+fib(n-2)
print(fib(n))
print(fabnacci(n))