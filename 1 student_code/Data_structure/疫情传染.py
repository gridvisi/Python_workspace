
# limin是最早发现发热的，有三名同学接触过的人群记录
limin =  ['yangyi' ,'lisi','zhangsan','wangwu','zhaoliu']
wangwu = ['maba','niushi','limin']
liangzi = ['yanglan','jiangjun','kongzi']

# 首先左边的人作为 key， 右边的列表作为 value
mapConnect = {
              'limin': ['lisi','zhangsan','zhaoliu'],
              'wangwu': ['maba','niushi','limin'],
              'lisi':['yanglan','jiangjun','kongzi'],
              'kongzi' : ['liangyi','hulu','lisi']
              }

source = "limin"
touch = {}
nonctouch = {}
for k,v in mapConnect.items():
    if k == source:
        for person in mapConnect[k]:
            if person in mapConnect.keys():
                print(person)
                touch[person] = "" #mapConnect.get(person,"None")
            else:
                #if person

                nonctouch[person] = ""   #.get(person,"没有接触！")

print('limin 接触过的人：',touch)
print('limin 没有接触过的人：',nonctouch)


#Pycharm
rmb = 10   #
candy = 3  #
print(rmb / candy)
print(rmb//candy , rmb % candy) #取整，取余



rmb = 10  #有多少钱？
wrappers = 0 #
eaten = 0 #
price = 3 #
while rmb > 0: #10->9->8->7
    rmb -= price  # 价格
    eaten += 1 # 吃掉的增加了一个
    wrappers += 1 # 糖纸增加一个

    if wrappers == 2:
        wrappers -= 2
        eaten += 1
        wrappers += 1
print("Answer:", eaten) #改成 最终吃掉的糖