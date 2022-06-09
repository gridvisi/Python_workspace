'''
https://www.codewars.com/kata/55e2adece53b4cdcb900006c/train/python

race(720, 850, 70) => [0, 32, 18] or "0 32 18"
race(80, 91, 37)   => [3, 21, 49] or "3 21 49"
'''

def race(v1, v2, g):
    if v2 - v1 < 0:return None
    sec = g/(v2-v1)*3600
    h = sec//3600
    m = (sec - h*3600) // 60
    s = sec - m*60 - h*3600
    return list(map(int,[h,m,s]))
v1, v2, g = 80, 91, 37
v1, v2, g = 10, 20, 101
print(race(v1, v2, g))


def race(v1, v2, g):
    if v2 - v1 < 0:return None
    #sec = g/(v2-v1)*3600
    h = g/(v2 - v1)
    m = (h - int(h))*60
    s = (m - int(m))*60
    return list(map(int,[h,m,s]))  #,[h,m,s]
v1, v2, g = 80, 91, 37
v1, v2, g = 10, 20, 101
print(race(v1, v2, g))


#1
def race(v1, v2, g):
    if v1>v2: return None
    res = g*3600/(v2-v1)
    return [res/3600,res%3600/60,res%60]