'''
https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python

一个书商有很多书，分为26个类别，标有A，B，...。每本书都有一个由3、4、5或更多字符组成的代码c。
代码的第一个字符是一个大写字母，它定义了书籍的类别。

在书商的库存清单中，每个代码c后面都有一个空格和一个正整数n（int n >= 0），表示这个代码的图书
库存数量。

例如，一份库存清单的摘要可以是。

l = {"abart 20", "cdxef 50", "bkwrk 25", "btsqz 89", "drtym 60" }。
或
L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] 或 ....
你将得到一个库存列表（例如：L）和一个大写字母的类别列表，例如：:

m = {"a", "b", "c", "w"}
或
M = ["A", "B", "C", "W"] 或...
你的任务是找到L中所有编码属于M中每个类别的书籍，并根据每个类别对其数量进行求和。

对于例子中的列表L和M，你必须返回一个字符串（在Haskell/Clojure/Racket中是一个对的列表）。

(A : 20) - (B : 114) - (C : 50) - (W : 0)
其中A、B、C、W是类别，20是类别A的唯一书的总和，114是对应于 "BKWRK "和 "BTSQZ "的总和，50
对应于 "CDXEF"，0是类别 "W"，因为没有以W开头的代码。

如果L或M是空的，则返回字符串为""（Clojure和Racket应该返回一个空数组/列表）。

注意。
在结果中，代码和它们的值与M的顺序相同。

通过www.DeepL.com/Translator（免费版）翻译
'''


def stock_list(listOfArt, listOfCat):
    ans = ''
    flag = []
    for c in listOfCat:
        s = sum([int(b.split(' ')[1]) for b in listOfArt if b[0] == c])
        flag.append(s)
        ans += f"({c} : {s}) - "
        
    if not sum(flag): return ''
    return ans[:-3]
listOfArt, listOfCat = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"],["A", "B"]
print(stock_list(listOfArt, listOfCat))


#1st
def stock_list(listOfArt, listOfCat):
    if (len(listOfArt) == 0) or (len(listOfCat) == 0):
        return ""
    result = ""
    for cat in listOfCat:
        total = 0
        for book in listOfArt:
            if (book[0] == cat[0]):
                total += int(book.split(" ")[1])
        if (len(result) != 0):
            result += " - "
        result += "(" + str(cat) + " : " + str(total) + ")"
    return result

#2nd
from collections import Counter

def stock_list(listOfArt, listOfCat):
    if not listOfArt:
        return ''
    codePos = listOfArt[0].index(' ') + 1
    cnt = Counter()
    for s in listOfArt:
        cnt[s[0]] += int(s[codePos:])
    return ' - '.join('({} : {})'.format(cat, cnt[cat]) for cat in listOfCat)