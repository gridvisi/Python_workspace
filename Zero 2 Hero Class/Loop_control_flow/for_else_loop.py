'''
在一个房间里有 N 个人，其中一个是名人，大家都认识他，但他不认识任何人。其他人可能认识房间里面的一部分人。

你可以问任何人问题，但是问题只能是：你认识 某人吗，对方回答 Yes or No. 请问最少要问多少个问题才能把名人找出来？

解题：

依次问他是否认识他的下一个，比如 2， 如果 1 说认识，那么 1 一定不是名人，2 有可能是名人； 如果1 说不认识，2 一定不是名人，1 却有可能是名人。依次问下去，直到第 N 个人。我们问 （N - 1） 个问题就可以把名人找出来。

算法的For Else:
'''

def celeb(G):
    n = len(G)
    u, v = 0, 1                 # The first two
    for c in range(2,n+1):      # Others to check
        if G[u][v]: u = c       # u knows v? Replace u
        else: v = c             # Otherwise, replace v
    if u == n: c = v            # u was replaced last; use v
    else: c = u                 # Otherwise, u is a candidate
    for v in range(n):          # For everyone else...
        if c == v: continue             # Same person? Skip.
        if G[c][v]: break       # Candidate knows other
        if not G[v][c]: break           # Other doesn't know candidate
    else:
        return c            # No breaks? Celebrity!  MARK~~~~~~~~~~~~~~~~~~~~
    return None                 # Couldn't find anyone


# No.2 prime_sum
sum = 0
for n in range(2,100):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        sum+=n
print(sum)

#一个传统的解决方案是定义一个 "flag "变量，当我们找到特定的项目时将其设置
# 为True

leaders = ["Yang", "Elon", "Tim", "Warren"]
have_yang = False
for i in leaders:
    if i == "Yang":
        have_yang = True
        # Do something
        break

if have_yang == False:  # no yang
    ...  # Do others

