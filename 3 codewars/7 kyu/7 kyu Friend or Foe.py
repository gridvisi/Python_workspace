'''
https://www.codewars.com/kata/55b42574ff091733d900002f/train/python
Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
i.e.
friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
'''
x = ["Ryan", "Kieran", "Mark"]

from collections import Counter
def friend(x):
    l = Counter([len(i) for i in x])

    return [i for i in x if len(i) == 4]  #dict(zip(x,l))
print(friend(x))


'''
def friend(x):
    l = Counter([len(i) for i in x])
    print(l)
    for k,v in l.items():
        print(k,v)
        if v > 1:
            return [i for i in x if len(i) == k]  #dict(zip(x,l))
'''