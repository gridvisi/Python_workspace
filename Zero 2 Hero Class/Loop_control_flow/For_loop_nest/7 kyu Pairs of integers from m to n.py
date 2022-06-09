'''
https://www.codewars.com/kata/588e2a1ad1140d31cb00008c/solutions/python


'''


def generate_pairs(m, n):
    pair = []
    for i in range(m, n + 1):
        for j in range(i, n + 1):
            pair.append((i, j))

    return pair


from itertools import combinations_with_replacement
def generate_pairs(m, n):
    return list(combinations_with_replacement(range(m,n+1),2))


def generate_pairs(m, n):
    return [(i, j) for i in range(m, n + 1) for j in range(i, n + 1)]


def generate_pairs(m, n):
    return [(x, y) for x in range(m, n + 1) for y in range(m, n + 1) if x <= y]


