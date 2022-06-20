R= .1
N = 2000
Q = 1e-9
k = 9e9
n = 0

charges = []
while n < N:
    r = R * vector(2 * random() - 1, 2 * random() - 1, 2 * random() - 1)
    charges = charges + [sphere(pos=r, radius=0.002, q=Q / N)]
    n = n + 1
