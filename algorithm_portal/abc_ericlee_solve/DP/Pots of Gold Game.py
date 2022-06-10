# Recursive function to maximize the number of coins collected by a player,
# assuming that the opponent also plays optimally

def findMaxCoins(coin, i, j):
    # base case: one pot left, only one choice possible
    if i == j:
        return coin[i]

    # if we are left with only two pots, choose one with maximum coins
    if i + 1 == j:
        return max(coin[i], coin[j])

    # if a player chooses front pot `i`, the opponent is left to choose from [i+1, j]
    # 1. If the opponent chooses front pot `i+1`, recur for [i+2, j]
    # 2. If the opponent chooses rear pot `j`, recur for [i+1, j-1]

    start = coin[i] + min(findMaxCoins(coin, i + 2, j),
                          findMaxCoins(coin, i + 1, j - 1))

    # if a player chooses rear pot `j`, the opponent is left to choose from [i, j-1]
    # 1. If the opponent chooses front pot `i`, recur for [i+1, j-1]
    # 2. If the opponent chooses rear pot `j-1`, recur for [i, j-2]

    end = coin[j] + min(findMaxCoins(coin, i + 1, j - 1),
                        findMaxCoins(coin, i, j - 2))

    # return the maximum of two choices
    return max(start, end)


# Pots of gold game using dynamic programming
if __name__ == '__main__':
    # pots of gold (even number) arranged in a line
    coin = [4, 6, 2, 3]
    coin = [5, 3, 5, 4, 4, 3, 2]
    print('The maximum coins collected by player is',
          findMaxCoins(coin, 0, len(coin) - 1))

# Cat 2014-senior 12-14
coin = [5,3,5,4,4,3,2]