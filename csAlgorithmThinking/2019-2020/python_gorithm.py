from pygorithm.pathing import dijkstra

# import a graph data structure
from pygorithm.data_structures import graph

# initialize the graph with nodes from (0, 0) to (4, 4)
# with weight corresponding to distance (orthogonal
# is 1, diagonal is sqrt(2))
my_graph = graph.WeightedUndirectedGraph()
my_graph.gridify(5, 1)

# make the graph more interesting by removing along the
# x=2 column except for (2,4)
my_graph.remove_edge((2, 0))
my_graph.remove_edge((2, 1))
my_graph.remove_edge((2, 2))
my_graph.remove_edge((2, 3))

# calculate a path
my_path = dijkstra.find_path(my_graph, (0, 0), (3, 0))

# print path
print(' -> '.join(my_path))