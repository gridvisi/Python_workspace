import random

n = int(input('请输入马匹数：'))
tj = []  # 创建集合收集马匹速度
qw = []
reward = 0
for i in range(0, n):
    tj.append(random.randint(0, 100))
    qw.append(random.randint(0, 100))

tj = sorted(tj)  # 升序排序
qw = sorted(qw)

while len(tj):  # 循环进行比较，当集合为空时停止

    if tj[0] > qw[0]:  # 田忌最慢的比齐王最慢的快，这两只比较，删除
        reward += 1
        del tj[0], qw[0]

    elif tj[0] < qw[0]:  # 田忌最慢的比齐王最慢的慢
        if tj[0] == qw[-1]:  # 田忌最慢的与齐王最快的相等，最慢比最快，删除
            reward += 0
            del tj[0], qw[-1]

        else:
            reward -= 1  # 田忌最慢的与齐王最快的慢，最慢比最快，删除
            del tj[0], qw[-1]

    elif tj[0] == qw[0]:  # 田忌最慢的与齐王最慢相等

        if tj[-1] > qw[-1]:  # 田忌最快的与齐王最快相等，最快比最快，删除
            reward += 1
            del tj[-1], qw[-1]

        elif tj[-1] < qw[-1]:  # 田忌最快的与齐王最快慢，最慢比最快，删除

            reward -= 1
            del tj[0], qw[-1]

        elif tj[-1] == qw[-1]:  # 田忌最快的与齐王最快相等

            if tj[0] == qw[-1]:  # 田忌最慢的与齐王最快相等，最慢比最快，删除
                reward += 0
                del tj[0], qw[-1]

            else:
                reward -= 1  # 田忌最慢的与齐王最快慢，最慢比最快，删除
                del tj[0], qw[-1]

print(reward)