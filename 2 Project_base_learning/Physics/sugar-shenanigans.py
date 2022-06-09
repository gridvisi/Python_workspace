
import numpy as np
u, w = 1.1 * 2 / 3, 3  # u = µ, w = radius shaker
g = 9.8
table = [(2, u), (3, u), (4, u), (5, u), (6, u)]  # (height, µ)

for a_cloth in np.arange(1, 20, 0.1):
  result = [[], [], [], [], []]
  for i, shaker in enumerate(table):
    if a_cloth > g * shaker[1]:
      result[i].append("s+")  # shaker slides
    else:
      result[i].append("s-")
    if a_cloth > g * w / shaker[0]:
      result[i].append("t+")  # shaker topples
    else:
      result[i].append("t-")
  if len([ True for x, y in result if x == "s+"]) == len(table):
    print(f"{a_cloth:.2f}", "m/s²", result)
    break