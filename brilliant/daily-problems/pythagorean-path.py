'''
https://brilliant.org/daily-problems/pythagorean-path/
'''

from math import sqrt

solutions = ("48", "41 + sqrt(32) + sqrt(50)", "41 + sqrt(18) + sqrt(32) + sqrt(50)",
             "45 + sqrt(32) + sqrt(50)", "48 + sqrt(18) + sqrt(32) + sqrt(50)")

# representig the shape as a graph with nodes and edges
graph = {}
nodes = ["a b 3 i 3 h sqrt(18)",
         "b a 3 c 4 e 4 h 3 d sqrt(32)",
         "c b 4 d 4",
         "d c 4 e 4 b sqrt(32)",
         "e d 4 b 4 h 5 f 5 g sqrt(50)",
         "f e 5 g 5",
         "g f 5 h 5 sqrt(50)",
         "h g 5 e 5 b 3 i 3 a sqrt(18)",
         "i a 3 h 3"]
allPossibleEdges = set()
cache = {}

# create graph
for node in nodes:
    node = node.split()
    graph[node[0]] = {"neighbours": []}
    for i in range(1, len(node)-1, 2):
        allPossibleEdges.add(tuple(sorted((node[0], node[i]))))
        graph[node[0]]["neighbours"].append((node[i], eval(node[i+1])))

# dfs tracing through the graph
def tracing(node, visited, tractablePath, length):
    for neighbour, distance in graph[node]["neighbours"]:
        if tuple(sorted((node, neighbour))) in visited:
            continue
        else:
            visited.add(tuple(sorted((node, neighbour))))
            length += distance
            tractablePath += 1
            tracing(neighbour, visited, tractablePath, length)
            visited.remove(tuple(sorted((node, neighbour))))
            if tractablePath not in cache:
                cache[tractablePath] = length
            else:
                cache[tractablePath] = max(cache[tractablePath], length)
            length -= distance
            tractablePath -= 1

# each node as starting point
for node in graph:
    tracing(node, set(), 0, 0)

# print solution
print(f"maximum of segments: {max(cache)} of {len(allPossibleEdges)},\ntotal length: {cache[max(cache)]} = ")
for v in cache.values():
    for i, s in enumerate(solutions):
        if eval(s) == v:
            print(f"{solutions[i]}")