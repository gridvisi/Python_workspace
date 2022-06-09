'''
语法
dictionary.setdefault(keyname, value)
参数值
参数	描述
keyname	必需。您要从中返回值的项目的键名。
value 可选。如果键存在，则此参数无效。
如果键不存在，则此值将成为键的值。
默认值 None。
'''

car = {
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}

x = car.setdefault("model", "Macan")

print(x)


car = {
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}

x = car.setdefault("color", "white")

print(x)


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