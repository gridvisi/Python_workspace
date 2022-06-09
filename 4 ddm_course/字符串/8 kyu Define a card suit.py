'''
You get any card as an argument. Your task is to return the suit of this card (in lowercase).

Our deck (is preloaded):

DECK = ['2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS',
        '2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD',
        '2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH',
        '2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC']
('3C') -> return 'clubs'
('3D') -> return 'diamonds'
('3H') -> return 'hearts'
('3S') -> return 'spades'
FUNDAMENTALSSTRINGSBASIC LANGUAGE FEATURESLANGUAGE FEATURES
'''

from pprint import pprint
DECKSORT = ('2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS',
        '2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD',
        '2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH',
        '2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC')

DECK = ['2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS',
        '2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD',
        '2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH',
        '2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC']

def turn_right(rect):
    s_line, d_line, h_line, c_line = rect[:13], rect[13:26], rect[26:39], rect[39:]
    for i in range(13):
        pprint(f"{c_line[i]} {h_line[i]} {d_line[i]} {s_line[i]}\n")

print(turn_right(DECK))

def define_suit(card):
    return # Good luck

# ericlee new tasks
def countSuit(DECK):
    suit = {'C':'Club',
            'H':'Heart',
            'D':'Diamand',
            'S':'Spader'}

    collect = {'Club':0,
               'Heart':0,
               'Diamand':0,
               'Spader':0}
    for card in DECK:
        collect[suit[card[-1]]] += 1 #why [-1 instead of [1]
    return collect
print(countSuit(DECK))

# 2、统计任意花色的牌，大于正整数 n 的牌，A==1
# 黑桃spade,红桃heart,方片diamond,梅花club



'''

3、洗牌后实现下面顺序：
自上而下2，3，.... J, K , Q, A
花色依顺序为：黑桃spade, 方片diamond,红桃, heart,梅花club, 

'''

import numpy as np
DECK = [DECK[i:i+13] for i in range(0,len(DECK),len(DECK)//4)]
A = np.mat(DECK)
pprint(A.T)
#print(A.swapaxes(0, 1))

'''
大同花顺>同花顺>四条>满堂红>同花>顺子>三条>两对>一对>无对
数字比较：A＞K＞Q＞J＞10＞9＞8 
花式比较：黑桃＞红桃＞草花＞方片 

大同花顺（RoyalFlush）:最高为Ace（一点)的同花顺。例:A♠K♠Q♠J♠10♠
同花顺（StraightFlush）:同一花色，顺序的牌。例：Q♦J♦10♦9♦8♦
四条（FourofaKind）:有四张同一点数的牌。例：4♣4♦4♥4♠9♥
满堂红（Fullhouse）:三张同一点数的牌，加一对其他点数的牌。例:8♣8♦8♠K♥K♠

同花（Flush）:五张同一花色的牌。例：K♠J♠8♠4♠3♠
顺子（Straight）:五张顺连的牌。例：5♦4♥3♠2♦A♦
三条（Threeofakind）:有三张同一点数的牌。例：7♣7♥7♠K♦2♠
两对（TwoPairs）:两张相同点数的牌，加另外两张相同点数的牌。例：A♣A♦8♥8♠Q♠

一对（OnePair）:两张相同点数的牌。例：9♥9♠A♣J♠4♥
无对（NoPair):不能排成以上组合的牌，以点数决定大小。例：A♦10♦9♠5♣4♣
'''
import random

DECK = ['2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS',
        '2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD',
        '2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH',
        '2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC']
rank = {
        "RoyalFlush":0,
        "StraightFlush":1,
        "FourofaKind":2,
        "Fullhouse":3,
        "Flush":4,
        "Straight":5,
        "Threeofakind":6,
        "TwoPairs":7,
        "OnePair":8,
        "NoPair":9
        }

#print(DECK)
#print([[]]*6)
person = [[]] * 6
person[0].append("A")
print('Nested list',person[0],person)

#2 发牌
def deal(DECK,n): # n == 人数
    random.shuffle(DECK)
    #print('SHUFFLED',DECK)
    person = []
    for i in range(n):
        c = DECK[i:len(DECK):n]
        person.append(c)
    return person
n = 4


#3 理顺牌  黑桃Spade, 方片Diamond,红桃heart,梅花Club,
person = deal(DECK,n)
print('Deals: ',person)
print(sorted(person[0],key=lambda x:x[-1]))


def shuffle(person):
    cards = []
    for card in person:
        suit = {'C':[],
                'H':[],
                'D':[],
                'S':[]
                }

        for c in card:
            suit[c[-1]].append(c)
            #print(suit)
        cards.append(suit)
    return cards

print('shuffle;',shuffle(person))


def seq(k, v):
    ctod = {'K':13,'Q':12,'J':11,'A':1}
    i, j = 0, 1
    cunt = 1
    v = sorted([ctod[c[:-1]] if c[:-1] in ctod.keys() else int(c[:-1]) for c in v])
    print('sorted kv',v)
    while i <= j and j < len(v):

        if v[i] + 1 == v[j]:
            i += 1
            j += 1
            cunt += 1
            if cunt >= 3 and j == len(v) - 1:
                return [str(i)+k for i in v[j-3:j]]

        elif v[i] == v[j]:
            i += 1
            j += 1
            cunt += 1
            if cunt == 4:
                return k
        else:
            i += 1
            j += 1
    return [k,0]


k,v = 'D', ['10D', '4D', '5D', '3D']
print(seq(k,v))

def flush(cards):
    ans = []
    for c in cards:
        for k,v in c.items():
            ans.append(seq(k,v))
    return ans
cards = shuffle(person)
print(flush(cards))




'''

class C:
    def __init__(self):
        self.
    collect = {'Club':0,
               'Heart':0,
               'Diamand':0,
               'Spader':0}
'''


list_of_shows = ["Bojack Horseman",
                 "我的英雄学院",
                 "Ozark",
                 "Arrested Development",
                 "Derry Girls",
                 "Tuca & Bertie"]


list_of_characters = [["Todd", "Princess Carolyn", "Judah", "Diane"],
                      ["绿谷", "庄户", "全能", "巴古", "雾岛"],
                      ["Ruth", "Jonah", "Wyatt"],
                      ["托比亚斯","戈布","安妮","马比"],
                      ["迈克尔修女","奥拉","艾琳","克莱尔","詹姆斯"],
                      ["Bertie", "Speckle", "Tuca", "Dakota"]]

combined_shows_characters = dict(zip(list_of_shows, list_of_characters))

print(combined_shows_characters['我的英雄学院'])

pprint(combined_shows_characters)