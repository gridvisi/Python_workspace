'''
https://www.codewars.com/kata/6167e70fc9bd9b00565ffa4e/train/python
'''

def barista(coffees):
    prev,subtotal = 0,0
    for t in sorted(coffees):
        prev += t
        subtotal += prev
        prev += 2
    return subtotal


#4
def barista(coffees):
    coffees = list(sorted(coffees))
    curr, total = 0, 0
    for t in coffees:
        curr += t + (2 if curr else 0)
        total += curr
    return total

#电阻d

def Parallel(x, y, counter, a, b):
    # global cache
    global cache
    if counter >= 1:
        cache = x * y / (x + y)
        # 并联电阻公式1/(1/x + 1/y)
        x = cache + a
        y = cache + b
        counter -= 1
        #print('counter', counter, ':', x, y, cache)
        return Parallel(x, y, counter, a, b), cache
        #递归调用函数本身

x = int(input("电阻X的值："))
y = int(input("电阻Y的值："))
a = x
b = y
counter = int(input("串联级数："))
Parallel(x, y, counter, a, b)
print("R=", cache)


# 递归的简化写法

def Parallel(x, y, layer,a,b):

    if layer > 0:
        #layer -= 1
        return Parallel(x*y/(x+y)+a, x*y/(x+y)+b,layer-1,a,b)
        #递归调用函数本身
    return x,y,x*y/(x+y)

#layer 串联级数
x,y,layer = 1,2,990
a,b = x,y
print('递归简化：',Parallel(x,y,layer,a,b))

#递推的思路

def Parallel(x,y,layer):
    a,b = x,y
    for i in range(layer):
        x,y = x*y/(x+y)+a,x*y/(x+y)+b
        #print(f"layer:{i}",x,y)
    return (x*y)/(x+y)
x,y,layer = 1,2,1000
print('递推：',Parallel(x,y,layer))

'''
继续新的挑战是观察下图，计算绿色部分的面积。数学思路求解无限趋近0，求和是非常容易的：
假设 S = 1/3 + 1/9 + 1/27 .... .. 1/3**n  ，n->无穷大

3*S = S + 1,  推导可得​：S = 1/2

​现在n并不是无穷大，而是有限的正整数，该如何实现？
'''

def area(s,n): #n是缩小的倍数
    areaSum = 0
    for i in range(n):

        areaSum += s * (1/3)**i
    return areaSum
s,n = 1/3,10
print(area(s,n))