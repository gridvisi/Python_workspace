__author__ = 'Administrator'
'''

想要统计dict中key为“参”时，values的第三个元素进行求和，
开始的时候一直报整型不能迭代的错误。后来先将第三个元素记录在列表中，导入functools中的reduce方法，
能将列表中的元素进行迭代相加
'''

adjacencies = {
1 : [7, 13, 19], 2 : [12, 18, 20], 3 : [16, 17, 19], 4 : [11, 14, 18],
5 : [13, 15, 18], 6 : [9, 14, 16], 7 : [1, 15, 17], 8 : [10, 16, 20],
9 : [6, 11, 19], 10 : [8, 12, 17], 11 : [4, 9, 13], 12 : [2, 10, 15],
13 : [1, 5, 11], 14 : [4, 6, 20], 15 : [5, 7, 12], 16 : [3, 6, 8],
17 : [3, 7, 10], 18 : [2, 4, 5], 19 : [1, 3, 9], 20 : [2, 8, 14]
}
'''
key = []
for i in range(1,21):
    key.append(i)
print(key)
print(adjacencies[1][0])

def routemapping(key,route):
    global adjacencies

    for key in adjacencies.keys():
        print(key)
    #key_remove = [i for i in key if i != key]
    #for j in (adjacencies[k][0],adjacencies[k][1],adjacencies[k][2]):
        route = adjacencies[key]
        route.pop(1)
        i = adjacencies[key][1]
        route.append(i)
        i = adjacencies[key][2]
        route.append(i)
        return routemapping(i,route)

#global adjacencies
adjacencies = {
1 : [7, 13, 19], 2 : [12, 18, 20], 3 : [16, 17, 19], 4 : [11, 14, 18],
5 : [13, 15, 18], 6 : [9, 14, 16], 7 : [1, 15, 17], 8 : [10, 16, 20],
9 : [6, 11, 19], 10 : [8, 12, 17], 11 : [4, 9, 13], 12 : [2, 10, 15],
13 : [1, 5, 11], 14 : [4, 6, 20], 15 : [5, 7, 12], 16 : [3, 6, 8],
17 : [3, 7, 10], 18 : [2, 4, 5], 19 : [1, 3, 9], 20 : [2, 8, 14]
}

print(routemapping(1,[7, 13, 19]))
'''
adjacencies = {
1 : [7, 13, 19], 2 : [12, 18, 20], 3 : [16, 17, 19], 4 : [11, 14, 18],
5 : [13, 15, 18], 6 : [9, 14, 16], 7 : [1, 15, 17], 8 : [10, 16, 20],
9 : [6, 11, 19], 10 : [8, 12, 17], 11 : [4, 9, 13], 12 : [2, 10, 15],
13 : [1, 5, 11], 14 : [4, 6, 20], 15 : [5, 7, 12], 16 : [3, 6, 8],
17 : [3, 7, 10], 18 : [2, 4, 5], 19 : [1, 3, 9], 20 : [2, 8, 14]
}

#Constructing Hamiltonian paths between two points
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
for i in adjacencies[1]:
    set.append(find_all_paths(adjacencies, 1, i))
print(len(set),set)
print(len([j for i in set for j in i]))