'''
https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f/train/python

Examples
# N = 4
1 + 2 + 3 + 4 = 10

# N = 10
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46

# N = 12
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51
'''


def compute_sum(n):
    def num_str(x):
        return sum([int(i) for i in str(x)])
    return sum([num_str(i) for i in range(1,n+1)])
n = 12
print(compute_sum(n))

def compute_sum(n):
    return sum(int(c) for i in range(1, n+1) for c in str(i))


def compute_sum(n):
    return sum(map(int,''.join(str(n) for n in range(n+1))))

def it(n):
    for i in range(1, n+1):
        yield from map(int, str(i))

def compute_sum(n):
    return sum(it(n))