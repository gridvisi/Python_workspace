
cq = ['hotpot','rabbit','noodle']
cd = ['hotpot','rabbit','chuanchuan']
#menu = [item for item in cq for in cd]
ans = []
for item in cq:
    for j in cd:
        print(item,j)
        if item == j:
            ans.append(item)
print(ans)

#key 不重合
#value 可不可以重复
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

stock = {
    'football': 4,
    'boardgame': 10,
    'leggos': 1,
    'doll': 5,
}


