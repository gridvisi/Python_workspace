import string
from codecs import encode as _dont_use_this_

def rot13(message):
    strr = list(message)
    for i in range(len(strr)):
        if ord(strr[i])+13 > 122:
            strr[i] = chr(ord(strr[i])-13)
        else:
            strr[i] = chr(ord(strr[i])+13)
    strr = ''.join(strr)
    return strr
print(rot13("test"))
