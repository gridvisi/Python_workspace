# https://www.codewars.com/kata/604287495a72ae00131685c7/train/python


def middle_me(N, X, Y):
    if N % 2 == 1:
        return X
    else:
        return Y * (N//2) + X + Y * (N//2)

def middle_me(N, X, Y):
    return f'{(N//2)*Y}{X}{(N//2)*Y}' if N % 2 == 0 else X