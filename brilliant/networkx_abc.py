'''
https://zhuanlan.zhihu.com/p/104008807
'''

import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_node('a')
G.add_node_from(['b','c','d','e'])
nx.draw(G,with_labels=True)
plt.show()