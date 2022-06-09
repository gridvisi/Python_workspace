

sl = [
['amal', 20],
['kamal', 25],
['amal', 30]
]

#should ouput:
#[amal,20,30]
#[kamal,25]

from itertools import groupby
from operator import itemgetter as g

print([[k, *(i[1] for i in v)] for k,v in groupby(sorted(sl, key=g(0)), g(0))])
# [['amal', 20, 30], ['kamal', 25]]


import pandas as pd
import numpy
data = [
    ['amal', 20],
    ['kamal', 25],
    ['amal', 30]
]

df = pd.DataFrame(data, columns=['key', 'value'])
grouped = data.groupby('key').agg(list)
print(grouped.head())