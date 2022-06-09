__author__ = 'Administrator'
#20200322
# Find the smallest positive integer which ends in 17, is divisible by 17, and whose digits sum to 17.

#print(35/289)

s = [x*17 for x in range(1,100) if sum([int(i) for i in str(x*17)]) == 9]
print(s[0]*100+17,(s[0]*100+17)/17)

'''
if ''.join(sorted(str(x)+str(y)+str(x*y))) == '0123456789':
    print(x,y)

s1 = [[x,y] for x in range(1,10) for y in range(1000,10000) if ''.join(sorted(str(x)+str(y)+str(x*y))) == '0123456789']
print(s1)
s2 = [[x,y] for x in range(10,100) for y in range(100,1000) if ''.join(sorted(str(x)+str(y)+str(x*y))) == '0123456789']
print(s2)
'''

'''
x = 1
while True:
    if sum([int(x) for i in list(str(x*17))]) == 9 and str(x*17)[-2:]==17:
        print(x)
        break
    x += 1
'''

