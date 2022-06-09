def max_profit(prices):
    out = prices[1] - prices[0]
    min_price = prices[0]

    for i, e in enumerate(prices[1:]):
        if e - min_price > out:
            out = e - min_price
            sell = e
        if e < min_price:
            min_price = e
    return round(out, 2), sell - round(out, 2), sell

plate = '渝A9886' #string
print('5' == 5)
print(f'{plate}',int(plate[-1]) % 2 == 0)
