#https://www.codewars.com/kata/5592fc599a7f40adac0000a8/train/python

def sum_diagonals(matrix):
    re = 0
    for i,e in enumerate(matrix):
        #if [i][i] != [i][len(matrix)-i]:
        re += matrix[i][i] + matrix[i][len(matrix)-i-1]
            #re += matrix[i][len(matrix)-i] + matrix[len(matrix)-i][len(matrix)-i]
    return re
matrix = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
  ]
print(sum_diagonals(matrix))

def sum_diagonals(matrix):
    return sum(row[i] + row[-i - 1] for i, row in enumerate(matrix))


import numpy as np

def sum_diagonals(matrix):
    # your code here

    matrix = np.matrix(matrix)
    print(matrix)
    print('1:',np.diag(matrix, 0))
    print('2:',np.diag(np.flip(matrix, axis=1)))
    return sum(np.diag(matrix, 0)) + sum(np.diag(np.flip(matrix, axis=1), 0))
print(sum_diagonals(matrix))