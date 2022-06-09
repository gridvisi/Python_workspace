__author__ = 'Administrator'
from life import LifeGrid

# 网格大小
GRID_WIDTH = int(input("Please enter a positive integer as width: "))
GRID_HEIGHT = int(input("Please enter a positive integer as height: "))

# 初始状态
INIT_CONFIG = [(0, 0), (0, 1), (1, 0), (1, 2), (3, 2), (3, 4), (5, 4), (5, 6), (7, 6), (7, 8), (9, 8), (9, 10), (11, 10), (11, 12), (12, 11), (12, 12)]

# 世代数
NUM_GENS = int(input("Please enter a positive integer as generation: "))

# 产生下一代的生命
def evolve(grid):
    # 储存下一代活细胞的列表
    liveCells = list()

    # 遍历整个网格
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            # 读取周围活细胞数
            neighbors = grid.numLiveNeighbors(i, j)

            # 如果该坐标有活细胞，并且周围活细胞数是2或3，将该坐标加入到下一代活细胞的列表
            if (neighbors == 2 and grid.isLiveCell(i, j)) or (neighbors == 3):
                liveCells.append((i, j))

    # 使用下一代活细胞的列表去初始化网格
    grid.configure(liveCells)

# 打印一个基于文本表示的生命游戏
def draw(grid):
    for i in range(grid.numRows()):
        string = ''
        for j in range(grid.numCols()):
            if grid.isLiveCell(i, j):
                string += '@  '
            else:
                string += '.  '
        print (string)
    print ('\n')

def main():
    # 构建游戏网格，并初始化
    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    # 游戏开始
    draw(grid)
    # for i in INIT_CONFIG:
        # print grid.numLiveNeighbors(*i)
    for i in range(NUM_GENS):
        evolve(grid)
        draw(grid)

if __name__ == "__main__":
    main()

from myarray2d import Array2D

class LifeGrid(object):
    # 定义代表细胞状态的常量
    DEAD_CELL = 0
    LIVE_CELL = 1

    # 创建游戏网格实例，并将所有细胞设定为死细胞状态
    def __init__(self, numRows, numCols):
        # 创建网格实例
        self._grid = Array2D(numRows, numCols)
        # 将所有细胞设定为死细胞状态
        self.configure(list())

    def numRows(self):
        return self._grid.numRows()

    def numCols(self):
        return self._grid.numCols()

    # 将给定网格坐标的细胞设为活细胞，网格坐标由列表传入
    def configure(self, coordList):
        # 先将所有网格中的细胞设为死细胞
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)

        # 再将给定网格坐标的细胞设为活细胞
        for coord in coordList:
            self.setCell(coord[0], coord[1])