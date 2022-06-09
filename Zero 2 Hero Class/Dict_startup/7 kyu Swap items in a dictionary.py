'''
https://www.codewars.com/kata/5a21e090f28b824def00013c/train/python
'''

def switch_dict(dic):
    ans = {}
    for k,v in dic.items():
        if v not in ans:
            ans[v] = [k]
        else:
            ans[v].append(k)
    return ans
dic = {
          'Ice': 'Cream',
          'Age': '21',
          'Light': 'Cream',
          'Double': 'Cream'
          }
print(switch_dict(dic))

#1st
def switch_dict(dic):
    result = {}
    for key, value in dic.items():
        result.setdefault(value, []).append(key)
    return result

#2nd
from collections import defaultdict

def switch_dict(dct):
    revDct = defaultdict(list)
    for k,v in dct.items(): revDct[v].append(k)
    return revDct

#3rd
from collections import defaultdict
def switch_dict(dic):
    res = defaultdict(list)
    for k, v in dic.items():
        res[v].append(k)
    return res

