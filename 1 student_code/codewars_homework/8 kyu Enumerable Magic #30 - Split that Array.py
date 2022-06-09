'''
https://www.codewars.com/kata/545b342082e55dc9da000051/train/python

animals = ["cat", "dog", "duck", "cow", "donkey"]
test.describe("partition")
test.assert_equals(partition(animals, lambda x: len(x) == 3), (['cat', 'dog', 'cow'], ['duck', 'donkey']))
The equivalent in Python would be:

animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
partition(animals, lambda x: len(x) == 3)
    # (['cat', 'dog', 'cow'], ['duck', 'donkey'])
'''


#1st
from itertools import filterfalse
def partition(lis, classifier_method):
    fir = list(filter(classifier_method, lis))
    sec = list(filterfalse(classifier_method, lis))
    return (fir, sec)

#2nd
def partition(list, classifier_method):
    listTrue = []
    listFalse = []
    for l in list:
        if classifier_method(l):
            listTrue.append(l)
        else:
            listFalse.append(l)
    return listTrue, listFalse