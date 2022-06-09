'''
https://www.codewars.com/kata/5e5acfe31b1c240012717a78/train/python

哦，不！有人把你当地汽车经销商的服务器放在离搅拌机太近的地方，现在他们所有
的数据都被扰乱了。

你的工作是解开这些数据，并将其放入一个易于阅读的字典中。

解开给你的列表，并在一个字典中返回值，如下面这样。

dictionary = {'make': make, 'model': model, 'year': year, 'new': new}
你将得到一个包含一个字符串（汽车的品牌）、一个包含两个字符串（型号和子型号）、一个整数（汽车生产年份）和一个布尔值（汽车是新的还是旧的'真'或'假'）的列表，但你将不知道列表的顺序。

返回字典，其中'make'是一个字符串，'model'是一个字符串，'year'是一个整数，'new'是一个布尔值，表示它是新的（True）还是旧的（False）。

P.S 模型应该被转换为字符串，用一个空格来分隔这些值

基本疏解算法字符串结构数据结构数字整数布尔值

通过www.DeepL.com/Translator（免费版）翻译
'''

def make_model_year(lst):
    tag = {'make':'','model':(),'year':0,'new':1}
    for i in lst:
        if type(i) == str:
            tag['make'] = i
        elif type(i) == tuple:
            tag['model'] = ' '.join(i)
        elif type(i) == int:
            tag['year'] = i
        elif type(i) == bool:
            tag['new'] = i
    return tag

#1st
id_=lambda k: lambda v: (k,v)

CONFIG = {
    bool:  id_('new'),
    int:   id_('year'),
    tuple: lambda t:('model',' '.join(t)),
    str:   id_('make'),
}

def make_model_year(lst):
    return dict( CONFIG[type(data)](data) for data in lst)

#3rd
def make_model_year(lst):
    new, year, make, model = sorted(lst, key=lambda i: str(type(i)))
    return {'make':make, 'model':' '.join(model), 'year':year, 'new':new}


keys = {str: "make", tuple: "model", int: "year", bool: "new"}

def make_model_year(lst):
    return {keys[type(item)]: (" ".join(item) if isinstance(item, tuple) else item) for item in lst}

def make_model_year(lst):
    result = {}
    for item in lst:
        if isinstance(item, bool):
            result["new"] = item
        elif isinstance(item, int):
            result["year"] = item
        elif isinstance(item, tuple):
            result["model"] = " ".join(item)
        elif isinstance(item, str):
            result["make"] = item
    return result