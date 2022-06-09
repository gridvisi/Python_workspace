

#统计词频
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
result = {}
for color in colors:
    if result.get(color)==None:
        result[color]=1
    else:
        result[color]+=1
print (result)
#{'red': 2, 'blue': 3, 'green': 1}

from collections import Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print(c)
print (dict(c))

cnt = Counter()
c = Counter('gallahad')                 # 传进字符串
c = Counter({'red': 4, 'blue': 2})      # 传进字典
c = Counter(cats=4, dogs=8)             # 传进元组


c = Counter(['eggs', 'ham'])
c['bacon']                              # 不存在就返回0
#0

c = Counter(a=4, b=2, c=0, d=-2)
list(c.elements())
#['a', 'a', 'a', 'a', 'b', 'b']

Counter('abracadabra').most_common(3)
#[('a', 5), ('r', 2), ('b', 2)]

c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c + d                       # 相加
#Counter({'a': 4, 'b': 3})
c - d                       # 相减，如果小于等于0，删去
#Counter({'a': 2})
c & d                       # 求最小
#Counter({'a': 1, 'b': 1})
c | d                       # 求最大
#Counter({'a': 3, 'b': 2})


# 例子：读文件统计词频并按照出现次数排序，文件是以空格隔开的单词的诸多句子：
from collections import Counter
lines = open("./data/input.txt","r").read().splitlines()
lines = [lines[i].split(" ") for i in range(len(lines))]
words = []
for line in lines:
    words.extend(line)
result = Counter(words)
print (result.most_common(10))


# 当需要统计的文件比较大，使用read()一次读不完的情况：
from collections import Counter
result = Counter()
with open("./data/input.txt","r") as f:
    while True:
        lines = f.read(1024).splitlines()
        if lines==[]:
            break
        lines = [lines[i].split(" ") for i in range(len(lines))]
        words = []
        for line in lines:
            words.extend(line)
        tmp = Counter(words)
        result+=tmp

print (result.most_common(10))
