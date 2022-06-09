#https://brilliant.org/daily-problems/conditional-statements-3/

'''
1950~2050年之间的闰年：
1952、1956、1960、1964、1968、1972、1976、1980、1984、1988、
1992、1996、2000、2004、2008、2012、2016、2020、2024、2028、
2032、2036、2040、2044、2048。

if it is rainning and 新冠肺炎：
    go sleep，play game
else：
    or 沙尘暴 :



if it is rainning:
    if it is 沙尘暴：
        if it is 新冠肺炎：
            go sleep，play game

'''





y = 2020
print(y%4 == 0 and y%100 != 0)

y = 2021
if y % 4 == 0:
    if y % 100 != 0:
        print(f"{y}是闰年")
else:
    print(f"{y}不是闰年")




x,y = 10,50
print([i for i in range(1,x+1)])

for i in range(1,x+1):
    if x%i == 0 and y%i == 0:
        print(i)


x = 3
y = 4
print(x + y)

x = [i for i in range(101)]
x = [590,600,550,460,630]
print(sorted(x,reverse=True))

ls = [3,3,3,3,4,4,4,4,6,6,6,9]
team = set(ls)
print(ls)

print([i for i in range(101) if i % 2 == 0])
print([i for i in range(101)][0:101:2])
print()

def multiply(a,b):
    return a * b