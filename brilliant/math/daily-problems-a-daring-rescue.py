# https://brilliant.org/daily-problems/a-daring-rescue/

import math

def min_t(h):
    t1 = math.sqrt(10**2 + h**2)
    t2 = (5 * math.sqrt(21*h**2 + 100)) / (4*h*math.sqrt(10))
    return t1 + t2

for h in range(1,10):
    print(h,min_t(h))


# solution

v = 4.0
d = 10.0
dh = 0.01
h = 2.0

################################################

tmin = 9999999999.0
h_store = 0.0

while h <= 10.0:
    theta = math.pi/6.0
    for j in range(0,100):
        y = h*math.cos(theta) + d*math.sin(theta) - d
        yp = -h*math.sin(theta) + d*math.cos(theta)
        theta = theta - y/yp

    res = math.fabs(h*math.cos(theta) + d*math.sin(theta) - d)
    if res < 10.0**(-4.0):
        D = math.hypot(d,h)
        t1 = D/v
        t2 = d/(v*math.cos(theta))
        t = t1 + t2

        if t < tmin:
            tmin = t
            h_store = h

    h = h + dh

print('################################################')

print(tmin)
print(h_store)

#>>>
#5.71135731462
#6.85
#>>>