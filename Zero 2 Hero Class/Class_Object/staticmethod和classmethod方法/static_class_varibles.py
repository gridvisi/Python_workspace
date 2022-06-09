#https://stackoverflow.com/questions/68645/are-static-class-variables-possible-in-python

# -*- coding: utf-8 -*-
class Worker:
    id = 1

    def __init__(self):
        self.name = ''
        self.document = ''
        self.id = Worker.id
        Worker.id += 1  #id = 1 class

    def __str__(self):
        return f"{self.id}, {self.name}, {self.document}"
        #u"{}.- {} {}".format(self.id, self.name, self.document).encode('utf8')


class Workers:
    def __init__(self):
        self.list = []

    def add(self, name, doc):
        worker = Worker()
        worker.name = name
        worker.document = doc
        self.list.append(worker)


if __name__ == "__main__":
    workers = Workers()
    for item in (('Fiona', '0009898'), ('Maria', '66328191'), ("Sandra", '2342184'), ('Elvira', '425872')):
        workers.add(item[0], item[1])
    for worker in workers.list:
        print(worker)
    print("next id: %i" % Worker.id)


#break math
# https://brilliant.org/daily-problems/quarter-off/

import math
R_circle = 0.5 * math.pi * (15**2 + 8**2)/4
r_circle = 0.25 * math.pi * (8**2)
s_total = 15*8 * 0.5 + R_circle - r_circle
print(s_total)


#https://brilliant.org/daily-problems/dont-roll-1-2/

#每个点数的概率是均等的，这样以来第1轮贷款总额大概率落在：
# 出现1或2点的概率是 1/3，金额是10000*(1/6)+20000*(1/6) = 5000，5000*1/3
# 其他3，4，5，6的概率是 2/3
# 30000*(1/6)，40000*(1/6)，50000*(1/6)，60000*(1/6) = 30000，30000*2/3

# 10000*(1/6)，20000*(1/6) ... ... 60000*(1/6)

rmb = 10000
doll = [i for i in range(1,7)]
reward = sum([i*(1/6)*rmb for i in doll])
print(reward)

#第2轮、第3轮 ......后，贷款总额落在未知数设为X
#经过n轮色子连续落在3，4，5，6之间，直到n+1轮出现1或2
#思考经过很多轮后，将无限趋近X，最后1轮与倒数第2轮的X值趋同
#那么将第1到第n轮的金额相加为x，最后一轮即第n+1轮为X, so that:
# X = (X+30000)*2/3 + 5000*1/3
# X =
#

#
start = 30000
rate = 2/3
start = 30000*rate
rate_ls = []
for i in range(100):
    start += start * rate
    rate_ls.append(rate)
    rate = rate*(2/3)
    if rate < 0.017:
        print(f"{i} round:",start)
        break
print(rate_ls)

print((2/3)**5)

import random
dice = list(range(1,7))
m = 1000
def loan(m):
    d = 7
    total = []
    while d > 2:
        d = random.choice(dice)
        total.append(d*m)
        #if d <= 2:
    return sum(total)/len(total) #total_s,total_b

def loan_all(m):
    d = 7
    total = []
    d = random.choice(dice)
    total.append(d*m)
    return sum(total)/len(total) #total_s,total_b

averg = 0
sub,sub_All = [],[]
for _ in range(10000):
    sub.append(loan(m))
    sub_All.append(loan_all(m))
averg = sum(sub)//len(sub)
averg_all = sum(sub_All)//len(sub_All)
print(averg,averg_all)







'''



At each stage of the game, one of these two happens:

You roll a 11 or a 2,2, which happens with a probability of \frac{1}{3}. 
3
1
​
 .
You roll one of the remaining numbers, which happens with a probability of \frac{2}{3}. 
3
2
​
 .
In the first case, the expected win of the roll is (1+2)/2 = \frac{3}{2}(1+2)/2= 
2
3
​
  dollars.

In the second case, the expected win of the roll is (3+4+5+6)/4 = \frac{9}{2}(3+4+5+6)/4= 
2
9
​
  dollars, and the game starts afresh with that money in your pocket.

Let dd denote the total expected win in dollars, then we can summarize these two cases in one equation:

d=\frac{1}{3} \times \frac{3}{2}+\frac{2}{3} \times \left(\frac{9}{2}+d\right).
d= 
3
1
​
 × 
2
3
​
 + 
3
2
​
 ×( 
2
9
​
 +d).

From this equation, we learn that d=10.5.d=10.5.
'''

