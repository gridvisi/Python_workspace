
'''
https://brilliant.org/daily-problems/produce-order/

今天的挑战
你要去当地农贸市场买五样东西：鳄梨、香蕉、菜花、枣和茄子。

鳄梨和香蕉一起买比菜花和枣子便宜。
香蕉和菜花一起比红枣和茄子便宜。
菜花和红枣在一起比茄子和鳄梨便宜。
枣和茄子在一起比鳄梨和香蕉便宜。

哪种物品最便宜cheapest，哪种物品最贵most expensive？

最便宜的：茄子。最贵的：鳄梨。
最便宜的：茄子。最贵的是：枣。
最便宜的：香蕉。最贵的：椰枣。
最便宜的：香蕉。最贵的：鳄梨
不熟悉代码的同学，只运用逻辑推理即可！
四个哪一句为真？ 请提交

——————————————————————
原题中英文对照发邮箱，请同学借机会熟悉英文表达，常用的短语包括比较价格，求和等；讨论是否可以运用编程表达
原题的逻辑关系，并且运用编程解决；比较编程解决的优缺点等

附上英文原文供学习参考

Today's Challenge
You're going to the local farmers' market to buy five items: avocados, bananas,
cauliflowers, dates, and eggplants.

Avocados and bananas together are cheaper than cauliflowers and dates.
Bananas and cauliflowers together are cheaper than dates and eggplants.
Cauliflowers and dates together are cheaper than eggplants and avocados.
Dates and eggplants together are cheaper than avocados and bananas
Which item is the cheapest, and which the most expensive?

Cheapest: eggplants. Most expensive: avocados.
Cheapest: eggplants. Most expensive: dates.
Cheapest: bananas. Most expensive: dates.
Cheapest: bananas. Most expensive: avocados.

'''
stat_a = {'avocados': -1, 'bananas': -1, 'cauliflowers': 1, 'dates': 1}
stat_b = {'bananas': -1, 'cauliflowers': -1, 'dates': 1, 'eggplants': 1}
stat_c = {'cauliflowers': -1, 'dates': -1, 'eggplants': 1, 'avocados': 1}
stat_d = {'dates': -1, 'eggplants': -1, 'avocados': 1, 'bananas': 1}

from collections import Counter
from itertools import combinations
goods = ['avocados', 'bananas', 'cauliflowers', 'dates', 'eggplants']
rMinusl = dict(zip(goods,[0]*len(goods)))
state = [stat_a,stat_b,stat_c,stat_d]

ans = []
for n in range(2,len(goods)+1):
    comball = combinations(state,n)
    for d in comball:
        rMinusl = dict(zip(goods, [0] * len(goods)))
        for e in d:

            for k,v in e.items():
                rMinusl[k] += v
            s = [(k,v) for k,v in rMinusl.items() if v!=0]
            if len(s) == 2:
                ans.append(s)

print('r-l:',ans)

for c in ans:

    for d in c:
        rMinusl[d[0]] += d[1]

print('res',sorted(rMinusl.items(),key= lambda x:x[1]),rMinusl)
print('res',sorted(rMinusl.keys(),key= lambda x:x[1]),rMinusl)


strg = '''    left                  right
Avocados and bananas <  cauliflowers and dates,
Bananas and cauliflowers < dates and eggplants,
Cauliflowers and dates < eggplants and avocados,
Dates and eggplants < avocados and bananas'''

# c < e and d < a and c < a and b < d and b < e
# b < d < a


strg.replace('and',"+")
#print('replace and with +',strg)
'''

Avocados + bananas <  cauliflowers + dates.
Bananas + cauliflowers < dates and eggplants.
Cauliflowers and dates < eggplants and avocados.
Dates and eggplants < avocados and bananas

Which item is the cheapest, and which the most expensive?
'''

#prepair for the format input

s = '''
Avocados and bananas <  cauliflowers and dates,
Bananas and cauliflowers < dates and eggplants,
Cauliflowers and dates < eggplants and avocados,
Dates and eggplants < avocados and bananas
'''
#1st 以逗号split为四个字符串

s = s.split(",")
#print(s)

#2nd 小于号左右的字符串去掉空格\n,并且在and处split

lrpair = []
left,right = [],[]
for c in s:
    lrpair.append(c.strip().split(" < "))
lrpairs = [[l.strip().lower().split(" and "),r.strip().lower().split(" and ")] for l,r in lrpair]
print('lrpairs:',lrpairs)


# 算法关键步骤！！
# 嵌套for循环实现c[0]与c[1]逐一组合比较，消去<小于号左右相同的物品
# 字典实现链式比较
print("字典实现链式比较,lft < rgt --> key < value")

#3 set命令去重得到物品名单goods
from collections import Counter
from itertools import combinations
goods = ['avocados', 'bananas', 'cauliflowers', 'dates', 'eggplants']
rMinusl = dict(zip(goods,[""]*len(goods)))

print([(Counter(d[0]),Counter(d[1])) for d in lrpairs])
status_1, status_2, status_3,status_4 = [(Counter(d[0])+Counter(d[1])) for d in lrpairs]

'''Avocados and bananas <  cauliflowers and dates '''
'''Bananas and cauliflowers < dates and eggplants '''
'''Cauliflowers and dates < eggplants and avocados'''
'''Dates and eggplants < avocados and bananas'''

print(status_1)
print(status_2)
print(status_3)
print(status_4)


'''

print(list(combinations(lrpairs,2)))
for n in range(2,len(left)+1):
    for l in combinations(lrpairs,n):
        print('l',l)


#small2large = {}.fromkeys(goods)
#print('smalllarge',small2large)



for lft in lrpair:
    for rgt in lrpair:
        #if lft != rgt:
        cunt += 1
        commonlr = set(lft[0]) & set(rgt[1])
        lft[0] = [i for i in lft[0] if i not in commonlr]
        rgt[1] = [i for i in rgt[1] if i not in commonlr]
        if len(lft[0])==1 and len(rgt[1]) == 1:
            #rMinusl.append(dict(zip(lft[0],rgt[1])))
            print(lft[0],rgt[1])
            rMinusl[lft[0][0]] += rgt[1][0]+" "
print("rMinusl",cunt,len(rMinusl),rMinusl)

# 不能穷尽所有组合，不完备的
comparekv = {}
for pair in rMinusl:
    print(pair)
    for k,v in pair.items():
        small2large[k] += v+" "

print('rank:',small2large)
'''
# < 左边的单独赋值left列表
# < 右边的单独赋值给right列表


#4th
# 导入permutation
# 导入Count函数实现右边减去左边的同类物品数量
# left和right一一组合消去同类物品
result,lft,rgt = [],[],[]
for lr in lrpair:
    lft += lr[0]
    rgt += lr[1]
    result.append(set(lft)^set(rgt))
print('求异^',result)




# 其他角度
#去掉字符串左边\n和" "空格，and处split，且全部字符首字母小写

ls = []
left,right = [],[]


for c in s:
    ls.append(c.strip().split("<"))

for c in ls:
    left += [i.strip(" ") for i in c[0].lower().split("and")]
    right += [i.strip(" ") for i in c[1].lower().split("and")]
#print(left,right)



# 导入Count，统计所有小于号左边和右边，物品出现的次数

leftCunt,rightCunt = Counter(left),Counter(right)
#print(leftCunt,rightCunt)

# set命令去重得到物品名单
goods = set(left + right)
#print(goods)

# 左右同类的物品相减
minusGood = {}

for good in goods:
    minusGood[good] = rightCunt[good] - leftCunt[good]
print(minusGood)

# 由题意可知，minusGood 中键值为正的必然大于键值为负的
# 分别将键值为正，和为负的输出
positive,nagtive = [],[]
for k,v in minusGood.items():
    if v > 0: positive.append(k)
    if v < 0: nagtive.append(k)
print(positive,nagtive)

# 新增成立的比较
# 'cauliflowers' and 'bananas' < 'eggplants' and 'avocados'
'''
Avocados and bananas <  cauliflowers and dates.
Bananas and cauliflowers < dates and eggplants.
Cauliflowers and dates < eggplants and avocados.
Dates and eggplants < avocados and bananas

for c in lrpair:
    left += [i for i in c[0]]
    right += [i for i in c[1]]
goods = set(left + right)
print('goods',goods)
#for good in goods:
'''