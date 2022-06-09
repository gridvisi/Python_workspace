'''
https://www.codewars.com/kata/57ab3c09bb994429df000a4a/train/python
'''

def two_highest(arg1):
    return sorted(list(set(arg1)))[-2:][::-1]

#1st
def two_highest(ls):
    result = sorted(list(set(ls)), reverse=True)[:2]
    return result if isinstance(ls, (list)) else False

#3rd
import heapq
def two_highest(list_):
    return heapq.nlargest(2, set(list_)) if type(list_) == list else False

from heapq import nlargest

def two_highest(lst):
    return isinstance(lst, list) and nlargest(2, set(lst))


# not good recursion
def two_highest(arg1,cunt=0,ans=[]):
    biggest = float("-inf")
    if cunt==2:return list(set(ans))
    for i in set(arg1):
        if i > biggest:
            biggest = i
            ans.append(i)

    arg1.remove(biggest)
    print(arg1)
    cunt +=1
    return two_highest(arg1,cunt,ans) #ans[-2:],ans

arg1 = [15, 20, 20, 17]
print('Recursion:',two_highest(arg1))


def two_highest(arg1):
    return sorted(set(arg1))[-2:]








