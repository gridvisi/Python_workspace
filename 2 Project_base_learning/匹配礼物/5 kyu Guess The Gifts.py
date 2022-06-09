'''
https://www.codewars.com/kata/52ae6b6623b443d9090002c8/train/python


Rules
Possible values for size: "small", "medium", "large"
Possible values for clatters: "no", "a bit", "yes"
Possible values for weight: "light", "medium", "heavy"
Don't add any item more than once to the result
The order of names in the output doesn't matter
It's possible, that multiple items from your wish list have the same attribute values.
If they match the attributes of one of the presents, add all of them.

wishlist = [{'name': "mini puzzle", 'size': "small", 'clatters': "yes", 'weight': "light"},
            {'name': "toy car", 'size': "medium", 'clatters': "a bit", 'weight': "medium"},
            {'name': "card game", 'size': "small", 'clatters': "no", 'weight': "light"}]
presents = [{'size': "medium", 'clatters': "a bit", 'weight': "medium"},
            {'size': "small", 'clatters': "yes", 'weight': "light"}]

guess_gifts(wishlist, presents) # => must return ["Toy Car", "Mini Puzzle"]
'''



wishlist = [{'name': "mini puzzle", 'size': "small", 'clatters': "yes", 'weight': "light"},
            {'name': "toy car", 'size': "medium", 'clatters': "a bit", 'weight': "medium"},
            {'name': "card game", 'size': "small", 'clatters': "no", 'weight': "light"}]
presents = [{'size': "medium", 'clatters': "a bit", 'weight': "medium"},
            {'size': "small", 'clatters': "yes", 'weight': "light"}]

def guess_gifts(wishlist, presents):
    ans = []
    for c in presents:
        fill = [w['name'] for w in wishlist if all([w[k] == v for k,v in c.items()])]
        ans.extend(fill)
    return ans
print(guess_gifts(wishlist, presents))


#something
def guess_gifts(wishlist, presents):
    confirmed = set()
    for d in wishlist:
        if {"size":d["size"], "clatters":d["clatters"], "weight":d["weight"]} in presents:
            confirmed.add(d["name"])

    return confirmed


def guess_gifts(wishlist, presents):
    guesses = []
    for wish in wishlist:
        for gift in presents:
            if list(wish.values())[1:] == list(gift.values()):
                guesses.append(wish['name'])
                break
    return guesses


def guess_gifts(wishlist, presents):
    expectation = []
    count=0
    for i in presents:
        for y in wishlist:
            if i['size']==y['size'] and i['clatters']==y['clatters'] and i['weight']==y['weight']:
                    if y['name'] not in expectation:
                        expectation.append(y['name'])
    return expectation