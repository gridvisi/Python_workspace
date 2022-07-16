'''
无向图中的汉密尔顿路径是一条对每个顶点都精确访问一次的路径。
哈密顿循环（或哈密顿回路）是一条哈密顿路径，在图中有一条边
（从最后一个顶点到哈密顿路径的第一个顶点）。判断一个给定的
图形是否包含哈密尔顿循环。如果包含，则打印出该路径。以下是所需函数的输入和输出。
输入。
一个二维数组graph[V][V]，其中V是图中顶点的数量，graph[V][V]
是图的邻接矩阵表示。如果有一条从i到j的直接边，graph[i][j]
的值就是1，否则graph[i][j]
就是0。
输出。
一个数组path[V]，它应该包含哈密尔顿路径。path[i]
应该代表哈密尔顿路径中的第i个顶点。如果图中没有汉密尔顿循环，代码还应该返回false。
例如，以下图形中的汉密尔顿循环是
{0, 1, 2, 4, 3, 0}。

(0) - -(1) - -(2)
| /  \ |
| /  \ |
| /  \ |
(3) - ------(4)
而下面的图形不包含任何哈密尔顿循环。

(0) - -(1) - -(2)
| /  \ |
| /  \ |
| /  \ |
(3)(4)
建议。请先在
"PRACTICE "
上解决这个问题，然后再继续解决。
天真算法
生成所有可能的顶点配置，并打印一个满足给定约束条件的配置。将会有n个！（n个因子）的配置。

当有未尝试的冲突时
{
    产生下一个配置
如果（这个配置的两个连续顶点之间有边
配置的两个连续顶点之间有边，并且有一条边从最后一个顶点到
的边）。
{
    打印此配置。
破解。
}
}
回溯算法
创建一个空的路径数组，将顶点0添加到其中。添加其他顶点，从顶点1开始。
在添加一个顶点之前，检查该顶点是否与之前添加的顶点相邻，是否已经添加。
如果我们找到这样的顶点，我们就把这个顶点作为解决方案的一部分加入。
如果我们没有找到顶点，我们就返回false。

逆向追踪解决方案的实现
以下是回溯解决方法的实现。

'''


# Python program for solution of
# hamiltonian cycle problem

class Graph():
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.V = vertices

    ''' Check if this vertex is an adjacent vertex
        of the previously added vertex and is not
        included in the path earlier '''

    def isSafe(self, v, pos, path):
        # Check if current vertex and last vertex
        # in path are adjacent
        if self.graph[path[pos - 1]][v] == 0:
            return False

        # Check if current vertex not already in path
        for vertex in path:
            if vertex == v:
                return False

        return True

    # A recursive utility function to solve
    # hamiltonian cycle problem
    def hamCycleUtil(self, path, pos):

        # base case: if all vertices are
        # included in the path
        if pos == self.V:
            # Last vertex must be adjacent to the
            # first vertex in path to make a cycle
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        # Try different vertices as a next candidate
        # in Hamiltonian Cycle. We don't try for 0 as
        # we included 0 as starting point in hamCycle()
        for v in range(1, self.V):

            if self.isSafe(v, pos, path) == True:

                path[pos] = v

                if self.hamCycleUtil(path, pos + 1) == True:
                    return True

                # Remove current vertex if it doesn't
                # lead to a solution
                path[pos] = -1

        return False

    def hamCycle(self):
        path = [-1] * self.V

        ''' Let us put vertex 0 as the first vertex
            in the path. If there is a Hamiltonian Cycle,
            then the path can be started from any point
            of the cycle as the graph is undirected '''
        path[0] = 0

        if self.hamCycleUtil(path, 1) == False:
            print("Solution does not exist\n")
            return False

        self.printSolution(path)
        return True

    def printSolution(self, path):
        print("Solution Exists: Following",
              "is one Hamiltonian Cycle")
        for vertex in path:
            print(vertex, end=" ")
        print(path[0], "\n")


# Driver Code

''' Let us create the following graph
    (0)--(1)--(2)
    | / \ |
    | / \ |
    | /     \ |
    (3)-------(4) '''
g1 = Graph(5)
g1.graph = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1, ], [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0], ]

# Print the solution
g1.hamCycle();

''' Let us create the following graph
    (0)--(1)--(2)
    | / \ |
    | / \ |
    | /     \ |
    (3)     (4) '''
g2 = Graph(5)
g2.graph = [[0, 1, 0, 1, 0],
            [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0], ]

# Print the solution
g2.hamCycle()

# This code is contributed by Divyanshu Mehta
g2.graph = [[]]
graph = {'A': set(['B', 'C', 'D']),
         'B': set(['A', 'C', 'J']),
         'C': set(['A','B', 'D', 'E','F']),
         'D': set(['A', 'C', 'F']),
         'E': set(['C', 'G', 'H']),
         'F': set(['D', 'G']),
         'G': set(['E', 'F', 'H']),
         'H': set(['E', 'G', 'J']),
         'J': set(['B', 'H'])}

print(graph['A'])



#高铁
# 遍历各个城市到其他城市之间的票价生成“城市：票价列表”
station = ['cq','bj','sh','hz','sz','cd','xa','suz']
#station = ['cq','bj','sh','hz','sz','cd','xa']
price_dic = [(0,925,860,787,819,146,409,554),(925,0,553,528,939,779,516,542),
             (860,553,73,0,568,933,670,39),(787,558,73,0,512,662,654,111),
             (819, 936, 568, 512, 0, 10000, 888,599),(146,779,933,662,10000,0,263,899),
             (409,516,670,654,888,263,0,636),(554,524,39,111,599,899,636,0)]

