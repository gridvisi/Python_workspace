'''
https://www.codewars.com/kata/559ee79ab98119dd0100001d/train/python

tips ： https://blog.csdn.net/weixin_26713521/article/details/108133623

Test.assert_equals(decoder
("Lor-.tile gnicsipida rutetcesnoc ,tema tis rolod muspi me", '-'),
 "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
'''
source = 'Lor-.tile gnicsipida rutetcesnoc ,tema tis rolod muspi me'
decode = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

from collections import Counter
s = Counter(source)
d = Counter(decode)
print(s - d)
#print(Counter(source),sorted(list(source)))
#print(Counter(decode),sorted(list(decode)))

def decoder(encoded, marker):
    s,l = encoded,len(marker)
    while marker in s:
        st = s.rfind(marker)
        left, right = s[:st],s[st+l:][::-1]
        s = ''.join(left + right)
    return s

encoded, marker = "Lor-.tile gnicsipida rutetcesnoc ,tema tis rolod muspi me", '-'
encoded, marker = 'q.qSusqsitanenev cen lsin sillom subinif ecsuF .itnetop essidnep','q'

#Curaaitur sdb.dbit amet ornare orci. Donec henorerit vestiaulum oictum
encoded, marker = 'Curaaitur sdb.dbit amet ornare orci. Donec henorerit vestiaulum oictum','db'
'''
'Curaaitur sdb.mutcio muluaitsev tireroneh cenoD .icro eranro tema tib' should equal 
'Curaaitur sit amet ornare orci. Donec henorerit vestiaulum oictum.'
'''
print('split:',encoded.split(marker))
parts = encoded.split(marker)
print(''.join(parts[::2]), ''.join(parts[1::2])[::-1])
test = 'abcdef'
print(test[::2])

print(decoder(encoded, marker))
print(decoder(encoded, marker).rfind('q'))
#print(decoder(encoded, marker) == decode)

'''
'pendisse potenti. Fusce finibus mollis nisl nec venenatisqsuSq.' should equal 
'Suspendisse potenti. Fusce finibus mollis nisl nec venenatis.'
'''

#1st solution
def decoder(encoded, marker):
  try:
      x = encoded.index(marker);
      return encoded[:x] + decoder(encoded[x + len(marker):], marker)[::-1]
  except:
      return encoded

#2nd solution
def decoder(encoded, marker):
    ss = encoded.split(marker)
    return ''.join(ss[::2]) + ''.join(ss[1::2])[::-1]

#3rd solution
def decoder(encoded, marker):
    while marker in encoded:
        a, b, c = encoded.rpartition(marker)
        encoded = a + c[::-1]
    return encoded

def decoder(encoded, marker):
    m = encoded.rfind(marker)
    while m > -1 :
        encoded = encoded[:m] + encoded[:m + len(marker) - 1:-1]
        m = encoded.rfind(marker)
    return encoded

def decoder(encoded, marker):
    parts = encoded.split(marker)
    res = ''.join(parts[::2]) + ''.join(parts[1::2])[::-1]
    return res