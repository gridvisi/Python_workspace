'''

price_dic = [[0,925,860,787,819,146,409],[925,0,553,528,939,779,516],
             [860,553,73,0,568,933,670],[787,553,73,512,0,886],
             [819, 936, 568, 512, 0, -1, 888],[146,779,933,662,-1,0,263],
            [409,516,670,654,888,263,0]]
price_dic = [(0,925,860,787,819,146,409),(925,0,553,528,939,779,516),
             (860,553,73,0,568,933,670),(787,553,73,512,662,654),
             (819, 936, 568, 512, 0, -1, 888),(146,779,933,662,-1,0,263),
             (409,516,670,654,888,263,0)]
append(哈尔滨，海口）

suz = (554 524 39 111 599 899 636,0)
'''

# 遍历各个城市到其他城市之间的票价生成“城市：票价列表”
station = ['cq','bj','sh','hz','sz','cd','xa','suz']
#station = ['cq','bj','sh','hz','sz','cd','xa']
price_dic = [(0,925,860,787,819,146,409,554),(925,0,553,528,939,779,516,542),
             (860,553,73,0,568,933,670,39),(787,558,73,0,512,662,654,111),
             (819, 936, 568, 512, 0, 10000, 888,599),(146,779,933,662,10000,0,263,899),
             (409,516,670,654,888,263,0,636),(554,524,39,111,599,899,636,0)]
'''
price_dic = [(0,925,860,787,819,146,409),(925,0,553,528,939,779,516),
             (860,553,73,0,568,933,670),(787,553,73,512,662,654),
             (819, 936, 568, 512, 0, 10000, 888),(146,779,933,662,10000,0,263),
             (409,516,670,654,888,263,0)]
'''




table = []
for i,city in enumerate(price_dic): # 出发地高铁票价表
    city_price = dict(zip(station,city))
    table.append((station[i],city_price))
print('table:',table)

num = [i for i in range(len(station))]
station_num = dict(zip(num,station))
#print(station_num)
agenda = dict(zip(station,price_dic))
print('agenda:',agenda)

# 遍历每个城市连接的城市，排除自身和不通车的连接
def graph_link(agenda):
    st_all = {}
    for key in agenda.keys():
        st = []
        #print('K:',key,st_all[key])
        for i,v in enumerate(agenda[key]):
            if v != 0 and v != -1:
                st.append(station_num[i])
        st_all[key] = tuple(st)
    return st_all
print('graph_link:',graph_link(agenda))


# 输入起始到达站，遍历start to end之间所有开通高铁的线路
start = str(input('起始站:'))
end = str(input('到达站:'))
graph = graph_link(agenda)

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                if len(newpath)==len(graph):
                    paths.append(newpath)
    return paths
print(find_all_paths(graph, start, end, path=[]))

print(start,end)
map = graph_link(agenda)
print('map:',map)
print('agenda:',agenda)

def price_sheet(start,end):
    for i in table:
        if i[0] == start:
            for k,v in i[1].items():
                if k == end:
                    return i[1][k]
print(start,"到",end,'的票价是:',price_sheet(start,end))

def cost_path(start,end):
    sub_total,sub,cost =[],[],0
    all_path = find_all_paths(graph, start, end, path=[])

    for path in all_path:
        cost = 0
        for i in range(len(path)-1):
            cost += price_sheet(path[i],path[i+1])
        sub.append((cost,path))
    return min(sub)  #len(sub),min(sub),max(sub)

print(cost_path(start,end))

price_sheet(start,end)


start = str(input('起始站:'))
#end = str(input('到达站:'))
def start_end(start):
    #station = ['cq', 'bj', 'sh', 'hz', 'sz', 'cd', 'xa']
    res,cal,loop = [],[],[]
    end_lst = [x for x in station if x != start]
    for i,end in enumerate(end_lst):
        res.append(cost_path(start, end))
        s = price_sheet(start,end)
        x = res[i][1]
        x.append(start)
        re = s + res[i][0]
        cal.append((re,x))
    return min(cal) #cal,len(cal),

print(start_end(start))

'''
s = lambda x,y:x+y,(c[0] for c in res),(nd for nd in end_lst)

temp = ['cq', 'sh', 'sz', 'hz', 'cd', 'xa', 'bj']
cost,route = 0,[]
for i in range(len(temp)-1):
    st,nd = temp[i],temp[i+1]
    cost += price_sheet(st,nd)
    route.append((cost,temp))
print(st,'to',nd,price_sheet(st,nd),cost)


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]

#if len(newpath)==len(agenda):    # 走过的面达到20时递归终止
#    paths.append(newpath)

#newpaths = find_all_paths(agenda, node, end, path)
#for newpath in newpaths:
#  if len(newpath)==len(agenda):
#      paths.append(newpath)

#set=[]
#for i in agenda[1]:
#    set.append(find_all_paths(agenda, 1, i))
#print(set)
#print(len([j for i in set for j in i]))

#Constructing Hamiltonian paths between two points两点之间建立

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                if len(newpath)==len(graph):
                    paths.append(newpath)
    return paths

set=[]
start = 'cq'
graph = agenda
print(agenda[start])
for i in agenda['cq']:
    set.append(find_all_paths(agenda, 'cq', 'bj',path=[]))
    print(set,len([j for i in set for j in i]))
'''

