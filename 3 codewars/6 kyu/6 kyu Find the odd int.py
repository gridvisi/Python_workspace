'''
https://www.codewars.com/kata/find-the-odd-int/train/python
def find_it(seq):
    return len([x for x in seq if x>0 and x%2==0])
'''
seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
def find_it(seq):
    re = [seq.count(x) for x in set(seq)]
    return len(re),re
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 == 1: return i

print(find_it(seq))

