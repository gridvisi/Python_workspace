'''
https://brilliant.org/daily-problems/find-your-keys/
'''
from collections import defaultdict
# Categorize the outputs we can get (numbers instead of color)
poss = {0: [(0,0)], 1:[(0,1)], 2:[(0,2), (1,1)],
3:[(0,3), (1,2), (2,2)], 4:[(0,4), (1,3), (2,3)]}
# reverse them for easy lookup
rev_pos = {v:k for k, vs in poss.items() for v in vs}

# the 'kind' of a point is based on the Manhattan distance
def kind(a, b):
    x = abs(a[0] - b[0])
    y = abs(a[1] - b[1])
    d = tuple(sorted([x,y]))
    return rev_pos.get(d, 'X')

def make_board(s=8):
    points = set()
    for i in range(s):
        for j in range(s):
            points.add((i, j))
    return points

# The points a key could be in are the points
# that return the same value as the spot we've picked
def prune(spot, spot_kind, points):
    keep = set()
    for p in points:
        if kind(spot, p) == spot_kind:
            keep.add(p)
    return keep - {spot}

# Given a test spot and a set of spots where the key could be,
# what's the worst amount of spots left after pruning?
def get_worst(test_spot, avail):
    worst = 0
    for possible_key in avail:
        res = kind(test_spot, possible_key)
        new_pts = prune(test_spot, res, avail)
        worst = max(worst, len(new_pts))
    return worst

# Uses get_worst to find the best worst-case options
# and deal with ties
def get_possible(avail):
    values = [get_worst(pt, avail) for pt in avail]
    use = [x for x, v in zip(avail, values) if v == min(values)]
    return use

# depth-first search to build the probability table
# under those rules
def play(moves, prob, key, curr, avail, data):
    if key == curr:
        data[moves].append(prob)
        return
    avail2 = prune(curr, kind(curr, key), avail)
    # minimax it
    usable = get_possible(avail2)
    pr = 1 / len(usable)
    for u in usable:
        play(moves + 1, prob*pr, key, u, avail2, data)

# Then we run the `play` function for each possible key location and our
# #defined starting point of [3,4]. My positions are 0-indexed here.

start = (3, 4)
data = defaultdict(list)
for key in make_board():
    play(1, 1/64, key, start, make_board(), data)

n_games = {k:len(v) for k, v in data.items()}
max(n_games)
#6

# to test that it's near enough to 1 to know we found the full state space
total_prob = sum(sum(vs) for k, vs in data.items())
#0.9999999999999991

# Expected value
print(sum(k * sum(vs) for k, vs in data.items()))
#3.6700520833333297