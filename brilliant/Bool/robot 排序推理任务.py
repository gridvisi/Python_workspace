'''
Rae, Knuck, and Lex are robots from 3 different models.
Rae is not the newest.
Knuck is the oldest.
Lex is not the oldest.
What’s the correct order, from newest to oldest?

Rae、Knuck和Lex是来自3个不同型号的机器人。
Rae不是最新的。
Knuck是最老的。
Lex不是最老的。
正确的顺序是什么，从最新的到最老的？
'''


from itertools import permutations #排列组合
result = []

#同学们习惯换编程视角描述新和旧，
# 简单如列表最左边是最newest，最右边是oldest
names = ['Rae', 'Knuck','Lex']
#任意次序即可开始排列组合
'''
Rae不是最新的: 不能出现在列表最left边
Knuck是最老的：只能出现在列表最right边
Lex不是最老的：不能出现在列表最左边

robot = [newest, middle  ,oldest]
最左边是最newest，最右边是oldest
'''
result = [] #result：结果 满足条件判断要求的结果放入result列表里
# permutations 排列组合
# 红绿蓝：[" "," "," "] 第一个位置3，第二个位置2，第三个1
# 总共有：3 * 2 * 1 = 6

s = []
for name in permutations(names,len(names)):
    s.append(name) #暴力枚举
    #print('s:',len(s),s)
    #if name.index("Rae") != len(names)-1:
    #[-1] and：都满足； or 两者只满足一个；或者
    if name[0] != "Rae" and name[-1] == "Knuck" and name[-1] != "Lex":
        result.append(name)
print('排列顺序：',result)

'''
第二个任务

Arrange the robots to make the following true:
Loy is in one of the two middle spaces.
Mig is left of Lex and right of Rae.
Rae is directly next to Mig.

排列机器人次序，使下列情况成为事实。
Lex在中间的两个空间中的一个。
Mig在Lex的左边，Rae的右边。
Rae紧挨着Mig
'''
names = ['Rae', 'Knuck','Ty']
for name in permutations(names,len(names)):
    if name.index('Rae') < name.index("Ty"):
    #    #'Rae',
        result.append(name)
print(result,len(result))

for name in permutations(names,len(names)):
    if name.index('Rae') < name.index("Ty"):
        #'Rae',
        result.append(name)
print(result,len(result))
