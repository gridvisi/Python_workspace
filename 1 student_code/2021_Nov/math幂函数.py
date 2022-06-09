name = "刘芷墨"
title = ["版主","同学","同志"]
title_2 = ["粉丝","老师","学生"]
title.append(title_2) #inbed
print('1:',title)

title = ["版主","同学","同志"]
title_2 = ["粉丝","老师","学生"]
title.extend(title_2)  #flat
print('2:',title)

print(name + title[1])
title.append("队友") #
print("append:",title)
title.extend(["队友"]) #extend
print("extend:",title)




import random
import math

names = ['zhang',"su","liu","li"]
print(names[:10])  #切片

plate = "渝B88888"
print(' "渝B88888:',plate[-1])
print(' "渝B88888:',plate[2:])

print('花名册：',sorted(names))
print('花名册倒过来：',sorted(names)[::-1][:10])
print('花名册倒过来：',sorted(names,reverse=True))
import random
print('随机函数提名：',random.choice(names))
a,b,c = 1,2,3
a,b,c = 3,2,1
a,b,c = 2,3,1
print(a,b,c)

# and or

a,b,c = 3,3,3
a,b,c = 10,9,8
if a+b > c:
    if a+c > b:
        if b+c > a:
            print("yes,well done it is triangle")
else:
    print("yes,well done it is not triangle")



# 算法 是否某些数学等式或定律或定理或常识...公理
# 表达 数据结构

# a + b > c,





print(min(a,b,c),max(a,b,c))
print(sorted([a,b,c]))  #排序函数sorted
a,b,c = 19,7,4
a,b,c = sorted([a,b,c])


def isTriangle(a,b,c):
    a, b, c = sorted([a, b, c])
    return a + b > c

#sorted函数更多用法：




ddm = "life is short, I love python"


print('1024:',bin(1024))
print(len("10000000000"))

print(len("任务：已知年龄推算年级"))
print(len("abcdefghijk"))

print('rices:',2 ** 64)


#     1        1     1     0
print(2**3 + 2**2 + 2**1 + 2**0)

print('test 1:',2 ** 3 == 2 * 2 * 2) # 4
print(2 ** 3)  # = 2 * 2 * 2

print(bin(8)) #0b

