'''
https://www.codewars.com/kata/5a296b571f7f70b0b3000100/train/python

“树犬”（Treeing Cur）、{“挪威黑麋鹿”（Black Norwegian Elkhound）、“迦南狗”（Canaan Dog）、
“加拿大爱斯基摩狗”（Canadian Eskimo Dog）、“兰开夏犬”（Lancashire Heeler）、“美国无毛猎犬”（American Hairless Terrier）、
“澳大利亚海豹”（Australian Kelpie）、“拉萨阿普索”（lahasa Apso）、“杰克罗素猎犬”（Jack Russell Terrier）、
“艾瑞德尔猎犬”（Airedale Terrier）、“普，“施慈”、“巴辛基”、“瑞典瓦尔亨德”、“穆迪”、“库伊克汉杰”、“杜伯曼·平舍尔”、
“新斯科舍省鸣鸭猎犬”、“罗素猎犬”、“边境猎犬”、“猎狼”、“法国斗牛犬”、“英国玩具猎犬”、“印度斯皮茨犬”、“美国爱斯基摩犬”、
“马雷玛牧羊犬”、“西班牙水狗”、“设得兰牧羊犬”、“蓝花边狗”，“秘鲁无毛狗”、“意大利猎犬”、“爱尔兰水猎犬”、“日本下巴”、
“威尔士梗”、“Prazsky Krysarik”、“胡须牧羊犬”、“德国牧羊犬”、“Sakhalin Husky”、“玩具Fox Terrier”、
“墨西哥无毛狗”、“捕鼠梗犬”、“澳大利亚短毛尾巴牛狗”、“懒虫”、“丹麦瑞典农家犬”、“威马拉纳犬”、
“欧马赛尔犬”、'Papillon'，'Poodle'，'Border Collie'}）
'''

from collections import defaultdict
s=[('yellow',1),('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d=defaultdict(list)
for k, v in s:
    d[k].append(v)
a=sorted(d.items())
print(a)

#原文链接：https://blog.csdn.net/yangsong95/article/details/82319675

breed,dogs = 'Treeing Cur', {'Black Norwegian Elkhound', 'Canaan Dog', 'Canadian Eskimo Dog', 'Lancashire Heeler', 'American Hairless Terrier', 'Australian Kelpie', 'Lhasa Apso', 'Jack Russell Terrier', 'Airedale Terrier', 'Plott Hound', 'Miniature Schnauzer', 'Greyhound', 'Siberian Husky', 'Kai Ken', 'Croatian Sheepdog', 'English Springer Spaniel', 'Shih Tzu', 'Basenji', 'Swedish Vallhund', 'Mudi', 'Kooikerhondje', 'Doberman Pinscher', 'Nova Scotia Duck-Tolling Retriever', 'Russell Terrier', 'Border Terrier', 'Borzoi', 'French Bulldog', 'English Toy Terrier', 'Indian Spitz', 'American Eskimo Dog', 'Maremma Sheepdog', 'Spanish Water Dog', 'Shetland Sheepdog', 'Blue Lacy', 'Peruvian Hairless Dog', 'Italian Greyhound', 'Irish Water Spaniel', 'Japanese Chin', 'Welsh Terrier', 'Prazsky Krysarik', 'Bearded Collie', 'German Shepherd Dog', 'Sakhalin Husky', 'Toy Fox Terrier', 'Mexican Hairless Dog', 'Rat Terrier', 'Australian Stumpy Tail Cattle Dog', 'Sloughi', 'Danish Swedish Farmdog', 'Weimaraner', 'Eurasier', 'Papillon', 'Poodle', 'Border Collie'}
from collections import defaultdict

def find_similar_dogs(breed):
    simil = defaultdict(set)
    for dog,v in dogs.items():
        if dog != breed:
            simil[len(v & dogs[breed]) ].add(dog)
    return simil[max(simil)]
print(find_similar_dogs(breed))
