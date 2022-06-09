
import re
a = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0))   #123abc456,返回整体
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1))   #123
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))   #abc
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3))   #456

a = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0))

'''

import re

p=re.compile(ur"(\w)(\1+)")
s="abbbcccbba"
p.sub(ur"\1",s)

p=re.compile(ur"([a-zA-Z])(\1+)")
s="abbbcccbba"
p.sub(ur"\1",s)
'abcba'


import re
p=re.compile(ur"([a-zA-Z])(\1*)")
s="abbbcccbba"
p.sub(lambdam:m.group(1)+str(1+len(m.group(2))),s)
'a1b3c3b2a1'
'''