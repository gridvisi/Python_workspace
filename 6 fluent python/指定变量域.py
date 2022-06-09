
#变量作用域
b = 2
def f(a):
    #a = 1
    print(a)
    print(b)
    b = 3
#f(1)

#global
b = 2
def f(a):
    global b
    #a = 1
    print(a)
    print(b)
    b = 3
f(1)

# deep understanding iter()

import random

def dice():
    return random.randint(1,6)
diter = iter(dice,6)
ans = []
for i in diter:
    ans.append(i)
print(ans,i)
print(diter)
print(list(diter))
print([i for i in diter])