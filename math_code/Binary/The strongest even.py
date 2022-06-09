def factor(x):
    n, d, re = x, 2, []
    while x > 2:
        if x % d == 0:
            re.append(d)
            re.append(x // d)
            x = x//d
        d += 1
    return sorted(re)
print(factor(16))

age_max = max([14,12,14,11,11,13])
age_min = min([14,12,14,11,11,13])

x = bin(14)  #binary
print(x)
'10: 0,1,2,3,4,5'
'2:0,1,10,11,100,'
#100 - 1000 最强偶数

print(int('0b1000000000',2))

n,m = 1,10000000
def strongest_even(n, m):
    while True:
        if m & m - 1 < n: return m
        m &= m - 1





'''
n,m = 16,2
def strongest_even(n, m):
    bin_lst = min([str(bin(i))[2:][::-1] for i in range(n,m+1)])
    return int(str(bin_lst)[::-1],2)
print(strongest_even(n,m))
'''