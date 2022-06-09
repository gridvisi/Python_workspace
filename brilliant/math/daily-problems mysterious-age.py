'''
https://brilliant.org/daily-problems/mysterious-age/

一个朋友问以利亚，他的年龄是多少。他回答说："我的年龄我年龄数字的四倍乘积 + 1"
如果以利亚比100小，那么他的年龄是多少？

A friend asks Elijah how old he is. He responds, "My age is 11 greater
than quadruple the product of my age's digits."
If Elijah is younger than 100,100, how old is he?
'''

digits = [i for i in range(1,10)]

for x in digits:
    for y in digits:
        if 10*x + y - 1 == 4*x*y:
            print(x,y)
