
#1 只要有人姓胡
#1 是想判断两人中有没有姓胡的，有一个满足，就输出字符串result的值。但是，算法考虑的并不周到！
#  思考有哪些情况没有考虑到？该怎么补齐代码

name1,name2 = '胡迪童','胡越'
surname = name1[0]
print(surname,name1[0] == name2[0])

#1 只要有人姓胡
if name1[0] == '胡' or name2[0] == '胡':
    result = "至少有一人姓胡"
    print('有幸福的吗？',result)

#2 是否两人都姓胡
#  代码存在类似问题，找出算法问题，并试着补充

if name1[0] == '胡' and name2[0] == '李':
    result = "都姓胡"
    print('全部都幸福吗？',result)
else:
    result = "都不姓胡"
    print('全部都幸福吗？', result)