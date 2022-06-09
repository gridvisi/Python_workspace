#https://www.codewars.com/kata/562f91ff6a8b77dfe900006e/train/python
'''
movie(500, 15, 0.9) should return 43
    (with card the total price is 634, with tickets 645)
movie(100, 10, 0.95) should return 24
    (with card the total price is 235, with tickets 240)
'''


import math
print(int(2.6),math.ceil(2.6),math.floor(2.6),round(2.6,0))

card, ticket, perc = 500, 15, 0.9
def movie(card, ticket, perc):
    num = 0
    card_price = ticket
    card_total, ticket_total = card,ticket*num
    while math.ceil(card_total) >= ticket_total:
        card_total += card_price * perc
        ticket_total = ticket * num
        card_price *= perc
        num += 1
    return num,round(card_total,0),ticket_total/ticket

def movie(card, ticket, perc):
    num = 1
    card_price = ticket
    card_total, ticket_total = card,ticket*num
    while math.ceil(card_total) > ticket_total:
        card_total += ticket * perc**num
        ticket_total = ticket * num
        card_price *= perc
        num += 1
    return num,round(card_total,0),ticket_total/ticket
print(movie(card, ticket, perc))
print(movie(card, ticket, perc))


#1st solution
import math


def movie(card, ticket, perc):
    num = 0
    priceA = 0
    priceB = card

    while math.ceil(priceB) >= priceA:
        num += 1
        priceA += ticket
        priceB += ticket * (perc ** num)

    return num


