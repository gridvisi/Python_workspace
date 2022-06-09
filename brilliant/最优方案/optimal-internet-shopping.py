'''
https://brilliant.org/problems/optimal-internet-shopping/

            Shop 1	Shop 2	Shop 3	Shop 4	Shop 5	Shop 6	Shop 7	Shop 8	Shop 9	Shop 10
English	    13	    19	    16	    19	    19	    18	    17	    16	    15	    14
Math	    18	    13	    17	    14	    15	    16	    15	    17	    18	    17
French	    17	    14	    13	    17	    16	    18	    16	    17	    18	    17
History	    19	    18	    17	    13	    16	    15	    15	    16	    17	    14
Art	        16	    14	    17	    18	    13	    16	    15	    16	    17	    16
Geography	17	    17	    16	    14	    15	    13	    16	    17	    18	    16
Biology	    17	    14	    16	    17	    15	    16	    13	    18	    19	    17
Physics	    17	    16	    15	    14	    17	    16	    15	    13	    15	    15
Chemistry	15	    15	    16	    18	    17	    15	    16	    15	    13	    14
Music	    16	    14	    16	    18	    17	    17	    15	    16	    18	    13
Delivery cost	4	4	4	4	4	4	4	4	4	4
'''

shop_1 = [13,18,17,19,16,17,17,17,15,16]
shop_2 = [19,13,14,18,14,17,14,16,15,14]
shop_3 = [16,17,13,17,17,16,16,15,16,16]
shop_4 = [19,14,17,13,18,14,17,14,18,18]
shop_5 = [19,15,16,16,13,15,15,17,17,17]
shop_6 = [18,16,18,15,16,13,16,16,15,17]
shop_7 = [17,15,16,15,15,16,13,15,16,15]
shop_8 = [16,17,17,16,16,17,18,13,15,16]
shop_9 = [15,18,18,17,17,18,18,15,13,18]
shop_10 = [14,17,17,14,16,16,17,15,14,13]


bookCount = 10
shopCount = 10
deliveryCharge = 4

cost = [[13, 19, 16, 19, 19, 18, 17, 16, 15, 14],
        [18, 13, 17, 14, 15, 16, 15, 17, 18, 17],
        [17, 14, 13, 17, 16, 18, 16, 17, 18, 17],
        [19, 18, 17, 13, 16, 15, 15, 16, 17, 14],
        [16, 14, 17, 18, 13, 16, 15, 16, 17, 16],
        [17, 17, 16, 14, 15, 13, 16, 17, 18, 16],
        [17, 14, 16, 17, 15, 16, 13, 18, 19, 17],
        [17, 16, 15, 14, 17, 16, 15, 13, 15, 15],
        [15, 15, 16, 18, 17, 15, 16, 15, 13, 14],
        [16, 14, 16, 18, 17, 17, 15, 16, 18, 13]]

def countSetBits(x):
    bits = 0
    while x:
            bits += 1
            x &= x-1
    return bits

bestCostSoFar = float('inf')
bestSourcesSoFar = [None for i in range(bookCount)]
#from where should you buy the books

for setIndex in range(1, 1 << shopCount):
    # iterate over all possible subsets -- excluding the empty set
    totalDeliveryCharge = deliveryCharge * countSetBits(setIndex)
    costForThisSet = 0
    bookSourcesForThisSet = [None for i in range(bookCount)]
    costForThisSet += totalDeliveryCharge
    for bookId in range(bookCount):
        minBookCost = float('inf')
        for shopId in range(shopCount):
            #find out which shop in our set sells this book for the cheapest price
            if (1 << shopId) & setIndex:
                #if this particular shop is in the set we are considering
                if cost[bookId][shopId] < minBookCost:
                    bookSourcesForThisSet[bookId] = shopId
                    minBookCost = cost[bookId][shopId]
        costForThisSet += minBookCost
    if costForThisSet < bestCostSoFar:
        bestCostSoFar = costForThisSet
        bestSourcesSoFar = bookSourcesForThisSet

print(bestCostSoFar)
print(bestSourcesSoFar)