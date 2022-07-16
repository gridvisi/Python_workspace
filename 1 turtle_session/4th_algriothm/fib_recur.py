
x = 0
def draw_fibonacci(x):
    # F = f(x)
    # F = f(kesou,temp,hesuan) all
    # F0=1
    # F1=1
    # Fn= F（n-1）+F（n-2）
    a, b = 1, 1
    for _ in range(x):
        a,b = b,a+b
        print(a,b)

    # 产生斐波那契数列，用于查表
    # 像这种计算复杂性指数增长的计算，不要写个函数去每次求一个数
    # 最好的办法是，按照规律写出查找表，用查找的方法来得到数据
    return

x = 50
print(draw_fibonacci(x))

print(all([i%2==0 for i in (2,4,6,8)]))
print(any([i%2==1 for i in (2,4,6,8)]))
#filter()