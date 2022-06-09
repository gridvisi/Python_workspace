'''
https://brilliant.org/daily-problems/ramons-socks/

It has been a while since Ramon has done laundry, so he only has five pairs of clean socks
left in his drawer: three white pairs and two black pairs. Once again Ramon reaches in and
grabs a pair of socks. What is the probability that he gets a mismatched pair?

refer:https://blog.csdn.net/ckk727/article/details/99548223
'''

# Math solve

# The ratio of first fetch black is 4/10, and the rotio of Second fetch white is 6/9: 2/5 * 2/3 = 4/15
# The ratio of first fetch white is 6/10, and the rotio of Second fetch black is 4/9: 3/5 * 4/9 = 4/15
# total of above is 8/15

import random
sock = ['w','w'] * 3 + ['b','b'] * 2
print(sock)
random.shuffle(sock)
print(sock)


match,mismatch = 0,0
fetch = 1000
for i in range(fetch):
    test = random.sample(sock,2)
    if test[0] == test[1]:
        match += 1
    elif test[0] != test[1]:
        mismatch += 1
print(mismatch/fetch,mismatch,fetch,8/15)


# 2nd solution by shuffle
for i in range(10):
    random.shuffle(sock)
    #print(test)
    if test[0] == test[1]:
        match += 1
    elif test[0] != test[1]:
        mismatch += 1
print(mismatch / fetch, mismatch, fetch, 8 / 15)




