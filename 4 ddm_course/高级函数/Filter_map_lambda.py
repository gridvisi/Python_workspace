
def is_odd(n):
    return n % 2 == 1
lst1 = filter(is_odd,[1,2,3,4,5,6,7,8,9,10])


def is_odd(n):
    return n % 2 == 1


newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(newlist)
# Python3.6结果：<filter object at 0x00000184ED881358>
# Python2.x结果：[1, 3, 5, 7, 9]

# Python3.6返回的是迭代器对象，可以转换成list
print(list(newlist))
# [1, 3, 5, 7, 9]

# -------------------------------------------

# 以上函数可以用lambda表达式书写
newlist = list(filter(lambda n: n % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(newlist)
# [1, 3, 5, 7, 9]

# -------------------------------------------

# 在对象遍历处理方面，其实Python的for..in..if语法已经很强大，并且在易读上胜过了lambda。
# 以上函数还可以写成如下：
newlist = list(x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if x % 2 == 1)
print(newlist)
# [1, 3, 5, 7, 9]
