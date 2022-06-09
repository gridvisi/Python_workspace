__author__ = 'Administrator'

# 从1加到10如何实现？方法一：
num = [1,2,3,4,5,6,7,8,9]
total = sum(num)
print(total)

#2nd
answer = 0
for x in range(1,9):
    answer += x
print(answer)

#3rd
x = [x*x for x in range(1,9)]   #正解
print(x)
print (",".join(str(i) for i in x))
y = x
print(y)
print(sum(x))  # 为什么结果是36，而不是45？

print("一行代码搞定：",sum([x for x in range(1,9)]))

# 从1加到10如何实现？方法二：
x = 0
for i in range(1,10):
    x = x + i
    print(x)

# 糖纸换糖的机会最多换法
rmb = 100
wrappers = 0
eaten = 0
while rmb > 0:  #phil 退出条件要根据糖的价格变换
    rmb -= 1
    eaten += 1
    wrappers += 1
    if wrappers == 3:
        wrappers -= 3
        eaten += 1
        wrappers += 1
print("total candy Answer:", eaten)


# 糖纸换糖的机会最多换法
rmb = 10
wrappers = 0
eaten = 0
while rmb > 0:  #phil 退出条件要根据糖的价格变换
    rmb -= 2
    eaten += 1
    wrappers += 1
    if wrappers == 5:
        wrappers -= 5
        eaten += 1
        wrappers += 1
print("total candy Answer:", eaten)

