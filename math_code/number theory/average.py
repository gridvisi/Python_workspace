__author__ = 'Administrator'
ave=92.5
ben=ave*6
for x in range(76,99):
    for y in range(76,99):
        if sum([99, y, x, x - 1, x - 2, 76]) == ben:
            print(x)
            print(x,x-1,x-2)

'''
import random
per=6
max=99
min=76
ave=92.5
ben=ave*6
print(ben)


scor=[99,76]
#print(random.choice(scor))
#x=int(min)
sum = ben-sum(scor)
print(sum)
aver=sum/4
print(aver)

aver=95




for i in range(1,5):
    scor.append(1 + scor[-1])
    print(x)
    print(scor)
    s=sum(scor)
    print(s)
'''