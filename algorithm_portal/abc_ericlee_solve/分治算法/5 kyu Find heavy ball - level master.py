'''
https://www.codewars.com/kata/544034f426bc6adda200000e/train/python
'''

def find_ball(scales):
    part = [[None, 0, 1], [2, 3, 4], [5, 6, 7]]
    res1 = scales.get_weight(part[-1], part[1])
    res2 = scales.get_weight([part[res1][-1]], [part[res1][1]])
    return part[res1][res2]