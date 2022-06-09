'''
https://brilliant.org/daily-problems/conservation-energy-1/


'''
import math
print(math.log(2,2),math.log(4,2))


h = hight = 2

bounce = 5
v = [0] * (bounce+1)
v[0] = 10
g = 10
print(v)


def percent(h0,bounce,v0,ht,g=10):
    # h0 = ht = 2m,
    # v0 = 10m/s Equivalent to g*t=10,so that t=1s
    # 在 0.5*g*t**2 = 5m 高处零速度放手 h = 5+2 = 7
    # h = 0.5 * g * t^2, t = 1
    h = (0.5 * (v0 ** 2) + g * h0)/g # Why is 6 instead of 7 ?
    print('折算为等效高度:',h)
    arr_h = [h0] + [0] * (bounce - 1) + [ht]
    # 5 bounce,h = 2
    #ht = h0 * rate**bounce  #
    rate = math.pow(ht/h,1/bounce)
    return round(rate,2),h
h,bounce,v0,ht = 2,5,10,2
print('每次损失率：',percent(h,bounce,v0,ht,g=10))


rate,h0 = percent(h,bounce,v0,ht,g=10)
print(rate,h0)
for i in range(bounce):
    h0 *= rate
    print(h0)



def percent(h0,bounce,v0,ht,g=30.71):
     # h0 = ht = 2m,
     # v0 = 10m/s Equivalent to drop the ball from 7m hight
     # above prove : g*t=10,so that t = 1s
     # h = 0.5 * g * t^2  (t = 1)

     h = (0.5 * (v0 ** 2) + g * h0)/g 

     # ht = h0 * rate**bounce
     # rate = math.pow(ht/h,1/bounce)
     return round(rate,2)
print('mars:',percent(h0,bounce,v0,ht,g=3.71))