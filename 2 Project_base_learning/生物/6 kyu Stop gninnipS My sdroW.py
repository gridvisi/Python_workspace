'''

https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
'''

def spin_words(sentence):
    res = []
    s = sentence.split(' ')
    for w in s:
        if len(w) >= 5:
            res.append(w[::-1])
        else:
            res.append(w)
    return " ".join(res)
sentence = 'desrever will sdrow tneserp of'

def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)

import re
def spin_words(sentence):
    # Your code goes here
    return re.sub(r"\w{5,}", lambda w: w.group(0)[::-1], sentence)
print(spin_words(sentence))