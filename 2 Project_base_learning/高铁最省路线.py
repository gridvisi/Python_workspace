#重庆出发到其他各城市之间最省钱的路线
# 遍历各个城市到其他城市之间的票价生成“城市：票价列表”
station = ['cq','bj','sh','hz','sz','cd','xa','suz']
#station = ['cq','bj','sh','hz','sz','cd','xa']
price_dic = [(0,925,860,787,819,146,409,554),(925,0,553,528,939,779,516,542),
             (860,553,73,0,568,933,670,39),(787,558,73,0,512,662,654,111),
             (819, 936, 568, 512, 0, 10000, 888,599),(146,779,933,662,10000,0,263,899),
             (409,516,670,654,888,263,0,636),(554,524,39,111,599,899,636,0)]


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
def cost_path(start,end):
   sub_total,sub,cost =[],[],0
   all_path = find_all_paths(graph, start, end, path=[])
   for path in all_path:
       cost = 0
       for i in range(len(path)-1):
           cost += price_sheet(path[i],path[i+1])
       sub.append((cost,path))
   return min(sub)

#各个城市直达重庆的高铁票价
def price_sheet(start,end):
    for i in table:
        if i[0] == start:
            for k,v in i[1].items():
                if k == end:
                    return i[1][k]

#递归遍历的子程序

def start_end(start):
    station = ['cq', 'bj', 'sh', 'hz', 'sz', 'cd', 'xa', 'suz']
    res,cal,loop,end_lst = [],[],[],[x for x in station if x != start]
    for i,end in enumerate(end_lst):
        res.append(cost_path(start, end))
        s = price_sheet(start,end)
        x = res[i][1]
        x.append(start)
        re = s + res[i][0]
    cal.append((re,x))
    return min(cal) #cal,len(cal)

print(start,"到",end,'的票价是:')


