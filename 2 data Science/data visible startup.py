from matplotlib import pyplot as plt
plt.plot([0,1,2,3,4]) #
plt.show()

plt.plot([0,1,2,3,4], label='y = x')
plt.title('Y = X Straight Line')
plt.ylabel('Y Axis')
plt.yticks([1,2,3,4])
plt.legend(loc = 'best')
plt.show()

import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
x = [8.0, 1, 2.5, 4, 28.0]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]
print(x)
#[8.0, 1, 2.5, 4, 28.0]
print(x_with_nan)
#[8.0, 1, 2.5, nan, 4, 28.0]

y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)
print(y)
#array([ 8. ,  1. ,  2.5, 4. , 28. ])
print(y_with_nan)
#array([ 8. ,  1. ,  2.5,  nan,  4. , 28. ])
print(z)

'''
0     8.0
1     1.0
2     2.5
3     4.0
4    28.0
dtype: float64
'''

print(z_with_nan)
'''
0     8.0
1     1.0
2     2.5
3     NaN
4     4.0
5    28.0
dtype: float64
'''
