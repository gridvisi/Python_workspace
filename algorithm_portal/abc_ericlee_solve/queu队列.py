#https://blog.csdn.net/weixin_43533825/article/details/89155648

from collections import deque

graph = {'john': ['bm', 'am'], 'bm': [], 'am': []}
name = 'john'
search_queue = deque()
search_queue += graph[name]
print(search_queue)
searched,res = [],[]


def search(grahp,craver,res=[]):
    search_queue = deque()
    search_queue += graph[craver]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if 'm' in person:
                res.append(person)
                print('res',res)
                return search(graph,person,res)
            else:
                search_queue += graph[person]
                searched.append(person)
        return res

graph = {'john': ['bm', 'am'], 'am': [], 'bm': []}
relations,craver = [('john', 'bm'), ('john', 'am')] , 'john'
#relations,craver = [('john', 'adam'), ('john', 'zach'), ('zach', 'bob')], 'adam'
print(search(graph,craver))