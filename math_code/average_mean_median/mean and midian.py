#平均数  中位数  众数

# 中国收入众数

x = 8
fruit_median = [6, 4, 2, 7, 10, x,]
fruit_median = [60,80,75,45,120]

print(sorted(fruit_median),sum(fruit_median)/len(fruit_median))

if len(fruit_median)//2 == 0:
    midian = len(fruit_median)//2
    print(sorted(fruit_median)[midian-1] + sorted(fruit_median)[midian-1])
else:
    midian = (1 + len(fruit_median)) // 2
    print(sorted(fruit_median)[midian-1])
