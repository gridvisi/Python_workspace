__author__ = 'Administrator'
'''
A queen bee has two parents: one male and one female.
A male bee has just one parent, a queen bee.
If we go back just one generation, a queen bee has two ancestors.
If we go back two generations, this rises to three ancestors in that generation.
How many ancestors does a queen bee have going back 20 generations (again, only in that generation)?
蜂王有两个父母：一男一女。
雄性蜜蜂只有一个母蜂，一只蜂王。
如果我们只回去一代，蜂王就有两个祖先。
如果我们追溯到两代人，这一代的祖先将增加到三位。
一只蜂后有多少祖先又回到了20代（再一次，只有在那一代）？
def queen(female,male,gen):
    if gen == 1 and female == 1:
        female = 1
        male = 0
        return 1
    if gen == 2:
        female += 1
        male = 1
        return
    if gen > 2:

if gen == 1:
    female = 1
    male = 0

if gen == 2:
    female = 1
    male = 1


for i in range(gen):
    fe_temp = female
    ma_temp = male
    #male = 1
    #while gen < 20:
    gen += 1

    female = fe_temp + ma_temp
    male = fe_temp
'''

gen = int(input("queen gen number:"))
female = 1
male = 0
for i in range(gen):
    female,male = female+male,female
print('第',gen+1,'代有 queen:',female,'只',',有male bee',male)
print('第',gen+1,'代有 ancestors:',female+male)