# https://www.codewars.com/kata/5b853229cfde412a470000d0/train/python
'''
Your function takes two arguments:

current father's age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as
his son (or in how many years he will be twice as old).

FUNDAMENTALSMATHEMATICSALGORITHMSNUMBERS

你的函数需要两个参数。

当前父亲的年龄（岁）。
他儿子目前的年龄（岁）。
计算多少年前父亲的年龄是他儿子的两倍（或多少年后他的年龄将是儿子的两倍）。
'''


def twice_as_old(dad, son):
    year = 0
    while son * 2 != dad:
        year += 1
        son += 1
        dad += 1
    return year
dad,son = 42,9
print(twice_as_old(dad, son))

dad,son = 72,42
def twice_as_old(dad, son):
    year = 0
    while son * 2 != dad:
        year -= 1
        son -= 1
        dad -= 1
    return year
#><== !=
print(twice_as_old(dad, son))

print(abs(-5))