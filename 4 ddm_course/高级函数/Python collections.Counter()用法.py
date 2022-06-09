
#统计词频
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
result = {}
for color in colors:
    if result.get(color)==None:
        result[color]=1
    else:
        result[color]+=1
print(result)
#{'red': 2, 'blue': 3, 'green': 1}

from collections import Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print(dict(c))