
L = {100000,10000,1000,100,10,1}
L = [100000,10000,1000,100,10,1]
V = 234


def greedyMakeChange(L, V):
    minCoin = 0
    for change in L:
        print(change)
        while V >= change:
            V -= change
            minCoin += 1
    return minCoin

print('greedy:',greedyMakeChange(L,V))

minCoins = []

def dpMakeChange(L, V, minCoins):
    for cents in range(V+1):
        coinCount = cents
        for j in [c for c in L if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
        minCoins[cents] = coinCount
    return minCoins[V]

print(dpMakeChange(L, V, minCoins))


