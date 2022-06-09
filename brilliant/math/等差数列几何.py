'''
https://brilliant.org/daily-problems/rearrange-dots/

# 函数
f(1) = 4
f(2) = 8
f(1) = 4
f(2) = 8
'''

albert = 8 # number
harrypot = 10

print(f"albert is {albert} years old")

#num += 1
#num = num + 1
#print('No.2nd',num)

num = 0
for i in range(0,10):
    num = num + i
print(num)

def triangle_tail(n):
    return sum([i for i in range(1,n+2)])+n
n = 3
#print(triangle_tail(n))