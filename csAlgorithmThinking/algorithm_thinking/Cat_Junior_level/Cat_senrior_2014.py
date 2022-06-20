
'''
Cat_senior_2014 Board game
安娜和布雷特正在玩一个游戏，一个计数器沿着一个有数字的棋盘移动。
安娜首先把计数器放在最左边的两个数字上。然后玩家轮流移动，将柜
台向右移动一到两个地方。将计数器放在一个数字上可以使玩家获得这
个分数。获胜的优势是（获胜者的分数）−（失败者的分数）。这个游
戏的目的是获得尽可能大的获胜优势。如果双方都打得尽可能好，安娜
的胜优势是多少？
'''
board = [5,3,5,4,4,3,2]
# 递推思想
# 最后一步到达数组最右边，有 2 种走法：
# board[-2]->board[-1],board[-3]->board[-1]
# 以此类推，直到起点 board[0],数组 score[(i,j)]记录沿途两人的积分i,j
# 初始化 score
'''
#1 score[0] = [5,0] # 因为先手占据 5分，后手不能再占据board[0]
#2 score[1] = [5,-3] # 先手占 5，后手占 3
#3 score[2] = max(path_1,path_2) 
#                 path_1 = i 由 board[i-1]->board[2] i=先手 
                  path_2 = j 由 board[i-1]->board[2] j=后手

score[-1] = max(score[-2],score[-3])
sum(score[1]=0 - 5, 此时后手不选择#2，跳过#2选 board[2]

'''

l = len(board)
sub = 0
i,j = 2,2
score_a = [0]*l
score_b = [0]*l
score_a[0] = board[0]
print(score_a)
score_b[1] = board[1]
print(score_b)
while i < l and j < l:
    buff = [1,2]
    for i,c in enumerate(board,2):

        # 3tr.Step: score[2] = max(path_1,path_2)
        # path_1 = i board[i-1]->board[2] i=先手
        # path_2 = j board[i-1]->board[2] j = 后手

        a = score_a[i-1] + board[i] - score_b[i-1]
        b = score_b[i-2] + board[i]
       '''
        score[i][1] = score[i-2][1] - board[i]
        path_1 = score[i][0] + sum(score[i-1])
        path_2 = score[i]
            c[0] = max([path_i,path_j])
            print(score)

       '''
# 股票的5种涨跌状态
'''
场景设置如时间序列的股票价格波动，
可以参考下面的5种分类：
1、无序，有增有减
2、严格递增，一直升高
3、没有递减，存在价格不变的情况
4、严格递减，一直减少
5、保持不变
'''
TYPE_SEQ = {(1,): 1, (0,1): 2, (-1,):3, (-1,0): 4, (0,): 5}

def sequence_classifier(arr):
    countSet = { (a<b) - (a>b) for a,b in zip(arr, arr[1:]) }
    return TYPE_SEQ.get(tuple(sorted(countSet)), 0)
