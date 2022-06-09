'''
https://www.codewars.com/kata/5bb50eb68f8bbdb4b300021d/train/python
'''
input_ = ["one", "one", "two", "two", "three", "three", "four", "one"]
output = ["one", "two", "three", "four", "one", "two", "three", "one"]

from collections import Counter
from itertools import groupby
def distribute_evenly(lst):
    arabic = [i for i in range(1,10)]
    en = ["one", "two", "three", "four",'five','six','seven','eight','nine']
    switch = dict(zip(en,arabic))
    lst_en = [switch[k] for k in lst]

    return sorted(lst_en)
#Counter(lst_en)
#sorted(lst_en,key=lambda x:sorted(Counter(lst_en)))
#[(list(group)) in k,group in groupby(lst_en)] #,key=lambda x:sorted(Counter(lst_en))
lst = input_
print(distribute_evenly(lst))