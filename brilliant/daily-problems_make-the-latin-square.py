'''
https://brilliant.org/daily-problems/make-the-latin-square/
'''

"""
solution of:
    https://brilliant.org/daily-problems/make-the-latin-square/
"""
import itertools
def check_conditions(in_data):
    """
    Verifies, if in_data (storing only the first n-rows) satisfies
    the "arithmetic" conditions of the puzzle
    https://brilliant.org/daily-problems/make-the-latin-square/
    (for which only the first n-rows are needed).
    If the input data has the size n, it assumes,
    that the result of this function for the first n-1 "rows" was True.
    """
    res = True
    if len(in_data) == 1:
        res = in_data[0][0] == 1 and in_data[0][1] == 2 and in_data[0][2] == 3
    if len(in_data) == 2:
        res = in_data[1][2] == 4
    elif len(in_data) == 3:
        res = in_data[2][0] == 3
    elif len(in_data) == 4:
        res = in_data[3][0] == 2 and in_data[3][1] == 1 and in_data[3][4] == 4
    elif len(in_data) == 5:
        res = in_data[4][2] == 1 and in_data[4][3] == 2 and in_data[4][4] == 3
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
    returns a string representation of a solutions
    """
    return '\n'.join(' '.join(str(_) for _ in cur_row) for cur_row in sol_data)

print("Solutions:")
for cur_sq in gen_solution(5, check_conditions):
    print(sol_to_str(cur_sq))
    print(f"answer -> {''.join(str(_) for _ in cur_sq[3-1])}")