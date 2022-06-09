'''
https://www.codewars.com/kata/598d91785d4ce3ec4f000018/train/python
'''
import string
def name_value(my_list):
    res,ls = [],[i for i in my_list if i != " "]
    res, ls = [], [i for i in my_list if i.isalpha()]

    score = dict(zip(string.ascii_lowercase,[i for i in range(1,27)]))
    score = dict(((letter, i) for i, letter in enumerate(string.ascii_lowercase,1)))
    score.update({' ':0})
    print(score)
    for i,w in enumerate(ls):
        value = sum([score[i] for i in w]) * (i+1)
        res.append(value)
    return res
my_list = ["codewars","abc","xyz"]
#print(my_list.split(' '))
my_list = [' ']
my_list = ["abc","abc","abc"," ","abc"]

# 1st solution
def nameValue(myList):
    return [ i*sum(map(lambda c: [0, ord(c)-96][c.isalpha()], w.lower())) for i,w in enumerate(myList,1)]
print(name_value(my_list))

# 2nd solution
def nameValue(myList):
    from string import ascii_lowercase as alphabet
    value_map = dict(((letter, i) for i, letter in enumerate(alphabet, 1)))
    return [i * sum(value_map.get(letter, 0) for letter in name) for i, name in
            enumerate(myList, 1)]