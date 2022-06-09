
'''
https://brilliant.org/daily-problems/produce-order/

Today's Challenge
You're going to the local farmers' market to buy five items: avocados, bananas, cauliflowers, dates, and eggplants.

Avocados and bananas together are cheaper than cauliflowers and dates.
Bananas and cauliflowers together are cheaper than dates and eggplants.
Cauliflowers and dates together are cheaper than eggplants and avocados.
Dates and eggplants together are cheaper than avocados and bananas.\\[-0.7em]
Which item is the cheapest, and which the most expensive?

Cheapest: eggplants. Most expensive: avocados.
Cheapest: eggplants. Most expensive: dates.
Cheapest: bananas. Most expensive: dates.
Cheapest: bananas. Most expensive: avocados. #Super
'''

#1: a + b < c + d
#2: b + c < d + e
#3: c + d < e + a
#4: d + e < a + b

"from 1 + 4 -> d + e < c + d -> e < c" \
"from 1 + 3 -> a + b < e + a -> b < e"
"from 2 + 4 -> b + c < a + b -> c < a"

