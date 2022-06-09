'''
https://www.codewars.com/kata/559ce00b70041bc7b600013d/train/python

描述。
我需要节省一些钱来购买礼物。我想我可以做这样的事情。
第一周（W0）我在星期天什么都不存，星期一存1，星期二存2...
第二周(W1)，周一存2个......周六存7个。
第二周(W1)星期一存2个，星期六存7个，以此类推，根据下表，日子从0到6编号。

你能告诉我在星期六晚上，在我存了12个钱之后，我将有多少钱来买礼物吗？
你的函数finance(6)应该返回168，这是表格中的存款之和）。

想象一下，我们现在生活在XY140Z-n星球上，
每周的天数从0到n（整数n>0），我从第0周到第n周储蓄（在下表中n=6）。

在XY140Z-n星球上，我的融资计划结束时将有多少钱？

test.assert_equals(finance(5), 105)
test.assert_equals(finance(6), 168)
test.assert_equals(finance(8), 360)
test.assert_equals(finance(15), 2040)
'''

def finance(n):
    # your code
    arr = list(range(7))
    w = [sum(arr[i:])+i*len(arr[i:]) for i in arr]
    return sum(w)*(n//7) + sum(w[:n%7])
n = 365
print(finance(n))
#print([finance(n) for n in range(8)])


def finance(n):
    # your code
    arr = list(range(7))
    w = [sum(arr[i:])+i*len(arr[i:]) for i in arr]
    return w #sum(w)*(n//7) + sum(w[:n%7])