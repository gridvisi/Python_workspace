'''
https://www.codewars.com/kata/588417e576933b0ec9000045/train/python

Example
For nCols = 16, nRows = 11, col = 5 and row = 3,
the output should be
Col:列  Row:行
Theater.seats nCols nRows col row == 96
'''

def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_cols - col + 1) * (tot_rows - row)