'''
https://www.codewars.com/kata/5e0a089cd77216002314bfb6/train/python
'''




#1st
def mango_friends(relations, craver):
    relations = [(a, b) for x, y in relations for a, b in [(x, y), (y, x)]]
    edges = [craver]
    seen = {craver}
    result = []
    while edges:
        new_edges = []
        for e in edges:
            for a, b in relations:
                if a == e and b not in seen:
                    new_edges.append(b)
                    seen.add(b)
                    if 'm' in b:
                        result.append(b)
        edges = new_edges
    return result

relations,caver = [('john', 'abid'), ('john', 'zach'),
     ('zach', 'bob'), ('mary', 'susan'),
     ('adam', 'mary'), ('tom', 'susan')],  'john'

relations,craver = [('john', 'adam'),
 ('john', 'zach'),
 ('zach', 'bob'),
 ('mary', 'susan'),
 ('adam', 'mary')], 'john'
print('result',mango_friends(relations, craver))

#3rd
from collections import defaultdict, deque

def mango_friends(relations, craver):
    es = defaultdict(list)
    for x, y in relations:
        es[x].append(y)
        es[y].append(x)
    res = []
    q = deque([craver])
    while q:
        x = q.popleft()
        if 'm' in x and x != craver:
            res.append(x)
        q.extend(y for y in es[x] if y in es)
        del es[x]
    return res


#print(len(relations))

craver = 'john'
root = 'mary'
from collections import deque
def infect(relations,root):
    inf,visited,res = [],deque([root]),[]
    while len(visited) != 0:
        root = visited.popleft()
        #print(root)
        for group in relations:
            for person in group:
                #print(person)
                if person == root:
                    relations.remove(group)
                    #print(relations)
                    visited += deque(group)
                    inf += group
    return inf
#https://blog.51cto.com/yishi/2117743
print(f'{root}'+ ' infect: ',infect(relations,root))

def infect_net(relations,root):
    inf_list,visited = [],infect(relations,root)
    print(visited)
    for person in visited:
        inf_list += infect(relations,root)
    return inf_list
print(f'{root}'+ ' infect ',infect_net(relations,root))

#graph = {'john': ['bm', 'am'], 'bm': [], 'am': []}
#print('search',search(graph,'john'))
#relations = [('john', 'adam'), ('john', 'zach'), ('zach', 'bob'), ('mary', 'susan'), ('adam', 'mary')]
#k.append(p[0])
#    v.append(p[1:])  # {'john': 'adam', 'zach': 'bob', 'mary': 'susan', 'adam': 'mary'}

k, v = [], []
res = {}

for i,e in enumerate(relations):
    #print(i)
    if e[0] not in k:
        k.append(e[0])
    else:pass
key = [i[0] for i in relations if i[0] not in k]
print('key:',key)

# relations = [('john', 'bm'), ('john', 'am')]

relations = [ [ 'zyq', 'adq' ],
    [ 'izum', 'eiv' ],
    [ 'tzapcqzgm', 'oxbxufhdm' ],
    [ 'nmckljgk', 'tuj' ],
    [ 'scuqsbxvm', 'nmckljgk' ],
    [ 'jtfm', 'zbkydhglm' ],
    [ 'auavflvcm', 'alnufednm' ],
    [ 'xvkm', 'qxpqqzagm' ],
    [ 'jtfm', 'pcazizcgm' ],
    [ 'gvim', 'pcazizcgm' ],
    [ 'eiv', 'kzgm' ],
    [ 'auavflvcm', 'scuqsbxvm' ],
    [ 'pyom', 'adq' ],
    [ 'rxzm', 'vwom' ],
    [ 'dxz', 'ydtm' ],
    [ 'wlum', 'nwqnyynfm' ],
    [ 'zbkydhglm', 'auavflvcm' ],
    [ 'oxbxufhdm', 'auavflvcm' ] ]

craver = 'nmckljgk'

#    ['scuqsbxvm', 'auavflvcm', 'alnufednm', 'zbkydhglm',
#     'oxbxufhdm', 'jtfm', 'tzapcqzgm', 'pcazizcgm', 'gvim'])

relations = [('john', 'abid'), ('john', 'zach'),
     ('zach', 'bob'), ('mary', 'susan'),
     ('adam', 'mary'), ('tom', 'susan'),('susan','adam')]
craver = 'tom'

relations = [('john', 'bm'), ('john', 'am')]
craver = 'john'
#['bm', 'am'])

relations = [('john', 'abid'), ('john', 'zach'), ('zach', 'bob'), ('mary', 'susan'), ('adam', 'mary'), ('tom', 'susan')]
#print(len(relations))

craver = 'john'


print(mango_friends(relations, craver))

'''
def mango_friends(relations, craver):
    k, v = [], []
    for p in relations:
        k.append(p[0])
        v.append(p[1])  # {'john': 'adam', 'zach': 'bob', 'mary': 'susan', 'adam': 'mary'}
    no_child = set(k + v) - set(k)
    print('no_child:',no_child)

    graph = {}
    for person in relations:
        if person[0] not in graph:
            graph[person[0]] = [i for i in person[1:]]
        else:
            graph[person[0]].append(person[1])

    for c in no_child:
        graph.update({c: []})
    print('graph:',graph)
    return mango_friends(graph,craver)
relations,craver = [('john', 'adam'), ('john', 'zach'), ('zach', 'bob')], 'adam'
relations,craver = [('john', 'bm'), ('john', 'am')] , 'john'
print('mango:',mango_friends(relations, craver))

'''



relations = [('john', 'abid','elbert'),
             ('oliver','john', 'zach'),
             ('alyssa','zach', 'bob'),
             ('mary', 'susan'),
             ('alex', 'jason','lucas','luke','bashar'),
             ('allison','adam', 'mary'),
             ('bashar','tom', 'susan')]
from collections import deque
graph, res = {}, []

def res_to_graph(relations):
    for person in relations:
        if person[0] not in graph:
            graph[person[0]] = [i for i in person[1:]]
        else:
            graph[person[0]].append(person[1])
    return graph
print('graph:',res_to_graph(relations))

def search(graph,craver):
    searched,res = [],[],
    search_queue = deque()
    if craver in graph:
        search_queue += graph[craver]

    while search_queue:
        person = search_queue.popleft()
        if 'm' in person:res.append(person)
        if person in graph:
            for person in graph[person]:
                print(person)
                if 'm' in person:
                    print('2 ',person)
                    if person not in res:
                        res.append(person)
                        print(res)
                        search_queue += graph[person]
                else:
                    search_queue += graph[person]
                    print(search_queue)
        else:return res

def mango_friends(relations, craver):
    graph = res_to_graph(relations)
    print(graph)
    return search(graph, craver)
print('Graph:',mango_friends(relations,craver))