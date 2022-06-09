#10m * 5m 80cm  0.8
# 1000 * 500 / 80*80 =

print(1000 * 500 / (80*80)) #79 pcs #教条主义
#
print(10* 100 / 80) #12.5 --> 13
print(5 * 100 / 80) #6.25 --> 7
print(13 * 7)


import math
x = math.pi
print('取整',int(x),math.ceil(x),math.floor(x),round(x,5))

def TileCal(l,w,s):
    return math.ceil(l/s) * math.ceil(w/s)

l,w,s = 1000,500,80 #正方形
print(TileCal(l,w,s))