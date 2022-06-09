'''
https://blog.csdn.net/shenziheng1/article/details/83471905
'''
print(1, 2, 3, 4, 5, sep="\n")
print(1, 2, 3, 4, 5, sep="->")
#1--->2--->3--->4--->5

print([i for i in range(10)])
les = [str(i) for i in range(10)]
print("-".join(les))
print("e f f e c t".join("Hello World"))# faro shuffle

poke = ['k','Q','J','2','2','8']
first = ['k','2','Q','2','8','J']

step = 0
score = 0

while step < 100:
    step += 2
    score += 1
    print('jiajia say:', step, score)
print('jiajia SAY:',step,score)

import math
x = 19
for i in range(2,x):
    if i <= int(math.sqrt(x) + 1):
        if x % i == 0:
            print('Not prime')
            break
else:print("yes")




print('1.1*2.2*3.3:',eval('1.1*2.2*3.3'))
#7.986000000000001
print('1.1*2.2*3.3:',float(str(eval('1.1*2.2*3.3'))))

a = 4.2
b = 2.1
print(a + b)      # 6.300000000000001
print(a+b == 6.3) #False

from decimal import localcontext

#a = Decimal('1.3')
#b = Decimal('1.7')
print(a / b)  # 0.7647058823529411764705882353

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)  # 0.765

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)  # 0.76470588235294117647058823529411764705882352941176


