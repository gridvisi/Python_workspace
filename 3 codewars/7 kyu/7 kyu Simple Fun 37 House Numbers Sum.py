'''
https://www.codewars.com/kata/simple-fun-number-37-house-numbers-sum/train/python
一个男孩从学校走到他家很远。为了使散步更有趣，他决定把散步时经过的所有房子的数目加起来。不幸的是，并不是所有
的房子都有数字写在上面，除此之外，男孩还经常轮流换街，所以这些数字在他看来没有任何特殊的顺序。
在散步的某个时候，男孩遇到了一栋写着0的房子，这让他非常吃惊，以至于他在看到房子后就停止在总数上加数字。
对于给定的房屋序列，确定男孩将得到的金额。保证路上至少有一栋0号楼。
'''
# return 的缩进不同，得到的答案也不同
def house_numbers_sum(inp):
    for i,e in enumerate(inp):
        if e == 0:
            end = i
            return sum(inp[:end+1])

def house_numbers_sum(inp):
    return sum(inp[:inp.index(0)])
inp = [0, 1, 2, 3, 4, 5]
inp = [4, 1, 2, 3, 0, 10, 2]
#inp = [5, 1, 2, 3, 0, 1, 5, 0, 2]
print(house_numbers_sum(inp))