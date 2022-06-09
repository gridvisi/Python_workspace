
#计算蜜蜂代际祖先数量
gen = int(input("queen gen number:"))
female = 1
male = 0
for i in range(gen):
    female,male = female+male,female
print('第',gen,'代有 queen:',female,'只',',有male bee',male)
print('第',gen,'代有 ancestors:',female+male)


def bees_tree(n):
    female = 1
    male = 0
    for g in range(gen):
        female, male = female + male, female
    return female+male
n = 20
print(bees_tree(n))