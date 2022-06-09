__author__ = 'Administrator'
import numpy as np
a=np.arange(25).reshape(5,5)
WIDTH = 5
HEIGHT = 5
map = [
      [0, 1, -1, 1, -1],
      [-1, -1, 1, -1, -1],
      [-1, 1, 1, -1, 1],
      [1, -1, -1, 1, -1],
      [1, -1, 1, 1, 0 ]
      ]
print(map[3][3])
print(map[1])
score = np.arange(25).reshape(WIDTH,HEIGHT)
for j in range(5):
    score[j] = map[j]
position = score
print(position)
i = 0
score[0,0] = 0
x = 0
y = 0
while x < (WIDTH + 1) and y < (HEIGHT + 1):
    y += 1
    x += 1
    if position[x+1][y] > position[x][y+1] and position[x][y] + position[x+1][y] > 0:
        score[x+1][y] = score[x][y] + score[x+1][y]
    elif position[x+1][y] < position[x][y+1] and position[x][y] + position[x][y+1] > 0:
        score[x][y+1] = score[x][y]+score[x][y+1]

    print(score)

