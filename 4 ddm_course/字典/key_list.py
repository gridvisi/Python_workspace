
# dict
#python_command = {key: value}

comcn = ["循环","递归","条件判断","定义函数","返回"]  #value
comen = ["loop","recr","if else","def","return"] #key

word = "if else"

# 乐谱，小提琴、钢琴、
#zip(comen,comcn) <zip object at 0x00000218C81EAA40>
print(zip(comen,comcn))
python_command_dict = tuple(zip(comen,comcn))   #元组
print(python_command_dict)
python_command_dict = dict(zip(comen,comcn))
print(python_command_dict)

python_command_dict = list(zip(comen,comcn))
print("列表:",python_command_dict)
#print(python_command_dict)

'''
x = 3
y = 3
key_list = []
for i in range(1,x):
    for j in range(1,y):

        key_list.append([i,j])
print(key_list)
'''
def node(x,y,key):
    if x == 0 and y == 0:
        pace = {0:[0,0]}
        return pace
    else:
        xy_list = []
        rate = 0
        pace = {0:[0,0]}
        for i in range(x):
            j = 0
            xy_list.append([i,j])
            #pace[1] = xy_list[i]
            return xy_list
print(node(5,3,0))
