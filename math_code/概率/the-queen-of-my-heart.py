'''
https://brilliant.org/problems/the-queen-of-my-heart/

Which method's shuffles are closest to a random shuffling of cards?

Details

The more uniform the probability distribution between all possible permutations of the cards,
 the better the shuffling algorithm is.
Assume that random.randrange is perfectly uniformly random.
'''
import random
def aShuffle(l):
    cards = l[:]
    for i in range((len(cards) - 1), 0, -1):
            n = random.randrange(i+1)
            cards[i], cards[n] = cards[n], cards[i]
    return cards

def bShuffle(l):
    cards = l[:]
    for i in range(len(cards)):
            n = random.randrange(len(cards))
            cards[i], cards[n] = cards[n], cards[i]
    return cards

'''
Beware of bugs in the above code; I have only proved it correct, not tried it. -Knuth

Let me begin with showing some real experimental results to convince you.


1
2
3
4
5
6
bTest = []
aTest = []
for i in xrange(60000): aTest.append(aShuffle(range(3)))
for i in xrange(60000): bTest.append(bShuffle(range(3)))
for i in [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]:
    print bTest.count(i), aTest.count(i)


1
2
3
4
5
6
8772 9906
11091 10125
11051 10162
11089 9957
8924 9930
9073 9920

Suppose the number of cards is n.

In the first algorithm, the number of available cards between which the swaps are done continually 
reduces from n to 1. The number of possible sequences of swaps would be n!.

In the second algorithm, the swapping space does not decrease. That would make the number of 
possible sequences of swaps n^n.

Shouldn't more swaps make things better? Well, it actually makes things worse.

Notice that n^n is greater than n! which happens to be the number of possible permutations.
 In virtue of the pigeonhole principle, that would mean there would be some permutations which could be reached through more than one sequence of swaps in bShuffle. It gets worse since n^n is usually not divisible by n!.
'''