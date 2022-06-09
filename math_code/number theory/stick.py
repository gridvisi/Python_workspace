__author__ = 'Administrator'
'''
def cut(m,n,current):
    if current >= n:
        return 0
    elif current < m:
        return 1 + cut(m,n,current*2)
    else:
        return 1 + cut(m,n,current + m)

print(cut(3,20,3))
print(cut(2,20,3))
print(cut(3,20,1))


def cut2(m,n,s):  # i 个 s 米的木棍 粘起来，每一次最多同时不超过m个工人一起粘连，一个人一次只粘接两个木棍
    i= int(n/s)
    #print("i=",i)
    if s >= n:
        return 0
    elif i%2 == 0:
        return 1+cut2(m,i*s*0.5,s)+cut2(m,n-i*s*0.5,s)
    else:
        return 1+cut2(m,(i+1)*s*0.5,s)+ cut2(m,n-(i+1)*s*0.5,s)
print(cut2(3,20,3))
print(cut2(2,20,3))
# print(cut2(1,10,2))
'''
def cut3(m,n,s):
    i= int(n/s)
    j = 1
    while j*m + 0.5*m*(m-1) <= n:
        j+=1
    return int(j/s)+2
print(cut3(4,10,6))
print (int(10/6))