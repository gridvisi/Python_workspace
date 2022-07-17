
dna = "T T T T T G G G A C C C C C C G A A"
# 原字符串含有空格，需处理

def dnaCunt(dna):
    dna = "".join(dna.split(" ")) + '0'
    s,cnt = '',1
    for i in range(len(dna)-1):

        if dna[i] == dna[i+1]:
            cnt += 1
        else:
            s += f"{dna[i]}{cnt}"
            cnt = 1
    return s
print(dnaCunt(dna))

#再修改输出，得到字符串长度的变化

def dnaCunt(dna):
    dna = "".join(dna.split(" ")) + '0'
    # 原字符串含有空格，需去掉空格
    # for循环截止在A会漏掉末尾的两个A，增加一个’0‘

    s,cnt = '',1
    for i in range(len(dna)-1):

        if dna[i] == dna[i+1]:
            cnt += 1
        else:
            s += f"{dna[i]}{cnt}"
            cnt = 1
    return len(dna) - len(s) - 1
print(dnaCunt(dna))


# Not correct!
from collections import Counter
def dnaCount(dna):
    dnaCunt = Counter("".join(dna.split(" ")))
    dnalen = ''.join([str(k)+str(v) for k,v in dnaCunt.items()])
    return len("".join(dna.split(" "))) , len(dnalen),dnalen
print(dnaCount(dna))

# i,j 双指针
def dnaCount(dna):
    i,j,s,cnt = 0,1,"",0
    dna = "".join(dna.split(" "))
    while j <= len(dna):
        try:
            if dna[i] == dna[j]:
                j += 1
            else:
                s += f"{j-i}{dna[i]}"
                i = j
                j += 1
        except:
            #print(s,i,j)
            print(dna[i:j])
            s += f"{j-i}{dna[-1]}"
            break
    return len(dna) - len(s)
print(dnaCount(dna))

# queue

import queue
def dnaCunt(dna):
    cnt, s = 0, ""
    dna = "".join(dna.split(" "))
    it = iter(dna)

    while len(dna):

        try:
            pivot = next(it)
            print(pivot)
            if pivot == next(it):
                cnt += 1

            else:
                s += f"{cnt}{pivot}"
        except:
            print(s)
            break
    return s
print (dnaCunt(dna))


'''
# CAT 18 5th problem
流程图
'''
def func(a):
    b = 0
    while a > 10:
        a -= 10
        b += 1
    b += a
    return b
inp = [23, 47, 119, 123456]
ans = len([func(i) for i in inp if not func(i)%2])
ans = [func(i) for i in inp]
print(ans)


#6 三向 移动
import turtle as t

# 增加 4 步 1点钟方向走3步，5点钟方向走1步，
steps = [60,60,60,-60]
angles = [-60,-60,180,60,180,180,-60,180,
          60,180,60,180,180,-60,-60,-60,60,
          180,60,60,180,-60,-60]

mid = len(angles)
angles.extend(steps)
print(angles)

t.dot(10,'red')
for i,e in enumerate(angles):
    if i == mid:
        t.dot(17,'purple')
    t.speed(2)
    t.left(e)
    t.forward(80)
    t.left(-e)
t.dot(10,'blue')
t.done()


# left 为正，那么 left(-60)即为右拐 60 度
angles = [-60,-60,180,60,180,180,-60,180,
          60,180,60,180,180,-60,-60,-60,60,
          180,60,60,180,-60,-60]
t.dot(10,'red')
for i in angles:
    t.speed(2)
    t.left(i)
    t.forward(80)
    t.left(-i)
t.dot(10,'blue')
t.done()

# https://brilliant.org/daily-problems/circle-fill-18/
'''
x + y = z
z * z = x
z * z = y

so that
x = y

z**2 + z**2 = z
z**2 = z/2
z = 1/2

product = z * z**2 * z**2 * z = z**6 = 1/64
'''
