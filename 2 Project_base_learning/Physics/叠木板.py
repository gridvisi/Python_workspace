import math
layer = 10000000
l = 8.347655682928636

def extendlenth(layer):
    l = 0
    start = 1
    #l = 9.498948256926278
    for i in range(start,layer + 1):
        l += 1/(i*2)
    return l
print(227 * math.e ** 2)
layer = int(227 * math.e ** 2)
print(layer)
'''
悬空长度超过3倍的木块长，需要227块​
超过10倍，需要272 400 600块，即2亿7千万之多！
每增加一块砖长度的悬空约需要的砖块数目乘以 e 的平方 = 7.389
1  4

2  31

3  227

4  1674

5  12367

6  91380

7  675214

8  4989191

9   36865412

10  272400600
'''

print(extendlenth(layer))
#print([extendlenth(layer) for layer in range(1,100)])