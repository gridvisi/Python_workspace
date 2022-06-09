# https://brilliant.org/daily-problems/bark-genetics/

'''
编程解决依然是丁丁猫coder的必选操作，呵呵​哒
如何表示显性基因和隐性基因​？
如何表示基因组合的逻辑？
如何编程实现基因组合的​算法？


假设​：
显性为 1，隐性为0，逻辑采取 + 操作，会有下列组合结果
1 or  1 == 1 or  0 == 0  or  1 == 1
0 or  0 == 0​
'''

def barkGenetics(x,y):
    return x or y

# 大声吠叫是显性表达，吠叫的狗一定含有一个或两个显性基因，但绝不会含有两个安静基因
# 吠叫表达为Q, 安静表达为q，那么吠叫的狗只会有两种组合 QQ和Qq
# 那么，与另一只全部是qq基因的狗繁殖下一代
# Q = 1, q = 0
bark = ['11','10']
quite = '00'

ans = []
for i in bark:
    for x in i:
        for y in quite:
            ans.append(barkGenetics(x,y))
print(ans)
