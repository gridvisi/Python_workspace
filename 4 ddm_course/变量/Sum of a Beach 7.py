def sum_of_a_beach(beach):
    beach_low = beach.lower()
    return beach_low.count("sand")+beach_low.count("water")+beach_low.count("sun")+beach_low.count("fish")


#Find The Parity Outlier

print(sum_of_a_beach("sunsunsunsun"))

__author__ = 'Administrator'
'''
per = 6
max = 99
min = 76
ave = 92.5
ben = ave * 6

# print(random.choice(scor))
for x in range(76,99):
    if sum([99, 95, x, x - 1, x - 2, 76]) == ben:
        print(x,ben,ben-max-min,(ben-max-min)/4,ben-99-98-76)
'''

import random
per=6
max=99
min=76
ave=92.5
ben=ave*6
print(ben)

scor=[]
# print(random.choice(scor))
x=int(min)
'''
for j in range(0,9):
    print(j)
'''
#sum=sum(scor)

for i in range(77,99):
    scor.append(i)
    print(scor)
    s=sum(scor)
    print(s)
