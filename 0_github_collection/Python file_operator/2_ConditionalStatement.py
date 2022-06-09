# -*- coding: UTF-8 -*-
# python 数组用法
# array.array(typecode,[initializer])
# --typecode:元素类型代码；
# initializer:初始化器，若数组为空，则省略初始化器
import array

num = array.array('H', [1] * 21)
# print("len(num)=",len(num))
# print(num)
len = len(num)
for i in range(len):
    if 0 == i or i == 1:
        num[i] = 0
        continue
    j = i
    while i * j < len:
        if (num[j * i]):
            num[j * i] = 0
        j += 1
# for i in range(len):
#     print(i,num[i])
# print(num)
# 以上实现的是一个简单的质数筛法，PrimeNumber

for i in range(len):
    if i < 2:
        print(i, "既不是质数，也不是偶数。")
    elif num[i] and i % 2:
        print(i, "是质数，且是奇质数")
    elif num[i] and 0 == i % 2:
        print(i, "是质数，且是偶质数")
    elif not (num[i]) and not (i % 2):
        print(i, "非质数，且是偶数")
    else:  # not(num[i]) and (i%2)
        print(i, "非质数，且是奇数")

#条件语句，以及质数筛法
#while i * j < len:
    #statement

#该语句完全可以换成另外一种写法（殊途同归）

while True:
    #statement
    if i * j >= len:
        break
#	官方文档
#https://docs.python.org/2/library/array.html
