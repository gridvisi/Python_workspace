__author__ = 'Administrator'
'''
from scipy.linalg import solve
def trans(m):
    a = [[] for i in m[0]]
    for i in m:
        for j in range(len(i)):
            a[j].append(i[j])
    return a
'''
import numpy as np
from scipy.linalg import solve
a=[[1, 1, 0, 0], [1, 0, 1, 0],[1, 0, 0, 1],[0, 1, 1, 0],[0, 1, 0, 1],[0, 0, 1, 1]]

a=np.array([[1, 1, 0, 0], [1, 0, 1, 0],[1, 0, 0, 1],[0, 1, 1, 0],[0, 1, 0, 1],[0, 0, 1, 1]])
#b=[6,8,10,12,14,16]
#print (trans(a))
#a=trans(a)
z=[2,4,6,10]
z=np.array(z)
b=np.array([6,8,10,12,14,16])
print(a)
print(b)
print(z)

y=np.dot(a,z)
print('z time a:',y)

#w=np.linalg.solve(a,b)
w = solve(a,b)
print(w)



'''
import numpy as np
a=([1, 1, 0, 0], [1, 0, 1, 0],[1, 0, 0, 1],[0, 1, 1, 0],[0, 1, 0, 1],[0, 0, 1, 1])
a=np.array(a)
b=[[6,0,0,0,0,0],[0,8,0,0,0,0],[0,0,10,0,0,0],[0,0,0,12,0,0],[0,0,0,0,14,0],[0,0,0,0,0,16]]
#b=[[6,8,10,12,14,16]
b=np.array(b)
print(a)
print(b)
x=np.linalg.solve(a,b)
y=np.dot(a,b)
print(x)
print(y)
'''


'''
import numpy as np

# 2-D array: 2 x 3
two_dim_matrix_one = np.array([[1, 2, 3], [4, 5, 6]])
# 2-D array: 3 x 2
two_dim_matrix_two = np.array([[1, 2], [3, 4], [5, 6]])

two_multi_res = np.dot(two_dim_matrix_one, two_dim_matrix_two)
print('two_multi_res: %s' %(two_multi_res))

# 1-D array
one_dim_vec_one = np.array([1, 2, 3])
one_dim_vec_two = np.array([4, 5, 6])
one_result_res = np.dot(one_dim_vec_one, one_dim_vec_two)
print('one_result_res: %s' %(one_result_res))
'''