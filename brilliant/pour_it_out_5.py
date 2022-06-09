#https://brilliant.org/daily-problems/pour-it-out-5/

import networkx as x
# each function generates nodes and costs
def pour_a_to_b(a, b, max_b):
    final = min(max_b, a + b)
    poured = final - b
    yield (a - poured, b + poured)

def pours(a, b, maxes):
    l, r = pour_a_to_b(a, b, maxes[1])
    yield (l, r, 0)
    r, l = pour_a_to_b(b, a, maxes[0])
    yield (l, r, 0)

def dump(a, b, maxes):
    yield from [(0, b, a), (a, 0, b)]

def fill(a, b, maxes):
    yield from [(a, maxes[1], 0), (maxes[0], b, 0)]

# define the buckets
maxes = [7, 4]

# make the graph
to_open = [(0, 0)]
G = nx.DiGraph()
for a, b in to_open:
    for f in [pours, dump, fill]:
        for a2, b2, wt in f(a, b, maxes):
            if (a2, b2) not in to_open:
                to_open.append((a2, b2))
            G.add_edge((a, b), (a2, b2), weight=wt)

# find the the lowest cost paths
for t in [node for node in G if 2 in node]:
    c = nx.shortest_path_length(G, (0,0), t, weight='weight')
    print(t, c)