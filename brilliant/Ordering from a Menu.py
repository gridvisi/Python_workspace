'''
https://brilliant.org/problems/ordering-from-a-menu/
豆腐炒饭：1元
    煎饼：5元
    早午餐组合：$20
    藏红花水蜜桃茶：50元。
    松露：100美元
    鱼子酱：200美元
    tofu scramble: $1
    pancakes: $5
    brunch combo: $20
    saffron infused peach tea: $50
    truffles: $100
    caviar: $200

You have in your wallet $300, which you want to spend completely.
You decide to spend all of it by buying food from a fancy restaurant with the
following menu:

    tofu scramble: $1
    pancakes: $5
    brunch combo: $20
    saffron infused peach tea: $50
    truffles: $100
    caviar: $200
Let OO be the number of different ways that you can spend exactly $300.
What are the last 3 digits of OO?
'''

total, values = 300,[200, 100, 50, 20, 5, 1]

def nbWays(total, values):
        if len(values) == 1:
            if total % values[0] == 0:
                return 1
            else:
                return 0

        ways = 0
        for subamount in range(0, total+1, values[0]):
                ways += nbWays(total - subamount, values[1:])

        return ways

print(nbWays(total, values))
