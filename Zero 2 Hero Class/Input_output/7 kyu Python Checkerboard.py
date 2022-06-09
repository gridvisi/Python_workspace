'''
https://www.codewars.com/kata/57785441311a24465e000025/train/python

You are trying to make a checkerboard made up of X's and O's. You've implemented the
function before in a different language but it just won't work.
The function make_checkered_board(n) creates an N by N board of X's and O's.

For example

make_checkered_board(4)==
[['X', 'O', 'X', 'O'],
 ['O', 'X', 'O', 'X'],
 ['X', 'O', 'X', 'O'],
 ['O', 'X', 'O', 'X']]
'''

#1st
def make_checkered_board(n):
    line=['X' for x in range(n)]
    board = [line[:] for y in range(n)]  # why use line[:
    for row in range(0,n):
        for col in range(0,n):
            if (row+col)%2:
                board[row][col]="O"
    return board

n = 5
print(make_checkered_board(n))

#2nd
def make_checkered_board(n):
    return [['O' if (i+j)%2!=0 else 'X' for i in range(n)] for j in range(n)]


#fail try
def make_checkered_board(n):
    line=['X' for x in range(n)]
    board = [line for y in range(n)]  # why use line[:
    for row in range(0,n):
        for col in range(0,n):
            if (row+col)%2:
                board[row][col]="O"
    return board

n = 5
print(make_checkered_board(n))

