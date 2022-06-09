# https://brilliant.org/daily-problems/sugar-shenanigans-2/

import matplotlib.pyplot as plt
import numpy as np
import math
# example values
u, w = 0.5, 2.5
com_sugar, com_glass = 0, 5
M_sugar, M_glass = 0, 200
rho_sugar = 1.59
maxSugar = (0, 0)
g = 9.8
X, Y = [], []

# calculation
for com_sugar in np.arange(0, 7.1, 0.01):
    X.append(com_sugar)
    topple = (com_sugar, g * w / ((M_glass * com_glass +
                                   M_sugar * com_sugar) / (M_sugar + M_glass)))
    Y.append(topple)
    maxSugar = max(maxSugar, topple, key=lambda x: x[1])
    M_sugar = rho_sugar * math.pi * w**2 * com_sugar * 2 # M_sugar = density * A * h

print(f"sugar level: {maxSugar[0]:.2f} cm")

#plotting
plt.plot(X, Y)
plt.plot(X, [g * u]*len(X), color="violet")
plt.legend(("h_sugar curve", "topple curve", "sliding limit"), loc=0)
plt.xlabel("cm")
plt.ylabel("m/s²")
plt.axvline(0, linewidth=2, color="g")
plt.axhline(0, linewidth=2, color="g")
plt.scatter((maxSugar[0], maxSugar[0]), (0, maxSugar[1]), color="b")
plt.show()