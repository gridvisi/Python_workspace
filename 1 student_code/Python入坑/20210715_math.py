
family_name = 'li'

# 1,2,3,4 solve [-5]
n = [1,2,3,4,5]
n = n[:-1]
print(n)
group = list(range(1,5))
print(group)

num = []
for i in group:
    for j in group:
        for k in group:
            for l in group:
                if i != j and j!= k and k != l and i!=k and j!=l and i!=l:
                    num.append(f"{i}{j}{k}{l}")
print(len(num),sorted(num)[-5])

from itertools import combinations

print(sum(range(5)))

#2
ans = []
sl = [1,2,3,4,5,6,7,8]
for i in sl:
    for j in sl:
        if i != j:
            ans.append([i,j])
print(len(ans)) #length

#学习组合
#四种菜，每种菜只能吃一盘，
# [chicken，pork，beef，vegetable]
# 每次吃两种，但每次吃的不能相同，问你能吃多少回？
# math and coding solve it


my_fruit = {'watemelon','apple','mango','banana','peach'}
your_fruit = {'pear','strawberry','pear','mango'}
print(my_fruit & your_fruit)
print(my_fruit ^ your_fruit)
print(my_fruit | your_fruit)


#

course = ["math","scratch","physics","robot","history","python"]

phil = {"math","python","history"}






