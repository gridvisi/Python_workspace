
#2
'''
上下给数字1342的列表，您可以提取三个“上下”列表132、142和342，
其中第二个数字大于第一个数字，第三个数字小于第二个数字。
你能从132597684中得到多少“上下”列表？

(A) 30 (B) 32 (C) 34 (D) 36 (E) 38

'''
ans = []
s = [int(i) for i in '132597684']
for i in range(len(s)-2):
    for j in range(i+1,len(s)):
        for k in range(j+1,len(s)):
            if s[i] < s[j] and s[j] > s[k]:
                ans.append(f"{s[i]}{j}{k}")
print(len(ans),ans)


#5 The new truck
# 字典表达图的节点连接

graph = {'A': set(['B', 'C', 'D']),
         'B': set(['A', 'C', 'J']),
         'C': set(['A','B', 'D', 'E','F']),
         'D': set(['A', 'C', 'F']),
         'E': set(['C', 'G', 'H']),
         'F': set(['D', 'G']),
         'G': set(['E', 'F', 'H']),
         'H': set(['E', 'G', 'J']),
         'J': set(['B', 'H'])}

print(graph['A'])


'''
你有两张桌子，分别是A和 B. 

首先，桌子上有一排卡片 A. 每张卡显示一个单一数字：a1、a2或a3一起构成一个数字。
B为空。您希望将卡片移动到表B，以便它们制作尽可能大的数字。


您可以进行以下移动：
向W移动：从表A中取出最左边的卡，并将其放在表上的卡的最左边 B.
• 移动X：从表A中取出最左边的牌，放在桌子上的牌的最右端 B.
• 移动Y：从表A中取出最右边的牌，然后放在表A上的牌的最左端 B.
• 移动Z：从表A中取出最右边的牌，放在桌子上的牌的最右端 B.

A13213  B   Y→
A1321  B3   X→
A321   B31  W→
A21    B331  X→
A1     B3312  X→
A      B33121

* X :  左到 左；Y: 右到左 ；W：右到左

例如，假设表A以构成数字13213的五张卡开始。
下图说明了移动YXWXX，给出了表上的最终数字33121 
在以下每个问题中，您都有表A上的起始数字，并且您必须计算出使用上述移动在表B上形成的最大数字。
在每种情况下，你的答案都应该是这个数字的最后三个数字

(13).  32123112 
(14).  1231132312 
(15).  2312131132

'''
#  X : 右到右；Y: 右到左 ；W：左到左
s = '32123112'
print(s[:-1])
#s = deque(s)
print(s[0],s[-1])

from collections import deque
def shuffle(cards):
    d = deque(cards)
    ans = '0'
    while d:
        if d[0] >= d[-1]:
            if d[0] > ans[0]:
                ans = d.popleft() + ans
            elif d[0] < ans[0]:
                ans += d[0]
        else:
            if d[-1] >= d[0]:
                ans = d.pop() + ans
            else:
                ans += d.pop()
        print(ans)
    return ans[-3:]  #输出第4位数
s = '13213'
print('s = ',s)
#print('shuffle-deque: ',shuffle(s))


import copy
def shuffle(cards):
    d = copy.copy(cards)
    ans = ''
    i,j = 0,len(d)-1
    while i < j:
        if d[i] > d[j]:
            if not ans:
                ans = d[i] + ans
            else:
                if d[i] >= ans[0]:
                    ans = d[i] + ans
                    i += 1
                elif d[0] < ans[0]:
                    ans += d[0]
                    i += 1

        elif d[i] < d[j]:
            if not ans:
                ans = d[i] + ans
            else:
                if d[j] >= ans[0]:
                    ans = d[j] + ans
                    j -= 1
                else:
                    ans += d[j]
                    j -= 1

        elif d[i] == d[j]:
            if not ans:
                ans = d[i] + ans
            else:
                if d[i] >= ans[0]:
                    ans = d[i] + d[j] + ans
                    i += 1
                    j -= 1
                else:
                    ans += d[i] + d[j]
                    i += 1
                    j -= 1
        #print(ans)
    return ans[-3:],ans  #输出第4位数

s = '1231132312'
s = '2312131132'

s = '2312131132'
s = '13213'
print('s = ',s)
print('shuffle: ',shuffle(s))


class Move():
    def __init__(self,s,num):
        self.s = s
        self.num = num

    def lor(self): #X  Most left -> Most right
        #print(self.num,self.s)
        self.num += self.s[0]
        self.s = self.s[1:]
        return self.num

    def rol(self): #Y Most right -> Most left
        self.num = self.s[-1] + self.num
        self.s = self.s[:-1]
        return self.num

    def lol(self): #W #Y Most right -> Most left
        self.num = self.s[0] + self.num
        self.s = self.s[1:]
        return self.num

    def ror(self): #Z #Y Most right -> Most right
        self.num += self.s[-1]
        self.s = self.s[:-1]
        return self.num

    def maxNum(self):
        while len(self.s) > 0:

            print('s:',self.s)
            if self.s[0] > self.s[-1]: #Mleft -> Mleft
                 if s[0] <= num[0]:
                    self.lor()
                 self.lol()

            elif self.s[0] < self.s[-1]:  # Mleft -> Mleft
                if s[-1] > num[0]:
                    self.rol()
                #self.rol()

            elif self.s[0] == self.s[-1]:  # Mleft -> Mleft
                if self.s[0] > self.num[0]:
                    self.lor()
                self.rol()
            #break
        return self.num


s = '1231132312'
s = '2312131132'
s = '13213'
num = '0'
print(s[0] == s[-1])
m = Move(s,num)
print('s = ',s)
maxnum = m.maxNum()
print('max : ', m.maxNum())


print("# YXWXX")

'''


print("# YXWXX ")
print(m.rol())
m.lor()
m.lol()
m.lor()
print(m.lor())
print(m.ror())

s = '13213'
X = m.lor(s)
Y = m.rol(s)
W = m.lol(s)
num = ''

'''
# for _ in (Y,X,W,X,X):
