
#丁丁猫编程递归zero 2 hero

def revers_self(sl):
    if len(sl[1:]) == 0:return sl
    else:return revers_self(sl[1:])+sl[0]
sl = 'I love python'
print(revers_self(sl))
#nohtyp evol I


#输入："爸爸的爸爸是爷爷"
#输出："爷爷是爸爸的爸爸"

inp = "爸爸的爸爸是爷爷"
out = "爷爷是爸爸的爸爸"

rev = []
for i in range(len(inp)-1,0,-1):
    #why len(inp)-1
    rev.append(inp[i])
print(''.join(rev))

print(inp[::-1])

# 第四种：reverse函数
#print(inp.reverse())
print(list(reversed(inp)))
print(''.join(reversed(inp)))


# the fifth solution
from collections import deque
inp_que = deque(inp)
print(inp_que)
revs = inp_que.rotate(2)
print(revs)

def rotate(l, n):
    return l[-n:] + l[:-n]

import collections
d = collections.deque([1,2,3,4,5])
d.rotate(1)
print(d)
# deque([3, 4, 5, 1, 2])
print(d)
d.rotate(4)
print(d)