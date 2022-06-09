name = 'zhangbowen'
print(name[:])


'''
https://www.codewars.com/kata/55be10de92aad5ef28000023/train/python

你知道组合：例如，如果你从52张牌中抽取5张，你就有2,598,960种不同的组合。

在数学中，你能从一个由n个元素组成的集合中抽取的x个组合的数量被称为n和x的二项式系数，
或者更多的是n选择x。计算m=n选择x的公式是：m=n! / (x! *（n-x）！）其中！是阶乘运算符。

你是一位著名的海报设计师和画家。你被要求提供6张海报，每张海报都有相同的设计，都有两种颜色。
海报必须有不同的颜色组合，你可以选择4种颜色：红、蓝、黄、绿。你可以为每张海报选择多少种颜色？

答案是两种，因为4选2=6。组合将是。{红，蓝}，{红，黄}，{红，绿}，{蓝，黄}，{蓝，绿}，{黄，绿}。

现在同样的问题，但你有35张海报要提供，有7种颜色可供选择。每张海报有多少种颜色？如果你把组合7选2，
用上述公式就可以得到21种。但是21种方案对于35张海报来说是不够的。如果你采取7选5的组合，你也会得
到21个。幸运的是，如果你采取7选3或7选4的组合，你会得到35个，所以每张海报都会有不同的3色或5色组
合。你会选择3种颜色，因为它的价格比较低。

因此问题就来了。
知道m（要设计的海报数量），知道n（可用颜色的总数），让我们寻找x（每张海报的颜色数量，以便每张海报
都有独特的颜色组合，并且组合的数量与海报的数量完全相同）。

换句话说，我们必须找到x，如
'''



# First try is Execution Timed Out
# STDERR
# Execution Timed Out (12000 ms)
def fact(n,x):
    ans = 1
    for i in range(x):
        ans *= (n - i)/(i+1)
    return ans
print(fact(4,2))


def checkchoose(m, n): #m refer to number of post, n is types of color
    i = 1
    while fact(n,i) <= m:
        i += 1
        if fact(n,i) == m:
            return i
        elif fact(n,i) > m:
            return -1

m,n = 6,4
m,n = 47129212243961,50
m,n = 35, 7
print( checkchoose(m, n))


#1st
def checkchoose(m, n):
    c = 1
    for x in range(n // 2 + 1):
        if c == m: return x
        c = c * (n-x) // (x+1)
    else: return -1