'''
https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/python
i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array

Test.assert_equals(parse("ooo"), [0,0,0])
Test.assert_equals(parse("ioioio"), [1,2,3])
Test.assert_equals(parse("idoiido"), [0,1])
Test.assert_equals(parse("isoisoiso"), [1,4,25])
Test.assert_equals(parse("codewars"), [0])

'''
#parse("iiisdoso")  ==>  [8, 64]
data = "iiisdoso"
from collections import deque
def parse(data):
    re,res = 0,[]
    cal_queue = deque()
    cal_queue += data
    print(cal_queue)
    while cal_queue:
        op = cal_queue.popleft()
        if op == 'i':
            re += 1
        if op == 'd':
            re -= 1
        if op == 's':
            re *= re
        if op == 'o':
            res.append(re)
    return res
print(parse(data))

# no.1
def parse(data):
    value = 0
    res=[]
    for c in data:
        if c=="i": value+=1
        elif c=="d": value-=1
        elif c=="s": value*=value
        elif c=="o": res.append(value)
    return res

def parse(data):
    v, r = 0, []
    for c in data:
        v, r = v + {'i': 1, 'd': -1, 's': v * (v - 1)}.get(c, 0), r + [v] * (c == 'o')
    return r

