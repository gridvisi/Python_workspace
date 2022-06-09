'''
https://www.codewars.com/kata/5a043fbef3251a5a2b0002b0/train/python

Write a function that replaces 'two', 'too' and 'to' with the number '2'.
Even if the sound is found mid word (like in octopus) or not in lowercase
grandma still thinks that should be replaced with a 2. Bless her.

'I love to text' becomes 'I love 2 text'
'see you tomorrow' becomes 'see you 2morrow'
'look at that octopus' becomes 'look at that oc2pus'

test.describe("Basic tests")

test.assert_equals(textin('I love to text'),'I love 2 text',)
test.assert_equals(textin('see you tomorrow'),'see you 2morrow',)
test.assert_equals(textin('look at that octopus'),'look at that oc2pus',)
test.assert_equals(textin('BECAUSE I WANT TO'),'BECAUSE I WANT 2',)
'''

#9th solve by ericlee
def textin(st):
    ans = ''
    i = 0
    while i <= len(st) - 1:
        if st[i:i + 3].lower() == 'too' or st[i:i + 3].lower() == 'two':
            ans += '2'
            i += 3

        elif st[i:i + 2].lower() == 'to':
            ans += "2"
            i += 2
        else:
            ans += st[i]
            i += 1
    return ans

# st.replace('TO','2',st.count("TO")).replace('to','2',st.count("to"))
# ["2" if st[i:i+2] == "to" or st[i:i+2] == "TO" else st[i:i+2] for i in range(0,len(st),2)]
st = 'BECAUSE TO I WANT TO to'
print(textin(st))


#1st
import re

def textin(txt ):
  return re.sub(r'(two|too|to)', '2', txt, flags=re.I)

#2nd
import re

def textin(str):
    return re.sub('(?i)t[wo]?o','2',str)

#3rd
import re
def textin(s):
    return re.sub('(?i)t(wo|oo|o)','2',s)

#4th
from re import sub

def textin(st):
    return sub(r'(?i)too|to|two', '2', st)


#10th
def textin(st):
    for s in ["two", "Two", "tWo", "twO", "TWo", "tWO", "TwO", "TWO",
              "too", "Too", "tOo", "toO", "TOo", "tOO", "ToO", "TOO",
              "to", "tO", "To", "TO"]:
        st = st.replace(s, "2")
    return st

