


#key 不重合
#value 可不可以重复
#set

year = {88:"Leo finally won the oscar! Leo is happy",
        86:"Not even for Wolf of wallstreet?!",
        '<86': "When will you give Leo an Oscar?",
        '>88': "Leo got one already!"}


print(year[88])
print(year[86])
print('87',year.get(87,'not key_in'))

math = ['cathy','mike','eric']
code = ['mike','lucy','cathy']

math = ['小明',"小亮","小芳"]
code = ["电竞小王子","小芳","小明"]

for name in math:
    for nam in code:
        if name == nam:
            print(name)

print(set(math + code))

print(set(math) & set(code))



game_prince = [1,2,3,4,1,2,3]
print(set(game_prince))

cq = [23,'chongqing'] #列表
cq[0] = 28
print(cq)

cq = (23,'chongqing') #元组
#cq[0] = 28
print(cq)

cq = {23:'chongqing'} #字典
cq[23] = 'chengdu'
print(cq)
#TypeError: 'tuple' object does not support item assignment

ranklist = { 2000 : {1: ' Sara'  , 3 : 'Saj' , 2 : 'Pap' } ,
          2001 : {2: ' Sara'  , 1 : 'Saj' , 2 : 'Pap' } ,
          2002 : {3: ' Sara'  , 2 : 'Saj' , 1 : 'Pap' } ,
         }


a=[]
for year in ranklist:
    out = {i: [] for i in ranklist}
    for rank in ranklist[year] :
        if rank == 1:
            #a.append(ranklist[year][rank])
            out[year] = a.append(ranklist[year][rank])
'''
解决方案
这里有两个错误：

您每次out在外部for循环中“重置”您的内容；和
.append(..)返回None，而不是新列表。
但是，您可以将以上内容重写为：

out = { k: v.get(1) for k, v in ranklist.items() }
因此，在这里，我们为每个键值对取键，并使用键将其映射到相应字典中的值1。

或者，如果您想省略没有键的子目录，请执行以下操作1：

out = { k: v.get(1) for k, v in ranklist.items() if 1 in v }
'''

dial_codes = [
    (86,'china'),
    (91,'india'),
    (1,'United states'),
    (62,'Indonesia'),
    (55,'Brazil'),
    (92,'Pakistan'),
    (880,'Bangladesh'),
    (234,'Nigera'),
    (7,'Russia'),
    (81,'Japan'),
    (852,'hongkong')
    ]
d = dict(dial_codes) #字典
print(d.get(851,'bucunzai'))

#if stock.get(merch,)

print(d)
print(d[86])  #key:value

d2 = dict(sorted(dial_codes))
d3 = dict(sorted(dial_codes,key=lambda x:x[1]))
assert d == d2 and d2 == d3

print('d1:',d.keys())
print('d2:',d2.keys())
print('d3:',d3.keys())

print(d)

#下单的价格和库存查询

stock = {
    'football': (10,40),
    'shoes':(20,100),
    'headband':(20,100),
    'boardgame': (30,200),
    'leggos': (10,100),
    'doll': (30,50),
    'bag':0
    }

# 收到订单50个头带，库存够不够，触发最低库存警戒线，
# 如果库存里没有该商品，返回“库存没有x商品”
# 如果触发则显示“需要加订货x到达警戒线”，否则“显示库存”

def order(goods,num):
    s = f"库存没有{goods}"
    if goods not in stock: return s
    total,alert = stock.get(goods)[1],stock.get(goods)[0]

    renew = alert-total+num if total-num < alert else total-num
    return f"库存还剩{total-num}" if total-num >= alert else f"库存还剩{total-num},需要加订货{renew}到达警戒线"

goods,num = 'shoes',120
print(order(goods,num))
goods,num = 'shoes',10
print(order(goods,num))
goods,num = 'basketball',10
print(order(goods,num))

'''
任务三：两个库存的合并

你的业务势头很好，你收购了几家竞争对手。紧迫需要是将自己的库存清单和另外几家的库存清单合并。意味着相同货物的数量相加，保证合并后的库存清单包含的货物品名最全。
- 两个字典记录中相同的key如何处理？
- 相同key值对应的value相加如何操作​
- 仓库A和仓库B的货物不一样的这部分货物
- 如何解决输入多个字典且输入参数的个数不确定？
​
'''
stock_a = {
    'football': 10,
    'shoes':20,
    'headband':20,
    'boardgame': 30,
    'leggos': 10,
    'doll': 30,
    'bag':0,
    'pen':90
    }

stock_b = {
    'football': (5),
    'shoes':(7),
    'headband':(19),
    'boardgame': (20),
    'leggos': (30),
    'doll': (50),
    'bag':5,
    'T-shirt':20
    }

stock_c = {}

def combine(*stock):
    comb = {}
    for c in stock:
        for k, v in c.items():
            comb[k] = v + comb.get(k, 0)
    return comb

stock = [stock_a,stock_b,stock_c]
print(combine(*stock))


import jmespath
persons = {
    "persons": [
    { "name": "erik", "age": 38 },
    { "name": "john", "age": 45 },
    { "name": "rob", "age": 14 }
                ]
            }

print(jmespath.search('persons[*].age', persons))
#[38, 45, 14]