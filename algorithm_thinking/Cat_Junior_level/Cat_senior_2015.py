
#CAT Senior 2015
#1 Disco light
'''
如果在白色和蓝色灯之间的灯，则变成（或保持）蓝色，
如果在两个白色或两个蓝色灯之间，则变成（或保持）白色。

'''
import time
import copy
start = list('BWWBWWBB')
l = len(start)
end = [''] * l
i,round = 0, 0

# 每秒 8个灯同时变换的方案
while ''.join(end) != 'WWWWWWWW':
    print(''.join(start))
    print(''.join(end[i%l:(i+3)%l:2]))
    # start[i%l]+start[(i+2)%l]
    print(i,round)
    if ''.join(start[i%l]+start[(i+2)%l]) in ['WB','BW']:
        end[(i+1) % l] = 'B'
        #time.sleep(0.5)
    elif ''.join(start[i%l]+start[(i+2)%l]) in ['BB','WW']:
        end[(i+1) % l] = 'W'
        #time.sleep(0.5)
    i += 1
    round = i//8
    if i%8 == 0:
        start = copy.copy(end)
print(end,round)

'''
继续优化编程逻辑，问题升级为：
在事先并不清楚DJ灯会稳定在全部是白灯的情况下，如何程序判断最终的状态？
'''


# 代码2：事先并不清楚DJ灯最后的状态
while end != start:
    print(''.join(start))
    print(''.join(end[i%l:(i+3)%l:2]))
    # start[i%l]+start[(i+2)%l]
    print(i,round)
    if ''.join(start[i%l]+start[(i+2)%l]) in ['WB','BW']:
        end[(i+1) % l] = 'B'
        #time.sleep(0.5)
    elif ''.join(start[i%l]+start[(i+2)%l]) in ['BB','WW']:
        end[(i+1) % l] = 'W'
        #time.sleep(0.5)
    i += 1
    round = i//8
    if i%8 == 0:
        start = copy.copy(end)
print('2th solve:',round,end)



'''

# 每秒顺序变换的方案
while ''.join(start) != 'WWWWWWWW':
    print(''.join(start))
    print(''.join(start[i%l:(i+3)%l:2]))
    # start[i%l]+start[(i+2)%l]
    print(i,cunt)
    if ''.join(start[i%l]+start[(i+2)%l]) in ['WB','BW']:
        start[(i+1) % l] = 'B'
        cunt += 1
        #i += 1
        time.sleep(0.5)
    elif ''.join(start[i%l]+start[(i+2)%l]) in ['BB','WW']:
        start[(i+1) % l] = 'W'
        cunt += 1
        #i += 1
        time.sleep(0.5)
    i += 1


'''

#CAT Senior 2015
#3 Hop skip jump
'''
##回到原题
英文种的跳有很多表达方式，哈哈

弗雷德Hop，skip，jump的总距离是15米。人们注意到，他的每一跳(hop,skip,jump的统称)都是整数。
最后，每一次jump比一次skip远，skip比hop远。有多少种可能的距离组合可以达到15米的结果？
(A) 5 (B) 9 (C) 10 (D) 11 (E) 12

'''
# Hint
# 组合与 3 种跳法的前后次序无关！！
# 3 种跳法每次的距离是整数，且不为 0
# 3 种跳法的每次距离各不相同 hop < skip < jump

'''
四个选项的值也给出暗示的约束条件有，3 
例如对应题目顺序的3 种跳法距离 1*2 + 2*5+ 3*1 = 15
那么，1,2,3 算一种组合，1，2，4； 1，2，6 又是三种


转换问题：15可以由3个不同的整数相加的组合数量
组合数与姿势顺序无关，第一跳Hop不能大于 15//3 - 1，否则不能满足hop < skip < jump
   skip 不能大于 7，否则 jump = 15 - 7 - 1 无法大于 skip
   
Hop = [1,2,3,4]
Hop的若干条的总距离有以下可能，但需要逻辑排除不可能的情况，继续缩小范围
Hop = [1,2,3,4,1*2,2*2,3*2,4*2,1*3,2*3,3*3,4*3,1*4,2*4,3*4,1*5,2*5,1*6,1*7,1*8]
容易得到hop的总距离必须 <= 12 ，skip+jump = 7，skip,jump = [2,5],[3,4]

Hop            skip      Jump         total
12(4种步幅)     2         3             4
11(1种步幅)     [2,3]     [None,None]   0
10(2种步幅)     [2]       [3]           2
 9(2种步幅)     [2]       [3]           2



skip = [2,3,4,5,6] + [4,6,8,10,12] 
skip 若干次距离之和必须 < 10,否则余下的距离15-9-1=5 满足skip<jump
推得skip跳3次时，只有一种情况就算 skip=3，有了下列可能成立：
skip = [2,3,4,5, 2*2,2*3,2*4, 2*3,3*3] 去重后是skip的总距离可能有下面情况：
skip = [2,3,4,5, 6,8, 9]

jump = [3,4,5,6,7,8,9,10,11,12]
jump的总距离不能超过12，不解释了
jump = [3,4,5,6,7,8,9,10,11,12, 3*2,4*2,5*2,6*2, 3*3,4*3] 去重后
jump = [3,4,5,6,7,8,9,10,11,12]

暴力枚举可以解决

'''

#10-11 Elfstone
'''
译文：你已经发现了传说中的精灵石的藏身之处。它们被埋在等间距的缓存中，每个缓存中有几个精灵石。
您在最左边开始收集宝石，想要得到尽可能多的精灵石。然而，你取了n个精灵的缓存，右边的下一个安全
缓存将是n个缓存之外。

例如，如果缓存是2124，并且你取了最左边的2，你也可以取其他的2或4，但不能取它旁边的1。在这种
情况下，你取左边的2和4来得到最多结果。对于下面的每一组精灵石存，
你可以安全获得的最大精灵石数量是多少？

（10）23653514 

（11）1287351114 

（12）25238273112731

'''

def maxStone(s):
    s = [int(i) for i in s]
    num, sub = 0,[]
    #for i in range(len(s)):
    for i,e in enumerate(s):
        num = 0
        j = i
        #num += j
        while j < len(s):
            #print(j)
            num += s[j]
            j += s[j]
        sub.append(num)
    return sub
s = '1287351114'
roadmap = ['23653514','1287351114',"25238273112731"]
#10  12 16
#print('answer:',[max(maxStone(n)) for n in roadmap])

print([max(maxStone(n)) for n in roadmap])

# above solve it by recursion
# for s in roadmap:

def maxStone(s):
    s = [int(i) for i in s]
    num, sub = 0,[]

    for i,e in enumerate(s):
        num = 0
        j = i

        while j < len(s):
            num += s[j]
            j += s[j]
        sub.append(num)
    return sub
s = '1287351114'
roadmap = ['23653514','1287351114',"25238273112731"]

s = [int(i) for i in s]
n = len(s)
#print([0]*(n-1).extend(s[n-1]))
sub = [0 if i != len(s)-1 else s[-1] for i,e in enumerate(s)]
sub = [0] * (len(s)-1)
sub[-1] = s[-1]
print(sub)
# f(n) = s[n-1]
# f(n-1) = f(n) + s[n-2] if s[n-2]+n-2 < n-1 else max(s[n-2],f(n))

def recur(s):
    s = [int(i) for i in s]
    n = len(s)
    sub = [0] * len(s)
    sub[-1] = s[-1]
    ans = 0
    for i in range(n-2,-1,-1):
        p = s[i]+i
        if p < n:
            sub[i] = s[i] + sub[p]
        else:
            sub[i] = max(s[i],sub[i+1])
    return sub
s = '1287351114'
s = "25238273112731"
#s = '23653514'
print(recur(s))


# 修改 if 条件判断
def recur(s):
    s = [int(i) for i in s]
    n = len(s)
    sub = [0] * len(s)
    sub[-1] = s[-1]
    ans = 0
    for i in range(n-2,-1,-1):
        p = s[i]+i
        if p < n:
            sub[i] = s[i] + max(sub[p:])
        else:
            sub[i] = max(s[i],sub[i+1])
    return sub
s = '1287351114'
s = "25238273112731"
#s = '23653514'
print([max(recur(s)) for s in roadmap])