# https://www.codewars.com/kata/53e895e28f9e66a56900011a/train/python
from collections import Counter
import string
def letter_frequency(text):

    ans = Counter(text.lower())
    result = sorted([(v, k) for k,v in ans.items() if k in string.ascii_letters],key=lambda x:(x[1]))
    nkey = sorted(dict(result),reverse=True)
    final = dict(zip(nkey,' '*len(nkey)))
    print(final)
    for i in result:
        #if i[0] in nkey:
        final[i[0]] += i[1]

    return final
# sorted(result,key=lambda x:(x[0],[1])),key=lambda x:(x[1])
#KEY POINT:
#sorted([(k, v) for k,v in ans.items() if k in string.ascii_letters],key=lambda x:(x[1],x[0]),reverse=True)

text = "As long as I'm learning something, I figure I'm OK - it's a decent day."