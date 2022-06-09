'''
https://brilliant.org/problems/card-shuffler/
洗牌
计算机科学二级

Alice和Bob想为他们的扑克俱乐部制作一台洗牌机。问题是，他们提出了不同的算法，因此无法决定应用哪一种算法：

爱丽丝的算法思路：从左到右依次，每张牌只和位于右边的任何牌交换位置。
鲍勃的算法思路：从左到右一次，每张牌与任何其他牌交换位置。
谁的算法更好，或者这真的很重要吗？

'''
from random import randint
import matplotlib.pyplot as plt

n = 1000 #模拟1000次洗牌
x_data = []
y_data = []
# start simultion for distributed permutations
for simulation in range(n):
    # perfectly sorted array
    arr = [x + 1 for x in range(n)]
    for i in range(n):
        r = randint(0, i) # correct way

        # swap two elements
        arr[r], arr[i] = arr[i], arr[r]

    # collect result
    for i in range(n):
        x_data.append(arr[i])
        y_data.append(i+1)
# end simulation

# plot
fig, axs = plt.subplots(ncols = 2, sharey=True, figsize=(14, 6))
fig.subplots_adjust(hspace=0.5, left=0.07, right=0.93)
hb = axs[0].hexbin(x_data, y_data, gridsize=50, cmap='inferno')
axs[0].axis([0, 1000, 0, 1000])
axs[0].set_title("Distributed Permutation")
cb = fig.colorbar(hb, ax=axs[0])
cb.set_label('frequency')

x_data = []
y_data = []
# start simultion for biased permutations
for simulation in range(n):
    # perfectly sorted array
    arr = [x + 1 for x in range(n)]
    for i in range(n):
        r = randint(0,n-1) # wrong way

        # swap two elements
        arr[r], arr[i] = arr[i], arr[r]

    # collect result
    for i in range(n):
        x_data.append(arr[i])
        y_data.append(i+1)
# end simulation

# plot
fig.subplots_adjust(hspace=0.5, left=0.07, right=0.93)
hb = axs[1].hexbin(x_data, y_data, gridsize=50, cmap='inferno')
axs[1].axis([0, 1000, 0, 1000])
axs[1].set_title("Biased Permutation")
cb = fig.colorbar(hb, ax=axs[1])
cb.set_label('frequency')

plt.show()
