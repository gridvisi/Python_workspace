__author__ = 'Administrator'
'''
def cal(n):
    if n==1:
        return 1
    return n+cal(n-1)

#n=int(input("last number:"))
print(cal(n))
'''
n=int(input("last number:"))
i=0;j=0
while i < n or i == n:
    j=i+j
    i=i+1
print (j)
