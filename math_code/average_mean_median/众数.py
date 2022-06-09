'''
众数：一组数据中出现次数最多的数值，一组数据可以不存在、存在一个或多个众数，
众数用M表示。当所有数据出现次数都相同时，众数不存在。

实现思路
因为无法直接获知一个数组当中出现频率最高的数值，所以我们需要先统计数组中每
一个数值的出现次数，而后再找出所有出现次数最高的数值。其中：

记录每个数值的出现次数，可以使用哈希表存储，变量值的值作为key，变量值出现的频数作为value。
若发现变量值列表中所有数值均只出现了一次，则返回空数组（众数不存在）。
'''
def descriptive_mode(ls):
    # [第1步] 获取 变量值列表 中 所有不重复的变量值
    list_set = set(ls)  #将List转化为集合，去除重复元素
    # [第2步] 获取 所有不重复的变量值 在 变量值列表 中的 出现频数
    frequency_dict = {}   #定义存储 所有不重复的变量值 出现频数 的 哈希表
    for i in list_set: #遍历每一个list_set的元素(即去除重复元素后的集合)，得到每个元素在原始集合中包含的数量:count(i)
        frequency_dict[i] = ls.count(i)  #向frequency_dic中添加key-value对象:dict[key]=value
    # [第3步] 获取 变量值列表 中 出现频数 最高的数值的 出现频数
    print(frequency_dict)

    max_frequency = max(frequency_dict.values())
    mode_list = [] #定义存储 出现频数 最高的变量值的 数组
    if max_frequency == 1: # 若最高的 出现频数 为1，则没有众数
        return mode_list

    # [第4步] 找出 所有不重复的变量值 中 出现频数 最高的变量值
    for key,value in frequency_dict.items():   #遍历frequency_dic中每一个key-value对象
        if value == max_frequency:
            mode_list.append(key) #将出现频数 最高的变量值添加到 数组
    return mode_list

ls = [2003,2004,2006,2007,2006,2008,2006]
print(descriptive_mode(ls))

import collections
from collections import Counter
def get_mode(lis: list) -> int:
    return sorted(Counter(lis).items(), key=lambda x: x[1])[::-1][0][0]
lis = ls
print(get_mode(lis))