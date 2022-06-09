#原文链接：https://blog.csdn.net/mamengyan/java/article/details/106764871

#分解质因数：把一个合数写成几个质数相乘的形式表示，比如36的所有质因数：36=2* 2* 3* 3
num=input('输入一个数字：')
num=int(num)
ls = []
m = 2
while num >= m: #不要使用for循环，for循环中的循环变量不可变，使用while循环控制循环变量
    if num%m == 0: #如果能除尽，说明m是num的一个因子
        ls.append(m)#将此因子追加到列表中
        num = num//m  #并将因子分解出来，继续除以m，直到m除不尽，m+1继续除，如此循环，直到num除以最大的因子num
    else:
        m += 1
print(ls)

