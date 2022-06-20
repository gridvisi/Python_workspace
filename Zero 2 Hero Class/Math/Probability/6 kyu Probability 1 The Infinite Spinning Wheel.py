'''
https://www.codewars.com/kata/605d58ab7f229d001bac446e/train/python

故事
你想和你的朋友一起玩转盘。不幸的是，你已经用你所有的钱买了比纺车更有用的东西。
所以你必须自己创造规则和纺车。

任务
你的转盘由几个部分组成，可以是 "赢 "或 "不赢"。如果你得到 "赢"，你马上就会赢。
但如果你得到 "不赢"，现在就轮到你的朋友来转盘了。这种情况会一直持续下去，直到有人获胜。
你会得到一个字符串，每个字符代表转盘的一个部分。(想象一下，把这根绳子放到现实世界中，
然后把它缠绕在一个旋转的轮子上。字符串的第一个字符与最后一个字符相连。）
"赢 "的部分被转化为 "W"，"不赢 "的部分被转化为 "N"。
如果你先走，请找出你赢得游戏的概率，以百分比计算，向下取整。

例子
例1
给出一个字符串 "WWWW"，其中所有的部分都是 "赢"。如果你先走，你就一定会赢。所以在这个例子中，
你必须返回100，以获得100%的获胜概率。

例2
给出一个字符串 "NNN"，所有的部分都是 "不赢"。在这种情况下，没有人会赢。所以你的获胜概率是0%。
所以你必须返回0。

Ex.3
如果你计算概率并得到31.6%，你必须返回31，因为0.6%会被舍去。

额外的
>概率不可能大于100%或小于0%。
>字符串将只由'W'或'N'组成。
关于四舍五入的注意事项
对于任何有效的输入字符串，都存在一个且只有一个正确的整数答案。
提示：不用浮点运算也可以解决这个问题。

数学游戏谜题
'''
def spinning_wheel(wheel):
    n, k = len(wheel), wheel.count('W')
    return 100 * n // (2*n - k) if k else 0

def spinning_wheel(wheel):
    ...
    circle = wheel * (100//len(wheel)) + wheel[0:100%len(wheel)]
    return circle.count('W')

# first = 1/3 ** len([1,2n,2]) * 2/3
# second = 1/3 ** len([2:2n:2]) * 2/3
# firstWin = first * second = 1/3 ** (2n) * 1/3 ** (2n-1) * (2/3)
'''
if total = 2*n + 1
firstwin  = (1 - (1-p)**n) * p
secondwin = (1-p)**n

if total == 2*n: # first have n times, second have n-1 times
firstwin  = (1-p)**n
secondwin = (1 - (1-p)**(n-1)) * p

firstwin = p - p*(1-p)**n
secondwin * (1-p) = p*(1-p) - p*(1-p)**n
firstwin - secondwin(1-p) = p - p*(1-p) = p*p
suppose that firstwin = x * secondwin

x * secondwin - secondwin + p*secondwin = p*p

'''

def spinning_wheel(wheel):
    n = 10
    first,second = 0,0
    p = wheel.count('W')/len(wheel)
    for i in range(n):
        if i % 2:
            first += (1 - (1-p)**i) * p
        else:
            second += (1 - (1-p)**(i-1)) * p

    return first /(first+second),p

wheel = 'NNNNNNNNNNNWWW'
#wheel = 'WWN'
print(spinning_wheel(wheel))


#只看最后 2 次的概率分布
'''
 p +      (1-p)*(1-p)*p  +      (1-p)*(1-p)*(1-p)*(1-p)*p + ...= F
(1-p)*p + (1-p)*(1-p)*(1-p)*p + (1-p)*(1-p)*(1-p)*(1-p)*(1-p)*p +... = S

S * (1-P) + P = F
S + F = 1

(1 - F) * (1-P) + P = 1 -P -F +FP + P = 1-F+FP
1-F+FP = F
-FP + 2*F  = 1
(2 - P) * F = 1
F = 1/(2 - P)
'''

def spinning_wheel(wheel):
    n, w = len(wheel), wheel.count('W')
    p = w / n
    '''
     p +      (1-p)*(1-p)*p  +      (1-p)*(1-p)*(1-p)*(1-p)*p + ...= F
    (1-p)*p + (1-p)*(1-p)*(1-p)*p + (1-p)*(1-p)*(1-p)*(1-p)*(1-p)*p +... = S

    S * (1-P) + P = F
    S + F = 1

    (1 - F) * (1-P) + P = 1 -P -F +FP + P = 1-F+FP
    1-F+FP = F
    -FP + 2*F  = 1
    (2 - P) * F = 1
    F = 1/(2 - P)
    '''
    #f = 1 / (2 - p)
    #f = 1*n/(2-p)*n
    f = 100*n / (2*n - w)
    return int(f) if w else 0
wheel = 'NNNNNNNNNNNWWW'
#wheel = 'WWN'
print(spinning_wheel(wheel))

