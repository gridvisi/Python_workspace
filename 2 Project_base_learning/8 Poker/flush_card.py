'''
常见的扑克牌为场景。桌上有一副牌，例如四个花色的牌各有若干张，在数组中有牌面的花色和大小，希望能编码输出每种花色的数量等等各种任务需要。

花色的简称为字母 C H D S, 扑克牌同一种花色的顺序牌
{'C':'Club',
'H':'Heart',
'D':'Diamand',
'S':'Spader'}

``` solve by code O(n) ```
```

```
洗牌后，遍历54张牌，切片长度为 5，5张牌是顺子的返回

'''
print(int('10'))
d = {'A':1,'J':11,'Q':12,'K':13}
e = 'AD'
print(d.get(e[:-1], e[:-1]))

DECK = ['2S','3S','4S','5S','6S','7S',
        '8S','9S','10S','JS','QS','KS','AS',
        '2D','3D','4D','5D','6D','7D','8D',
        '9D','10D','JD','QD','KD','AD',
        '2H','3H','4H','5H','6H','7H','8H',
        '9H','10H','JH','QH','KH','AH',
        '2C','3C','4C','5C','6C','7C','8C',
        '9C','10C','JC','QC','KC','AC']

import random
#deck = random.shuffle(DECK)
#print(deck)
print(random.shuffle(DECK))
print(DECK)

def maxseq(seq):
    color = set()
    d = {'A':1,'J':11,'Q':12,'K':13}

    if len(set([i[-1] for i in seq])) == 1:
        seq = sorted(seq,key=lambda x:int(d.get(x[:-1],x[:-1])))
        idx = seq[0]
        #print('lastID:',idx,seq)
        maxSrg = [idx]

        for i,e in enumerate(seq[:-1]):
            #print(maxSrg,idx)
            l = d.get(e[:-1],e[:-1])
            r = d.get(seq[i+1][:-1],seq[i+1][:-1])
            #print(e[:-1],l,r)
            if int(l) + 1 == int(r):
                maxSrg.append(e)

        return maxSrg

seq = ['10D', '9D', '8D', '7D', '6D']
color = set()
#print(color.add(6))
#print(color)
#print([color.add(i[-1]) for i in seq])
print('maxseq(seq)',maxseq(seq))




# nested list solve Maxseq
def maxseq(seq):
    #d = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
    d = {'A': '1', 'J': '11', 'Q': '12', 'K': '13'}
    #print(d.get(seq[-1][:-1],int(seq[-1][:-1])))
    # 高能预警，get的default输出报错是因为字符'J'不能用 int('J')
    seq = [int(d.get(c[:-1],c[:-1])) for c in seq]
    #print(seq)
    seq = sorted(seq)
    #print(seq)
    #last_idx = [seq[0]]
    maxSrg = [[seq[0]]]
    for i,e in enumerate(seq[1:]):

        if int(e) == int(maxSrg[-1][-1])+1:
            maxSrg[-1].append(e)
            #print(maxSrg, e)
            #continue
        else:
            maxSrg.append([e])
            #print(maxSrg)
    return maxSrg
seq = 'cdeffggfghijkaabcdecabccdd'
seq = '34567885678910111212345'
seq = ['10D', 'QD', '8D', 'KD', 'JD']
#print('No.2th solution:',maxseq(seq))
n = 4 #共 6 人玩牌

def shuffles(n):
    random.shuffle(DECK)
    final = []
    l = len(DECK)//n
    for i in range(0,len(DECK),l):
        d = {'A': '1', 'J': '11', 'Q': '12', 'K': '13'}
        card = maxseq(DECK[i:i+l])
        final.append(max(card,key=len))
    return print('final',max(final,key=len),final)
n = 6
shuffles(n)
'''

# need improve code
for l in range(0,len(DECK),n):
    d = {'A': '1', 'J': '11', 'Q': '12', 'K': '13'}
    card = DECK[l:l+n]
    card = sorted(card, key=lambda x: int(d.get(x[:-1], x[:-1])))
    final = []
    l,r = card[0][:-1],card[-1][:-1]
    l,r = d.get(l,l),d.get(r,r)
    print(card)
    #print([d.get(c[:-1], c[:-1]) for c in card],list(range(int(l), int(r))))
    source = [d.get(c[:-1], c[:-1]) for c in card]
    target = [str(i) for i in list(range(int(l), int(r)))]
    print(source,target)
    if source == target:

        final.append(card)
        print('flush appear:',card)
else:
    print('None')
'''