'''
https://brilliant.org/daily-problems/candy-graph/

solution of:
    https://brilliant.org/daily-problems/candy-graph/
'''





def fun(edge_data):
    """
    returns the score of a "longest path" for given graph
    """
    def get_node_set(edge_data):
        node_set = set()
        for cur_edge in edge_data:
            node_set.update(cur_edge[0])
        return node_set

    def input_to_hashable(cur_node, cur_edge_data):
        tmp_data = \
            tuple([(tuple(cur_edge[0]), cur_edge[1])
                   for cur_edge in cur_edge_data])
        return (cur_node, tmp_data)

    gain_data = {}

    def inner(cur_node, cur_edge_data, cur_value):
        cur_hash = input_to_hashable(cur_node, cur_edge_data)
        if cur_hash in gain_data:
            res = cur_value+gain_data[cur_hash]
        else:
            res_list = [cur_value]
            for (tmp_edge_ind, tmp_edge) in enumerate(cur_edge_data):
                cur_node_set = tmp_edge[0].copy()
                if cur_node in cur_node_set:
                    tmp_edge_data = \
                        [some_edge
                         for (some_ind, some_edge) in enumerate(cur_edge_data)
                         if some_ind != tmp_edge_ind]
                    cur_node_set.remove(cur_node)
                    new_node = cur_node_set.pop()
                    tmp_res = \
                        inner(new_node, tmp_edge_data, cur_value+tmp_edge[1])
                    res_list.append(tmp_res)
            res = max(res_list)
            gain_data[cur_hash] = res-cur_value
        return res
    return max([inner(_, edge_data, 0) for _ in get_node_set(edge_data)])


EDGE_DATA = [({0, 1}, 7), ({0, 2}, 7), ({1, 3}, 7),
             ({1, 4}, 6), ({2, 3}, 5), ({3, 4}, 8),
             ({2, 5}, 5), ({3, 6}, 4), ({4, 7}, 9),
             ({4, 6}, 10), ({5, 6}, 6), ({6, 7}, 7),
             ({5, 8}, 4), ({6, 8}, 4)]

assert len(EDGE_DATA) == 14

print(f"maximum amount of candy: {fun(EDGE_DATA)}")

#2nd solution
graph = {}
nodes = ["a b 7 c 7",
         "b a 7 d 7 e 6",
         "c a 7 d 5 f 5",
         "d b 7 c 5 e 8 g 4",
         "e b 6 d 8 g 10 h 9",
         "f c 5 g 6 i 4",
         "g d 4 f 6 e 10 h 7 i 4",
         "h e 9 g 7",
         "i f 4 g 4"]
allPossibleEdges = set()
cache = {}
maxLength = 0

# create graph
for node in nodes:
    node = node.split()
    graph[node[0]] = {"neighbours": []}
    for i in range(1, len(node)-1, 2):
        allPossibleEdges.add(tuple(sorted((node[0], node[i]))))
        graph[node[0]]["neighbours"].append((node[i], int(node[i+1])))

# dfs tracing through the graph
def tracing(node, visited, tractablePath, length):
    global maxLength
    for neighbour, distance in graph[node]["neighbours"]:
        if tuple(sorted((node, neighbour))) in visited:
            continue
        else:
            visited.add(tuple(sorted((node, neighbour))))
            length += distance
            maxLength = max(maxLength, length)
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
print(f"maximum of segments: {max(cache)} of {len(allPossibleEdges)},\ntotal length: {maxLength} pieces")

#maximum of segments: 13 of 14,
#total length: 84 pieces