# https://www.codewars.com/kata/5cb5eb1f03c3ff4778402099/train/python
'''
Some Examples
alice = plat,rend,bear,soar,mare,pare,flap,neat,clan,pore

bob = boar,clap,farm,lend,near,peat,pure,more,plan,soap

1) In the case of word = "send" and first = 0:

Alice responds to send with rend
Bob responds to rend with lend
Alice has no valid response to lend
Bob wins the game.
2) In the case of word = "flip" and first = 1:

Bob has no valid response to flip
Alice responds to flip with flap
Alice wins the game.
3) In the case of word = "maze" and first = 0:

Alice responds to maze with mare
Bob responds to mare with more
Alice responds to more with pore
Bob responds to pore with pure
Alice responds to pure with pare
Bob has no valid response to pare
Alice wins the game.
4) In the case of word = "calm" and first = 1:

Bob has no valid response to calm
Alice has no valid response to calm
Neither wins the game.
Input
alice  #  list of words in Alice's memory (10 <= n <= 2000)
bob    #  list of words in Bob's memory (10 <= n <= 2000)
word   #  string of the initial challenge word
first  #  integer of whom begins: 0 for Alice, 1 for Bob
Output
return  0  #  if Alice wins
return  1  #  if Bob wins
return -1  #  if both fail

https://www.codewars.com/kata/5cb5eb1f03c3ff4778402099/solutions

'''


x,y = 'bear','bear'
#print([x,y],len([]) == 0,''.join(['','','',x]))
def check_sum(x,y):
    return sum([x[i] != y[i] for i in range(len(x))])
#print(check_sum(x,y))

alice = ["plat", "rend", "bear", "soar", "mare", "pare", "flap", "neat", "clan", "pore"]
bob = ["boar", "clap", "farm", "lend", "near", "peat", "pure", "more", "plan", "soap"]

def mutations(alice, bob, word, first):
    def check(x, y):
        return [y for i in range(len(x)) if x[i] != y[i]]

    s,b = [0],[]
    words = [alice, bob]
    res = {'alice': [0], 'bob': [0]}
    keys = ['alice', 'bob']
    while len(word) != 0:
        key = keys[first]
        s = [w for w in words[first] if len(check(word, w)) == 1]
        b = [[w for w in words[first] if len(check(word, w)) == 1] for first in [0,1]]

        if b == [[], []]: return -1
        elif b != [[], []]:
            res[key] = word = [b[i] for i in [0,1] if b[i] != []][0]
            first = [i for i in [0,1] if b[i] != []][0]

        if len(word) == 0:return 'f',first
        words[first] = [x for x in words[first] if x != word[0]]

        first = int(bin(1 + first)[2:][-1])
        print(word,s,b,res,first)

        if res[keys[1]] == [0]:return 0
        if res[keys[0]] == [0]:return 1

word,first = "calm",1
#print((0 and 0),(0 and 1),not(1),not(0)
#word,first ="maze",0
#word,first = 'send',0
#word,first ="apse",0
#word,first = "sure",1 # Alice win
word,first = "boat",0
#word,first = 'soar',1
#word,first = 'soar',1  #0
#word,first = "neat", 1  #ouput 1
#word,first ="maze",0
#word,first ="apse",0
print(mutations(alice, bob, word, first))


def done(w, seen): return w in seen
def size(w): return len(w) == len(set(w))
def check(w, word):
    found = False
    for c1,c2 in zip(w, word):
        if c1 != c2:
            if found: return False
            else: found = True
    return True

def mutations(alice, bob, word, first):
    okay = lambda w: not done(w, seen) and size(w) and check(w, word)
    player = lambda: bob if first else alice
    seen, state = {word}, 0
    while True:
        try:
            word = next(filter(okay, player()))
            if state == 1: return first
            if state == 0: state = 2
            seen.add(word)
        except:
            if state == 1: return -1
            if state == 2: return 1 - first
            if state == 0: state = 1
        first = 1 - first


def mutations(alice1, bob1, ini, take):
    alice, bob, take_up, initial = alice1.copy(), bob1.copy(), take, ini
    def do(initial):
        for _ in range(bob.count(initial)) : bob.remove(initial)
        for _ in range(alice.count(initial)) : alice.remove(initial)
    find_first=lambda word,li:next((i for i,j in enumerate(li)if sum(k!=l for k,l in zip(j, word))==1 and len(set(j))==4),-1)
    alice__, bob__ = find_first(initial, alice), find_first(initial, bob)
    do(initial)
    if alice__ == -1 and  bob__ == -1 : return -1
    while True:
        alice__, bob__ = find_first(initial, alice), find_first(initial, bob)
        if take_up:  # bob
            if bob__ == -1 : return  0
            initial = bob[bob__]
        else:  # alice
            if alice__ == -1 : return 1
            initial = alice[alice__]
        do(initial)
        take_up ^= 1






'''
def mutations(alice, bob, word, first):

    b = True
    words= [alice, bob]
    res = {'alice':[],'bob':[]} #'alice':[],'bob':[]

    def check(x,y):
        return sum([x[i] != y[i] for i in range(len(x))])

    while b:

        s = [w for w in words[first] if check(word, w) == 1]
        if len(s) == 0:
            key = ['alice', 'bob'][first]
            res[key] = s = ['']
        else:
            key = ['alice', 'bob'][first]
            res[key] = word = s[0]

        print(words[first], word)

        words[first] = [x for x in words[first] if x != s[0]]
        print(words[first], word)
        first = int(bin(1 + first)[2:][-1])
        print('s2=', s, res['alice'], res['bob'],words[first])
        break
        if res['alice'] == [''] and res['bob'] == ['']:
            b = False
            return -1
            break
        elif res['alice'] != [''] and res['bob'] == ['']:
            b = False
            return 0
        elif res['alice'] == [''] and res['bob'] != ['']:
            b = False
            return 1

    if b[0] == [] and b[1] != []:return 1
    if b[0] != [] and b[1] == []: return 0
Test.assert_equals(mutations(alice, bob, "maze", 0),  0) # Alice goes  first, Alice   wins
Test.assert_equals(mutations(alice, bob, "send", 0),  1) # Alice goes  first, Bob     wins
Test.assert_equals(mutations(alice, bob, "boat", 0),  1) # Alice fails first, Bob     wins
Test.assert_equals(mutations(alice, bob, "apse", 0), -1) # Alice fails first, neither wins
Test.assert_equals(mutations(alice, bob, "neat", 1),  1) # Bob   goes  first, Bob     wins
Test.assert_equals(mutations(alice, bob, "soar", 1),  0) # Bob   goes  first, Alice   wins
Test.assert_equals(mutations(alice, bob, "mark", 1),  0) # Bob   fails first, Alice   wins
Test.assert_equals(mutations(alice, bob, "calm", 1), -1) # Bob   fails first, neither wins


        while len(s) == 0:
            res[key] = [0]
            first = int(bin(1 + first)[2:][-1])
            s = [w for w in words[first] if check(word, w) == 1]
            if res['alice'] == [0] and res['bob'] == [0]:
                return -1
'''



# [w for w in list(map(check,xls,yls)) if len(w)==1]
# [[x,y] for x in sl for y in st if x != y]
# res = map(check,[x for x in xls],[y for y in yls])

'''


>>> a = [0, 2, 2, 3] 
>>> a.remove(2) 
>>> a 
[0, 2, 3]
而对于 del 来说，它是根据索引（元素所在位置）来删除的，如下例：
>>> a = [3, 2, 2, 1] 
>>> del a[1] 
[3, 2, 1] 
        第1个元素为a[0] －－是以0开始计数的。则a[1]是指第2个元素，即里面的值2.
        del还可以删除指定范围内的值

        a = [3,2,2,1]

        del a[1,3]

        print a

        结果[3]



        del还可以删除整个列表

        del a



pop返回的是你弹出的那个数值。

所以使用时要根据你的具体需求选用合适的方法


>>> a = [4, 3, 5] 
>>> a.pop(1) 
3 
>>> a 
[4, 5]
另外它们如果出错，出错模式也是不一样的。注意看下面区别：

>>> a = [4, 5, 6] 
>>> a.remove(7) 
Traceback (most recent call last): 
  File "<stdin>", line 1, in <module> 
ValueError: list.remove(x): x not in list 
>>> del a[7] 
Traceback (most recent call last): 
  File "<stdin>", line 1, in <module> 
IndexError: list assignment index out of range 
>>> a.pop(7) 
Traceback (most recent call last): 
  File "<stdin>", line 1, in <module> 
IndexError: pop index out of range
'''

print('bear' or 'dear')
def mutations(alice, bob, word, first):



    return -1