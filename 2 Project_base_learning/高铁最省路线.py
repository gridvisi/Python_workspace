#重庆出发到其他各城市之间最省钱的路线

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


