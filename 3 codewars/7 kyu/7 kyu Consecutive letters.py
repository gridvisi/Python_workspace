'''
https://www.codewars.com/kata/5ce6728c939bf80029988b57/train/python
'''
st = 'dabcf'
print(ord('s'))
def solve(st):
    sl = sorted(list(st))
    return all((ord(sl[i])-ord(sl[i-1])==1 for i in range(1,len(sl))))
print(solve(st))

import string
def solve(st):
  return ''.join(sorted(st)) in string.ascii_letters