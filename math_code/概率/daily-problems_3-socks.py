# https://brilliant.org/daily-problems/3-socks/

'''
Today's Challenge
A three-legged creature has an unorganized sock drawer with 4 red socks, 6 blue socks,
and 8 yellow socks.

The creature reaches into the sock drawer without looking and pulls out three random socks.
Which of the following events is the most likely?
'''

socks = ('red '*4 + 'blue '*6 + 'yellow '*8).split(' ')
socks = ('r '*4 + 'b '*6 + 'y '*8).split(' ')
print(socks[:-1])
sock = socks[:-1]
import random
round,res = [],[]
for i in range(10):
    init = socks
    while len(init) >= 3:
        #print(len(init),init,res)
        first = random.choice(init)
        init.pop(init.index(first))
        second = random.choice(init)
        init.pop(init.index(second))
        third = random.choice(init)
        init.pop(init.index(third))
        round.append(''.join([first,second,third]))
    res.append(round)
print(res)

class color:
    def __init__(self,red,blue,yellow):
        self.red = red
        self.blue = blue
        self.yellow = yellow

    def same_rate(self,red,blue,yellow):
        same_red = same_yellow = same_blue = 1
        total = sum([red,blue,yellow])
        '''
        same_red = (red/total)*(red-1/total-1)*(red-2/total-2)
        same_blue = (blue/total)*(blue-1/total-1)*(blue-2/total-2)
        same_yellow = (yellow/total)*(yellow-1/total-1)*(yellow-2/total-2)
        sum([same_red,same_blue,same_yellow])
        '''
        res = 0
        total = sum([red, blue, yellow])
        for x in (red,blue,yellow):
            res += (x/total)*(x-1/total-1)*(x-2/total-2)
        return res

    def differ2color(self,red,blue,yellow):
        res,colors = 0,[red, blue, yellow]
        total = sum(colors)
        for x,y in colors:
            res += (x/total)*(x-1/total-1)*(y-2/total-2)
        return res

#same_total = same_red + same_blue + same_yellow

# __________-------------------_____________________
def differ2color(red,blue,yellow):
    res,colors = 0,[red, blue, yellow]
    total = sum(colors)
    for x,y in zip(colors,colors[::-1]):
        print(x,y)
        res += (x/total)*(x-1/total-1)*(y-2/total-2)
    return res

red,blue,yellow = 4,6,8
print(differ2color(red,blue,yellow))


def same_rate(red, blue, yellow):
    same_red = same_yellow = same_blue = 1
    total = sum([red, blue, yellow])
    '''
    same_red = (red/total)*(red-1/total-1)*(red-2/total-2)
    same_blue = (blue/total)*(blue-1/total-1)*(blue-2/total-2)
    same_yellow = (yellow/total)*(yellow-1/total-1)*(yellow-2/total-2)
    sum([same_red,same_blue,same_yellow])
    '''
    res = 0
    total = sum([red, blue, yellow])

    for x in (red, blue, yellow):
        res += (x / total) * ((x - 1)/(total - 1)) * ((x - 2) /(total - 2))
        print(res)
    return res
red,blue,yellow = 4,6,8
print(same_rate(red,blue,yellow))


from itertools import combinations #permutations
sock = ('r '*4 + 'b '*6 + 'y '*8).split(' ')[:-1]
print('sock:',sock)
total = []  #all possibilities initial

for c in combinations(sock,3):
    res.append(''.join(c))

# all the three colors is same
same_c = 0  #all color same
for i in ('yyy','bbb','rrr'):
    same_c += res.count(i)
print(len(res),same_c/len(res))

# two kind of colors is same
same2c = 0
for i in ('yyr','yyb','bby','ybb','bbr','rry','rrb','rbb','byy','ryy','yrr','brr'):
    same2c += res.count(i)
print(len(res),same2c/len(res))

# three kind of colors is differ
diff3c = 0
for i in ('ybr','yrb','rby','ryb','byr','bry'):
    diff3c += res.count(i)
print(len(res),diff3c/len(res))


from collections import defaultdict, Counter
socks = (("yellow " * 8).split() + ("blue " * 6).split() + ("red " * 4).split())
counter = 0
results = defaultdict(int)

def chooseSocks(n, chosen, last):
    global counter
    if n == 3:
        counter += 1
        result = tuple(sorted(Counter(chosen).values()))
        # (3,): all equal, (1, 2): 2 equal, (1, 1, 1): all different
        results[result] += 1
        return
    else:
        for i, sock in enumerate(socks):
            if i < last: # non-ordered combination of socks
                continue
            else:
                chosen.append(sock)
                last = i
                chooseSocks(n+1, chosen, last+1)
                chosen.remove(sock)

chooseSocks(0, [], 0)
print("all possibilities: ", counter)
print(f"all equal: {results[(3,)]}/{counter} = {results[(3,)]/counter:.3f}")
print(f"2 equal:  {results[(1,2)]}/{counter} = {results[(1,2)]/counter:.3f}")
print(f"all different: {results[(1,1,1)]}/{counter} = {results[(1,1,1)]/counter:.3f}")

#all possibilities:  816
#all equal: 80/816 = 0.098
#2 equal:  544/816 = 0.667
#all different: 192/816 = 0.235