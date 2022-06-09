n = int(input())
print(len(str(n)))

n = int(input('请输入：'))
s = 1
for i in range(1,n+1):
    s *= i
print(s)
#res = lambda x,y:x*y,[i for i in range(1,n)]
print(s)


#print(sum([i for i in range(1,100,2)]))

start = 0
i = 1
end = 'l'

name1 = 'ucas'
name2 = 'eric'
for i in range(0,4):
    end = end + name1[i]
    print(end)
print(end)