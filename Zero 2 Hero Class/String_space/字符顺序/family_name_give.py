
'''
首先，中文姓名先姓后名，护照上英文好象也如此。但写英语论文是为了便利国际交流。
既然是国际交流，就要便利于国外读者理解和识别。也就是说，从语用学角度，中国人
的英语姓名书写就应按国际的或英语的习惯或规则来。即便你不这么书写，在投稿系统
上也分first name和last name，填写后自动生成的姓名顺序就是英语的“先名后姓”。

其次，翻译中的“名从主人”，主要是针对人名、地名而言的，似乎没有人指中国人的英
语姓名的书写顺序。即便是翻译人名、地名，也无法彻底遵循“名从主人”原则，因为还
有另一原则“约定俗成”存在。因为很多人名、地名原来的翻译几乎都不是严格按“主人”
的发音翻译的，如果全部改一遍，很多我们所熟悉的人名、地名就佰生了。


三字姓名：
单姓，比如：王海棠 应该写：Wang Haitang
复姓，比如：诸葛亮 应该写：Zhuge Liang

四字姓名：
单姓，比如：李王文思 应该写：Li Wangwensi
复姓，比如：司马相如 应该写：Sima Xiangru
'''





#https://www.codewars.com/kata/57f759bb664021a30300007d/train/python
def switcheroo(s):
    return  ''.join(['b' if i == 'a' else 'a' if i=='b' else i for i in list(s)])


def switcheroo(s):
    return s.translate(str.maketrans('ab','ba'))


def switcheroo(string):
    #your code here
    result = ''
    for letter in string:
        if letter == 'a':
            letter = 'b'
        elif letter == 'b':
            letter = 'a'
        result += letter
    return result


def switcheroo(string):
    return ((string.replace('a','x')).replace('b','a')).replace('x','b')


def switcheroo(string):
    swap = {
        'a': 'b',
        'b': 'a',
    }

    return ''.join(swap.get(ch, ch) for ch in string)

def switcheroo(string):
    return ''.join({'a':'b', 'b':'a'}.get(c, c) for c in string)

switcheroo = lambda q: q.translate({97: 98, 98: 97})

def switcheroo(string):
    return ''.join(('bac')[ord(c) - 97] for c in string)


