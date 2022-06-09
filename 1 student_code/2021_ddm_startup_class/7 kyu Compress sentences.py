'''
https://www.codewars.com/kata/59de469cfc3c492da80000c5/train/python


'''

#not perfect solution
def compress(sentence):
    print(sentence.split())
    return ''.join([str(sentence.lower().split().index(c)) for c in sentence.lower().split()])

sentence = "the one bumble bee one bumble the bee"
sentence = "Ask not what your COUNTRY can do for you ASK WHAT YOU CAN DO FOR YOUR country"
print(compress(sentence))

#1st
def compress(sentence):
    ref = []
    for i in sentence.lower().split():
        if i not in ref:
            ref.append(i)
    return ''.join([str(ref.index(n)) for n in sentence.lower().split()])

#2nd
def compress(sentence):
    memo = {}
    return ''.join(map(str, (memo.setdefault(s, len(memo)) for s in sentence.lower().split())))