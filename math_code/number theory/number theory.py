__author__ = 'Administrator'

import math
print(6+4*math.sqrt(2))


'''
s1 = [[x,y] for x in range(1,10) for y in range(1000,10000) if ''.join(sorted(str(x)+str(y)+str(x*y))) == '0123456789']
print(s1)
s2 = [[x,y] for x in range(10,100) for y in range(100,1000) if ''.join(sorted(str(x)+str(y)+str(x*y))) == '0123456789']
print(s2)
'''

s1 = [[x,y] for x in range(1,10) for y in range(1000,10000)
if ''.join(sorted(str(x)+str(y)+str(x*y))) == '0123456789']

s2 = [[x,y] for x in range(10,100) for y in range(100,1000)
if ''.join(sorted(str(x)+str(y)+str(x*y))) == '0123456789']
one_digit = set([x[0] for x in s1])
two_digit = set([x[0] for x in s2])
three_digit = set([x[1] for x in s2])
four_digit = set([x[1] for x in s1])
print(s1,s1[0])
print(s2)
print(one_digit,two_digit,three_digit,four_digit)
print(sum(one_digit) + sum(two_digit) + sum(three_digit) + sum(four_digit))
print('***** following TEST s1 equation:*****')
print(s1[0][0]*s1[0][1])

print('3*5694 =',3*5694)
print('78*345 =',78*345)

for i in range(len(s1)):
    #print(len(s1))
    print(s1[i][0],'*',s1[i][1],'=',s1[i][0]*s1[i][1])
print('***** following TEST s2 equation:*****')
for j in range(len(s2)):
    #print(len(s1))
    print(s2[j][0],'*',s2[j][1],'=',s2[j][0]*s2[j][1])