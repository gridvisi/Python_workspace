n = 33
a,b,c = 7,4,3
# 1,2,6
if n <= 2:
    print(-1)
    exit()
i,j = 1,0
p = [a, b, c]

print((n // sum([a, b, c])),(n // sum([a, b, c])),(n // sum([a, b, c]) + (n % sum([a, b, c])) // c))



#total = [i for i in range(n//c) if n - sum(p) * i >= 0]