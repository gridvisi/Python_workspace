
import collections
# 将纸牌定义为具名元组，每个纸牌都有等级和花色
Card = collections.namedtuple('Card', 'rank suit')

class FrenchDeck:
    # 等级2-A
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    # 花色红黑方草
    suits = 'spades diamonds clubs hearts'.split()
    # 构建纸牌
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    # 获取纸牌
    def __getitem__(self, position):
        return self._cards[position]

french_deck = FrenchDeck()
print(french_deck[0])
Card(rank='2', suit='spades')
print(french_deck[0].rank)
'2'
print(french_deck[0].suit)
'spades'