
print("".join(map(chr, range(ord('a'),ord('z')+1))))

li = 12
liu = 9
if liu > li:
    print('liu比li年龄大')
else:print('liu比li年龄小')


fruit_case = {'apple':'30','orange':'20','banana':'10'} #水果库存

fruit = 'apple'
if fruit in fruit_case:
    print('yes,i have',f"{fruit}")

if fruit == "apple" or fruit == "orange" or fruit == "berry":
    print('yes,i have',f"{fruit}")


dial_codes = [
    (86,'中国'),
    (91,'印度'),
    (1,'美国'),
    ]

#print(dial_codes[91])



dial_codes = [
    (86,'中国'),
    (91,'印度'),
    (1,'美国'),
    (62,'Indonesia'),
    (55,'Brazil'),
    (92,'Pakistan'),
    (880,'Bangladesh'),
    (234,'Nigera'),
    (7,'Russia'),
    (81,'Japan'),
    (852,'hongkong')
    ]
d1 = dict(dial_codes)#
print(d1)
print(d1[86])




l = ['s', 'P', 'r']
ddm_morning = ['zhou','han','li','summer','eric','tang']
ddm_morning[0] = 'ma'
print(ddm_morning)
ddm_morning = ('zhou','han','li','summer','eric','tang')
#ddm_morning[0] = 'ma'
print(ddm_morning)
print(l[0:3])


x_list,y_list,z_list = [1,2,3],[4,5,6],[7,8,9]
for x in x_list:
    for y in y_list:
        for z in z_list:
            print(x,y,z)# do something for x &amp;amp; y

from itertools import product
for x, y, z in product(x_list, y_list, z_list):
    print(x, y, z)  # do something for x, y, z

li = [chr(i) for i in range(ord("A"),ord("Z")+1)]
print(li)
name = " Albert Einstein"
str = "If All the bees die on earth, we would die due to not enough food sustain the living"
def name_in_str(str, name):
    it = iter(str.lower())
    return all(c in it for c in name.lower())
print(name_in_str(str, name))

sub = [1,3,6,9]
nest = [1,2,3,6,7,9,11]

for name in sub:
    if name not in nest:
        print('不吃饭',name)


def sub_in_nest(sub, nest):
    for name in sub:
        i = iter(sub)
        print(list(i))
    return all(c in nest for c in i)
print(sub_in_nest(sub, nest))

# 判断丁丁猫的学员

name_ls = ['张三','李林','王五', '赵六']
all_name = ['张三','李林','王五', '赵六','钱七']

for name in all_name:
    if name not in all_name:
        print('不吃饭:',name)

def name_in_all(name_ls, all_name):
    n = iter(name_ls)
    print(n)
    return all(c in all_name for c in n)
print(name_in_all(name_ls, all_name))
