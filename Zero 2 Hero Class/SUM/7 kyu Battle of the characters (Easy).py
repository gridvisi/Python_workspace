'''
https://www.codewars.com/kata/595519279be6c575b5000016/train/python


'''

import string
def battle(x, y):
    alpha = dict(zip(list(string.ascii_uppercase),list(range(1,27))))
    #X,Y = [i for i in x if i not in y],[i for i in y if i not in x]
    ans = sum([alpha[i] for i in x]) - sum([alpha[i] for i in y])
    return x if ans > 0 else y if ans < 0 else "Tie!"

x,y = 'PAFWDVWFDUDVVZECGTMWELOVSXRUN','XSRMTKGLENFEQBIDIFCYBRUMXNSBGOQGTSTYKJZCAELG'
print(battle(x, y))

#1st
def battle(x, y):

    # Compute x score using Unicode
    x_value = sum(ord(char) - 64 for char in x)

    # Compute y score using Unicode
    y_value = sum(ord(char) - 64 for char in y)

    if x_value < y_value:
        return y

    if x_value > y_value:
        return x

    return "Tie!"

#2nd
def battle(x, y):
    d={chr(i):c+1 for c,i in enumerate(range(65,91))}
    a=sum(d[c] for c in x)
    b=sum(d[c] for c in y)
    return 'Tie!' if a==b else [y,x][a>b]

#3rd
from string import ascii_uppercase as uppers
value = {c: i for i, c in enumerate(uppers, 1)}
def battle(s1, s2):
    v1, v2 = (sum(value[c] for c in s) for s in (s1, s2))
    return s1 if v2 < v1 else s2 if v1 < v2 else "Tie!"

import string
def battle(x, y):
    alpha = dict(zip(list(string.ascii_uppercase),list(range(1,27))))
    ans = [alpha[i]-alpha[j] for i,j in zip(x,y)]
    return x if sum(ans) > 0 else y if sum(ans)<0 else "Tie"
print(battle("FOUR", "FIVE"))

