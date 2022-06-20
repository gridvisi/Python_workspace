
x = 'lizhenjie'
print(x[8])

#print(s[::-1])
sl = 'edcba'
s = 'abcde'
def recursion(s):
    ans = ""
    for i in range(len(s)-1,-1,-1):
       ans += s[i]
    return ans
print(recursion(s))
'''

回文的几种写法

输入："爸爸的爸爸是爷爷"

输出："爷爷是爸爸的爸爸"

两种写法
第一种递归：简洁易懂

'''
def revers_self(sl):

    if len(sl[1:]) == 0:return sl

    else:return revers_self(sl[1:])+sl[0]

sl = 'I love python'
sl = "爸爸的爸爸是爷爷"
print(revers_self(sl))

# 第二种：循环
inp = "爸爸的爸爸是爷爷"
out = "爷爷是爸爸的爸爸"

rev = []

for i in range(len(inp)-1,0,-1):

    #why len(inp)-1 intead of len(inp)

    rev.append(inp[i])
print(''.join(rev))


# 第三种：地址下标切片
inp = "爸爸的爸爸是爷爷"
out = "爷爷是爸爸的爸爸"
print(inp[::-1])


# 第四种：reverse函数
inp = "爸爸的爸爸是爷爷"
out = "爷爷是爸爸的爸爸"
print(''.join(reversed(inp)))

'''

10-12. 机器人图书管理员
学校购置了一个机器人来帮助图书管理员。它可以对书架上的书进行分类，但
它可以对书架上的书进行分类，但只能将书拿出来放在书架的两端。
例如，如果书架上的书ABC是按BAC的顺序排列的，那么可以通过把A移到前面来进行分类。
把A移到前面。如果书架上的书是按CBA的顺序排列的，那么就可以通过以下方式进行分类
将C移到最后，然后将A移到前面，（或将A移到前面，然后将C
到最后）。
以下列表中的每一个都代表一个书架。对于每一个书架，机器人必须移动的最小数量是什么？
机器人必须移动多少本书才能把书按字母顺序分类？
10. FCABDE
11. DECAFBGH -> CDEAFBGH -> BCDEAFGH -> ABCDEFGH  3
12. DFAECIGBJH  -> DFACIGBJH E -> DACIGBJH EF -> C DAIGBJH EF-> BC DAIGJH EF-> ABC DIGJH EF
-> ABC DI JH EFG-> ABC DI J EFGH-> ABC D J EFGHI -> ABC D EFGHIJ

#CDFAEIGBJH -> BCDFAEGJHI -> ABCDFEGJHI -> ABCDEIGJHGF -> ABCDE

'''

'FCABDE BFCADE ABFCDE ABCDEF -> 3'
start = 'FCABDE'

#start = 'ABCD'
def swapcase(start,swap = {},cunt = 0):
    t = 0
    if start == sorted(start):
        return cunt,swap
    else:
        for i,c in enumerate(s):
            if c == min(s[i:]):
                #print('c = ',c,t,i)
                s[t],s[i] = s[i], s[t]  # 不能用 c ！！1
                #print('s = ',s)
                if s[t] != s[i]:
                    swap[cunt] = f"{s[t]} <-> {s[i]}"
                    cunt += 1
                t += 1

        return swapcase(s,swap,cunt)
start = 'FCABDE'
start = 'FCADBE'
start = 'ECADBF'
#start = 'DFAECIGBJH'
s = [ord(i) for i in start]
#print('swap:',swapcase(s))


print(" %%%%%%%%%%%%%%%%%%%%%%% \n")
def swapcaseUp(start,swap = {},cunt = 0):
    t = 0
    if start == sorted(start):
        return cunt,swap
    else:
        s = [x for x,y in zip(start,sorted(start)) if x != y]
        print([chr(i) for i in s])
        for i,c in enumerate(s):
            if c == min(s[i:]):
                #print('c = ',c,t,i)
                s[t],s[i] = s[i], s[t]  # 不能用 c ！！1
                #print('s = ',s)
                if s[t] != s[i]:
                    swap[cunt] = f"{chr(s[t])} <-> {chr(s[i])}"
                    cunt += 1
                t += 1

        return swapcaseUp(s,swap,cunt)
start = 'FCABDE'
s = [ord(i) for i in start]
#print('swapup:',swapcaseUp(s))

start = 'FCADBE'
s = [ord(i) for i in start]
#print('swap-up:',swapcaseUp(s))

start = 'ECADBF'
s = [ord(i) for i in start]
#print('swapup:',swapcaseUp(s))

start = 'FEDCBA'
s = [ord(i) for i in start]
#print('swap-up:',swapcaseUp(s))

start = 'ABCDEFGHIJK'
s = [ord(i) for i in start]
#print('swapup:',swapcaseUp(s))

start = 'DFAECIGBJH'
s = [ord(i) for i in start]
#print('swapup:',swapcaseUp(s))


start = 'CDABEKIHGJF'
s = [ord(i) for i in start]
print(f'swapcaseUp {start}:',swapcaseUp(s))


print(" %%%%%%%%%%%%%%%%%%%%%%% \n")
def swapcaseUP(start):
    s = [ord(i) for i in start]
    swap = {}
    cunt = 1
    while s != sorted(s):
        sorder = sorted(s)
        #print([chr(i) for i in s])
        for i,c in enumerate(s):
            if i == sorder.index(c):pass
            else:
                t = sorder.index(c)
                s[t],s[i] = s[i], s[t]  # 不能用 c ！！1
                swap[cunt] = f"{chr(s[t])} <-> {chr(s[i])}"
                cunt += 1

    return len(swap),swap,''.join([chr(i) for i in s])

start = 'ABCDEFGHIJK'
print(f' {start}:',swapcaseUP(start))

start = 'ABCDEFGHIJK'[::-1]
print(f' {start}:',swapcaseUP(start))

start = 'FCABDE'
print(f'{start}:',swapcaseUP(start))

start = 'FCADBE'
print(f' {start}:',swapcaseUP(start))

start = 'ECADBF'
print(f' {start}:',swapcaseUP(start))

start = 'FEDCBA'
print(f' {start}:',swapcaseUP(start))


start = 'FEDCBAGH'
print(f' {start}:',swapcaseUP(start))


start = 'FEDCBAGHIJ'
print(f'{start}:',swapcaseUP(start))


start = 'FEDCBAGHJI'
print(f' {start}:',swapcaseUP(start))


start = 'FEDCBAHGJI'
print(f' {start}:',swapcaseUP(start))


start = 'FAJIHGKEDCB'
print(f' {start}:',swapcaseUP(start))


start = 'DFAECIGBJH'
print(f' {start}:',swapcaseUP(start))

start = 'CDABEKIHGJF'
print(f' {start}:',swapcaseUP(start))


start = 'LVBZAUEMINFCWGJKQDXOTSHPY'
print(f' {start}:',swapcaseUP(start)[0])
chaos = [abs(ord(x)-ord(y)) for x,y in zip(start,sorted(start))]
print(sum(chaos),len(start),chaos)


start = 'ALVBZUEMWGJKINFCQDXOTSHPY'
print(f' {start}:',swapcaseUP(start)[0])
chaos = [abs(ord(x)-ord(y)) for x,y in zip(start,sorted(start))]
print(sum(chaos),len(start),chaos)


start = 'MWGJKALVBZUEINFCQDXOTSHPY'
print(f' {start}:',swapcaseUP(start)[0])
chaos = [abs(ord(x)-ord(y)) for x,y in zip(start,sorted(start))]
print(sum(chaos),len(start),chaos)

print(" %%%%%%%%%%%%%%%%%%%%%%% \n")
start = 'FCABDE'
def lessChrMove(start):
    alpha, notalpha = [],[]

    s = [ord(i) for i in start]
    small = min(s)
    for i in s:
        if i == small:
            alpha.append(chr(small))
            small += 1
        else:notalpha.append(chr(i))

    print(alpha,notalpha)

    # notalpha排序从最小的字母开始移动的alpha尾部
    seq = {}
    prev = start
    for i in sorted(notalpha):
        tail = [c for c in prev if c != i]
        tail = ''.join(tail) + i
        seq[i] = (prev,tail)
        prev = tail
    return seq

start = 'DFAECIGBJH'
#print(lessChrMove(start))
#print('FCABDE BFCADE ABFCDE ABCDEF -> 3')


'''
一家美术馆的馆长希望重新安排一些画作，使展览更有趣。目前的摆放是十二幅画沿着画廊的墙排列。
前4幅画是梵高，中间4幅是莫奈，后4幅是毕加索。

导演决定安排交替出现，当你沿着墙观赏时，你会看到4个周期：每个周期是斯特里顿的作品，一个
是威瑟斯的作品，然后是罗伯茨的作品。然而，这些画是脆弱的。每幅画每天只能移动一次。

即使这样，它也只能与它两边的一幅画相交换。重新安排画作所需的最少天数是多少？
(A) 5 (B) 6 (C) 7 (D) 8 (E) 9

'''

'''
自发组织团购了一车新鲜水果，预约的货车运载量是5千公斤左右。
在疫情期间，我将分给小区的200多家。

数量需求不尽不同，还好经验丰富的供货商考虑到水果发放要尽量便捷，
提供大小不同的包装袋密封好，到小区后不必打开包装，通过适当的几
种包装的组合能够凑出订购的数量。这样做以来，不仅省去每一家称重
的时间，也极大地缩短人员聚集的时间。

你作为程序员更容易想到一个办法，建议水果供货商将水果分为固定的
几种若干斤的重量的包装，最终能保证每家来领水果的时候，无论订购
了多少斤，一定能找到组合出每一家的水果需求量。同时不会剩下，如
何做到看起来近乎不可能的事情，希望你能给出各种包装的数量。

'''

# 策略
# 首先要准确量出 1 -> n,且 sum(1+ ... +n) <= 5000 less or above
# 找到某种规律组合，能够凑出上述任意数量的水果
# 每一种包装的数量确定

def evensplit(n):
    total = 1
    i = 1
    bench = []
    while total <= n:
       bench.append(i)
       total += i
       i += 1
    maxwgt = len(bin(bench[-1])[2:])
    bins = [2**i for i in range(maxwgt+1)][::-1]
    weights = dict(zip(bins,len(bins)*[0]))

    for n in bench[::-1]:
        for k,v in weights.items():
            weights[k] += n//k
            n = n % k
    return total,bins,weights
n = 5000
print('total ',evensplit(n))

# 领取水果的分配包装
# 输入参数是领取的重量
def pick(n):
    b = bin(n)[2:][::-1]
    ans = [2**int(i) for i,e in enumerate(b) if e == '1']
    return [f"{i} kg 一袋" for i in ans]
n = 10
print(pick(n))

n = 17
print(pick(n))

n = 50
print(pick(n))

n = 100
print(pick(n))

p = {}
for w in range(1,101):
    p[w] = pick(w)
print(p)

'''

启发商家的包装从小到大可以采用 1，2，4，8，... ..kg的包装

当然上述例子假设每一家的需求数量都不同时，而且一整车货载重固定
5000kg的约束条件下，批发水果的包装大小的组合数量分布。

进一步看实际遇到有顾客订购相同数量的需求，现在解决起来变得容易。只需稍微修改代码：
例如：有 5 人 购买 20kg，有 7 人购买 30kg
我们需要在总量不变的情况下，调整特定包装的数量。

'''

#1 首先看要增加哪些包装
s = [(5,20),(7,30)]

def picknum(n):
    b = bin(n)[2:][::-1]
    ans = [2**int(i) for i,e in enumerate(b) if e == '1']
    return ans

def adjust(s,n):
    n = n - sum([x*y for x,y in s])
    wgt = evensplit(n)[2]
    t = [(w[0],picknum(w[1])) for w in s]
    for m in t:
        for k,v in wgt.items():
            for i in m[1]:
                if i == k:
                    wgt[k] += m[0]

    return wgt
s,n = [(5,20),(7,30)],5000
print(adjust(s,n))
# {128: 0, 64: 37, 32: 37, 16: 48, 8: 48, 4: 49, 2: 50, 1: 50})

print(2520 / 9)

# https://www.codewars.com/kata/56cca888a9d0f25985000036/train/python
# 6 kyu
# Kids and candies

def candies_to_buy(amount_of_kids_invited):
    num = amount_of_kids_invited
    n = 1
    while True:

        if all([not num * n % i for i in range(1, num)]):
            return n * num
        else:n += 1
amount_of_kids_invited = 1
print(candies_to_buy(amount_of_kids_invited))
'''
STDERR
Execution Timed Out (12000 ms)
Why did my code time out?
Our servers are configured to only allow a certain amount of 
time for your code to execute. In rare cases the server may 
be taking on too much work and simply wasn't able to run your 
code efficiently enough. Most of the time though this issue 
is caused by inefficient algorithms. If you see this error multiple 
times you should try to optimize your code further.

[2,4,6,8]
[3,6,9]
[4,8]
[5,10]
[6]
[7]
[8]
[9]
[10]
'''
def candies_to_buy(n):
    xx = 1
    for i in range(n):
        x = xx
        while xx % (i+1):
            xx += x
    return xx
amount_of_kids_invited = 10
print(f'{amount_of_kids_invited}',candies_to_buy(amount_of_kids_invited))

'''

from math import lcm

def candies_to_buy(amount_of_kids_invited):
    return lcm(*range(1, amount_of_kids_invited + 1))

'''

def candies_to_buy(amount_of_kids_invited):
    p = amount_of_kids_invited

    num = list(range(1,p))
    ans = []
    s = 1
    for i in range(p,p//2+1,-1):
        s *= p//i * i
        ans.append(i)
        #if s % (p-1):
        if all([not s % (p-i) for i in range(1,int((p)**2))]):
            break
    else:
        #k = [n % i for n in ans]
        return s,ans

amount_of_kids_invited = 10
print(f'{amount_of_kids_invited}',candies_to_buy(amount_of_kids_invited))



def candies_to_buy(amount_of_kids_invited):
    p = amount_of_kids_invited
    edge = int(p**0.5)+1
    num = list(range(1,p))
    ans = [i for i in num if not i % 2]
    for j in range(1,edge): #range(2,)
        for i in num:
            if not i%j and i not in ans:
                ans.append(i)
    n = 1
    #print('ans', ans,p)
    while True:
        if all([not p*n % i for i in set(ans)]):
            return p * n
        else:n += 1
amount_of_kids_invited = 10
print(candies_to_buy(amount_of_kids_invited))