#https://brilliant.org/problems/blackjack-what-are-the-chances/

from random import shuffle

# define the card ranks, and suits
ranks = [_ for _ in range(2, 11)] + ['JACK', 'QUEEN', 'KING', 'ACE']
suits = ['SPADE', 'HEART ', 'DIAMOND', 'CLUB']
print(ranks)
def get_deck():
    """Return a new deck of cards."""
    return [[rank, suit] for rank in ranks for suit in suits]

# get a deck of cards, and randomly shuffle it
print(get_deck())
deck = get_deck()
shuffle(deck)
print(shuffle(deck))
# issue the player and dealer their first two cards
player_hand = [deck.pop(), deck.pop()]
