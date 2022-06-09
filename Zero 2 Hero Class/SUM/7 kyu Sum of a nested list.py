'''
https://www.codewars.com/kata/5a15a4db06d5b6d33c000018/train/python

for i in str([1, [2, [3, [4]]]]):
    print(i)
'''

def sum_nested(lst):
    return sum(sum_nested(x) if isinstance(x,list) else x for x in lst)



def sum_nested(lst,s=0):
    s = ''.join(str(lst).split('[')).split(']')
    s = ''.join(s).split("'")[0]
    return sum([int(i) for i in  s.split(',')])



def sum_nested(lst):
    ans = ['0' if i in '[] ' else i for i in str(lst) ]
    print(ans)
    return sum(ans)#
lst = []
#print(sum_nested(lst))

