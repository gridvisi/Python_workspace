'''
https://www.codewars.com/kata/5b6db1acb118141f6b000060/train/python

你会得到一个对象列表。每个对象都有类型，材料，可能还有第二材料。现有的材料有：纸、玻璃、有机物和塑料。

你的工作是根据这些物体的材料（如果存在的话，还有第二材料），将这些物体分门别类地放入4个回收箱中，
列出这些物体的类型。

注意事项
箱子的顺序应与上述材料的顺序相同。
所有的料箱都应该在输出中列出，即使其中一些是空的。
如果一个物体是由两种材料制成的，其类型应分别列在这两种材料中。
每个仓中类型的顺序应该与输入列表中各自对象的顺序相同。
与下面的例子相反，Python中的输出应该是4个列表的元组，而不是一个二维列表
例子
输入 = [
  {"类型": "烂苹果", "材料": "有机"}。
  {"类型": "过时的酸奶"，"材料"，"有机"，"第二材料"： "有机", "第二材料": "塑料"}。
  {"类型": "酒瓶"，"材料"， "玻璃", "第二材料": "纸"}。
  {"type": "amazon box", "material": "纸"}。
  {"类型": "啤酒瓶"，"材料"， "玻璃", "第二材料": "纸"}
]

输出 = [
  ["酒瓶"、"亚马逊盒子"、"啤酒瓶"]。
  ["酒瓶"、"啤酒瓶"]。
  ["烂苹果"、"过期酸奶"]。
  ["过时的酸奶"]
]
FUNDAMENTALSARRAYSOBJECTS

dict.get(key, default=None) 方法详解：
Parameters：
key -- This is the Key to be searched in the dictionary.
default -- This is the Value to be returned in case key does not exist.
如果default没指定，而且没有搜到值的话，会返回None

#2 case

d = {1: 2}
#print(d.get(0, default=0))
#Traceback (most recent call last):  File "<stdin>", line 1, in <module> TypeError: get() takes no keyword arguments
print(d.get(0, 0))

'''
input = [
  {"type": "rotten apples", "material": "organic"},
  {"type": "out of date yogurt", "material": "organic", "secondMaterial": "plastic"},
  {"type": "wine bottle", "material": "glass", "secondMaterial": "paper"},
  {"type": "amazon box", "material": "paper"},
  {"type": "beer bottle", "material": "glass", "secondMaterial": "paper"}
]

output = [
  ["wine bottle", "amazon box", "beer bottle"],
  ["wine bottle", "beer bottle"],
  ["rotten apples", "out of date yogurt"],
  ["out of date yogurt"]
]

from collections import defaultdict
print([(k,v) for k,v in input[0].items()])
print(dict([(k,v) for k,v in input[0].items()]))
#print(defaultdict([(k,v) for k,v in input[0].items()]))

t = {}
if t.get('1'):  # right:这种通过key来查询是否存在的方式是比较好的
    print(t['1'])
    print('right')

#if t['1']:  # wrong:这种直接判断是否存在的方式因为会在判断之前调用，所以会报错
#    print(t['1'])

#print(input[0].get("material",default=None))
#print(input[0].get("secondMaterial",default=None))

# Note the oder of materials refer to The existing materials are:
# paper, glass, organic, and plastic.
# paper, glass, organic, and plastic


def recycle(input):
    order = ['paper', 'glass', 'organic', 'plastic']
    #box,temp = [[]] * len(order),[]   #not good!
    box = dict(zip(order,[''] * len(order)))
    print(box)

    for i,e in enumerate(order):
        box[e] =[m['type'] for m in input if m.get('material', None)==e or m.get('secondMaterial',None)==e]
    return tuple(v for k,v in box.items())

print(recycle(input))

# answer ['wine bottle', 'amazon box', 'beer bottle'], ['wine bottle', 'beer bottle'], ['rotten apples', 'out of date yogurt'], ['out of date yogurt']

#1st solution
def recycle(a):
    bins = {"paper":[], "glass":[], "organic":[], "plastic":[]}
    for i in a:
        bins[i["material"]].append(i["type"])
        if "secondMaterial" in i:
            bins[i["secondMaterial"]].append(i["type"])
    return tuple(bins.values())

#2nd solution
from collections import defaultdict

def recycle(a):
    d = defaultdict(list)
    for o in a:
        d[o["material"]].append(o['type'])
        if "secondMaterial" in o:
            d[ o["secondMaterial"] ].append(o['type'])
    return tuple(map(d.__getitem__, "paper glass organic plastic".split()))

#3rd solution
def recycle(a):
    r = {'paper':[],'glass':[],'organic':[],'plastic':[]}
    for d in a:
        r[d['material']].append(d['type'])
        if 'secondMaterial' in d:
            r[d['secondMaterial']].append(d['type'])
    return tuple(r.values())

#4th solution
def recycle(a):
    materials = {
        "paper": [],
        "glass": [],
        "organic": [],
        "plastic": []
    }

    for item in a:
        materials[item['material']].append(item['type'])
        if 'secondMaterial' in item:
            materials[item['secondMaterial']].append(item['type'])

    return tuple(materials.values())


# 走弯路的原因是 for loop 遍历先选order or input
def recycle(input):
    order = ['paper', 'glass', 'organic', 'plastic']
    i,box,output = 0,[[]] * len(order),[]
    #print(box)
    while i < len(order):

        for m in input:
            #print(m)
            for k,v in m.items():

                if k != 'type' and m[k] == order[i]:
                    temp = m['type']
                    box[i].append(temp)
        #output.append(box)
        i += 1
    return box
#print(recycle(input))