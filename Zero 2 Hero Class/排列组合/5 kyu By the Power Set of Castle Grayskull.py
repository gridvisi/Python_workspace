'''
https://www.codewars.com/kata/53d3173cf4eb7605c10001a8/train/python

Write a function that returns all of the sublists of a list/array.

Example:

power([1,2,3])
# => [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
For more details regarding this, see the power set entry in wikipedia.

ALGORITHMSMATHEMATICSNUMBERS
'''
s = ['ada','bony','cici','david','emma','helen','jack','kathy','lucy','maria']
s = ['ada','bony','cici','david','emma','helen','jack','kathy']
num = 4
def power(s,num):
  """Computes all of the sublists of s"""
  setname = [[]]
  for name in s:
    setname += [x+[name] for x in setname]
  ans = [i for i in setname if len(i) == num]
  return len(ans),ans
#print('ans:',power(s,num))

#step 2nd
namels = power(s,num)[1]
vs = []
#print(namels)

for a in namels:
    for b in namels:
        if len(set(a+b)) == 8:
            if (a,b) and (b,a) not in vs:
                vs.append((a,b))
print('pk:',vs,len(vs))




#2
import itertools

def power(s):
  "Computes all of the sublists of s"
  return [list(c) for i in range(len(s)+1) for c in itertools.combinations(s, i)]

password = ['a','b','c','d','e','f','1','2']


def pwcrack(password):
    """Computes all of the sublists of s"""
    setpw = [[]]
    ans = ''
    for num in password:
        print(num)
        setpw += [x+[num] for x in setpw]
        print(setpw)
    for pw in setpw:
        if len(pw) == 6 and pw[2] == 'c':
            ans += ''.join(pw) + ' '
    return ans

#print('ans:',pwcrack(password))