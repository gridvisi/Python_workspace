__author__ = 'Administrator'

def step(n):
    if n < 3:
        return n
    else:
        return step(n-1)+step(n-2)

n=int(input("输入楼梯的层数："))

print(step(n))
'''
def jump1(n):
    if n==1:
        return return jump1(n-1)+jump1(n-2)

def jump2(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return 2*jump1(n-1)

print(jump1(5))
print(jump2(5))
'''