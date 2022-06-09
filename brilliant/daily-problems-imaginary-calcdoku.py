# https://brilliant.org/daily-problems/imaginary-calcdoku/

"""
solution of:
    https://brilliant.org/daily-problems/imaginary-calcdoku/
"""

import itertools

def transform(in_data):
    """
    transforms the solution data to a complex solution data
    """
    transform_dict = {1: 1, 2:-1, 3:1j, 4:-1j}
    return [[transform_dict[_] for _ in row] for row in in_data]

def check_conditions(in_data):
    """
    Verifies, if in_data (storing only the first n-rows) satisfies
    the "arithmetic" conditions of the puzzle
    https://brilliant.org/daily-problems/imaginary-calcdoku/
    (for which only the first n-rows are needed).
    If the input data has the size n, it assumes,
    that the result of this function for the first n-1 "rows" was True.
    """
    tmp_data = transform(in_data)
    assert len(in_data) <= 4
    for _ in in_data:
        assert len(_) <= 4
    res = True
    if len(tmp_data) == 1:
        res = tmp_data[0][1]+tmp_data[0][2]+tmp_data[0][3] == -1j
    elif len(tmp_data) == 2:
        res = tmp_data[1][1]*tmp_data[1][2]*tmp_data[1][3] == 1
    elif len(tmp_data) == 4:
        res = tmp_data[0][0]*tmp_data[1][0]*tmp_data[2][0]*tmp_data[3][0]*tmp_data[3][1] == 1 and \
            tmp_data[2][1]*tmp_data[2][2]*tmp_data[3][2] == 1j and \
            tmp_data[2][3]*tmp_data[3][3] == -1
    return res

def gen_solution(in_size, in_check_arithmetic_cond):
    """
    generates all Latin squares of the order in_size, which
    satisfy the additional conditions described in in_check_arithmetic_cond
    """
    def are_all_different(in_list):
        """
        checks if all of the entries in in_list are different
        """
        return len(set(in_list)) == len(in_list)
    def add_row(cur_row_data):
        if len(cur_row_data) == in_size:
            yield tuple(cur_row_data)
        else:
            for tmp_row in itertools.permutations(range(1, in_size+1)):
                tmp_row_data = cur_row_data.copy()
                tmp_row_data.append(tmp_row)
                for col_num in range(in_size):
                    cur_col = [tmp_row_data[_][col_num] for _ in range(len(tmp_row_data))]
                    if not are_all_different(cur_col):
                        break
                else:
                    if in_check_arithmetic_cond(tmp_row_data):
                        for _ in add_row(tmp_row_data):
                            yield _
    for _ in add_row([]):
        yield _

def sol_to_str(sol_data):
    """
    returns a string representation of a solution
    """
    return '\n'.join('\t'.join(str(_) for _ in cur_row) for cur_row in sol_data)

for cur_sol in gen_solution(4, check_conditions):
    transform_sol = transform(cur_sol)
    print(f"solution:\n{sol_to_str(transform_sol)}")
    corner_sum = transform_sol[0][0]+transform_sol[0][3]+transform_sol[3][0]+transform_sol[3][3]
    print(f"corner sum: {corner_sum}")



# solution 2nd

import itertools
from itertools import permutations
import numpy as np
def columns_different(row, grid):
    for i in range(row):
        if any([True for j in range(len(grid[0]))
                if grid[i][j] == grid[row][j]]):
            return False
    return True


def calc(n, grid, activation):
    green, yellow, blue, red, orange = activation
    if n < 4:
        for row in permutations([1j, 1, -1, -1j]):
            grid[n] = row
            if not columns_different(n, grid):
                continue
            if yellow and n == 0 and sum(grid[0][1:4]) != -1j:
                continue
            if green and n == 1 and grid[1][1] * grid[1][2] * grid[1][3] != 1:
                continue
            if red and n == 3 and grid[0][0] * grid[1][0] * grid[2][0] * grid[3][0] * grid[3][1] != 1:
                continue
            if blue and n == 3 and grid[2][1] * grid[2][2] * grid[3][2] != 1j:
                continue
            if orange and n == 3 and grid[2][3] * grid[3][3] != -1:
                continue

            calc(n + 1, grid, activation)
    else:
        #print(*grid, sep="\n")
        print("sum of corners:", grid[0][0] +
              grid[0][3] + grid[3][0] + grid[3][3])


for active in product([1, 0], repeat=5):
    if active.count(0) in [0, 1] or active == (0, 1, 0, 1, 1):
        print("green {}, yellow {}, blue {}, red {}, orange {}:".format(*active))
        calc(0, [[] for i in range(4)], active)