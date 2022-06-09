__author__ = 'Administrator'
import numpy as np

ini_matrix = [
          [0, 1, 1, 0, 1],
          [1, 0, 0, 1, 0],
          [1, 0, 0, 0, 1],
          [0, 1, 0, 0, 0],
          [1, 0, 1, 0, 0]
         ]


def bfs(matrix_para, start_point_para, end_point_para):
    """
    广度优先搜索
    :param matrix_para 图
    :param start_point_para 起点
    :param end_point_para 终点
    :return: 返回关联度
    """
    matrix = matrix_para
    start_point = start_point_para
    end_point = end_point_para

    vertex_num = len(matrix) # 顶点个数

    que = np.zeros(vertex_num, dtype=np.int) # 队列， 用于存储遍历过的顶点
    book = np.zeros(vertex_num, dtype=np.int) # 标记顶点i是否已经被访问，1表被访问，0表未被访问

    point_step_dict = dict() # key:点，value:起点到该点的步长

    # 队列初始化
    head = 0
    tail = 0

    # 从起点出发，将起点加入队列
    que[tail] = start_point # 等号右边为顶点号（起点）
    tail += 1
    book[start_point] = 1 # book[i] i为顶点号

    while head<tail:
        cur = que[head]
        for i in range(vertex_num):
            # 判断从顶点cur到顶点i是否有边，并判断顶点i是否已经被访问过
            if matrix[cur][i] == 1 and book[i] == 0:
                que[tail] = i # 将顶点i放入队列中
                tail += 1 # tail指针往后移
                book[i] = 1 # 标记顶点i为已经访问过
                point_step_dict[i] = head + 1 # 记录步长
            if tail == vertex_num: # 说明所有顶点都被访问过
                break
        head += 1

    for i in range(tail):
        print(que[i])

    try:
        relevancy = point_step_dict[end_point]
        return relevancy
    except KeyError: # 捕获错误，如果起点不能到达end_point，则字典里没有这个键，返回None
        return None

result = bfs(ini_matrix, 1, 4)
print("result:", result)