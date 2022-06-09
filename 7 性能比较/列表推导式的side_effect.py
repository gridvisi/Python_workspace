# https://stackoverflow.com/questions/5753597/is-it-pythonic-to-use-list-comprehensions-for-just-side-effects

#consume(side_effects(x) for x in xs)

#for x in xs:
#    side_effects(x)

from collections import Counter
def consume(iterator, n=None):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)